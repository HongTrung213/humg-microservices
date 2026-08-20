import { Component} from '@angular/core';
import { settingSupportTickets1, settingSupportTickets2, settingSupportTickets3, settingSupportTickets4 } from 'src/app/models/model';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';

@Component({
  selector: 'app-setting-support-tickets',
  templateUrl: './setting-support-tickets.component.html',
  styleUrls: ['./setting-support-tickets.component.scss']
})
export class SettingSupportTicketsComponent  {
  public routes = routes;
  public settingSupportTickets1: settingSupportTickets1[] = [];
  public settingSupportTickets2: settingSupportTickets2[] = [];
  public settingSupportTickets3: settingSupportTickets3[] = [];
  public settingSupportTickets4: settingSupportTickets4[] = [];

  constructor(private DataService: DataService) {
    this.settingSupportTickets1 = this.DataService.settingSupportTickets1;
    this.settingSupportTickets2 = this.DataService.settingSupportTickets2;
    this.settingSupportTickets3 = this.DataService.settingSupportTickets3;
    this.settingSupportTickets4 = this.DataService.settingSupportTickets4;
  }

 

}
