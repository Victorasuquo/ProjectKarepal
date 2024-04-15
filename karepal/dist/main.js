"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const core_1 = require("@nestjs/core");
const app_module_1 = require("./app.module");
const helmet_1 = require("helmet");
const express = require("express");
const common_1 = require("@nestjs/common");
const filter_1 = require("./common/filter/filter");
const environment_1 = require("./common/configs/environment");
const response_interceptor_1 = require("./common/interceptors/response.interceptor");
async function bootstrap() {
    const app = await core_1.NestFactory.create(app_module_1.AppModule, {
        cors: true,
    });
    app.use((0, helmet_1.default)());
    app.use(express.json({ limit: '50mb' }));
    app.use(express.urlencoded({ limit: '50mb', extended: true }));
    app.useGlobalInterceptors(new response_interceptor_1.ResponseTransformerInterceptor(app.get(core_1.Reflector)));
    app.useGlobalFilters(new filter_1.HttpExceptionFilter());
    app.setGlobalPrefix('/api');
    app.useGlobalPipes(new common_1.ValidationPipe({
        whitelist: true,
        forbidNonWhitelisted: true,
        transform: true,
    }));
    await app.listen(environment_1.ENVIRONMENT.APP.PORT);
}
bootstrap();
//# sourceMappingURL=main.js.map