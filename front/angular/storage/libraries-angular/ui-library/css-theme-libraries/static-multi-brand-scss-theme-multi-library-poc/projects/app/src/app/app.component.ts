import { Component } from '@angular/core';


import { ButtonComponent } from 'ui-lib';
import { Button2Component } from 'ui-lib-2';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ButtonComponent, Button2Component],
  template: `
  <div>
  <ui-button>Click Me</ui-button>
  </div>
  <div>
    <ui-button-2>Click Me</ui-button-2>
  </div>
  
  `
})
export class AppComponent {}