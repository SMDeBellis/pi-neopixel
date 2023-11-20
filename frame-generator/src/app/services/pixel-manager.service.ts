import { Injectable, OnInit } from '@angular/core';
import { ControlPanelComponent } from '../components/control-panel/control-panel.component';
import { FramesComponent } from '../components/frames/frames.component';

@Injectable({
  providedIn: 'root'
})
export class PixelManagerService implements OnInit {

  constructor(private controlPanel: ControlPanelComponent, private framesComponent: FramesComponent) { }

  ngOnInit(): void {
    this.controlPanel.submitDisplayData().subscribe((formData) => this.framesComponent.buildPixelMatrix(formData));
  }
}
