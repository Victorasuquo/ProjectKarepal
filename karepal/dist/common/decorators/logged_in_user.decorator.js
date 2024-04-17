"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.LoggedInUserDecorator = void 0;
const common_1 = require("@nestjs/common");
exports.LoggedInUserDecorator = (0, common_1.createParamDecorator)((_, ctx) => {
    const request = ctx.switchToHttp().getRequest();
    return request.user;
});
//# sourceMappingURL=logged_in_user.decorator.js.map