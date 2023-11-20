import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ColorPickerModule } from 'ngx-color-picker';

import { AppComponent } from './app.component';
import { HeaderComponent } from './components/header/header.component';
import { ButtonComponent } from './components/button/button.component';
import { ControlPanelComponent } from './components/control-panel/control-panel.component';
import { FramesComponent } from './components/frames/frames.component';
import { NumericTextBoxComponent } from './components/numeric-text-box/numeric-text-box.component';
import { PixelComponent } from './components/pixel/pixel.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';


@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    ButtonComponent,
    ControlPanelComponent,
    FramesComponent,
    NumericTextBoxComponent,
    PixelComponent
  ],
  imports: [
    BrowserModule,
    ColorPickerModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
