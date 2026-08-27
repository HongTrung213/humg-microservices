<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layoutsinstructor></layoutsinstructor>

    <!-- Page Wrapper -->
    <div class="page-content">
      <div class="container">
        <div class="row">
          <instructorsidebar></instructorsidebar>

          <!-- Instructor Dashboard -->
          <div class="col-xl-9 col-lg-8 col-md-12">
            <div class="row">
              <div class="col-md-12">
                <div class="settings-widget">
                  <div class="settings-inner-blk p-0">
                    <div class="sell-course-head comman-space">
                      <h3>Orders</h3>
                      <p>Order Dashboard is a quick overview of all current orders.</p>
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
                              <th>INVOICE</th>
                              <th>DATE</th>
                              <th>METHOD</th>
                              <th></th>
                            </tr>
                          </thead>
                          <tbody>
                            <tr>
                              <td class="instruct-orders-info">
                                <p>
                                  <router-link to="course-details"
                                    >Information About UI/UX Design Degree</router-link
                                  >
                                </p>
                              </td>
                              <td>34</td>
                              <td>#10021</td>
                              <td>10-05-23</td>
                              <td>Mastercard</td>
                              <td>
                                <a href="javascript:;"
                                  ><i class="feather-more-vertical"></i
                                ></a>
                              </td>
                            </tr>
                            <tr>
                              <td class="instruct-orders-info">
                                <p>
                                  <router-link to="course-details"
                                    >Wordpress for Beginners - Master Wordpress
                                    Quickly</router-link
                                  >
                                </p>
                              </td>
                              <td>30</td>
                              <td>#12421</td>
                              <td>10-05-23</td>
                              <td>Visa</td>
                              <td>
                                <a href="javascript:;"
                                  ><i class="feather-more-vertical"></i
                                ></a>
                              </td>
                            </tr>
                            <tr>
                              <td class="instruct-orders-info">
                                <p>
                                  <router-link to="course-details"
                                    >Sketch from A to Z (2023): Become an app
                                    designer</router-link
                                  >
                                </p>
                              </td>
                              <td>24</td>
                              <td>#11021</td>
                              <td>10-05-23</td>
                              <td>Mastercard</td>
                              <td>
                                <a href="javascript:;"
                                  ><i class="feather-more-vertical"></i
                                ></a>
                              </td>
                            </tr>
                            <tr>
                              <td class="instruct-orders-info">
                                <p>
                                  <router-link to="course-details"
                                    >Learn Angular Fundamentals From beginning to advance
                                    lavel</router-link
                                  >
                                </p>
                              </td>
                              <td>34</td>
                              <td>#10021</td>
                              <td>10-05-23</td>
                              <td>Mastercard</td>
                              <td>
                                <a href="javascript:;"
                                  ><i class="feather-more-vertical"></i
                                ></a>
                              </td>
                            </tr>
                            <tr>
                              <td class="instruct-orders-info">
                                <p>
                                  <router-link to="course-details"
                                    >Build Responsive Real World Websites with HTML5 and
                                    CSS3</router-link
                                  >
                                </p>
                              </td>
                              <td>34</td>
                              <td>#10021</td>
                              <td>10-05-23</td>
                              <td>Mastercard</td>
                              <td>
                                <a href="javascript:;"
                                  ><i class="feather-more-vertical"></i
                                ></a>
                              </td>
                            </tr>
                            <tr>
                              <td class="instruct-orders-info">
                                <p>
                                  <router-link to="course-details"
                                    >C# Developers Double Your Coding Speed with Visual
                                    Studio</router-link
                                  >
                                </p>
                              </td>
                              <td>34</td>
                              <td>#10021</td>
                              <td>10-05-23</td>
                              <td>Mastercard</td>
                              <td>
                                <a href="javascript:;"
                                  ><i class="feather-more-vertical"></i
                                ></a>
                              </td>
                            </tr>
                            <tr>
                              <td class="instruct-orders-info">
                                <p>
                                  <router-link to="course-details"
                                    >Learn JavaScript and Express to become a professional
                                    JavaScript</router-link
                                  >
                                </p>
                              </td>
                              <td>34</td>
                              <td>#10021</td>
                              <td>10-05-23</td>
                              <td>Mastercard</td>
                              <td>
                                <a href="javascript:;"
                                  ><i class="feather-more-vertical"></i
                                ></a>
                              </td>
                            </tr>
                            <tr>
                              <td class="instruct-orders-info">
                                <p>
                                  <router-link to="course-details"
                                    >Learn and Understand AngularJS to become a
                                    professional developer</router-link
                                  >
                                </p>
                              </td>
                              <td>34</td>
                              <td>#10021</td>
                              <td>10-05-23</td>
                              <td>Mastercard</td>
                              <td>
                                <a href="javascript:;"
                                  ><i class="feather-more-vertical"></i
                                ></a>
                              </td>
                            </tr>
                            <tr>
                              <td class="instruct-orders-info">
                                <p>
                                  <router-link to="course-details"
                                    >Responsive Web Design Essentials HTML5 CSS3 and
                                    Bootstrap</router-link
                                  >
                                </p>
                              </td>
                              <td>34</td>
                              <td>#10021</td>
                              <td>10-05-23</td>
                              <td>Mastercard</td>
                              <td>
                                <a href="javascript:;"
                                  ><i class="feather-more-vertical"></i
                                ></a>
                              </td>
                            </tr>
                            <tr>
                              <td class="instruct-orders-info">
                                <p>
                                  <router-link to="course-details"
                                    >The Complete App Design Course - UX, UI and Design
                                    Thinking</router-link
                                  >
                                </p>
                              </td>
                              <td>34</td>
                              <td>#10021</td>
                              <td>10-05-23</td>
                              <td>Mastercard</td>
                              <td>
                                <a href="javascript:;"
                                  ><i class="feather-more-vertical"></i
                                ></a>
                              </td>
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
