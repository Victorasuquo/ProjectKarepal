import { MailerService } from '@nestjs-modules/mailer/dist';
export declare class MailService {
    private mailerService;
    constructor(mailerService: MailerService);
    sendEmail(toEmail: string, subject: string, template: string): Promise<void>;
}
