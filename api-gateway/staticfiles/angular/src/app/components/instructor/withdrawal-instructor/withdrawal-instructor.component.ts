import { Component} from '@angular/core';
import { withdrawalInstructor, withdrawalInstructorProfile } from 'src/app/models/model';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';

@Component({
  selector: 'app-withdrawal-instructor',
  templateUrl: './withdrawal-instructor.component.html',
  styleUrls: ['./withdrawal-instructor.component.scss']
})
export class WithdrawalInstructorComponent  {
  public withdrawalInstructor: withdrawalInstructor[] = [];
  public routes = routes;
  public withdrawalInstructorProfile: withdrawalInstructorProfile[] = [];

  constructor(private DataService: DataService) {
    this.withdrawalInstructor = this.DataService.withdrawalInstructor;
    this.withdrawalInstructorProfile = this.DataService.withdrawalInstructorProfile;

  }

}
