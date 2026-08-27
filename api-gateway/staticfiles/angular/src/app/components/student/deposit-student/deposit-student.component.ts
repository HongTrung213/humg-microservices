import { Component } from '@angular/core';
import { depositStudent } from 'src/app/models/model';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';

@Component({
  selector: 'app-deposit-student',
  templateUrl: './deposit-student.component.html',
  styleUrls: ['./deposit-student.component.scss']
})
export class DepositStudentComponent  {
  public routes = routes;
  public depositStudent : depositStudent[] = [];

  constructor(private DataService: DataService) {
    this.depositStudent = this.DataService.depositStudent;
    }


}
