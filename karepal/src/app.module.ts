/* eslint-disable prettier/prettier */
import { Module } from '@nestjs/common';
import { UserModule } from './module/v1/user/user.module';
import { DatabaseModule } from './module/v1/database/database.module';
import { AuthModule } from './module/v1/auth/auth.module';
import { OtpModule } from './module/v1/otp/otp.module';
import { MailModule } from './module/v1/mail/mail.module';
import { SubscriberModule } from './module/v1/subscriber/subscriber.module';

@Module({
  imports: [
    UserModule,
    DatabaseModule,
    AuthModule,
    OtpModule,
    MailModule,
    SubscriberModule,
  ],
  controllers: [],
  providers: [],
})
export class AppModule {}
