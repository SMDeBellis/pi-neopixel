import { Component, Input } from '@angular/core';
import { ColorReporterService } from 'src/app/service/color-reporter.service';

@Component({
  selector: 'app-color-matrix',
  templateUrl: './color-matrix.component.html',
  styleUrls: ['./color-matrix.component.css']
})
export class ColorMatrixComponent {
  @Input() rows: number = 0;
  @Input() columns: number = 0;

  rowsArray: any[] = [];
  columnsArray: any[] = [];

  constructor(private colorService: ColorReporterService) {}

  ngOnChanges() {
    this.rowsArray = Array(this.rows).fill(0);
    this.columnsArray = Array(this.columns).fill(0);
  }

  onColorChange(colorEvent: Event) {
    const color = (colorEvent.target as HTMLInputElement).value  as string;
    this.colorService.setColor(color);
  }
}
