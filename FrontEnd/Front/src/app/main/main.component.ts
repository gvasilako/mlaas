import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Injectable } from '@angular/core';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})

@Injectable({providedIn:'root'})
export class MainComponent  {

  sl : string = '';
  sw : string = '' ;
  pl : string = '';
  pw : string = '' ;
  prediction : string ='';
  baseURL : string = "http://localhost:8000/"

  constructor(private http: HttpClient) { }

  Submit():void {
    let input_data = {
      'sl': + this.sl,
      'sw': + this.sw,
      'pl': + this.pl,
      'pw': + this.pw
    };

    this.Prediction(input_data).subscribe(data => {
      this.prediction = data['Prediction'];
    });
    
  }

  Prediction(data:any): Observable<any>{
    const headers = { 'content-type': 'application/json'}  
    const body=JSON.stringify(data);
    return this.http.post(this.baseURL + 'prediction', body,{'headers':headers})
  }

}
