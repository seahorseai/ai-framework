import { plainToInstance } from "class-transformer";
import { validate } from "class-validator";
import { SigninRequest } from "./signin-request.dto";


describe("User Entity", () => {
  it("should create a new instance without validation's errors", async () => {
    const siginRequest: SigninRequest = {
        name: "pepe",
        email: "pepe@email.com",
        password: "pepe1234",
        confirmPassword: ''
      }
    const userEntity = plainToInstance(SigninRequest, siginRequest);
    const errors = await validate(userEntity);
    expect(errors.length).toBe(0);
  });
});