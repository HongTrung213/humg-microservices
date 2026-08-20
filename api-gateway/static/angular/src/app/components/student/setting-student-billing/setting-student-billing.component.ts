import { Component } from '@angular/core';
import { routes } from 'src/app/shared/service/routes/routes';

@Component({
  selector: 'app-setting-student-billing',
  templateUrl: './setting-student-billing.component.html',
  styleUrls: ['./setting-student-billing.component.scss']
})
export class SettingStudentBillingComponent  {
  public routes = routes;



}
