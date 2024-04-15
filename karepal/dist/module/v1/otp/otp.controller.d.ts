import { OtpService } from './otp.service';
import { ValidateOtpDto } from './dto/otp.dto';
export declare class OtpController {
    private readonly otpService;
    constructor(otpService: OtpService);
    verifyOTP(payload: ValidateOtpDto): Promise<void>;
}
