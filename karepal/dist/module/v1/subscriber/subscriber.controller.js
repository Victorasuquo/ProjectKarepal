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
exports.SubscriberController = void 0;
const common_1 = require("@nestjs/common");
const subscriber_service_1 = require("./subscriber.service");
const subscriber_dto_1 = require("./dto/subscriber.dto");
const response_constant_1 = require("../../../common/constants/response.constant");
const response_decorator_1 = require("../../../common/decorators/response.decorator");
const public_decorator_1 = require("../../../common/decorators/public.decorator");
let SubscriberController = class SubscriberController {
    constructor(subscriberService) {
        this.subscriberService = subscriberService;
    }
    async createSubscription(payload) {
        return await this.subscriberService.createSubscription(payload);
    }
};
exports.SubscriberController = SubscriberController;
__decorate([
    (0, public_decorator_1.Public)(),
    (0, common_1.Post)(),
    (0, response_decorator_1.ResponseMessage)(response_constant_1.RESPONSE_CONSTANT.NEWSLETTER.SUBSCRIPTION_SUCCESS),
    __param(0, (0, common_1.Body)()),
    __metadata("design:type", Function),
    __metadata("design:paramtypes", [subscriber_dto_1.SubscriberDto]),
    __metadata("design:returntype", Promise)
], SubscriberController.prototype, "createSubscription", null);
exports.SubscriberController = SubscriberController = __decorate([
    (0, common_1.Controller)('subscribe'),
    __metadata("design:paramtypes", [subscriber_service_1.SubscriberService])
], SubscriberController);
//# sourceMappingURL=subscriber.controller.js.map