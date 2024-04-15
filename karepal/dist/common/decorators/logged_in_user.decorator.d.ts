import { UserRoleEnum } from '../enums/user.enum';
export interface ILoggedInUser {
    _id: string;
    email: string;
    role: UserRoleEnum;
}
export declare const LoggedInUserDecorator: (...dataOrPipes: unknown[]) => ParameterDecorator;
