import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { Document } from 'mongoose';
import { UserRoleEnum } from '../../../../common/enums/user.enum';

export type UserDocument = User & Document;

@Schema({ timestamps: true })
export class User {
  @Prop({ required: true, unique: true })
  email: string;

  @Prop({ required: false })
  phone: string;

  @Prop({ default: false })
  emailVerified: boolean;

  @Prop({ select: false })
  password: string;

  @Prop({ enum: UserRoleEnum, default: UserRoleEnum.USER })
  role: UserRoleEnum;

  @Prop()
  age: string;

  @Prop()
  username: string;

  @Prop({ default: false })
  isGoogleAuth: boolean;
}

export const UserSchema = SchemaFactory.createForClass(User);
