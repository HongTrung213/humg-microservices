import { Component } from '@angular/core';
import { profileDetails, referredUsers, depositInstructorDashboard } from 'src/app/models/model';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';
@Component({
  selector: 'app-deposit-instructor-dashboard',
  templateUrl: './deposit-instructor-dashboard.component.html',
  styleUrls: ['./deposit-instructor-dashboard.component.scss']
})
export class DepositInstructorDashboardComponent  {
  public profileDetails: profileDetails[] = []; 
  public routes = routes;
  public referredUsers: referredUsers[] = [];
  public depositInstructorDashboard:depositInstructorDashboard[]= [];


  constructor(private DataService: DataService) {
    this.profileDetails = this.DataService.profileDetails;
    this.referredUsers = this.DataService.referredUsers;
    this.depositInstructorDashboard = this.DataService.depositInstructorDashboard;

  }



}
