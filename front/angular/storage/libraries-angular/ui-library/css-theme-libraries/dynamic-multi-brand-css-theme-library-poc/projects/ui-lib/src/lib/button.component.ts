import { Component, Input, HostBinding, effect } from '@angular/core';
import { NgClass, NgIf } from '@angular/common';
import { BrandService } from './brand.service';

@Component({
  selector: 'button-lib',
  standalone: true,
  imports: [NgClass, NgIf],
  template: `
    <button
      [disabled]="disabled"
      [ngClass]="variant">
      <ng-content></ng-content>
    </button>
  `,
  styles: [`
    :host {
      display: inline-block;
    }
    
    button {
      border: none;
      border-radius: 4px;
      cursor: pointer;
      padding: 8px 16px;
      font-size: 14px;
      transition: all 0.2s ease;
    }
    
    button:disabled {
      opacity: 0.6;
      cursor: not-allowed;
    }
    
    /* Brand A styles */
    :host.brand-a button.primary {
      background-color: var(--brand-a-primary, #1e88e5);
      color: white;
    }
    
    :host.brand-a button.primary:hover:not(:disabled) {
      background-color: var(--brand-a-primary-hover, #1976d2);
    }
    
    :host.brand-a button.secondary {
      background-color: var(--brand-a-secondary, #e0e0e0);
      color: var(--brand-a-text, #212121);
    }
    
    :host.brand-a button.secondary:hover:not(:disabled) {
      background-color: var(--brand-a-secondary-hover, #d5d5d5);
    }
    
    /* Brand B styles */
    :host.brand-b button.primary {
      background-color: var(--brand-b-primary, #6200ea);
      color: white;
    }
    
    :host.brand-b button.primary:hover:not(:disabled) {
      background-color: var(--brand-b-primary-hover, #5600e8);
    }
    
    :host.brand-b button.secondary {
      background-color: var(--brand-b-secondary, #ff4081);
      color: var(--brand-b-text, #212121);
    }
    
    :host.brand-b button.secondary:hover:not(:disabled) {
      background-color: var(--brand-b-secondary-hover, #f50057);
    }
  `]
})
export class ButtonComponent {
  @Input() variant: 'primary' | 'secondary' = 'primary';
  @Input() disabled = false;
  @HostBinding('class') brandClass = '';
  
  constructor(private brandService: BrandService) {
    // React to brand changes using Angular's effect
    effect(() => {
      this.brandClass = this.brandService.brand();
    });
  }
}