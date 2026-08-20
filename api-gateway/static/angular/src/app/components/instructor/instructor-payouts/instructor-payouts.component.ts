import { Component } from '@angular/core';
import { withdrawHistory } from 'src/app/models/model';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';

@Component({
  selector: 'app-instructor-payouts',
  templateUrl: './instructor-payouts.component.html',
  styleUrls: ['./instructor-payouts.component.scss']
})
export class InstructorPayoutsComponent  {
  public withdrawHistory: withdrawHistory[] = [];
  public routes = routes;
  selected='option1'
  selected2='option1'
  selected3 ='option1'
  constructor(private DataService: DataService) {
    this.withdrawHistory = this.DataService.withdrawHistory;
  }


}

