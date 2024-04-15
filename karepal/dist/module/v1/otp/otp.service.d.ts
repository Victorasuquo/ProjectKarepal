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
import { OTP, OTPDocument } from './schemas/otp.schema';
import { Model } from 'mongoose';
import { CreateOtpDto, SendOtpDto, ValidateOtpDto, VerifyOtpDto } from './dto/otp.dto';
import { MailService } from '../mail/mail.service';
export declare class OtpService {
    private otpModel;
    private readonly mailService;
    constructor(otpModel: Model<OTPDocument>, mailService: MailService);
    createOTP(payload: CreateOtpDto): Promise<OTPDocument>;
    getOtpById(id: string): Promise<OTPDocument>;
    getOtpByEmail(email: string): Promise<OTPDocument>;
    getOtpByCode(code: number): Promise<OTPDocument>;
    validateOTP(payload: ValidateOtpDto): Promise<import("mongoose").Document<unknown, {}, OTPDocument> & OTP & Document & {
        _id: import("mongoose").Types.ObjectId;
    }>;
    verifyOTP(payload: VerifyOtpDto): Promise<boolean>;
    sendOTP(payload: SendOtpDto): Promise<void>;
    deleteOTP(id: string): Promise<import("mongoose").Document<unknown, {}, OTPDocument> & OTP & Document & {
        _id: import("mongoose").Types.ObjectId;
    }>;
}
