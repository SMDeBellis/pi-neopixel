import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { ColorMatrixComponent } from './components/color-matrix/color-matrix.component';
import { ColorReporterService } from './service/color-reporter.service';
import { PixelComponent } from './components/pixel/pixel.component';
import { NavbarComponent } from './components/navbar/navbar.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

@NgModule({
  declarations: [
    AppComponent,
    ColorMatrixComponent,
    PixelComponent,
    NavbarComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    NgbModule
  ],
  providers: [ColorReporterService],
  bootstrap: [AppComponent]
})
export class AppModule { }
