import { Global, Module } from '@nestjs/common';
import { AuthService } from './auth.service';
import { JwtModule } from '@nestjs/jwt';
import { PassportModule } from '@nestjs/passport';
import { localGuard } from './guards/local.guard';
import { LocalStrategy } from './strategies/local.strategy';
import { ConfigModule } from '@nestjs/config';
import { jwtStrategy } from './strategies/jwt.startegy';
import { UserModule } from 'src/user/user.module';
import { AuthController } from './auth.controller';
import { UsersService } from 'src/user/user.service';
import { jwtGuard } from './guards/jwt.guard';
import { RoleGuard } from './guards/role.guard';

@Global()
@Module({
  imports: [UserModule, PassportModule, JwtModule, ConfigModule.forRoot()],
  controllers: [AuthController],
  providers: [
    AuthService,
    localGuard,
    LocalStrategy,
    jwtStrategy,
    UsersService,
    jwtGuard,
    RoleGuard
  ],
  exports: [RoleGuard, jwtGuard,JwtModule],
})
export class AuthModule {}
