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
exports.AuthService = void 0;
const common_1 = require("@nestjs/common");
const user_service_1 = require("../user/user.service");
const helper_util_1 = require("../../../common/utils/helper.util");
const jwt_1 = require("@nestjs/jwt");
const otp_service_1 = require("../otp/otp.service");
const otp_enum_1 = require("../../../common/enums/otp.enum");
let AuthService = class AuthService {
    constructor(userService, jwtService, otpService) {
        this.userService = userService;
        this.jwtService = jwtService;
        this.otpService = otpService;
    }
    async register(payload) {
        const user = await this.userService.createUser(payload);
        await this.otpService.sendOTP({
            email: user.email,
            type: otp_enum_1.OtpTypeEnum.VERIFY_EMAIL,
        });
        return user;
    }
    async login(payload) {
        const { email, password } = payload;
        const user = await this.userService.getUserByEmailIncludePassword(email);
        if (!user) {
            throw new common_1.BadRequestException('Invalid Credential');
        }
        const passwordMatch = await helper_util_1.BaseHelper.compareHashedData(password, user.password);
        if (!passwordMatch) {
            throw new common_1.BadRequestException('Incorrect Password');
        }
        if (!user.emailVerified) {
            throw new common_1.BadRequestException('kindly verify your email to login');
        }
        const token = this.jwtService.sign({ _id: user._id });
        delete user['_doc'].password;
        return {
            ...user['_doc'],
            accessToken: token,
        };
    }
    async verifyEmail(payload) {
        const { code, email } = payload;
        const user = await this.userService.getUserByEmail(email);
        if (!user) {
            throw new common_1.BadRequestException('Invalid Email');
        }
        if (user.emailVerified) {
            throw new common_1.UnprocessableEntityException('Email already verified');
        }
        await this.otpService.verifyOTP({
            code,
            email,
            type: otp_enum_1.OtpTypeEnum.VERIFY_EMAIL,
        });
        await this.userService.updateUserByEmail(email, {
            emailVerified: true,
        });
    }
    async sendVerificationMail(payload) {
        await this.userService.checkUserExistByEmail(payload.email);
        await this.otpService.sendOTP({
            ...payload,
            type: otp_enum_1.OtpTypeEnum.VERIFY_EMAIL,
        });
    }
    async sendPasswordResetEmail(payload) {
        await this.userService.checkUserExistByEmail(payload.email);
        await this.otpService.sendOTP({
            ...payload,
            type: otp_enum_1.OtpTypeEnum.RESET_PASSWORD,
        });
    }
    async resetPassword(payload) {
        const { email, password, confirmPassword, code } = payload;
        if (password !== confirmPassword) {
            throw new common_1.ConflictException('Passwords do not match');
        }
        await this.otpService.verifyOTP({
            email,
            code,
            type: otp_enum_1.OtpTypeEnum.RESET_PASSWORD,
        });
        const hashedPassword = await helper_util_1.BaseHelper.hashData(password);
        await this.userService.updateUserByEmail(email, {
            password: hashedPassword,
        });
    }
    async googleAuth(payload) {
        const { email } = payload;
        const user = await this.userService.getUserByEmail(email);
        if (user) {
            if (!user.isGoogleAuth) {
                throw new common_1.ConflictException('Looks like you already have an account! Use your existing login details or choose a different email address to sign up with Google');
            }
            const token = this.jwtService.sign({ _id: user._id });
            return { ...user['_doc'], accessToken: token };
        }
        const newUser = await this.userService.createUserFromGoogle(payload);
        const token = this.jwtService.sign({ _id: newUser._id });
        return { ...newUser['_doc'], accessToken: token };
    }
};
exports.AuthService = AuthService;
exports.AuthService = AuthService = __decorate([
    (0, common_1.Injectable)(),
    __param(2, (0, common_1.Inject)((0, common_1.forwardRef)(() => otp_service_1.OtpService))),
    __metadata("design:paramtypes", [user_service_1.UserService,
        jwt_1.JwtService,
        otp_service_1.OtpService])
], AuthService);
//# sourceMappingURL=auth.service.js.map