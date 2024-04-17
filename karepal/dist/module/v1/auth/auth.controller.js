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
exports.AuthController = void 0;
const common_1 = require("@nestjs/common");
const auth_service_1 = require("./auth.service");
const user_dto_1 = require("../user/dto/user.dto");
const response_decorator_1 = require("../../../common/decorators/response.decorator");
const auth_dto_1 = require("./dto/auth.dto");
const public_decorator_1 = require("../../../common/decorators/public.decorator");
const response_constant_1 = require("../../../common/constants/response.constant");
let AuthController = class AuthController {
    constructor(authService) {
        this.authService = authService;
    }
    async register(payload) {
        return await this.authService.register(payload);
    }
    async login(payload) {
        return await this.authService.login(payload);
    }
    async sendVerificationEmail(payload) {
        return await this.authService.sendVerificationMail(payload);
    }
    async verifyEmail(payload) {
        return await this.authService.verifyEmail(payload);
    }
    async sendPasswordResetEmail(payload) {
        return await this.authService.sendPasswordResetEmail(payload);
    }
    async resetPassword(payload) {
        return await this.authService.resetPassword(payload);
    }
    async googleAuth(payload) {
        return await this.authService.googleAuth(payload);
    }
};
exports.AuthController = AuthController;
__decorate([
    (0, public_decorator_1.Public)(),
    (0, common_1.Post)('register'),
    (0, response_decorator_1.ResponseMessage)(response_constant_1.RESPONSE_CONSTANT.AUTH.REGISTER_SUCCESS),
    __param(0, (0, common_1.Body)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [user_dto_1.CreateUserDto]),
    __metadata("design:returntype", Promise)
], AuthController.prototype, "register", null);
__decorate([
    (0, public_decorator_1.Public)(),
    (0, common_1.Post)('login'),
    (0, response_decorator_1.ResponseMessage)(response_constant_1.RESPONSE_CONSTANT.AUTH.LOGIN_SUCCESS),
    __param(0, (0, common_1.Body)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [auth_dto_1.LoginDto]),
    __metadata("design:returntype", Promise)
], AuthController.prototype, "login", null);
__decorate([
    (0, public_decorator_1.Public)(),
    (0, common_1.Post)('verify-email/otp'),
    __param(0, (0, common_1.Body)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [auth_dto_1.RequestVerifyEmailOtpDto]),
    __metadata("design:returntype", Promise)
], AuthController.prototype, "sendVerificationEmail", null);
__decorate([
    (0, public_decorator_1.Public)(),
    (0, common_1.Post)('verify-email'),
    (0, response_decorator_1.ResponseMessage)(response_constant_1.RESPONSE_CONSTANT.AUTH.EMAIL_VERIFICATION_SUCCESS),
    __param(0, (0, common_1.Body)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [auth_dto_1.VerifyEmailDto]),
    __metadata("design:returntype", Promise)
], AuthController.prototype, "verifyEmail", null);
__decorate([
    (0, public_decorator_1.Public)(),
    (0, common_1.Post)('forgot-password'),
    (0, response_decorator_1.ResponseMessage)(response_constant_1.RESPONSE_CONSTANT.AUTH.PASSWORD_RESET_EMAIL_SUCCESS),
    __param(0, (0, common_1.Body)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [auth_dto_1.ForgotPasswordDto]),
    __metadata("design:returntype", Promise)
], AuthController.prototype, "sendPasswordResetEmail", null);
__decorate([
    (0, public_decorator_1.Public)(),
    (0, common_1.Post)('forgot-password/update'),
    (0, response_decorator_1.ResponseMessage)(response_constant_1.RESPONSE_CONSTANT.AUTH.PASSWORD_RESET_SUCCESS),
    __param(0, (0, common_1.Body)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [auth_dto_1.ResetPasswordDto]),
    __metadata("design:returntype", Promise)
], AuthController.prototype, "resetPassword", null);
__decorate([
    (0, public_decorator_1.Public)(),
    (0, common_1.Post)('google'),
    (0, response_decorator_1.ResponseMessage)(response_constant_1.RESPONSE_CONSTANT.AUTH.LOGIN_SUCCESS),
    __param(0, (0, common_1.Body)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [user_dto_1.GoogleAuthDto]),
    __metadata("design:returntype", Promise)
], AuthController.prototype, "googleAuth", null);
exports.AuthController = AuthController = __decorate([
    (0, common_1.Controller)('auth'),
    __metadata("design:paramtypes", [auth_service_1.AuthService])
], AuthController);
//# sourceMappingURL=auth.controller.js.map