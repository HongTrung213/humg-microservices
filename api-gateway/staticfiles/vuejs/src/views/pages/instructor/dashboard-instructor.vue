<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layoutsinstructorborder></layoutsinstructorborder>
    <instructorbreadcrumb></instructorbreadcrumb>
    <!-- Instructor Dashboard -->
    <section class="page-content course-sec">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="card instructor-card">
              <div class="card-header">
                <h4>My Courses</h4>
                <router-link to="add-course" class="btn btn-dark"
                  >Create New Course</router-link
                >
              </div>
              <div class="card-body">
                <div class="instructor-grid">
                  <div class="product-img">
                    <router-link to="course-details">
                      <img
                        src="@/assets/img/course/course-10.jpg"
                        class="img-fluid"
                        alt=""
                      />
                    </router-link>
                  </div>
                  <div class="instructor-product-content">
                    <div class="head-course-title">
                      <h3 class="title">
                        <router-link to="course-details"
                          >Information About UI/UX Design Degree</router-link
                        >
                      </h3>
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
                    <div class="rating mb-0">
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
                <div class="instructor-grid">
                  <div class="product-img">
                    <router-link to="course-details">
                      <img
                        src="@/assets/img/course/course-11.jpg"
                        class="img-fluid"
                        alt=""
                      />
                    </router-link>
                  </div>
                  <div class="instructor-product-content">
                    <div class="head-course-title">
                      <h3 class="title">
                        <router-link to="course-details"
                          >Wordpress for Beginners - Master Wordpress Quickly</router-link
                        >
                      </h3>
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
                    <div class="rating mb-0">
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star me-1"></i>
                      <span class="d-inline-block average-rating"
                        ><span>4.2</span> (20)</span
                      >
                    </div>
                  </div>
                </div>
                <div class="instructor-grid">
                  <div class="product-img">
                    <router-link to="course-details">
                      <img
                        src="@/assets/img/course/course-12.jpg"
                        class="img-fluid"
                        alt=""
                      />
                    </router-link>
                  </div>
                  <div class="instructor-product-content">
                    <div class="head-course-title">
                      <h3 class="title">
                        <router-link to="course-details"
                          >Sketch from A to Z (2023): Become an app designer</router-link
                        >
                      </h3>
                    </div>
                    <div
                      class="course-info d-flex align-items-center border-bottom-0 pb-0"
                    >
                      <div class="rating-img d-flex align-items-center">
                        <img src="@/assets/img/icon/icon-01.svg" alt="" />
                        <p>05+ Lesson</p>
                      </div>
                      <div class="course-view d-flex align-items-center">
                        <img src="@/assets/img/icon/icon-02.svg" alt="" />
                        <p>8hr 00min</p>
                      </div>
                    </div>
                    <div class="rating mb-0">
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star me-1"></i>
                      <span class="d-inline-block average-rating"
                        ><span>4.0</span> (10)</span
                      >
                    </div>
                  </div>
                </div>
                <div class="instructor-grid">
                  <div class="product-img">
                    <router-link to="course-details">
                      <img
                        src="@/assets/img/course/course-13.jpg"
                        class="img-fluid"
                        alt=""
                      />
                    </router-link>
                  </div>
                  <div class="instructor-product-content">
                    <div class="head-course-title">
                      <h3 class="title">
                        <router-link to="course-details"
                          >Learn Angular Fundamentals From beginning to advance
                          lavel</router-link
                        >
                      </h3>
                    </div>
                    <div
                      class="course-info d-flex align-items-center border-bottom-0 pb-0"
                    >
                      <div class="rating-img d-flex align-items-center">
                        <img src="@/assets/img/icon/icon-01.svg" alt="" />
                        <p>30+ Lesson</p>
                      </div>
                      <div class="course-view d-flex align-items-center">
                        <img src="@/assets/img/icon/icon-02.svg" alt="" />
                        <p>10hr 30min</p>
                      </div>
                    </div>
                    <div class="rating mb-0">
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star me-1"></i>
                      <span class="d-inline-block average-rating"
                        ><span>4.3</span> (25)</span
                      >
                    </div>
                  </div>
                </div>
                <div class="instructor-grid">
                  <div class="product-img">
                    <router-link to="course-details">
                      <img
                        src="@/assets/img/course/course-14.jpg"
                        class="img-fluid"
                        alt=""
                      />
                    </router-link>
                  </div>
                  <div class="instructor-product-content">
                    <div class="head-course-title">
                      <h3 class="title">
                        <router-link to="course-details"
                          >Build Responsive Real World Websites with HTML5 and
                          CSS3</router-link
                        >
                      </h3>
                    </div>
                    <div
                      class="course-info d-flex align-items-center border-bottom-0 pb-0"
                    >
                      <div class="rating-img d-flex align-items-center">
                        <img src="@/assets/img/icon/icon-01.svg" alt="" />
                        <p>20+ Lesson</p>
                      </div>
                      <div class="course-view d-flex align-items-center">
                        <img src="@/assets/img/icon/icon-02.svg" alt="" />
                        <p>7hr 00min</p>
                      </div>
                    </div>
                    <div class="rating mb-0">
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
                <div class="instructor-grid mb-0">
                  <div class="product-img">
                    <router-link to="course-details">
                      <img
                        src="@/assets/img/course/course-15.jpg"
                        class="img-fluid"
                        alt=""
                      />
                    </router-link>
                  </div>
                  <div class="instructor-product-content">
                    <div class="head-course-title">
                      <h3 class="title">
                        <router-link to="course-details"
                          >C# Developers Double Your Coding Speed with Visual
                          Studio</router-link
                        >
                      </h3>
                    </div>
                    <div
                      class="course-info d-flex align-items-center border-bottom-0 pb-0"
                    >
                      <div class="rating-img d-flex align-items-center">
                        <img src="@/assets/img/icon/icon-01.svg" alt="" />
                        <p>50+ Lesson</p>
                      </div>
                      <div class="course-view d-flex align-items-center">
                        <img src="@/assets/img/icon/icon-02.svg" alt="" />
                        <p>10hr 30min</p>
                      </div>
                    </div>
                    <div class="rating mb-0">
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star filled me-1"></i>
                      <i class="fas fa-star me-1"></i>
                      <span class="d-inline-block average-rating"
                        ><span>4.5</span> (30)</span
                      >
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- /Instructor Dashboard -->

    <layouts1></layouts1>
  </div>
  <!-- /Main Wrapper -->
</template>
