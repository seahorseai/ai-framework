import { Test, TestingModule } from '@nestjs/testing';
import { AccountController } from './account.controller';
import { SigninUserStory } from './signin-user-story/signin.user-story';
import { SigninRequest } from './signin-user-story/signin-request.dto';
import { SigninResponse } from './signin-user-story/signin-response.dto';


describe('AccountController', () => {
  let controller: AccountController;
  
  const MockSigninUserStory = {
    execute: jest.fn()
  }


  beforeEach(async () => {
        const module: TestingModule = await Test.createTestingModule({
          controllers: [AccountController],
          providers: [
            {
              provide: SigninUserStory,
              useValue: MockSigninUserStory,
            },
          ],
        }).compile();
    
        controller = module.get<AccountController>(AccountController);
      });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });


    describe('create usert', () => {
      it('should create a new user', async () => {
      
      const signinRequest: SigninRequest = new SigninRequest();
      signinRequest.email = "pepe@mail.com";
      signinRequest.name = "Pepe";
      signinRequest.password = "changeme";
      signinRequest.confirmPassword = "changeme";
   
      jest.spyOn(MockSigninUserStory, 'execute').mockReturnValue(signinRequest);

      const signinResponse: SigninResponse = await controller.signin(signinRequest);

      expect(MockSigninUserStory.execute).toHaveBeenCalled();
      expect(MockSigninUserStory.execute).toHaveBeenCalledWith(signinRequest)
      expect(signinRequest.email).toEqual(signinResponse.email);
      expect(signinRequest.name).toEqual(signinResponse.name);
      expect(signinRequest.password).toEqual(signinResponse.password);
      })
   })

    

});