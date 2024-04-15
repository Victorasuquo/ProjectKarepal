/// <reference types="mongoose/types/aggregate" />
/// <reference types="mongoose/types/callback" />
/// <reference types="mongoose/types/collection" />
/// <reference types="mongoose/types/connection" />
/// <reference types="mongoose/types/cursor" />
/// <reference types="mongoose/types/document" />
/// <reference types="mongoose/types/error" />
/// <reference types="mongoose/types/expressions" />
/// <reference types="mongoose/types/helpers" />
/// <reference types="mongoose/types/middlewares" />
/// <reference types="mongoose/types/indexes" />
/// <reference types="mongoose/types/models" />
/// <reference types="mongoose/types/mongooseoptions" />
/// <reference types="mongoose/types/pipelinestage" />
/// <reference types="mongoose/types/populate" />
/// <reference types="mongoose/types/query" />
/// <reference types="mongoose/types/schemaoptions" />
/// <reference types="mongoose/types/schematypes" />
/// <reference types="mongoose/types/session" />
/// <reference types="mongoose/types/types" />
/// <reference types="mongoose/types/utility" />
/// <reference types="mongoose/types/validation" />
/// <reference types="mongoose/types/virtuals" />
/// <reference types="mongoose/types/inferschematype" />
import { User, UserDocument } from './schemas/user.schema';
import { Model } from 'mongoose';
import { CreateUserDto, GoogleAuthDto, UpdateUserDto } from './dto/user.dto';
export declare class UserService {
    private userModel;
    constructor(userModel: Model<UserDocument>);
    createUser(payload: CreateUserDto): Promise<UserDocument>;
    getUserByEmailIncludePassword(email: string): Promise<UserDocument>;
    getUser(id: string): Promise<UserDocument>;
    getUserByEmail(email: string): Promise<UserDocument>;
    updateUserByEmail(email: string, details: any): Promise<import("mongoose").UpdateWriteOpResult>;
    checkUserExistByEmail(email: string): Promise<boolean>;
    updateUser(payload: UpdateUserDto, userId: string): Promise<void>;
    createUserFromGoogle(payload: GoogleAuthDto): Promise<import("mongoose").Document<unknown, {}, UserDocument> & User & import("mongoose").Document<any, any, any> & {
        _id: import("mongoose").Types.ObjectId;
    }>;
}
