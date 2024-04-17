import { Request } from 'express';
import { UserService } from '../../user/user.service';
declare const JwtStrategy_base: new (...args: any[]) => any;
export declare class JwtStrategy extends JwtStrategy_base {
    private userService;
    constructor(userService: UserService);
    validate(req: Request, payload: Partial<{
        _id: string;
    }>): Promise<import("../../user/schemas/user.schema").UserDocument>;
}
export {};
