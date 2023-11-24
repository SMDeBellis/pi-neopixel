import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ColorReporterService {
  private colorSubject = new Subject<{ color: string; row: number; column: number }>;
  color$ = this.colorSubject.asObservable();

  constructor(private http: HttpClient) {}

  setColor(color: string, row: number, column: number) {
    this.colorSubject.next({ color, row, column });
    this.sendColorToAPI({ color, row, column }).subscribe(
      response => console.log('Color sent to API:', response),
      error => console.error('Error sending color to API:', error)
    );
  }

  private sendColorToAPI(data: { color: string; row: number; column: number }) {
    const apiUrl = 'https://myapi.org/picker-change';
    return this.http.post(apiUrl, data);
  }
}
