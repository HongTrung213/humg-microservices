import { Component } from '@angular/core';
import { studentGrid2 } from 'src/app/models/model';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';


@Component({
  selector: 'app-students-grid2',
  templateUrl: './students-grid2.component.html',
  styleUrls: ['./students-grid2.component.scss']
})
export class StudentsGrid2Component  {
  public routes = routes;
  public studentGrid2: studentGrid2[] = [];

  constructor(private DataService: DataService) {
    this.studentGrid2 = this.DataService.studentGrid2;}

  

}
