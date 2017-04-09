import {Injectable} from '@angular/core';
import {Report} from './report';

@Injectable()
export class AdminService {

  public reportList = [
    {
        "id": 1,
        "firstName": "Michael",
        "lastName": "Le",
        "telephone": 12345678,
        "location": "NTU",
        "description": "reporting haze",
        "crisisType": "Haze"
    },
    {
        "id": 2,
        "firstName": "Kelvin",
        "lastName": "Chong",
        "telephone": 98765432,
        "location": "East Coast Park",
        "description": "reporting dengue",
        "crisisType": "Dengue"
    },
    {
        "id": 5,
        "firstName": "Tuan",
        "lastName": "Phan",
        "telephone": 98762345,
        "location": "NTU",
        "description": "very haze",
        "crisisType": "Haze"
    }]

  getReportList(){
    return this.reportList;
  }

  deleteCrisis(values:Report){
      let index: number = this.reportList.indexOf(values.id);
      if(index !== -1){
        this.reportList.splice(index,1);
      }
  }
}