import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { ColorMatrixComponent } from './components/color-matrix/color-matrix.component';
import { ColorReporterService } from './service/color-reporter.service';

@NgModule({
  declarations: [
    AppComponent,
    ColorMatrixComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [ColorReporterService],
  bootstrap: [AppComponent]
})
export class AppModule { }
