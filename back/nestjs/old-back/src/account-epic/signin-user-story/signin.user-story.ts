import { ConflictException, Injectable } from '@nestjs/common';
import { SigninResponse } from './signin-response.dto';
import { SigninRequest } from './signin-request.dto';
import { AccountModel } from '../account.model';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';

@Injectable()
export class SigninUserStory {

  constructor(  
    @InjectModel(AccountModel.name)
    private model: Model<AccountModel>,
    
  ) {}
  
  async execute(createUserRequest: SigninRequest): Promise<SigninResponse> {

    
    
    const user: AccountModel = this.setUser(createUserRequest);

    if (await this.model.findOne({ email: createUserRequest.email })) {
      console.log('Email already exists')
      throw new ConflictException('This email already exists')
    }
    
    const userCreated = await this.model.create(user);

    const createUserResponse: SigninResponse = new SigninResponse();

    createUserResponse.email = userCreated.email;
    createUserResponse.name = userCreated.name;
    createUserResponse.password = userCreated.password;
    createUserResponse.id = userCreated._id;

    return createUserResponse;

  }


  private setUser(createUserRequest: SigninRequest): AccountModel {
    const user: AccountModel = new AccountModel();
    user.email = createUserRequest.email;
    user.name = createUserRequest.name;
    user.password = createUserRequest.password;
    return user;
  }







  // findAll() {
  //   return `This action returns all user`;
  // }



  // update(id: number, updateUserDto: UpdateUserDto) {
  //   return `This action updates a #${id} user`;
  // }

  // remove(id: number) {
  //   return `This action removes a #${id} user`;
  // }
}
