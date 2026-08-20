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
            <div class="tak-instruct-group">
              <div class="row">
                <div class="col-md-12">
                  <div class="settings-widget">
                    <div class="settings-inner-blk p-0">
                      <div
                        class="sell-course-head student-meet-head comman-space border-0"
                      >
                        <div class="tak-head d-flex align-items-center">
                          <div>
                            <h3>Students</h3>
                            <p>Meet people taking your course.</p>
                          </div>
                          <div class="view-icons">
                            <router-link
                              to="instructor-student-grid"
                              class="grid-view active"
                              ><i class="feather-grid"></i
                            ></router-link>
                            <router-link to="instructor-student-list" class="list-view"
                              ><i class="feather-list"></i
                            ></router-link>
                          </div>
                        </div>
                        <form>
                          <div class="student-search-form d-flex">
                            <div class="form-group mb-0">
                              <input
                                type="text"
                                class="form-control"
                                placeholder="Twitter Profile Name"
                              />
                            </div>
                            <div class="export-cvv-btn">
                              <button class="btn btn-primary">Export CSV</button>
                            </div>
                          </div>
                        </form>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                  <div class="student-box flex-fill">
                    <div class="student-box-blks">
                      <div class="message-text-img">
                        <a href="javascript:;">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/icon/message-text.svg"
                          />
                        </a>
                      </div>
                      <div class="student-img">
                        <router-link to="student-profile">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/user/user1.jpg"
                          />
                        </router-link>
                      </div>
                      <div class="student-content pb-0">
                        <h5>
                          <router-link to="student-profile">Wade Warren</router-link>
                        </h5>
                        <div
                          class="loc-blk d-flex align-items-center justify-content-center"
                        >
                          <i class="feather-map-pin me-2"></i>
                          <p>United States</p>
                        </div>
                      </div>
                    </div>
                    <div class="enrol-student-foot">
                      <ul>
                        <li>Enrolled <span>3/02/2023</span></li>
                        <li>
                          Progress
                          <div class="instruct-stip d-flex align-items-center">
                            <span>20%</span>
                            <div class="course-stip progress-stip">
                              <div
                                class="progress-bar bg-success progress-bar-striped active-stip"
                              ></div>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                  <div class="student-box flex-fill">
                    <div class="student-box-blks">
                      <div class="message-text-img">
                        <a href="javascript:;">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/icon/message-text.svg"
                          />
                        </a>
                      </div>
                      <div class="student-img">
                        <router-link to="student-profile">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/user/user3.jpg"
                          />
                        </router-link>
                      </div>
                      <div class="student-content pb-0">
                        <h5>
                          <router-link to="student-profile">Dianna Smiley</router-link>
                        </h5>
                        <div
                          class="loc-blk d-flex align-items-center justify-content-center"
                        >
                          <i class="feather-map-pin me-2"></i>
                          <p>Tunisia</p>
                        </div>
                      </div>
                    </div>
                    <div class="enrol-student-foot">
                      <ul>
                        <li>Enrolled <span>15/05/2023</span></li>
                        <li>
                          Progress
                          <div class="instruct-stip d-flex align-items-center">
                            <span>20%</span>
                            <div class="course-stip progress-stip">
                              <div
                                class="progress-bar bg-success progress-bar-striped active-stip"
                              ></div>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                  <div class="student-box flex-fill">
                    <div class="student-box-blks">
                      <div class="message-text-img">
                        <a href="javascript:;">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/icon/message-text.svg"
                          />
                        </a>
                      </div>
                      <div class="student-img">
                        <router-link to="student-profile">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/user/user2.jpg"
                          />
                        </router-link>
                      </div>
                      <div class="student-content pb-0">
                        <h5>
                          <router-link to="student-profile">Esther Howard</router-link>
                        </h5>
                        <div
                          class="loc-blk d-flex align-items-center justify-content-center"
                        >
                          <i class="feather-map-pin me-2"></i>
                          <p>Spain</p>
                        </div>
                      </div>
                    </div>
                    <div class="enrol-student-foot">
                      <ul>
                        <li>Enrolled <span>6/06/2023</span></li>
                        <li>
                          Progress
                          <div class="instruct-stip d-flex align-items-center">
                            <span>20%</span>
                            <div class="course-stip progress-stip">
                              <div
                                class="progress-bar bg-success progress-bar-striped active-stip"
                              ></div>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                  <div class="student-box flex-fill">
                    <div class="student-box-blks">
                      <div class="message-text-img">
                        <a href="javascript:;">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/icon/message-text.svg"
                          />
                        </a>
                      </div>
                      <div class="student-img">
                        <router-link to="student-profile">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/user/user5.jpg"
                          />
                        </router-link>
                      </div>
                      <div class="student-content pb-0">
                        <h5>
                          <router-link to="student-profile">Guy Hawkins</router-link>
                        </h5>
                        <div
                          class="loc-blk d-flex align-items-center justify-content-center"
                        >
                          <i class="feather-map-pin me-2"></i>
                          <p>United States</p>
                        </div>
                      </div>
                    </div>
                    <div class="enrol-student-foot">
                      <ul>
                        <li>Enrolled <span>13/01/2023</span></li>
                        <li>
                          Progress
                          <div class="instruct-stip d-flex align-items-center">
                            <span>20%</span>
                            <div class="course-stip progress-stip">
                              <div
                                class="progress-bar bg-success progress-bar-striped active-stip"
                              ></div>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                  <div class="student-box flex-fill">
                    <div class="student-box-blks">
                      <div class="message-text-img">
                        <a href="javascript:;">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/icon/message-text.svg"
                          />
                        </a>
                      </div>
                      <div class="student-img">
                        <router-link to="student-profile">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/user/user6.jpg"
                          />
                        </router-link>
                      </div>
                      <div class="student-content pb-0">
                        <h5>
                          <router-link to="student-profile">Jacob Jones</router-link>
                        </h5>
                        <div
                          class="loc-blk d-flex align-items-center justify-content-center"
                        >
                          <i class="feather-map-pin me-2"></i>
                          <p>United Kingdom</p>
                        </div>
                      </div>
                    </div>
                    <div class="enrol-student-foot">
                      <ul>
                        <li>Enrolled <span>2/06/2023</span></li>
                        <li>
                          Progress
                          <div class="instruct-stip d-flex align-items-center">
                            <span>20%</span>
                            <div class="course-stip progress-stip">
                              <div
                                class="progress-bar bg-success progress-bar-striped active-stip"
                              ></div>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                  <div class="student-box flex-fill">
                    <div class="student-box-blks">
                      <div class="message-text-img">
                        <a href="javascript:;">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/icon/message-text.svg"
                          />
                        </a>
                      </div>
                      <div class="student-img">
                        <router-link to="student-profile">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/user/user4.jpg"
                          />
                        </router-link>
                      </div>
                      <div class="student-content pb-0">
                        <h5>
                          <router-link to="student-profile">Kristin Watson</router-link>
                        </h5>
                        <div
                          class="loc-blk d-flex align-items-center justify-content-center"
                        >
                          <i class="feather-map-pin me-2"></i>
                          <p>Iceland</p>
                        </div>
                      </div>
                    </div>
                    <div class="enrol-student-foot">
                      <ul>
                        <li>Enrolled <span>22/02/2023</span></li>
                        <li>
                          Progress
                          <div class="instruct-stip d-flex align-items-center">
                            <span>20%</span>
                            <div class="course-stip progress-stip">
                              <div
                                class="progress-bar bg-success progress-bar-striped active-stip"
                              ></div>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                  <div class="student-box flex-fill">
                    <div class="student-box-blks">
                      <div class="message-text-img">
                        <a href="javascript:;">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/icon/message-text.svg"
                          />
                        </a>
                      </div>
                      <div class="student-img">
                        <router-link to="student-profile">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/user/user11.jpg"
                          />
                        </router-link>
                      </div>
                      <div class="student-content pb-0">
                        <h5>
                          <router-link to="student-profile">Rivao Luke</router-link>
                        </h5>
                        <div
                          class="loc-blk d-flex align-items-center justify-content-center"
                        >
                          <i class="feather-map-pin me-2"></i>
                          <p>Brazil</p>
                        </div>
                      </div>
                    </div>
                    <div class="enrol-student-foot">
                      <ul>
                        <li>Enrolled <span>3/02/2023</span></li>
                        <li>
                          Progress
                          <div class="instruct-stip d-flex align-items-center">
                            <span>20%</span>
                            <div class="course-stip progress-stip">
                              <div
                                class="progress-bar bg-success progress-bar-striped active-stip"
                              ></div>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                  <div class="student-box flex-fill">
                    <div class="student-box-blks">
                      <div class="message-text-img">
                        <a href="javascript:;">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/icon/message-text.svg"
                          />
                        </a>
                      </div>
                      <div class="student-img">
                        <router-link to="student-profile">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/user/user12.jpg"
                          />
                        </router-link>
                      </div>
                      <div class="student-content pb-0">
                        <h5>
                          <router-link to="student-profile">Nia Sikhone</router-link>
                        </h5>
                        <div
                          class="loc-blk d-flex align-items-center justify-content-center"
                        >
                          <i class="feather-map-pin me-2"></i>
                          <p>Italy</p>
                        </div>
                      </div>
                    </div>
                    <div class="enrol-student-foot">
                      <ul>
                        <li>Enrolled <span>10/02/2023</span></li>
                        <li>
                          Progress
                          <div class="instruct-stip d-flex align-items-center">
                            <span>20%</span>
                            <div class="course-stip progress-stip">
                              <div
                                class="progress-bar bg-success progress-bar-striped active-stip"
                              ></div>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
                <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                  <div class="student-box flex-fill">
                    <div class="student-box-blks">
                      <div class="message-text-img">
                        <a href="javascript:;">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/icon/message-text.svg"
                          />
                        </a>
                      </div>
                      <div class="student-img">
                        <router-link to="student-profile">
                          <img
                            class="img-fluid"
                            alt="Students Info"
                            src="@/assets/img/user/user13.jpg"
                          />
                        </router-link>
                      </div>
                      <div class="student-content pb-0">
                        <h5>
                          <router-link to="student-profile">Xiaon Merry</router-link>
                        </h5>
                        <div
                          class="loc-blk d-flex align-items-center justify-content-center"
                        >
                          <i class="feather-map-pin me-2"></i>
                          <p>France</p>
                        </div>
                      </div>
                    </div>
                    <div class="enrol-student-foot">
                      <ul>
                        <li>Enrolled <span>3/02/2023</span></li>
                        <li>
                          Progress
                          <div class="instruct-stip d-flex align-items-center">
                            <span>20%</span>
                            <div class="course-stip progress-stip">
                              <div
                                class="progress-bar bg-success progress-bar-striped active-stip"
                              ></div>
                            </div>
                          </div>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>

              <pagination></pagination>
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
