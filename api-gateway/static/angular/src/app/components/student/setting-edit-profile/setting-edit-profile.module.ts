import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { SettingEditProfileRoutingModule } from './setting-edit-profile-routing.module';
import { SettingEditProfileComponent } from './setting-edit-profile.component';
import { FeatherIconModule } from 'src/app/shared/module/feather.module';
import { SharedModule } from 'src/app/shared/module/shared.module';


@NgModule({
  declarations: [
    SettingEditProfileComponent
  ],
  imports: [
    CommonModule,
    SettingEditProfileRoutingModule,
    FeatherIconModule,
    SharedModule
  ]
})
export class SettingEditProfileModule { }
