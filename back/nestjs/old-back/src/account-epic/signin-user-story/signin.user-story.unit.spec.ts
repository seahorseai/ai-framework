import { Test, TestingModule } from '@nestjs/testing';
import { SigninUserStory } from './signin.user-story';
import { AccountModel, AccountModelHydratedDocument } from '../account.model';
import { SigninRequest } from './signin-request.dto';
import { SigninResponse } from './signin-response.dto';
import { Model } from 'mongoose';
import { getModelToken } from '@nestjs/mongoose';


describe('UserService', () => {
  let service: SigninUserStory;
  let userModel: Model<AccountModelHydratedDocument>;
  const userModeltoken = getModelToken('AccountModel');
  

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [SigninUserStory,
        {
          provide: userModeltoken,
          useValue: {
            exec: jest.fn(),
          }
        }

      ],
      
    }).compile();

    userRepository = module.get('UserRepository');
    service = module.get<SigninUserStory>(SigninUserStory);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });


  it('should create a new user', async () => {
    const createUserRequest: SigninRequest = new SigninRequest();
      createUserRequest.email = "pepe@mail.com";
      createUserRequest.name = "Pepe";
      createUserRequest.password = "changme";

      const createUserResponse: SigninResponse = await service.execute(createUserRequest);
      
      expect(createUserRequest.email).toEqual(createUserResponse.email);
      expect(createUserRequest.name).toEqual(createUserResponse.name);
      expect(createUserRequest.password).toEqual(createUserResponse.password);
  });



  it('should find a User by Id', async () => {

    const createUserRequest: SigninRequest = new SigninRequest();
    createUserRequest.email = "pepe@mail.com";
    createUserRequest.name = "Pepe";
    createUserRequest.password = "changme";

    const createUserResponse: SigninResponse = await service.execute(createUserRequest);

    const getUserResponse: GetUserResponse = await service.findOne(createUserResponse.id);
    expect(getUserResponse.email).toEqual(createUserResponse.email);
    expect(getUserResponse.name).toEqual(createUserResponse.name);
    expect(getUserResponse.password).toEqual(createUserResponse.password);
  })






});
