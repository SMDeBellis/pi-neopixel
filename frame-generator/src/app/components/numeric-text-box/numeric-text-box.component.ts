import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-numeric-text-box',
  templateUrl: './numeric-text-box.component.html',
  styleUrls: ['./numeric-text-box.component.css']
})
export class NumericTextBoxComponent {
	@Output() numericEntry = new EventEmitter();
	
	processText(value: number){
		console.log(value);
		this.numericEntry.emit(value);
	}
}
