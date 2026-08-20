<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layoutsinstructor></layoutsinstructor>

    <!-- Page Wrapper -->
    <div class="page-content instructor-page-content">
      <div class="container">
        <div class="row">
          <instructorsidebar></instructorsidebar>

          <!-- Instructor Dashboard -->
          <div class="col-xl-9 col-lg-8 col-md-12">
            <div class="row">
              <div class="col-md-4 d-flex">
                <div class="card instructor-card w-100">
                  <div class="card-body">
                    <div class="instructor-inner">
                      <h6>REVENUE</h6>
                      <h4 class="instructor-text-success">$467.34</h4>
                      <p>Earning this month</p>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-md-4 d-flex">
                <div class="card instructor-card w-100">
                  <div class="card-body">
                    <div class="instructor-inner">
                      <h6>STUDENTS ENROLLMENTS</h6>
                      <h4 class="instructor-text-info">12,000</h4>
                      <p>New this month</p>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-md-4 d-flex">
                <div class="card instructor-card w-100">
                  <div class="card-body">
                    <div class="instructor-inner">
                      <h6>COURSES RATING</h6>
                      <h4 class="instructor-text-warning">4.80</h4>
                      <p>Rating this month</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-12">
                <div class="card instructor-card">
                  <div class="card-header">
                    <h4>Earnings</h4>
                  </div>
                  <div class="card-body">
                    <apexchart
                      type="area"
                      height="300"
                      :options="chartOptions"
                      :series="series"
                    ></apexchart>
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-12">
                <div class="card instructor-card">
                  <div class="card-header">
                    <h4>Order</h4>
                  </div>
                  <div class="card-body">
                    <apexchart
                      type="bar"
                      height="350"
                      :options="chartOption"
                      :series="series1"
                    ></apexchart>
                  </div>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-md-12">
                <div class="settings-widget">
                  <div class="settings-inner-blk p-0">
                    <div class="sell-course-head comman-space">
                      <h3>Best Selling Courses</h3>
                    </div>
                    <div class="comman-space pb-0">
                      <div
                        class="settings-tickets-blk course-instruct-blk table-responsive"
                      >
                        <!-- Referred Users-->
                        <table class="table table-nowrap mb-0">
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
                                <div class="sell-table-group d-flex align-items-center">
                                  <div class="sell-group-img">
                                    <router-link to="course-details">
                                      <img
                                        src="@/assets/img/course/course-10.jpg"
                                        class="img-fluid"
                                        alt=""
                                      />
                                    </router-link>
                                  </div>
                                  <div class="sell-tabel-info">
                                    <p>
                                      <router-link to="course-details"
                                        >Information About UI/UX Design
                                        Degree</router-link
                                      >
                                    </p>
                                  </div>
                                </div>
                              </td>
                              <td>34</td>
                              <td>$3,145.23</td>
                            </tr>
                            <tr>
                              <td>
                                <div class="sell-table-group d-flex align-items-center">
                                  <div class="sell-group-img">
                                    <router-link to="course-details">
                                      <img
                                        src="@/assets/img/course/course-11.jpg"
                                        class="img-fluid"
                                        alt=""
                                      />
                                    </router-link>
                                  </div>
                                  <div class="sell-tabel-info">
                                    <p>
                                      <router-link to="course-details"
                                        >Wordpress for Beginners - Master Wordpress
                                        Quickly</router-link
                                      >
                                    </p>
                                  </div>
                                </div>
                              </td>
                              <td>34</td>
                              <td>$3,145.23</td>
                            </tr>
                            <tr>
                              <td>
                                <div class="sell-table-group d-flex align-items-center">
                                  <div class="sell-group-img">
                                    <router-link to="course-details">
                                      <img
                                        src="@/assets/img/course/course-12.jpg"
                                        class="img-fluid"
                                        alt=""
                                      />
                                    </router-link>
                                  </div>
                                  <div class="sell-tabel-info">
                                    <p>
                                      <router-link to="course-details"
                                        >Sketch from A to Z (2023): Become an app
                                        designer</router-link
                                      >
                                    </p>
                                  </div>
                                </div>
                              </td>
                              <td>34</td>
                              <td>$3,145.23</td>
                            </tr>
                          </tbody>
                        </table>
                        <!-- /Referred Users-->
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /Instructor Dashboard -->
        </div>
      </div>
    </div>
    <!-- /Page Wrapper -->

    <layouts1></layouts1>
  </div>
  <!-- /Main Wrapper -->
</template>
<script>
import { ref } from "vue";
import ApexCharts from "apexcharts";
export default {
  data: function () {
    return {
      chartOptions: {
        chart: {
          id: "vuechart-example",
        },

        colors: ["#FF9364"],
        chart: {
          type: "area",
          height: 300,
          toolbar: {
            show: false,
          },
          zoom: {
            enabled: true,
          },
        },
        markers: {
          size: 3,
        },
        dataLabels: {
          enabled: false,
        },
        stroke: {
          curve: "smooth",
          width: 3,
        },
        legend: {
          position: "top",
          horizontalAlign: "right",
        },
        grid: {
          show: false,
        },
        yaxis: {
          axisBorder: {
            show: true,
          },
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
            "Nov",
            "Dec",
          ],
        },
      },
      series: [
        {
          name: "Current month",
          data: [0, 10, 40, 43, 40, 25, 35, 25, 40, 30],
        },
      ],
      chartOption: {
        chart: {
          id: "vuechart-example",
        },

        chart: {
          height: 350,
          type: "bar",
          toolbar: {
            show: false,
          },
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: "20%",
            endingShape: "rounded",
            startingShape: "rounded",
          },
        },
        colors: ["#1D9CFD"],
        dataLabels: {
          enabled: false,
        },
        stroke: {
          show: true,
          width: 2,
          colors: ["transparent"],
        },

        xaxis: {
          categories: ["Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"],
        },
        fill: {
          opacity: 1,
        },
        tooltip: {
          y: {
            formatter: function (val) {
              return "$ " + val + " thousands";
            },
          },
        },
      },
      series1: [
        {
          name: "Revenue",
          data: [76, 85, 101, 98, 87, 105, 91, 114, 94],
        },
      ],
    };
  },
};
</script>
