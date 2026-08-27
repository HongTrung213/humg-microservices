import { Component } from '@angular/core';
import { routes } from 'src/app/shared/service/routes/routes';

@Component({
  selector: 'app-setting-student-accounts',
  templateUrl: './setting-student-accounts.component.html',
  styleUrls: ['./setting-student-accounts.component.scss']
})
export class SettingStudentAccountsComponent  {
  public routes = routes;


}
