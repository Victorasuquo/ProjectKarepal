"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var __param = (this && this.__param) || function (paramIndex, decorator) {
    return function (target, key) { decorator(target, key, paramIndex); }
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.OtpService = void 0;
const common_1 = require("@nestjs/common");
const mongoose_1 = require("@nestjs/mongoose");
const otp_schema_1 = require("./schemas/otp.schema");
const mongoose_2 = require("mongoose");
const helper_util_1 = require("../../../common/utils/helper.util");
const mail_service_1 = require("../mail/mail.service");
const otp_enum_1 = require("../../../common/enums/otp.enum");
const verify_email_email_1 = require("../mail/templates/verify-email.email");
const forgot_password_email_1 = require("../mail/templates/forgot-password.email");
let OtpService = class OtpService {
    constructor(otpModel, mailService) {
        this.otpModel = otpModel;
        this.mailService = mailService;
    }
    async createOTP(payload) {
        return this.otpModel.findOneAndUpdate({ email: payload.email }, payload, {
            upsert: true,
            new: true,
        });
    }
    async getOtpById(id) {
        return this.otpModel.findById(id);
    }
    async getOtpByEmail(email) {
        return this.otpModel.findOne({ email });
    }
    async getOtpByCode(code) {
        return this.otpModel.findOne({ code });
    }
    async validateOTP(payload) {
        const { email, code, type } = payload;
        const otp = await this.otpModel.findOne({ email, code, type });
        if (!otp) {
            throw new common_1.NotFoundException('Invalid OTP code');
        }
        return otp;
    }
    async verifyOTP(payload) {
        const otp = await this.validateOTP(payload);
        await this.deleteOTP(otp._id.toString());
        return true;
    }
    async sendOTP(payload) {
        const { email, type } = payload;
        const code = helper_util_1.BaseHelper.generateOTP();
        let template;
        let subject;
        switch (type) {
            case otp_enum_1.OtpTypeEnum.RESET_PASSWORD:
                template = (0, forgot_password_email_1.ForgotPasswordTemplate)({ code });
                subject = 'Reset Your Password';
                break;
            case otp_enum_1.OtpTypeEnum.VERIFY_EMAIL:
                template = (0, verify_email_email_1.VerifyEmailTemplate)({ code });
                subject = 'Verify Email';
                break;
        }
        const otp = await this.createOTP({
            email,
            code,
            type,
        });
        if (!otp)
            throw new common_1.InternalServerErrorException('Unable to send otp at the moment , try again later');
        await this.mailService.sendEmail(email, subject, template);
    }
    async deleteOTP(id) {
        return this.otpModel.findByIdAndDelete(id);
    }
};
exports.OtpService = OtpService;
exports.OtpService = OtpService = __decorate([
    (0, common_1.Injectable)(),
    __param(0, (0, mongoose_1.InjectModel)(otp_schema_1.OTP.name)),
    __metadata("design:paramtypes", [mongoose_2.Model,
        mail_service_1.MailService])
], OtpService);
//# sourceMappingURL=otp.service.js.map