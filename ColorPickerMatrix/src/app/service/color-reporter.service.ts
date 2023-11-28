import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ColorReporterService {
  private colorSubject = new Subject<{ color: string; row: number; col: number }>;
  color$ = this.colorSubject.asObservable();
  private logoutSubject = new BehaviorSubject<boolean>(false);
  logout$ = this.logoutSubject.asObservable();

  constructor(private http: HttpClient) {}

  setColor(color: string, row: number, col: number) {
    this.colorSubject.next({color: color, row: row, col: col});
    this.sendColorToAPI({ color, row, col }).subscribe( 
      response => console.log('Color sent to API:', response),
      error => console.error('Error sending color to API:', error)
    );
  }

  private sendColorToAPI(data: { color: string, row: number, col: number }) {
    const apiUrl = 'https://localhost/picker-change';
    return this.http.post(apiUrl, data);
  }

  logout() {
    this.sendLogout().subscribe(
      response => console.log("logged out of matrix."),
      error => console.error("Error sending logout.")
    );
  }

  private sendLogout() {
    const apiUrl = 'https://localhost/logout';
    return this.http.post(apiUrl, { "logout": true });
  }
}
 