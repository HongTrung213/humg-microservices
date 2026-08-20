import { Component } from '@angular/core';
import { routes } from 'src/app/shared/service/routes/routes';

@Component({
  selector: 'app-setting-student-privacy',
  templateUrl: './setting-student-privacy.component.html',
  styleUrls: ['./setting-student-privacy.component.scss']
})
export class SettingStudentPrivacyComponent  {
  public routes = routes;
  selected='option1';


}
