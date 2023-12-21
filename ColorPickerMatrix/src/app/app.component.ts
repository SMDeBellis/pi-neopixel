import { Component } from '@angular/core';
import { ColorReporterService } from './service/color-reporter.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  numRows: number = 0;
  numColumns: number = 0;
  matrixGenerated: boolean = false;
  logged_in: boolean = false;

  constructor(private colorReporterService: ColorReporterService) {
    this.colorReporterService.connected$.subscribe( v => {
      console.log("loggedIn: ", v);
      this.logged_in = v;

    });
  }

  generateMatrix() {
    if(this.logged_in) {
      this.matrixGenerated = true;
    }
    
  }
}
