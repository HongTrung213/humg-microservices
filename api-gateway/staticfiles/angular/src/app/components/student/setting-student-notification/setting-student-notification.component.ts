import { Component} from '@angular/core';
import { routes } from 'src/app/shared/service/routes/routes';

@Component({
  selector: 'app-setting-student-notification',
  templateUrl: './setting-student-notification.component.html',
  styleUrls: ['./setting-student-notification.component.scss']
})
export class SettingStudentNotificationComponent  {
  public routes = routes;


}
