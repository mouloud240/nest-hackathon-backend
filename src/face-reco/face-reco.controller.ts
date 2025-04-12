import {
  Controller,
  Post,
  UploadedFile,
  UseInterceptors,
} from '@nestjs/common';
import { FaceRecoService } from './face-reco.service';
import { MessagePattern, Payload } from '@nestjs/microservices';
import { Multer } from 'multer';
import * as fs from 'fs';
import { FileInterceptor } from '@nestjs/platform-express';
import { Public } from 'src/auth/decorators/public.decorator';
@Controller('face-reco')
export class FaceRecoController {
  constructor(private readonly faceRecoService: FaceRecoService) {}
  @MessagePattern('face/reco')
  handleFaceRecognition(@Payload() data: { image: string }) {
    const buffer = Buffer.from(data.image, 'base64');
    // Optional: Save to file for testing
    fs.writeFileSync('snapshot.jpg', buffer);
    console.log('Image saved as snapshot.jpg');
  }
  @UseInterceptors(FileInterceptor('image'))
  @Post()
  async uploadImage(@UploadedFile() file: Express.Multer.File) {
    const result = await this.faceRecoService.authenticateFace(
      file,
      'cameraId',
    );
    return result;
  }
  @Public()
  @MessagePattern('door/open-request')
  handleDoorOpenRequest() {}
}
