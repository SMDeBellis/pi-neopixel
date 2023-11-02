import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { HeaderComponent } from './components/header/header.component';
import { ButtonComponent } from './components/button/button.component';
import { ControlPanelComponent } from './components/control-panel/control-panel.component';
import { FramesComponent } from './components/frames/frames.component';
import { NumericTextBoxComponent } from './components/numeric-text-box/numeric-text-box.component';

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    ButtonComponent,
    ControlPanelComponent,
    FramesComponent,
    NumericTextBoxComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
