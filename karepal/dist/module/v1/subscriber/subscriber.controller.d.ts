import { SubscriberService } from './subscriber.service';
import { SubscriberDto } from './dto/subscriber.dto';
export declare class SubscriberController {
    private subscriberService;
    constructor(subscriberService: SubscriberService);
    createSubscription(payload: SubscriberDto): Promise<import("./schema/subscriber.schema").SubscriberDocument>;
}
