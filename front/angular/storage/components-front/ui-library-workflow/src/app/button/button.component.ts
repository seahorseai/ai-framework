import { Component, EventEmitter, Input, Output } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-button',
  standalone: true,
  imports: [CommonModule],
  template:`
    
      <button [disabled]="disabled" [ngClass]="variant">{{ label }}</button>
  
  `,
  styles:[

    `
    button.primary { background-color: var(--primary-color); }
    button.secondary { background-color: var(--secondary-color); }
  `
  ]
})
export class ButtonComponent {

  @Input() label!: string;
  @Input() variant: 'primary' | 'secondary' = 'primary';
  @Input() disabled = false;
  @Output() clicked = new EventEmitter<void>();

}
