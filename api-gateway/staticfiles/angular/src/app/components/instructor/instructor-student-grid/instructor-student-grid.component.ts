import { Component } from '@angular/core';
import { instructorStudentGrid } from 'src/app/models/model';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';

@Component({
  selector: 'app-instructor-student-grid',
  templateUrl: './instructor-student-grid.component.html',
  styleUrls: ['./instructor-student-grid.component.scss']
})
export class InstructorStudentGridComponent  {
  public routes = routes;
  public instructorStudentGrid: instructorStudentGrid[] = [];

  constructor(private DataService: DataService) {
    this.instructorStudentGrid = this.DataService.instructorStudentGrid;
  }


}
