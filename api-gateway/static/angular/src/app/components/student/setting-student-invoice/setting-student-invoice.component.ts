import { Component} from '@angular/core';
import { settingStudentInvoice } from 'src/app/models/model';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';

@Component({
  selector: 'app-setting-student-invoice',
  templateUrl: './setting-student-invoice.component.html',
  styleUrls: ['./setting-student-invoice.component.scss']
})
export class SettingStudentInvoiceComponent  {
  public routes = routes;
  public settingStudentInvoice : settingStudentInvoice [] = [];

  constructor(private DataService: DataService) {
    this.settingStudentInvoice = this.DataService.settingStudentInvoice;
    }


}
