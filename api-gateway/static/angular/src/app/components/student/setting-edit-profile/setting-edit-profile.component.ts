import { Component } from '@angular/core';
import { routes } from 'src/app/shared/service/routes/routes';

@Component({
  selector: 'app-setting-edit-profile',
  templateUrl: './setting-edit-profile.component.html',
  styleUrls: ['./setting-edit-profile.component.scss']
})
export class SettingEditProfileComponent  {
  public routes = routes;
  selected ='option1';

}
