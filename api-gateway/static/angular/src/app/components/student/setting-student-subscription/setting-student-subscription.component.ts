import { Component } from '@angular/core';
import { settingStudentActive, settingStudentExpired } from 'src/app/models/model';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';


@Component({
  selector: 'app-setting-student-subscription',
  templateUrl: './setting-student-subscription.component.html',
  styleUrls: ['./setting-student-subscription.component.scss']
})
export class SettingStudentSubscriptionComponent {
  public routes = routes;
  public settingStudentActive: settingStudentActive[] = [];
  public settingStudentExpired: settingStudentExpired[] = [];

  constructor(private DataService: DataService) {
    this.settingStudentActive = this.DataService.settingStudentActive;
    this.settingStudentExpired = this.DataService.settingStudentExpired;

  }



}
