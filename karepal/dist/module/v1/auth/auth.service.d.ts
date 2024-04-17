import { CreateUserDto, GoogleAuthDto } from '../user/dto/user.dto';
import { UserService } from '../user/user.service';
import { ForgotPasswordDto, LoginDto, RequestVerifyEmailOtpDto, ResetPasswordDto, VerifyEmailDto } from './dto/auth.dto';
import { JwtService } from '@nestjs/jwt';
import { OtpService } from '../otp/otp.service';
export declare class AuthService {
    private userService;
    private jwtService;
    private readonly otpService;
    constructor(userService: UserService, jwtService: JwtService, otpService: OtpService);
    register(payload: CreateUserDto): Promise<import("../user/schemas/user.schema").UserDocument>;
    login(payload: LoginDto): Promise<any>;
    verifyEmail(payload: VerifyEmailDto): Promise<void>;
    sendVerificationMail(payload: RequestVerifyEmailOtpDto): Promise<void>;
    sendPasswordResetEmail(payload: ForgotPasswordDto): Promise<void>;
    resetPassword(payload: ResetPasswordDto): Promise<void>;
    googleAuth(payload: GoogleAuthDto): Promise<any>;
}
