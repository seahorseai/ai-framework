import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { MongooseModule } from '@nestjs/mongoose';
import { AccountModule } from './account-epic/account.module';

@Module({
  imports: [
    MongooseModule.forRoot('mongodb://root:1234@localhost:27017/',{
      dbName: 'seahorse'
    }),
      AccountModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
