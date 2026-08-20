import { Component} from '@angular/core';
import { TransactionStudent } from 'src/app/models/model';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';

@Component({
  selector: 'app-transactions-student',
  templateUrl: './transactions-student.component.html',
  styleUrls: ['./transactions-student.component.scss']
})
export class TransactionsStudentComponent {
  public routes = routes;
  public transactionStudent: TransactionStudent [] = [];

  constructor(private DataService: DataService) {
    this.transactionStudent = this.DataService.transactionStudent;
  }


}
