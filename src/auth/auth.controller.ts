import { Body, Controller, Post, UseGuards } from '@nestjs/common';
import { localGuard } from './guards/local.guard';
import { currentUser } from './decorators/getUser.decorator';
import { user } from '@prisma/client';
import { AuthService } from './auth.service';
import { RefreshTokenDto } from './dto/refreshTokenDto';
import { ConfigService } from '@nestjs/config';
import { refreshToken } from './dto/refreshToken.dto';
import { ApiBody, ApiOperation, ApiResponse } from '@nestjs/swagger';
import { loginReqDto } from './dto/login.req.dto';
import { LoginResDto } from './dto/login.res.dto';

@Controller('auth')
export class AuthController {
  constructor(
    private readonly authServices: AuthService,
    private readonly ConfigService: ConfigService,
  ) {}
  @ApiOperation({ summary: 'Login to an existing account' })
  @ApiBody({ type: loginReqDto })
  @ApiResponse({
    status: 200,
    description: 'Login Successful',
    type: LoginResDto,
  })
  @ApiResponse({ status: 401, description: 'Wrong Credentials' })
  @Post('login')
  @UseGuards(localGuard)
  login(@currentUser() user: user) {
    return this.authServices.login(user);
  }
  @Post('refresh')
  @ApiOperation({ summary: 'Refresh the access token' })
  @ApiBody({ type: RefreshTokenDto })
  @ApiResponse({
    status: 200,
    description: 'Refresh Token Successful',
    type: refreshToken,
  })
  @ApiResponse({ status: 401, description: 'Invalid Refresh Token' })
  @ApiResponse({ status: 403, description: 'Forbidden' })
  @ApiResponse({ status: 404, description: 'User not found' })
  refreshToken(@Body() body: RefreshTokenDto): refreshToken {
    return this.authServices.validateRefreshToken(body.refreshToken);
  }
}
