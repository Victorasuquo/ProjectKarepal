"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.AuthModule = void 0;
const common_1 = require("@nestjs/common");
const auth_service_1 = require("./auth.service");
const auth_controller_1 = require("./auth.controller");
const jwt_1 = require("@nestjs/jwt");
const environment_1 = require("../../../common/configs/environment");
const user_module_1 = require("../user/user.module");
const jwt_guard_1 = require("./guards/jwt.guard");
const core_1 = require("@nestjs/core");
const jwt_strategy_1 = require("./strategies/jwt.strategy");
const otp_module_1 = require("../otp/otp.module");
const mail_module_1 = require("../mail/mail.module");
let AuthModule = class AuthModule {
};
exports.AuthModule = AuthModule;
exports.AuthModule = AuthModule = __decorate([
    (0, common_1.Module)({
        imports: [
            {
                ...jwt_1.JwtModule.register({
                    secret: environment_1.ENVIRONMENT.JWT.SECRET,
                    signOptions: { expiresIn: '1d' },
                }),
                global: true,
            },
            user_module_1.UserModule,
            otp_module_1.OtpModule,
            mail_module_1.MailModule,
        ],
        controllers: [auth_controller_1.AuthController],
        providers: [
            auth_service_1.AuthService,
            jwt_strategy_1.JwtStrategy,
            {
                provide: core_1.APP_GUARD,
                useClass: jwt_guard_1.JwtAuthGuard,
            },
        ],
    })
], AuthModule);
//# sourceMappingURL=auth.module.js.map