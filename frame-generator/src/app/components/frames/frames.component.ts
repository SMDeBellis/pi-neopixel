import { Component } from '@angular/core';

@Component({
  selector: 'app-frames',
  templateUrl: './frames.component.html',
  styleUrls: ['./frames.component.css']
})
export class FramesComponent {

  constructor(){}

  buildPixelMatrix(data: [string, number, number]){
    console.log(data);
  }
}
