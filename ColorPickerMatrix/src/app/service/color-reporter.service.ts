import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Subject } from 'rxjs';
import { v4 as uuid } from 'uuid';

@Injectable({
  providedIn: 'root'
})
export class ColorReporterService {
  private colorSubject = new Subject<{ color: string; row: number; col: number }>;
  color$ = this.colorSubject.asObservable();

  private connectedSubject = new BehaviorSubject<boolean>(false);
  connected$ = this.connectedSubject.asObservable();
  connection_uuid: string = "";

  constructor(private http: HttpClient) {}

  setColor(color: string, row: number, col: number) {
    this.colorSubject.next({color: color, row: row, col: col});
    this.sendColorToAPI({ color, row, col }).subscribe( 
      response => console.log('Color sent to API:', response),
      error => console.error('Error sending color to API:', error)
    );
  }

  private sendColorToAPI(data: { color: string, row: number, col: number }) {
    const apiUrl = 'http://10.0.0.110:5000/picker-change';
    let wrapped_data = {"data": [data]} 
    return this.http.post(apiUrl, wrapped_data);
  }

  connect() {
    if(this.connection_uuid == ""){
      this.sendConnect().subscribe(
        response => { 
          console.log(response);
          this.connectedSubject.next(true);
        },
        error => {
          console.log("Error connecting to server.");
          this.connectedSubject.next(false);
          this.connection_uuid = "";
        }
      );
    }
  }

  private sendConnect() {
    this.connection_uuid = uuid();
    const apiUrl = 'http://10.0.0.110:5000/connect';
    return this.http.post(apiUrl, { "connection-id":  this.connection_uuid});
  }

  logout() {
    this.sendLogout().subscribe(response => { 
      console.log(response);
      this.connectedSubject.next(false);
      this.connection_uuid = "";
    },
    error => {
      console.log("Error connecting to server.");
      this.connectedSubject.next(false);
    })
  }

  sendLogout() {
    const apiUrl = 'http://10.0.0.110:5000/logout';
    return this.http.post(apiUrl, { "logout": true, "connection-id:": this.connection_uuid });
  }
}
 