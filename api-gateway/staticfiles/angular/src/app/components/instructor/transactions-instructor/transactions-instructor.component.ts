import { Component} from '@angular/core';
import { transactionInstructorProfile, transactionsInstructor } from 'src/app/models/model';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';

@Component({
  selector: 'app-transactions-instructor',
  templateUrl: './transactions-instructor.component.html',
  styleUrls: ['./transactions-instructor.component.scss']
})
export class TransactionsInstructorComponent  {
  public routes = routes;
  public transactionsInstructor: transactionsInstructor[] = [];
  public transactionInstructorProfile: transactionInstructorProfile[] = [];

  constructor(private DataService: DataService) {
    this.transactionsInstructor = this.DataService.transactionsInstructor;
    this.transactionInstructorProfile = this.DataService.transactionInstructorProfile;
  }

}
