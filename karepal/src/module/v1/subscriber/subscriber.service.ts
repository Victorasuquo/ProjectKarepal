/* eslint-disable prettier/prettier */
import { ConflictException, Injectable } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Subscriber, SubscriberDocument } from './schema/subscriber.schema';
import { Model } from 'mongoose';
import { SubscriberDto } from './dto/subscriber.dto';

@Injectable()
export class SubscriberService {
  constructor(
    @InjectModel(Subscriber.name)
    private subscriberModel: Model<SubscriberDocument>,
  ) {}

  async createSubscription(payload: SubscriberDto): Promise<SubscriberDocument> {
    const existingSubscriber = await this.subscriberModel.findOne({
      email: payload.email,
    });

    if (existingSubscriber) {
      throw new ConflictException("Oops! It seems like you've already subscribed to our newsletter. Thank you for being a part of our community!");
    }

    return this.subscriberModel.create(payload);
  }

  async getSubscriberByEmail(email: string): Promise<SubscriberDocument> {
    return this.subscriberModel.findOne({ email });
  }

  async findAllSubscribers(): Promise<Subscriber[]> {
    return this.subscriberModel.find();
  }
}
