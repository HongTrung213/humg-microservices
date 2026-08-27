import { Component} from '@angular/core';
import { CourseStudent } from 'src/app/models/model';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';

@Component({
  selector: 'app-course-student',
  templateUrl: './course-student.component.html',
  styleUrls: ['./course-student.component.scss']
})
export class CourseStudentComponent  {
  public routes = routes;
  public courseStudent: CourseStudent[] = [];

  constructor(private DataService: DataService) {
    this.courseStudent = this.DataService.courseStudent;}


}
