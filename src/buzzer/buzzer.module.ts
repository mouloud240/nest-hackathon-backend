import { Module } from '@nestjs/common';
import { BuzzerService } from './buzzer.service';
import { BuzzerController } from './buzzer.controller';

@Module({
  controllers: [BuzzerController],
  providers: [BuzzerService],
})
export class BuzzerModule {}
