/* eslint-disable prettier/prettier */
import { IsEmail } from 'class-validator';

export class SubscriberDto {
  @IsEmail()
  email: string;
}
