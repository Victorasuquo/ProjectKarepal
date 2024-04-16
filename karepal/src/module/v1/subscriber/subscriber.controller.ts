/* eslint-disable prettier/prettier */
import { Controller, Post, Body } from '@nestjs/common';
import { SubscriberService } from './subscriber.service';
import { SubscriberDto } from './dto/subscriber.dto';
import { RESPONSE_CONSTANT } from 'src/common/constants/response.constant';
import { ResponseMessage } from 'src/common/decorators/response.decorator';
import { Public } from 'src/common/decorators/public.decorator';

@Controller('subscribe')
export class SubscriberController {
  constructor(private subscriberService: SubscriberService) {}

  @Public()
  @Post()
  @ResponseMessage(RESPONSE_CONSTANT.NEWSLETTER.SUBSCRIPTION_SUCCESS)
  async createSubscription(@Body() payload: SubscriberDto) {
    return await this.subscriberService.createSubscription(payload);
  }
}
