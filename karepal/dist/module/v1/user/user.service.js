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
exports.UserService = void 0;
const common_1 = require("@nestjs/common");
const user_schema_1 = require("./schemas/user.schema");
const mongoose_1 = require("mongoose");
const mongoose_2 = require("@nestjs/mongoose");
const helper_util_1 = require("../../../common/utils/helper.util");
let UserService = class UserService {
    constructor(userModel) {
        this.userModel = userModel;
    }
    async createUser(payload) {
        try {
            const hashedPassword = await helper_util_1.BaseHelper.hashData(payload.password);
            const result = await this.userModel.create({
                ...payload,
                password: hashedPassword,
            });
            delete result['_doc'].password;
            return result;
        }
        catch (e) {
            if (e.code === 11000) {
                throw new common_1.ConflictException(`${Object.keys(e.keyValue)} already exists`);
            }
            else {
                throw new common_1.InternalServerErrorException(e.response?.message || 'Something went wrong');
            }
        }
    }
    async getUserByEmailIncludePassword(email) {
        return this.userModel.findOne({ email }).select('+password');
    }
    async getUser(id) {
        return this.userModel.findOne({ _id: id });
    }
    async getUserByEmail(email) {
        return this.userModel.findOne({ email });
    }
    async updateUserByEmail(email, details) {
        return this.userModel.updateOne({ email }, details);
    }
    async checkUserExistByEmail(email) {
        const user = await this.getUserByEmail(email);
        if (!user) {
            throw new common_1.BadRequestException('No user exist with provided email');
        }
        return true;
    }
    async updateUser(payload, userId) {
        const { username, age } = payload;
        if (username) {
            const existingUserWithUsername = await this.userModel.findOne({
                username,
                _id: { $ne: userId },
            });
            if (existingUserWithUsername) {
                throw new common_1.BadRequestException('Username already used, kindly select a new username');
            }
        }
        await this.userModel.updateOne({ _id: userId }, { ...(username && { username }), ...(age && { age }) });
    }
    async createUserFromGoogle(payload) {
        return await this.userModel.create({
            ...payload,
            emailVerified: true,
            isGoogleAuth: true,
        });
    }
};
exports.UserService = UserService;
exports.UserService = UserService = __decorate([
    (0, common_1.Injectable)(),
    __param(0, (0, mongoose_2.InjectModel)(user_schema_1.User.name)),
    __metadata("design:paramtypes", [mongoose_1.Model])
], UserService);
//# sourceMappingURL=user.service.js.map