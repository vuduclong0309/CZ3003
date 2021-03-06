import {Injectable} from '@angular/core';
import { Http, Response, Headers, RequestOptions } from '@angular/http'
import {FormGroup, AbstractControl, FormBuilder, Validators} from '@angular/forms';
import {Observable} from 'rxjs/Rx';

import {FormReport}  from './formsreport';
import {BASEURL} from '../baseURL';

@Injectable()
export class AdminService {

  private formsUrl = BASEURL + "reportList/";
  public reportList:any;

  constructor(private http:Http){}

  getReportList(){
    this.reportList = this.http.get(this.formsUrl)
                                .map((res:Response) => res.json() as FormReport)
                                .catch((error:any) => Observable.throw(error.json().error || 'Server error'));

    return this.reportList;
  }


  deleteCrisis(values:FormReport){
      let index: number = this.reportList.indexOf(values.id);
      if(index !== -1){
        this.reportList.splice(index,1);
      }
  }
}
