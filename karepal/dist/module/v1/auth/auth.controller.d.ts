import { AuthService } from './auth.service';
import { CreateUserDto, GoogleAuthDto } from '../user/dto/user.dto';
import { ForgotPasswordDto, LoginDto, RequestVerifyEmailOtpDto, ResetPasswordDto, VerifyEmailDto } from './dto/auth.dto';
export declare class AuthController {
    private readonly authService;
    constructor(authService: AuthService);
    register(payload: CreateUserDto): Promise<import("../user/schemas/user.schema").UserDocument>;
    login(payload: LoginDto): Promise<any>;
    sendVerificationEmail(payload: RequestVerifyEmailOtpDto): Promise<void>;
    verifyEmail(payload: VerifyEmailDto): Promise<void>;
    sendPasswordResetEmail(payload: ForgotPasswordDto): Promise<void>;
    resetPassword(payload: ResetPasswordDto): Promise<void>;
    googleAuth(payload: GoogleAuthDto): Promise<any>;
}
