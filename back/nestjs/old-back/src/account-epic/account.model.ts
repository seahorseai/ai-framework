import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import mongoose, { HydratedDocument, } from 'mongoose';

export type AccountModelHydratedDocument = HydratedDocument<AccountModel>;

@Schema()
export class AccountModel {
    
    @Prop()
    name: string;
    @Prop({ unique: true, length: 100,  })
    email: string;
    @Prop()
    password: string;
    organizationId: mongoose.Types.ObjectId;


}

export const AccountModelSchema = SchemaFactory.createForClass(AccountModel);
