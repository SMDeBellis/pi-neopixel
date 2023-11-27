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

  constructor(private colorReporterService: ColorReporterService) {
    // this.colorReporterService.color$.subscribe(color => {
    //   console.log('Color changed:', color);
    // });
  }

  generateMatrix() {
    this.matrixGenerated = true;
  }
}
