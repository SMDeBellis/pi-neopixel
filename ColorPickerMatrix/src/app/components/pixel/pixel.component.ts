import { OnInit, Component, Input,  } from '@angular/core';
import { ColorReporterService } from 'src/app/service/color-reporter.service';

@Component({
  selector: 'app-pixel',
  templateUrl: './pixel.component.html',
  styleUrls: ['./pixel.component.css']
})
export class PixelComponent implements OnInit {

  @Input() row: number = 0;
  @Input() col: number = 0;

  constructor(private colorReporterService: ColorReporterService){}

  ngOnInit(){
    // console.log("row: ", this.row, ", col: ", this.col);
  }

  onColorChange(colorEvent: Event) {
    const color = (colorEvent.target as HTMLInputElement).value  as string;
    this.colorReporterService.setColor(color, this.row, this.col);
  }
}
