import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ColorReporterService {
  private colorSubject = new Subject<{ color: string; }>;
  color$ = this.colorSubject.asObservable();

  constructor(private http: HttpClient) {}

  setColor(color: string) {
    this.colorSubject.next({color: color});
    this.sendColorToAPI({ color }).subscribe(
      response => console.log('Color sent to API:', response),
      error => console.error('Error sending color to API:', error)
    );
  }

  private sendColorToAPI(data: { color: string }) {
    const apiUrl = 'https://myapi.org/picker-change';
    return this.http.post(apiUrl, data);
  }
}
