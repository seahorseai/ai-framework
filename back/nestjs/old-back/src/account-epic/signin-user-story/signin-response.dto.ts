import { ApiProperty } from "@nestjs/swagger";
import mongoose from "mongoose";

export class SigninResponse {
    @ApiProperty()
    id: mongoose.Types.ObjectId;
    @ApiProperty()
    name: string;
    @ApiProperty()
    email: string;
    @ApiProperty()
    password: string;
}