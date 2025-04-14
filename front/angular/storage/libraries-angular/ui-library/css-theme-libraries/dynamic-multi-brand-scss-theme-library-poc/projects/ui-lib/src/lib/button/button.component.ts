//projects/ui-lib/src/lib/button/button.component.ts

import { Component } from '@angular/core';

@Component({
  selector: 'ui-button',
  standalone: true,
  imports: [],
  template: `
  
    <button class="btn">
      <ng-content></ng-content>
    </button>
  
  `,
  styles: [
    `
    button {
      background-color: var(--primary-color);
      font-family: var(--font-family);
      color: white; /* Ensure text is readable */
      padding: 8px 16px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      opacity: 0.9;
    }
    
    `
  ]
})
export class ButtonComponent {

}
