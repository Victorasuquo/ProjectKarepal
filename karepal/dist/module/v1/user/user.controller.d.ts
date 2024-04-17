import { UserService } from './user.service';
import { ILoggedInUser } from 'src/common/decorators/logged_in_user.decorator';
import { UpdateUserDto } from './dto/user.dto';
export declare class UserController {
    private readonly userService;
    constructor(userService: UserService);
    getCurrentUser(user: any): Promise<import("./schemas/user.schema").UserDocument>;
    updateProfile(payload: UpdateUserDto, user: ILoggedInUser): Promise<void>;
}
