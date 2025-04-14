import { Component } from '@angular/core';


import { ButtonComponent } from 'ui-lib';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ButtonComponent],
  template: `<ui-button>Click Me</ui-button>`
})
export class AppComponent {}