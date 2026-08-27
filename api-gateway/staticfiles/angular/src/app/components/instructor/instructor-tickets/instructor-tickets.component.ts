import { Component, OnInit } from '@angular/core';
import { instructorTickets1, instructorTickets2, instructorTickets3, instructorTickets4 } from 'src/app/models/model';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';

@Component({
  selector: 'app-instructor-tickets',
  templateUrl: './instructor-tickets.component.html',
  styleUrls: ['./instructor-tickets.component.scss']
})
export class InstructorTicketsComponent implements OnInit {
  public routes = routes;
  public instructorTickets1: instructorTickets1[] = [];
  public instructorTickets2: instructorTickets2[] = [];
  public instructorTickets3: instructorTickets3[] = [];
  public instructorTickets4: instructorTickets4[] = [];

  constructor(private DataService: DataService) {
    
  }

  ngOnInit(): void {
    this.tableData1();
    this.tableData2();
    this.tableData3();
    this.tableData4();
  }
  private tableData1(): void {
    this.instructorTickets1= [];
    this.DataService.instructorTicket1().subscribe((res) => {
      res.data.map((res: instructorTickets1) => {
        this.instructorTickets1.push(res);
      });

    });
  }
  private tableData2(): void {
    this.instructorTickets2= [];
    this.DataService.instructorTicket2().subscribe((res) => {
      res.data.map((res: instructorTickets2) => {
        this.instructorTickets2.push(res);
      });

    });
  }
  private tableData3(): void {
    this.instructorTickets3= [];
    this.DataService.instructorTicket3().subscribe((res) => {
      res.data.map((res: instructorTickets3) => {
        this.instructorTickets3.push(res);
      });

    });
  }
  private tableData4(): void {
    this.instructorTickets4= [];
    this.DataService.instructorTicket4().subscribe((res) => {
      res.data.map((res: instructorTickets4) => {
        this.instructorTickets4.push(res);
      });

    });
  }
}
