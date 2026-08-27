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
                            <a href="instructor-student-grid" class="grid-view"
                              ><i class="feather-grid"></i
                            ></a>
                            <a href="instructor-student-list" class="list-view active"
                              ><i class="feather-list"></i
                            ></a>
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
                  <div class="settings-widget">
                    <div class="settings-inner-blk p-0">
                      <div class="comman-space pb-0">
                        <div class="settings-referral-blk table-responsive">
                          <!-- Instructor Users-->
                          <table class="table table-nowrap">
                            <thead>
                              <tr>
                                <th>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </th>
                                <th>NAME</th>
                                <th>ENROLLED</th>
                                <th>PROGRESS</th>
                                <th>LOCATIONS</th>
                                <th>&nbsp;</th>
                              </tr>
                            </thead>
                            <tbody>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <a
                                    href="student-profile"
                                    class="refer-avatar-blk d-flex align-items-center"
                                  >
                                    <img
                                      src="@/assets/img/students/refer-img1.png"
                                      class="rounded-circle me-2"
                                      alt="Referred User Info"
                                    />
                                    <p>Guy Hawkins</p>
                                  </a>
                                </td>
                                <td>10-05-23</td>
                                <td>0%</td>
                                <td><i class="feather-map-pin me-1"></i>United States</td>
                                <td>
                                  <a href="javascript:;" class="btn-style"
                                    ><i class="feather-clipboard"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <a
                                    href="student-profile"
                                    class="refer-avatar-blk d-flex align-items-center"
                                  >
                                    <img
                                      src="@/assets/img/students/refer-img2.png"
                                      class="rounded-circle me-2"
                                      alt="Referred User Info"
                                    />
                                    <p>Dianna Smiley</p>
                                  </a>
                                </td>
                                <td>10-05-23</td>
                                <td>0%</td>
                                <td><i class="feather-map-pin me-1"></i>United States</td>
                                <td>
                                  <a href="javascript:;" class="btn-style"
                                    ><i class="feather-clipboard"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <a
                                    href="student-profile"
                                    class="refer-avatar-blk d-flex align-items-center"
                                  >
                                    <img
                                      src="@/assets/img/students/refer-img3.png"
                                      class="rounded-circle me-2"
                                      alt="Referred User Info"
                                    />
                                    <p>Guy Hawkins</p>
                                  </a>
                                </td>
                                <td>10-05-23</td>
                                <td>0%</td>
                                <td><i class="feather-map-pin me-1"></i>United States</td>
                                <td>
                                  <a href="javascript:;" class="btn-style"
                                    ><i class="feather-clipboard"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <a
                                    href="student-profile"
                                    class="refer-avatar-blk d-flex align-items-center"
                                  >
                                    <img
                                      src="@/assets/img/students/refer-img4.png"
                                      class="rounded-circle me-2"
                                      alt="Referred User Info"
                                    />
                                    <p>Jacob Jones</p>
                                  </a>
                                </td>
                                <td>10-05-23</td>
                                <td>0%</td>
                                <td><i class="feather-map-pin me-1"></i>United States</td>
                                <td>
                                  <a href="javascript:;" class="btn-style"
                                    ><i class="feather-clipboard"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <a
                                    href="student-profile"
                                    class="refer-avatar-blk d-flex align-items-center"
                                  >
                                    <img
                                      src="@/assets/img/students/refer-img5.png"
                                      class="rounded-circle me-2"
                                      alt="Referred User Info"
                                    />
                                    <p>Kristin Watson</p>
                                  </a>
                                </td>
                                <td>10-05-23</td>
                                <td>0%</td>
                                <td><i class="feather-map-pin me-1"></i>United States</td>
                                <td>
                                  <a href="javascript:;" class="btn-style"
                                    ><i class="feather-clipboard"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <a
                                    href="student-profile"
                                    class="refer-avatar-blk d-flex align-items-center"
                                  >
                                    <img
                                      src="@/assets/img/students/refer-img2.png"
                                      class="rounded-circle me-2"
                                      alt="Referred User Info"
                                    />
                                    <p>Rivao Luke</p>
                                  </a>
                                </td>
                                <td>10-05-23</td>
                                <td>0%</td>
                                <td><i class="feather-map-pin me-1"></i>United States</td>
                                <td>
                                  <a href="javascript:;" class="btn-style"
                                    ><i class="feather-clipboard"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <a
                                    href="student-profile"
                                    class="refer-avatar-blk d-flex align-items-center"
                                  >
                                    <img
                                      src="@/assets/img/students/refer-img3.png"
                                      class="rounded-circle me-2"
                                      alt="Referred User Info"
                                    />
                                    <p>Nia Sikhone</p>
                                  </a>
                                </td>
                                <td>10-05-23</td>
                                <td>0%</td>
                                <td><i class="feather-map-pin me-1"></i>United States</td>
                                <td>
                                  <a href="javascript:;" class="btn-style"
                                    ><i class="feather-clipboard"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <a
                                    href="student-profile"
                                    class="refer-avatar-blk d-flex align-items-center"
                                  >
                                    <img
                                      src="@/assets/img/students/refer-img1.png"
                                      class="rounded-circle me-2"
                                      alt="Referred User Info"
                                    />
                                    <p>Xiaon Merry</p>
                                  </a>
                                </td>
                                <td>10-05-23</td>
                                <td>0%</td>
                                <td><i class="feather-map-pin me-1"></i>United States</td>
                                <td>
                                  <a href="javascript:;" class="btn-style"
                                    ><i class="feather-clipboard"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <a
                                    href="student-profile"
                                    class="refer-avatar-blk d-flex align-items-center"
                                  >
                                    <img
                                      src="@/assets/img/students/refer-img4.png"
                                      class="rounded-circle me-2"
                                      alt="Referred User Info"
                                    />
                                    <p>Guy Hawkins</p>
                                  </a>
                                </td>
                                <td>10-05-23</td>
                                <td>0%</td>
                                <td><i class="feather-map-pin me-1"></i>United States</td>
                                <td>
                                  <a href="javascript:;" class="btn-style"
                                    ><i class="feather-clipboard"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <a
                                    href="student-profile"
                                    class="refer-avatar-blk d-flex align-items-center"
                                  >
                                    <img
                                      src="@/assets/img/students/refer-img5.png"
                                      class="rounded-circle me-2"
                                      alt="Referred User Info"
                                    />
                                    <p>Dianna Smiley</p>
                                  </a>
                                </td>
                                <td>10-05-23</td>
                                <td>0%</td>
                                <td><i class="feather-map-pin me-1"></i>United States</td>
                                <td>
                                  <a href="javascript:;" class="btn-style"
                                    ><i class="feather-clipboard"></i
                                  ></a>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                          <!-- /Instructor List-->
                        </div>
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
