import { Component} from '@angular/core';
import { instructorGrid2 } from 'src/app/models/model';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';


@Component({
  selector: 'app-instructor-grid2',
  templateUrl: './instructor-grid2.component.html',
  styleUrls: ['./instructor-grid2.component.scss']
})
export class InstructorGrid2Component  {
  public routes = routes;
  public instructorGrid2: instructorGrid2[] = [];

  constructor(private DataService: DataService) {
    this.instructorGrid2 = this.DataService.instructorGrid2;
  }



}
