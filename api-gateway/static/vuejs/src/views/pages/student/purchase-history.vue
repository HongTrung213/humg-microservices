<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layouts></layouts>
    <courseheader></courseheader>
    <!-- Purchase History -->
    <section class="course-content purchase-widget">
      <div class="container">
        <div class="student-widget">
          <div class="student-widget-group">
            <div class="row">
              <div class="col-lg-12">
                <div class="row">
                  <div class="col-lg-12 col-md-12 d-flex">
                    <div class="course-box course-design list-course d-flex">
                      <div class="product">
                        <div class="product-img">
                          <router-link to="course-details">
                            <img
                              class="img-fluid"
                              alt=""
                              src="@/assets/img/course/course-10.jpg"
                            />
                          </router-link>
                          <div class="price">
                            <h3 class="free-color">FREE</h3>
                          </div>
                        </div>
                        <div class="product-content">
                          <div class="head-course-title">
                            <h3 class="title">
                              <router-link to="course-details"
                                >Information About UI/UX<br />
                                Design Degree</router-link
                              >
                            </h3>
                            <div class="all-btn all-category d-flex align-items-center">
                              <router-link to="view-invoice" class="btn btn-primary"
                                >Invoice</router-link
                              >
                            </div>
                          </div>
                          <div
                            class="course-info d-flex align-items-center border-bottom-0 pb-0"
                          >
                            <div class="rating-img d-flex align-items-center">
                              <img src="@/assets/img/icon/icon-01.svg" alt="" />
                              <p>12+ Lesson</p>
                            </div>
                            <div class="course-view d-flex align-items-center">
                              <img src="@/assets/img/icon/icon-02.svg" alt="" />
                              <p>9hr 30min</p>
                            </div>
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
                          <div class="course-group d-flex mb-0">
                            <div class="course-group-img d-flex">
                              <router-link to="student-profile"
                                ><img
                                  src="@/assets/img/user/user1.jpg"
                                  alt=""
                                  class="img-fluid"
                              /></router-link>
                              <div class="course-name">
                                <h4>
                                  <router-link to="student-profile"
                                    >Rolands R</router-link
                                  >
                                </h4>
                                <p>Instructor</p>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-12 col-md-12 d-flex">
                    <div class="course-box course-design list-course d-flex">
                      <div class="product">
                        <div class="product-img">
                          <router-link to="course-details">
                            <img
                              class="img-fluid"
                              alt=""
                              src="@/assets/img/course/course-11.jpg"
                            />
                          </router-link>
                          <div class="price">
                            <h3>$300 <span>$99.00</span></h3>
                          </div>
                        </div>
                        <div class="product-content">
                          <div class="head-course-title">
                            <h3 class="title">
                              <router-link to="course-details"
                                >Wordpress for Beginners - Master Wordpress <br />
                                Quickly</router-link
                              >
                            </h3>
                            <div class="all-btn all-category d-flex align-items-center">
                              <router-link to="view-invoice" class="btn btn-primary"
                                >Invoice</router-link
                              >
                            </div>
                          </div>
                          <div
                            class="course-info d-flex align-items-center border-bottom-0 pb-0"
                          >
                            <div class="rating-img d-flex align-items-center">
                              <img src="@/assets/img/icon/icon-01.svg" alt="" />
                              <p>10+ Lesson</p>
                            </div>
                            <div class="course-view d-flex align-items-center">
                              <img src="@/assets/img/icon/icon-02.svg" alt="" />
                              <p>7hr 20min</p>
                            </div>
                          </div>
                          <div class="rating">
                            <i class="fas fa-star filled me-1"></i>
                            <i class="fas fa-star filled me-1"></i>
                            <i class="fas fa-star filled me-1"></i>
                            <i class="fas fa-star filled me-1"></i>
                            <i class="fas fa-star me-1"></i>
                            <span class="d-inline-block average-rating"
                              ><span>4.2</span> (15)</span
                            >
                          </div>
                          <div class="course-group d-flex mb-0">
                            <div class="course-group-img d-flex">
                              <router-link to="student-profile"
                                ><img
                                  src="@/assets/img/user/user2.jpg"
                                  alt=""
                                  class="img-fluid"
                              /></router-link>
                              <div class="course-name">
                                <h4>
                                  <router-link to="student-profile">Jenis R.</router-link>
                                </h4>
                                <p>Instructor</p>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-lg-12 col-md-12 d-flex">
                    <div class="course-box course-design list-course d-flex mb-0">
                      <div class="product">
                        <div class="product-img">
                          <router-link to="course-details">
                            <img
                              class="img-fluid"
                              alt=""
                              src="@/assets/img/course/course-12.jpg"
                            />
                          </router-link>
                          <div class="price">
                            <h3>$300 <span>$99.00</span></h3>
                          </div>
                        </div>
                        <div class="product-content">
                          <div class="head-course-title">
                            <h3 class="title">
                              <router-link to="course-details"
                                >Sketch from A to Z (2023): Become an app<br />
                                designer</router-link
                              >
                            </h3>
                            <div class="all-btn all-category d-flex align-items-center">
                              <router-link to="view-invoice" class="btn btn-primary"
                                >Invoice</router-link
                              >
                            </div>
                          </div>
                          <div
                            class="course-info d-flex align-items-center border-bottom-0 pb-0"
                          >
                            <div class="rating-img d-flex align-items-center">
                              <img src="@/assets/img/icon/icon-01.svg" alt="" />
                              <p>12+ Lesson</p>
                            </div>
                            <div class="course-view d-flex align-items-center">
                              <img src="@/assets/img/icon/icon-02.svg" alt="" />
                              <p>9hr 30min</p>
                            </div>
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
                          <div class="course-group d-flex mb-0">
                            <div class="course-group-img d-flex">
                              <router-link to="student-profile"
                                ><img
                                  src="@/assets/img/user/user3.jpg"
                                  alt=""
                                  class="img-fluid"
                              /></router-link>
                              <div class="course-name">
                                <h4>
                                  <router-link to="student-profile"
                                    >Jesse Stevens</router-link
                                  >
                                </h4>
                                <p>Instructor</p>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- /Purchase History -->

    <layouts1></layouts1>
  </div>
  <!-- /Main Wrapper -->
</template>
