import React, {  useState } from "react";
import ReactApexChart from "react-apexcharts";
import { Link } from "react-router-dom";
import Footer from "../../footer";
import {
  Course10,
  Course11,
  Course12
} from "../../imagepath";
import { InstructorHeader } from "../header";
import InstructorSidebar from "../sidebar";

export default function InstructorEarnings() {
  const [initialState] = useState({
    series: [
      {
        name: "Current Month",
        data: [0, 10, 40, 43, 40, 25, 35, 25, 40, 30],
      },
    ],

    options: {
      chart: {
        height: 300,
        type: "area",
        toolbar: {
          show: false,
        },
      },
      dataLabels: {
        enabled: false,
      },
      stroke: {
        curve: "smooth",
        width: 3,
      },
      colors: ["#FF875A"],
      fill: {
        gradient: {
          opacityFrom: 0.6,
          opacityTo: 0.5,
        },
      },
      axisBorder: {
        show: true,
        color: "#78909C",
        offsetX: 0,
        offsetY: 0,
      },
      xaxis: {
        categories: [
          "",
          "Jan",
          "Feb",
          "Mar",
          "Apr",
          "May",
          "Jun",
          "Jul",
          "Aug",
          "Sep",
          "Oct",
        ],
      },

      title: {
        text: undefined,
        offsetX: 0,
        offsetY: 0,
        style: {
          color: undefined,
          fontSize: "12px",
          fontFamily: "Helvetica, Arial, sans-serif",
          fontWeight: 600,
          cssClass: "apexcharts-xaxis-title",
        },
      },
      yaxis: {
        // seriesName: "seriesY",
        logbase: 10,
        // logarithmic: true,
        tickAmount: 5,
        axisBorder: {
          show: true,
          color: "#E5E4E2",
          offsetX: 0,
          offsetY: 0,
        },
      },
      grid: {
        show: true, // you can either change hear to disable all grids
        xaxis: {
          lines: {
            show: false, //or just here to disable only x axis grids
          },
        },
        yaxis: {
          lines: {
            show: false, //or just here to disable only y axis
          },
        },
      },
      markers: {
        size: 3,
        colors: undefined,
        strokeColors: "#fff",
        strokeWidth: 2,
        strokeOpacity: 0.9,
        strokeDashArray: 0,
        fillOpacity: 1,
        discrete: [],
        shape: "circle",
        radius: 2,
        offsetX: 0,
        offsetY: 0,
        onClick: undefined,
        onDblClick: undefined,
        showNullDataPoints: true,
        hover: {
          size: 8,
          sizeOffset: 3,
        },
      },
      tooltip: {
        x: {
          // format: "dd/MM/yy HH:mm",
        },
      },
    },
  });
  return (
    <div className="main-wrapper">
      <InstructorHeader activeMenu={"Earnings"} />
      <div className="page-content">
        <div className="container">
          <div className="row">
            {/* Sidebar */}
            <InstructorSidebar activeMenu={"Earnings"} />
            {/* Sidebar */}

            {/* Instruction Dashboard */}
            <div className="col-xl-9 col-lg-8 col-md-12">
              <div className="row">
                <div className="col-md-4 d-flex">
                  <div className="card instructor-card w-100">
                    <div className="card-body">
                      <div className="instructor-inner">
                        <h6>REVENUE</h6>
                        <h4 className="instructor-text-success">$467.34</h4>
                        <p>Earning this month</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div className="col-md-4 d-flex">
                  <div className="card instructor-card w-100">
                    <div className="card-body">
                      <div className="instructor-inner">
                        <h6>STUDENTS ENROLLMENTS</h6>
                        <h4 className="instructor-text-info">12,000</h4>
                        <p>New this month</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div className="col-md-4 d-flex">
                  <div className="card instructor-card w-100">
                    <div className="card-body">
                      <div className="instructor-inner">
                        <h6>COURSES RATING</h6>
                        <h4 className="instructor-text-warning">4.80</h4>
                        <p>Rating this month</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className="row">
                <div className="col-md-12">
                  <div className="card instructor-card">
                    <div className="card-header">
                      <h4>Earnings</h4>
                    </div>
                    <div className="card-body">
                      <div id="instructor_chart">
                        <ReactApexChart
                          options={initialState.options}
                          series={initialState.series}
                          type="area"
                          height={300}
                        />
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <div className="row">
                <div className="col-md-12">
                  <div className="settings-widget">
                    <div className="settings-inner-blk p-0">
                      <div className="sell-course-head comman-space">
                        <h3>Best Selling Courses</h3>
                      </div>
                      <div className="comman-space pb-0">
                        <div className="settings-tickets-blk course-instruct-blk table-responsive">
                          {/* Referred Users */}
                          <table className="table table-nowrap">
                            <thead>
                              <tr>
                                <th>COURSES</th>
                                <th>SALES</th>
                                <th>AMOUNT</th>
                              </tr>
                            </thead>
                            <tbody>
                              <tr>
                                <td>
                                  <div className="sell-table-group d-flex align-items-center">
                                    <div className="sell-group-img">
                                      <Link to="/course-details">
                                        <img
                                          src={Course10}
                                          className="img-fluid "
                                          alt=""
                                        />
                                      </Link>
                                    </div>
                                    <div className="sell-tabel-info">
                                      <p>
                                        <Link to="/course-details">
                                          Information About UI/UX Design Degree
                                        </Link>
                                      </p>
                                    </div>
                                  </div>
                                </td>
                                <td>34</td>
                                <td>$3,145.23</td>
                              </tr>
                              <tr>
                                <td>
                                  <div className="sell-table-group d-flex align-items-center">
                                    <div className="sell-group-img">
                                      <Link to="/course-details">
                                        <img
                                          src={Course11}
                                          className="img-fluid "
                                          alt=""
                                        />
                                      </Link>
                                    </div>
                                    <div className="sell-tabel-info">
                                      <p>
                                        <Link to="/course-details">
                                          Wordpress for Beginners - Master
                                          Wordpress Quickly
                                        </Link>
                                      </p>
                                    </div>
                                  </div>
                                </td>
                                <td>34</td>
                                <td>$3,145.23</td>
                              </tr>
                              <tr>
                                <td>
                                  <div className="sell-table-group d-flex align-items-center">
                                    <div className="sell-group-img">
                                      <Link to="/course-details">
                                        <img
                                          src={Course12}
                                          className="img-fluid "
                                          alt=""
                                        />
                                      </Link>
                                    </div>
                                    <div className="sell-tabel-info">
                                      <p>
                                        <Link to="/course-details">
                                          Sketch from A to Z (2022): Become an
                                          app designer
                                        </Link>
                                      </p>
                                    </div>
                                  </div>
                                </td>
                                <td>34</td>
                                <td>$3,145.23</td>
                              </tr>
                            </tbody>
                          </table>
                          {/* Referred Users */}
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            {/* Instruction Dashboard */}
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
}
