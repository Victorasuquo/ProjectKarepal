import { OtpTypeEnum } from 'src/common/enums/otp.enum';
export declare class CreateOtpDto {
    type: OtpTypeEnum;
    email: string;
    code: number;
}
export declare class SendOtpDto {
    type: OtpTypeEnum;
    email: string;
}
export declare class VerifyOtpDto extends SendOtpDto {
    code: number;
}
export declare class ValidateOtpDto extends VerifyOtpDto {
}
