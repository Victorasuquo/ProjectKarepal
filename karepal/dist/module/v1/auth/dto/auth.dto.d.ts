export declare class LoginDto {
    email: string;
    password: string;
}
export declare class VerifyEmailDto {
    email: string;
    code: number;
}
export declare class RequestVerifyEmailOtpDto {
    email: string;
}
export declare class ForgotPasswordDto {
    email: string;
}
export declare class ResetPasswordDto extends LoginDto {
    code: number;
    confirmPassword: string;
}
