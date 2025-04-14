import { Injectable, signal } from '@angular/core';

export type BrandType = 'brand-a' | 'brand-b';

@Injectable({
  providedIn: 'root'
})
export class BrandService {
  // Using a signal for reactivity
  private brandSignal = signal<BrandType>('brand-a');
  
  // Expose as readonly
  readonly brand = this.brandSignal.asReadonly();

  constructor() {
    // Apply initial brand
    this.applyBrand(this.brand());
  }

  switchBrand(brand: BrandType): void {
    this.brandSignal.set(brand);
    this.applyBrand(brand);
  }

  private applyBrand(brand: BrandType): void {
    // Remove existing brand classes
    document.body.classList.remove('brand-a', 'brand-b');
    
    // Add current brand class
    document.body.classList.add(brand);
  }
}
