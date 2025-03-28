import { Module } from '@nestjs/common';

import { SigninUserStory } from './signin-user-story/signin.user-story';
import { AccountController } from './account.controller';


@Module({
  controllers: [AccountController],
  providers: [SigninUserStory],
})
export class AccountModule {}
