import { ApiProperty } from "@nestjs/swagger";
import { IsEmail, IsNotEmpty, IsString, Length, } from 'class-validator';


export class SigninRequest {


    @IsString({ message: 'Should be a string' })
    @IsNotEmpty({ message: 'Name should not be empty' })
    @ApiProperty()
    name: string;

    @IsEmail({}, { message: 'Should be a valid email' })
    @IsNotEmpty({ message: 'Email should not be empty' })
    @ApiProperty()
    email: string;

    //TODO Regex
    @IsString({ message: 'Should be a string' })
    @IsNotEmpty({ message: 'Password should not be empty' })
    @ApiProperty()
    password: string;

    @IsString({ message: 'Should be a string' })
    @IsNotEmpty({ message: 'Password should not be empty' })
    @ApiProperty()
    confirmPassword: string;
}


