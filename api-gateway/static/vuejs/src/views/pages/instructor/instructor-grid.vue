<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layoutsinstructorborder></layoutsinstructorborder>
    <instructorgrid2></instructorgrid2>
    <!-- Page Wrapper -->
    <div class="page-content">
      <div class="container">
        <div class="row">
          <div class="col-lg-9">
            <instructorfilter></instructorfilter>

            <div class="row">
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="instructor-box flex-fill">
                  <div class="instructor-img">
                    <router-link to="instructor-profile">
                      <img
                        class="img-fluid"
                        alt=""
                        src="@/assets/img/user/user11.jpg"
                      />
                    </router-link>
                    <a href="javascript:;" class="rating-count"
                      ><i class="fa-regular fa-heart"></i
                    ></a>
                  </div>
                  <div class="instructor-content">
                    <h5><router-link to="instructor-profile">Rolands R</router-link></h5>
                    <h6>Instructor</h6>
                    <div
                      class="rating-img d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-01.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>12+ Lesson</p>
                    </div>
                    <div
                      class="course-view d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-02.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>9hr 30min</p>
                    </div>
                    <div class="rating">
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star me-1"></i>
                      <span class="d-inline-block average-rating"
                        ><span>4.0</span> (15)</span
                      >
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="instructor-box flex-fill">
                  <div class="instructor-img">
                    <router-link to="instructor-profile">
                      <img
                        class="img-fluid"
                        alt=""
                        src="@/assets/img/user/user.jpg"
                      />
                    </router-link>
                    <a href="javascript:;" class="rating-count"
                      ><i class="fa-regular fa-heart"></i
                    ></a>
                  </div>
                  <div class="instructor-content">
                    <h5><router-link to="instructor-profile">Jenis R.</router-link></h5>
                    <h6>Instructor</h6>
                    <div
                      class="rating-img d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-01.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>12+ Lesson</p>
                    </div>
                    <div
                      class="course-view d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-02.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>9hr 30min</p>
                    </div>
                    <div class="rating">
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star me-1"></i>
                      <span class="d-inline-block average-rating"
                        ><span>4.0</span> (15)</span
                      >
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="instructor-box flex-fill">
                  <div class="instructor-img">
                    <router-link to="instructor-profile">
                      <img
                        class="img-fluid"
                        alt=""
                        src="@/assets/img/user/user4.jpg"
                      />
                    </router-link>
                    <a href="javascript:;" class="rating-count"
                      ><i class="fa-regular fa-heart"></i
                    ></a>
                  </div>
                  <div class="instructor-content">
                    <h5>
                      <router-link to="instructor-profile">Jesse Stevens</router-link>
                    </h5>
                    <h6>Instructor</h6>
                    <div
                      class="rating-img d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-01.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>12+ Lesson</p>
                    </div>
                    <div
                      class="course-view d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-02.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>9hr 30min</p>
                    </div>
                    <div class="rating">
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star me-1"></i>
                      <span class="d-inline-block average-rating"
                        ><span>4.0</span> (15)</span
                      >
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="instructor-box flex-fill">
                  <div class="instructor-img">
                    <router-link to="instructor-profile">
                      <img
                        class="img-fluid"
                        alt=""
                        src="@/assets/img/user/user2.jpg"
                      />
                    </router-link>
                    <a href="javascript:;" class="rating-count"
                      ><i class="fa-regular fa-heart"></i
                    ></a>
                  </div>
                  <div class="instructor-content">
                    <h5>
                      <router-link to="instructor-profile">Stevens Jes</router-link>
                    </h5>
                    <h6>Instructor</h6>
                    <div
                      class="rating-img d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-01.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>12+ Lesson</p>
                    </div>
                    <div
                      class="course-view d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-02.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>9hr 30min</p>
                    </div>
                    <div class="rating">
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star me-1"></i>
                      <span class="d-inline-block average-rating"
                        ><span>4.0</span> (15)</span
                      >
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="instructor-box flex-fill">
                  <div class="instructor-img">
                    <router-link to="instructor-profile">
                      <img
                        class="img-fluid"
                        alt=""
                        src="@/assets/img/user/user3.jpg"
                      />
                    </router-link>
                    <a href="javascript:;" class="rating-count"
                      ><i class="fa-regular fa-heart"></i
                    ></a>
                  </div>
                  <div class="instructor-content">
                    <h5><router-link to="instructor-profile">John Smith</router-link></h5>
                    <h6>Instructor</h6>
                    <div
                      class="rating-img d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-01.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>12+ Lesson</p>
                    </div>
                    <div
                      class="course-view d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-02.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>9hr 30min</p>
                    </div>
                    <div class="rating">
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star me-1"></i>
                      <span class="d-inline-block average-rating"
                        ><span>4.0</span> (15)</span
                      >
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="instructor-box flex-fill">
                  <div class="instructor-img">
                    <router-link to="instructor-profile">
                      <img
                        class="img-fluid"
                        alt=""
                        src="@/assets/img/user/user5.jpg"
                      />
                    </router-link>
                    <a href="javascript:;" class="rating-count"
                      ><i class="fa-regular fa-heart"></i
                    ></a>
                  </div>
                  <div class="instructor-content">
                    <h5>
                      <router-link to="instructor-profile">Stella Johnson</router-link>
                    </h5>
                    <h6>Instructor</h6>
                    <div
                      class="rating-img d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-01.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>12+ Lesson</p>
                    </div>
                    <div
                      class="course-view d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-02.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>9hr 30min</p>
                    </div>
                    <div class="rating">
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star me-1"></i>
                      <span class="d-inline-block average-rating"
                        ><span>4.0</span> (15)</span
                      >
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="instructor-box flex-fill">
                  <div class="instructor-img">
                    <router-link to="instructor-profile">
                      <img
                        class="img-fluid"
                        alt=""
                        src="@/assets/img/user/user12.jpg"
                      />
                    </router-link>
                    <a href="javascript:;" class="rating-count"
                      ><i class="fa-regular fa-heart"></i
                    ></a>
                  </div>
                  <div class="instructor-content">
                    <h5>
                      <router-link to="instructor-profile">John Michael</router-link>
                    </h5>
                    <h6>Instructor</h6>
                    <div
                      class="rating-img d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-01.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>12+ Lesson</p>
                    </div>
                    <div
                      class="course-view d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-02.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>9hr 30min</p>
                    </div>
                    <div class="rating">
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star me-1"></i>
                      <span class="d-inline-block average-rating"
                        ><span>4.0</span> (15)</span
                      >
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="instructor-box flex-fill">
                  <div class="instructor-img">
                    <router-link to="instructor-profile">
                      <img
                        class="img-fluid"
                        alt=""
                        src="@/assets/img/user/user1.jpg"
                      />
                    </router-link>
                    <a href="javascript:;" class="rating-count"
                      ><i class="fa-regular fa-heart"></i
                    ></a>
                  </div>
                  <div class="instructor-content">
                    <h5>
                      <router-link to="instructor-profile">Nicole Brown</router-link>
                    </h5>
                    <h6>Instructor</h6>
                    <div
                      class="rating-img d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-01.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>12+ Lesson</p>
                    </div>
                    <div
                      class="course-view d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-02.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>9hr 30min</p>
                    </div>
                    <div class="rating">
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star me-1"></i>
                      <span class="d-inline-block average-rating"
                        ><span>4.0</span> (15)</span
                      >
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="instructor-box flex-fill">
                  <div class="instructor-img">
                    <router-link to="instructor-profile">
                      <img
                        class="img-fluid"
                        alt=""
                        src="@/assets/img/user/user13.jpg"
                      />
                    </router-link>
                    <a href="javascript:;" class="rating-count"
                      ><i class="fa-regular fa-heart"></i
                    ></a>
                  </div>
                  <div class="instructor-content">
                    <h5>
                      <router-link to="instructor-profile">Monroe Parker</router-link>
                    </h5>
                    <h6>Instructor</h6>
                    <div
                      class="rating-img d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-01.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>12+ Lesson</p>
                    </div>
                    <div
                      class="course-view d-flex align-items-center justify-content-center"
                    >
                      <img
                        src="@/assets/img/icon/icon-02.svg"
                        class="me-1"
                        alt=""
                      />
                      <p>9hr 30min</p>
                    </div>
                    <div class="rating">
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star me-1"></i>
                      <span class="d-inline-block average-rating"
                        ><span>4.0</span> (15)</span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <pagination></pagination>
          </div>

          <div class="col-lg-3">
            <div class="filter-clear">
              <div class="clear-filter d-flex align-items-center">
                <h4><i class="feather-filter"></i>Filters</h4>
                <div class="clear-text">
                  <p>CLEAR</p>
                </div>
              </div>

              <!-- Search Filter -->
              <div class="card search-filter">
                <div class="card-body">
                  <div class="filter-widget mb-0">
                    <div class="categories-head d-flex align-items-center">
                      <h4>Course categories</h4>
                      <i class="fas fa-angle-down"></i>
                    </div>
                    <div>
                      <label class="custom_check">
                        <input type="checkbox" name="select_specialist" />
                        <span class="checkmark"></span> Backend (3)
                      </label>
                    </div>
                    <div>
                      <label class="custom_check">
                        <input type="checkbox" name="select_specialist" />
                        <span class="checkmark"></span> CSS (2)
                      </label>
                    </div>
                    <div>
                      <label class="custom_check">
                        <input type="checkbox" name="select_specialist" />
                        <span class="checkmark"></span> Frontend (2)
                      </label>
                    </div>
                    <div>
                      <label class="custom_check">
                        <input type="checkbox" name="select_specialist" checked />
                        <span class="checkmark"></span> General (2)
                      </label>
                    </div>
                    <div>
                      <label class="custom_check">
                        <input type="checkbox" name="select_specialist" checked />
                        <span class="checkmark"></span> IT & Software (2)
                      </label>
                    </div>
                    <div>
                      <label class="custom_check">
                        <input type="checkbox" name="select_specialist" />
                        <span class="checkmark"></span> Photography (2)
                      </label>
                    </div>
                    <div>
                      <label class="custom_check">
                        <input type="checkbox" name="select_specialist" />
                        <span class="checkmark"></span> Programming Language (3)
                      </label>
                    </div>
                    <div>
                      <label class="custom_check mb-0">
                        <input type="checkbox" name="select_specialist" />
                        <span class="checkmark"></span> Technology (2)
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <!-- /Search Filter -->

              <!-- Search Filter -->
              <div class="card search-filter">
                <div class="card-body">
                  <div class="filter-widget mb-0">
                    <div class="categories-head d-flex align-items-center">
                      <h4>Instructors</h4>
                      <i class="fas fa-angle-down"></i>
                    </div>
                    <div>
                      <label class="custom_check">
                        <input type="checkbox" name="select_specialist" />
                        <span class="checkmark"></span> Keny White (10)
                      </label>
                    </div>
                    <div>
                      <label class="custom_check">
                        <input type="checkbox" name="select_specialist" />
                        <span class="checkmark"></span> Hinata Hyuga (5)
                      </label>
                    </div>
                    <div>
                      <label class="custom_check">
                        <input type="checkbox" name="select_specialist" />
                        <span class="checkmark"></span> John Doe (3)
                      </label>
                    </div>
                    <div>
                      <label class="custom_check mb-0">
                        <input type="checkbox" name="select_specialist" checked />
                        <span class="checkmark"></span> Nicole Brown
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <!-- /Search Filter -->

              <!-- Search Filter -->
              <div class="card search-filter">
                <div class="card-body">
                  <div class="filter-widget mb-0">
                    <div class="categories-head d-flex align-items-center">
                      <h4>Price</h4>
                      <i class="fas fa-angle-down"></i>
                    </div>
                    <div>
                      <label class="custom_check custom_one">
                        <input type="radio" name="select_specialist" />
                        <span class="checkmark"></span> All (18)
                      </label>
                    </div>
                    <div>
                      <label class="custom_check custom_one">
                        <input type="radio" name="select_specialist" />
                        <span class="checkmark"></span> Free (3)
                      </label>
                    </div>
                    <div>
                      <label class="custom_check custom_one mb-0">
                        <input type="radio" name="select_specialist" checked />
                        <span class="checkmark"></span> Paid (15)
                      </label>
                    </div>
                  </div>
                </div>
              </div>
              <!-- /Search Filter -->
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- /Page Wrapper -->

    <layouts1></layouts1>
  </div>
  <!-- /Main Wrapper -->
</template>
