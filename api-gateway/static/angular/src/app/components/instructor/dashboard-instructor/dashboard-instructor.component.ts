import { Component } from '@angular/core';
import { myCourse } from 'src/app/models/model';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';
@Component({
  selector: 'app-dashboard-instructor',
  templateUrl: './dashboard-instructor.component.html',
  styleUrls: ['./dashboard-instructor.component.scss']
})
export class DashboardInstructorComponent  {
  public myCourse : myCourse[] = [];
  public routes = routes;
 constructor(private DataService: DataService) {
    this.myCourse = this.DataService.myCourse;
    } 



}
