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
exports.ResponseTransformerInterceptor = void 0;
const common_1 = require("@nestjs/common");
const core_1 = require("@nestjs/core");
const rxjs_1 = require("rxjs");
const response_decorator_1 = require("../decorators/response.decorator");
let ResponseTransformerInterceptor = class ResponseTransformerInterceptor {
    constructor(reflector) {
        this.reflector = reflector;
    }
    intercept(context, next) {
        const response = context.switchToHttp().getResponse();
        const responseMessage = this.reflector.get(response_decorator_1.ResponseMessageKey, context.getHandler()) ??
            null;
        return next.handle().pipe((0, rxjs_1.map)((data) => {
            return {
                success: response.statusCode === 201 || response.statusCode === 200,
                data: data,
                message: responseMessage || null,
            };
        }));
    }
};
exports.ResponseTransformerInterceptor = ResponseTransformerInterceptor;
exports.ResponseTransformerInterceptor = ResponseTransformerInterceptor = __decorate([
    (0, common_1.Injectable)(),
    __metadata("design:paramtypes", [core_1.Reflector])
], ResponseTransformerInterceptor);
//# sourceMappingURL=response.interceptor.js.map