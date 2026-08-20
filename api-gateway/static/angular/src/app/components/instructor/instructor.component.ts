import { Component } from '@angular/core';
import { NavigationStart, Router, Event as RouterEvent } from '@angular/router';
import { SidebarItem, url } from 'src/app/models/model';
import { CommonService } from 'src/app/shared/service/common/common.service';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';

@Component({
  selector: 'app-instructor',
  templateUrl: './instructor.component.html',
  styleUrls: ['./instructor.component.scss'],
})
export class InstructorComponent {
  public routes = routes;
  base = '';
  page = '';
  last = '';
  side_bar_data: SidebarItem[] = [];
  instructor = true;
  dashboard = true;
  constructor(
    private common: CommonService,
    private Router: Router,
    private data: DataService
  ) {
    this.common.base.subscribe((res: string) => {
      this.base = res;
    });
    this.common.page.subscribe((res: string) => {
      this.page = res;
    });
    this.common.last.subscribe((res: string) => {
      this.last = res;
    });

    Router.events.subscribe((event: RouterEvent) => {
      if (event instanceof NavigationStart) {
        this.getRoutes(event);
      }
    });
    this.getRoutes(this.Router);

    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    this.data.getInstructorSideBarData.subscribe((res: any) => {
      this.side_bar_data = res;
    });
  }

  getRoutes(event: url) {
    const splitVal = event.url.split('/');
    this.base = splitVal[1];
    this.page = splitVal[2];
    this.last = splitVal[3];
    if (
      event.url === '/instructor/instructor-profile' ||
      event.url === '/instructor/dashboard-instructor' ||
      event.url === '/instructor/deposit-instructor-dashboard' ||
      event.url === '/instructor/instructor-profile' ||
      event.url === '/instructor/instructor-new-tickets' ||
      event.url === '/instructor/instructor-view/instructor-list' ||
      event.url === '/instructor/instructor-view/instructor-grid' ||
      event.url === '/instructor/instructor-chat'
    ) {
      this.instructor = false;
    } else {
      this.instructor = true;
    }
  }
}
