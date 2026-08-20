import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { InstructorEditRoutingModule } from './instructor-edit-routing.module';
import { InstructorEditComponent } from './instructor-edit.component';
import { FeatherIconModule } from 'src/app/shared/module/feather.module';
import { RouterModule } from '@angular/router';


@NgModule({
  declarations: [
    InstructorEditComponent
  ],
  imports: [
    CommonModule,
    InstructorEditRoutingModule,
    FeatherIconModule,
    RouterModule
  ]
})
export class InstructorEditModule { }
