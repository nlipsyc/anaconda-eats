import { Injectable } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class AnacondaEatsService {
  private readonly apiBase = '/api/'

  constructor(private http: HttpClient) { }
}
