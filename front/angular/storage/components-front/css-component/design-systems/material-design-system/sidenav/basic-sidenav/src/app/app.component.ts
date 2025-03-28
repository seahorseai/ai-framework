import { Component, ViewChild } from '@angular/core';
import { MatSidenav, MatSidenavModule } from '@angular/material/sidenav';
import { MatButtonModule } from '@angular/material/button';

/** @title Sidenav with custom escape and backdrop click behavior */
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  standalone: true,
  imports: [
    MatSidenavModule,
    MatButtonModule,
  ],
})
export class AppComponent {
  title = 'sidenav';

  @ViewChild('sidenav') sidenav!: MatSidenav;

  reason = '';

  close(reason: string) {
    this.reason = reason;
    this.sidenav.close();
  }

 
}










// import { Component } from '@angular/core';
// import { RouterOutlet } from '@angular/router';
// import {MatSidenav, MatSidenavModule} from '@angular/material/sidenav';
// import {MatButtonModule} from '@angular/material/button';

// @Component({
//   selector: 'app-root',
//   standalone: true,
//   imports: [MatSidenavModule, MatButtonModule, RouterOutlet],
//   templateUrl: './app.component.html',
//   styleUrl: './app.component.css'
// })
// export class AppComponent {
//   title = 'sidenav';
//   sidenav!: MatSidenav;

//   reason = '';

//   close(reason: string) {
//     this.reason = reason;
//     this.sidenav.close();
//   }
// }

