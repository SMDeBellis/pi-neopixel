import { OnInit, Component, Input, Output, EventEmitter, Injectable, Inject } from '@angular/core';
import { Pixel } from '../../Pixel';
import { Observable } from 'rxjs';
import { Event } from '@angular/router';

@Component({
  selector: 'app-pixel',
  templateUrl: './pixel.component.html',
  styleUrls: ['./pixel.component.css']
})
export class PixelComponent implements OnInit {

  pixel!: Pixel;
  @Input() id!: string;
  @Input() row!: string;
  @Input() col!: string;
  @Input() color: string = "rgb(0,0,0)";
  @Input() changedColor: string = "";
  @Output() colorChanged: EventEmitter<Pixel> = new EventEmitter();

  constructor() {}

  ngOnInit(): void {
    this.pixel = {
      "id": parseInt(this.id), 
      "row": parseInt(this.row),
      "col": parseInt(this.col),
      "rgb_color": this.color
    } as Pixel
  }

  onColorPickerColorChange(changedColor: string) {
    this.pixel.rgb_color = changedColor;
    this.colorChanged.emit(this.pixel); 
  }
}
