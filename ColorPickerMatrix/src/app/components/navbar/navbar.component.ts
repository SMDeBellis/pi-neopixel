import { Component, Input } from '@angular/core';
import { ColorReporterService } from '../../service/color-reporter.service';

@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent {
  @Input() logged_in: boolean = false;

  constructor(private service: ColorReporterService ){
    service.connected$.subscribe(v => {
      console.log("logged_in changing to: ", v)
      this.logged_in = v
    });

  }

  logout() {
    // Add your logout logic here
    console.log('Logout clicked');
    this.service.logout();
  }

  connect() {
    console.log('Connect clicked');
    this.service.connect();
  }
}