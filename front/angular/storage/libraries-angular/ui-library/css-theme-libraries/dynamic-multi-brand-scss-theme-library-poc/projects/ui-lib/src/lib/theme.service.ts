// projects/ui-lib/src/lib/theme.service.ts

import { Injectable } from "@angular/core";
@Injectable({
    providedIn: 'root'
  })
  export class ThemeService {
    setTheme(theme: string) {
      document.documentElement.className = theme;
    }
  }