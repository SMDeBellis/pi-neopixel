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
      if(!this.logged_in && this.matrixGenerated){
        this.matrixGenerated = false;
        this.numRows = 0;
        this.numColumns = 0;
      }
    });
    this.colorReporterService.rows$.subscribe( v => {
      this.numRows = v;
    });
    this.colorReporterService.columns$.subscribe( v => {
      this.numColumns = v;
    });
  }

  generateMatrix() {
    this.matrixGenerated = true;
  }
}
