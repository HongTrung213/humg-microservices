import { Component } from '@angular/core';
import { depositHistory, depositInstructor } from 'src/app/models/model';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';

@Component({
  selector: 'app-deposit-instructor',
  templateUrl: './deposit-instructor.component.html',
  styleUrls: ['./deposit-instructor.component.scss']
})
export class DepositInstructorComponent  {
  public depositHistory: depositHistory[] = [];
  public routes = routes;
  public depositInstructor: depositInstructor[] = [];

  constructor(private DataService: DataService) {
    this.depositHistory = this.DataService.depositHistory;
    this.depositInstructor = this.DataService.depositInstructor;

  }


}
