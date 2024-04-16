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
Object.defineProperty(exports, "__esModule", { value: true });
exports.OTPSchema = exports.OTP = void 0;
const mongoose_1 = require("@nestjs/mongoose");
const otp_enum_1 = require("../../../../common/enums/otp.enum");
let OTP = class OTP {
};
exports.OTP = OTP;
__decorate([
    (0, mongoose_1.Prop)({ required: true, unique: true }),
    __metadata("design:type", String)
], OTP.prototype, "email", void 0);
__decorate([
    (0, mongoose_1.Prop)({ required: true, unique: true }),
    __metadata("design:type", Number)
], OTP.prototype, "code", void 0);
__decorate([
    (0, mongoose_1.Prop)({ required: true, enum: otp_enum_1.OtpTypeEnum }),
    __metadata("design:type", String)
], OTP.prototype, "type", void 0);
__decorate([
    (0, mongoose_1.Prop)({ default: new Date() }),
    __metadata("design:type", Date)
], OTP.prototype, "createdAt", void 0);
__decorate([
    (0, mongoose_1.Prop)({ default: Date.now(), expires: 1200 }),
    __metadata("design:type", Date)
], OTP.prototype, "expiresAt", void 0);
exports.OTP = OTP = __decorate([
    (0, mongoose_1.Schema)({ expires: 1200 })
], OTP);
exports.OTPSchema = mongoose_1.SchemaFactory.createForClass(OTP);
//# sourceMappingURL=otp.schema.js.map