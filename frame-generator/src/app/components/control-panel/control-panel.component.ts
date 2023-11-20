import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormControl, FormGroup, ReactiveFormsModule } from '@angular/forms';
import { Observable, of } from 'rxjs';

@Component({
  selector: 'app-control-panel',
  templateUrl: './control-panel.component.html',
  styleUrls: ['./control-panel.component.css']
})

export class ControlPanelComponent {
  displayDataForm = new FormGroup ({
    animationId: new FormControl(''),
    row: new FormControl(''),
    col: new FormControl('')
  });

  constructor(){}

  submitDisplayData(): Observable<[string, number, number]> {
    // console.log(this.displayDataForm.value.animationId);
    return of([this.displayDataForm.value.animationId ?? 'undefined', parseInt(this.displayDataForm.value.row ?? '0'), parseInt(this.displayDataForm.value.col ?? '0')]);
  }
}
