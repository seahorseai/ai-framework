
import { Meta, StoryObj } from "@storybook/angular";
import { ButtonComponent } from "./button.component";

export default {

    title: 'Components/Button',
    component: ButtonComponent,
  
    argTypes: {
      label: { control: 'text' },
      variant: { control: 'select', options: ['primary', 'secondary'] },
      disabled: { control: 'boolean' },
    },
  } as Meta<ButtonComponent>;
  
  
  export const primary: StoryObj<ButtonComponent> = {
    args: {
      label: 'Primary Button',
      variant: 'primary',
    },
  };
  
  export const secondary: StoryObj<ButtonComponent> = {
    args: {
      label: 'Secondary Button',
      variant: 'secondary',
    },
  };