/* eslint-disable @typescript-eslint/no-explicit-any */
import { Component, OnInit, ViewChild } from '@angular/core';
import {ChartComponent,ApexAxisChartSeries,ApexChart,ApexXAxis,ApexDataLabels,ApexTooltip,ApexStroke,ApexPlotOptions,ApexLegend,ApexYAxis,ApexFill,ApexGrid} from "ng-apexcharts";
import { instructorEarnings } from 'src/app/models/model';
import { DataService } from 'src/app/shared/service/data/data.service';
import { routes } from 'src/app/shared/service/routes/routes';
export type ChartOptions = {
   
  series: ApexAxisChartSeries |any;
  chart: ApexChart |any;
  xaxis: ApexXAxis |any;
  yaxis: ApexYAxis |any;
  stroke: ApexStroke |any;
  tooltip: ApexTooltip |any;
  dataLabels: ApexDataLabels |any;
  plotOptions: ApexPlotOptions |any;
  fill: ApexFill |any;
  legend: ApexLegend |any;
  grid: ApexGrid |any;
};

@Component({
  selector: 'app-instructor-earnings',
  templateUrl: './instructor-earnings.component.html',
  styleUrls: ['./instructor-earnings.component.scss']
})
export class InstructorEarningsComponent implements OnInit {
  public routes = routes;
  @ViewChild("chart") chart!: ChartComponent;
  public Areachart!: Partial<ChartOptions>;
  public instructorEarnings : instructorEarnings[] = [];

  constructor(private DataService: DataService) {
    this.instructorEarnings = this.DataService.instructorEarnings;
    }

  ngOnInit(): void {
    this.Areachart = {
      series: [
        {
          name: "Current month",data: [0, 10, 40, 43, 40, 25, 35, 25, 40, 30],color: "#FF9364"
        },
      ],
      chart: {
        height: 300,
        type: "area",
        toolbar: {
          show: false
        },
        zoom: {
          enabled: false
        }
      },
      dataLabels: {
        enabled: false
      },
      legend: {
        position: 'top',
        horizontalAlign: 'right',
       },
       grid: {
        show: false,
      },
      stroke: {
        curve: "smooth",
        width: 3,
      },
      xaxis: {
        categories: ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      },
      yaxis: {
        axisBorder: {
          show: true,
        },
      },
    };
  }

  public generateData(baseval: number, count: number, yrange: { max: number; min: number; }) {
    let i = 0;
    const series = [];
    while (i < count) {
      const x = Math.floor(Math.random() * (750 - 1 + 1)) + 1;
      const y =
        Math.floor(Math.random() * (yrange.max - yrange.min + 1)) + yrange.min;
      const z = Math.floor(Math.random() * (75 - 15 + 1)) + 15;

      series.push([x, y, z]);
      baseval += 86400000;
      i++;
    }
    return series;
  }
}
