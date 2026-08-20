<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layouts2></layouts2>
    <coursegridbreadcrumb></coursegridbreadcrumb>
    <!-- Course -->
    <section class="course-content">
      <div class="container">
        <div class="row">
          <div class="col-lg-9">
            <coursefilter></coursefilter>

            <div class="row">
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="course-box course-design d-flex">
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
                        <h3>$300 <span>$99.00</span></h3>
                      </div>
                    </div>
                    <div class="product-content">
                      <div class="course-group d-flex">
                        <div class="course-group-img d-flex">
                          <router-link to="instructor-profile"
                            ><img
                              src="@/assets/img/user/user1.jpg"
                              alt=""
                              class="img-fluid"
                          /></router-link>
                          <div class="course-name">
                            <h4>
                              <router-link to="instructor-profile">Rolands R</router-link>
                            </h4>
                            <p>Instructor</p>
                          </div>
                        </div>
                        <div
                          class="course-share d-flex align-items-center justify-content-center"
                        >
                          <a href="javascript:;"><i class="fa-regular fa-heart"></i></a>
                        </div>
                      </div>
                      <h3 class="title">
                        <router-link to="course-details"
                          >Information About UI/UX Design Degree</router-link
                        >
                      </h3>
                      <div class="course-info d-flex align-items-center">
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
                      <div class="all-btn all-category d-flex align-items-center">
                        <router-link to="checkout" class="btn btn-primary"
                          >BUY NOW</router-link
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="course-box course-design d-flex">
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
                        <h3>$200 <span>$99.00</span></h3>
                      </div>
                    </div>
                    <div class="product-content">
                      <div class="course-group d-flex">
                        <div class="course-group-img d-flex">
                          <router-link to="instructor-profile"
                            ><img
                              src="@/assets/img/user/user2.jpg"
                              alt=""
                              class="img-fluid"
                          /></router-link>
                          <div class="course-name">
                            <h4>
                              <router-link to="instructor-profile">Jenis R.</router-link>
                            </h4>
                            <p>Instructor</p>
                          </div>
                        </div>
                        <div
                          class="course-share d-flex align-items-center justify-content-center"
                        >
                          <a href="javascript:;"><i class="fa-regular fa-heart"></i></a>
                        </div>
                      </div>
                      <h3 class="title">
                        <router-link to="course-details"
                          >Wordpress for Beginners - Master Wordpress Quickly</router-link
                        >
                      </h3>
                      <div class="course-info d-flex align-items-center">
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
                      <div class="all-btn all-category d-flex align-items-center">
                        <router-link to="checkout" class="btn btn-primary"
                          >BUY NOW</router-link
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="course-box course-design d-flex">
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
                        <h3 class="free-color">FREE</h3>
                      </div>
                    </div>
                    <div class="product-content">
                      <div class="course-group d-flex">
                        <div class="course-group-img d-flex">
                          <router-link to="instructor-profile"
                            ><img
                              src="@/assets/img/user/user3.jpg"
                              alt=""
                              class="img-fluid"
                          /></router-link>
                          <div class="course-name">
                            <h4>
                              <router-link to="instructor-profile"
                                >Jesse Stevens</router-link
                              >
                            </h4>
                            <p>Instructor</p>
                          </div>
                        </div>
                        <div
                          class="course-share d-flex align-items-center justify-content-center"
                        >
                          <a href="javascript:;"><i class="fa-regular fa-heart"></i></a>
                        </div>
                      </div>
                      <h3 class="title">
                        <router-link to="course-details"
                          >Sketch from A to Z (2023): Become an app designer</router-link
                        >
                      </h3>
                      <div class="course-info d-flex align-items-center">
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
                      <div class="all-btn all-category d-flex align-items-center">
                        <router-link to="checkout" class="btn btn-primary"
                          >BUY NOW</router-link
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="course-box course-design d-flex">
                  <div class="product">
                    <div class="product-img">
                      <router-link to="course-details">
                        <img
                          class="img-fluid"
                          alt=""
                          src="@/assets/img/course/course-13.jpg"
                        />
                      </router-link>
                      <div class="price">
                        <h3 class="free-color">FREE</h3>
                      </div>
                    </div>
                    <div class="product-content">
                      <div class="course-group d-flex">
                        <div class="course-group-img d-flex">
                          <router-link to="instructor-profile"
                            ><img
                              src="@/assets/img/user/user4.jpg"
                              alt=""
                              class="img-fluid"
                          /></router-link>
                          <div class="course-name">
                            <h4>
                              <router-link to="instructor-profile"
                                >Nicole Brown</router-link
                              >
                            </h4>
                            <p>Instructor</p>
                          </div>
                        </div>
                        <div
                          class="course-share d-flex align-items-center justify-content-center"
                        >
                          <a href="javascript:;" class="active-heart"
                            ><i class="fa-regular fa-heart"></i
                          ></a>
                        </div>
                      </div>
                      <h3 class="title">
                        <router-link to="course-details"
                          >Learn Angular Fundamentals From ...</router-link
                        >
                      </h3>
                      <div class="course-info d-flex align-items-center">
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
                      <div class="all-btn all-category d-flex align-items-center">
                        <router-link to="checkout" class="btn btn-primary"
                          >BUY NOW</router-link
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="course-box course-design d-flex">
                  <div class="product">
                    <div class="product-img">
                      <router-link to="course-details">
                        <img
                          class="img-fluid"
                          alt=""
                          src="@/assets/img/course/course-14.jpg"
                        />
                      </router-link>
                      <div class="price">
                        <h3>$29.99</h3>
                      </div>
                    </div>
                    <div class="product-content">
                      <div class="course-group d-flex">
                        <div class="course-group-img d-flex">
                          <router-link to="instructor-profile"
                            ><img
                              src="@/assets/img/user/user5.jpg"
                              alt=""
                              class="img-fluid"
                          /></router-link>
                          <div class="course-name">
                            <h4>
                              <router-link to="instructor-profile"
                                >John Smith</router-link
                              >
                            </h4>
                            <p>Instructor</p>
                          </div>
                        </div>
                        <div
                          class="course-share d-flex align-items-center justify-content-center"
                        >
                          <a href="javascript:;" class="active-heart"
                            ><i class="fa-regular fa-heart"></i
                          ></a>
                        </div>
                      </div>
                      <h3 class="title">
                        <router-link to="course-details"
                          >Build Responsive Real World Websites with ...</router-link
                        >
                      </h3>
                      <div class="course-info d-flex align-items-center">
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
                      <div class="all-btn all-category d-flex align-items-center">
                        <router-link to="checkout" class="btn btn-primary"
                          >BUY NOW</router-link
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="course-box course-design d-flex">
                  <div class="product">
                    <div class="product-img">
                      <router-link to="course-details">
                        <img
                          class="img-fluid"
                          alt=""
                          src="@/assets/img/course/course-15.jpg"
                        />
                      </router-link>
                      <div class="price">
                        <h3>$300 <span>$99.00</span></h3>
                      </div>
                    </div>
                    <div class="product-content">
                      <div class="course-group d-flex">
                        <div class="course-group-img d-flex">
                          <router-link to="instructor-profile"
                            ><img
                              src="@/assets/img/user/user6.jpg"
                              alt=""
                              class="img-fluid"
                          /></router-link>
                          <div class="course-name">
                            <h4>
                              <router-link to="instructor-profile"
                                >Stella Johnson</router-link
                              >
                            </h4>
                            <p>Instructor</p>
                          </div>
                        </div>
                        <div
                          class="course-share d-flex align-items-center justify-content-center"
                        >
                          <a href="javascript:;" class="active-heart"
                            ><i class="fa-regular fa-heart"></i
                          ></a>
                        </div>
                      </div>
                      <h3 class="title">
                        <router-link to="course-details"
                          >C# Developers Double Your Coding Speed with ...</router-link
                        >
                      </h3>
                      <div class="course-info d-flex align-items-center">
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
                      <div class="all-btn all-category d-flex align-items-center">
                        <router-link to="checkout" class="btn btn-primary"
                          >BUY NOW</router-link
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="course-box course-design d-flex">
                  <div class="product">
                    <div class="product-img">
                      <router-link to="course-details">
                        <img
                          class="img-fluid"
                          alt=""
                          src="@/assets/img/course/course-16.jpg"
                        />
                      </router-link>
                      <div class="price">
                        <h3>$200 <span>$99.00</span></h3>
                      </div>
                    </div>
                    <div class="product-content">
                      <div class="course-group d-flex">
                        <div class="course-group-img d-flex">
                          <router-link to="instructor-profile"
                            ><img
                              src="@/assets/img/user/user.jpg"
                              alt=""
                              class="img-fluid"
                          /></router-link>
                          <div class="course-name">
                            <h4>
                              <router-link to="instructor-profile"
                                >John Michael</router-link
                              >
                            </h4>
                            <p>Instructor</p>
                          </div>
                        </div>
                        <div
                          class="course-share d-flex align-items-center justify-content-center"
                        >
                          <a href="javascript:;"><i class="fa-regular fa-heart"></i></a>
                        </div>
                      </div>
                      <h3 class="title">
                        <router-link to="course-details"
                          >Learn JavaScript and Express to become a...</router-link
                        >
                      </h3>
                      <div class="course-info d-flex align-items-center">
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
                      <div class="all-btn all-category d-flex align-items-center">
                        <router-link to="checkout" class="btn btn-primary"
                          >BUY NOW</router-link
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="course-box course-design d-flex">
                  <div class="product">
                    <div class="product-img">
                      <router-link to="course-details">
                        <img
                          class="img-fluid"
                          alt=""
                          src="@/assets/img/course/course-13.jpg"
                        />
                      </router-link>
                      <div class="price">
                        <h3>$300 <span>$99.00</span></h3>
                      </div>
                    </div>
                    <div class="product-content">
                      <div class="course-group d-flex">
                        <div class="course-group-img d-flex">
                          <router-link to="instructor-profile"
                            ><img
                              src="@/assets/img/user/user4.jpg"
                              alt=""
                              class="img-fluid"
                          /></router-link>
                          <div class="course-name">
                            <h4>
                              <router-link to="instructor-profile"
                                >Jesse Stevens</router-link
                              >
                            </h4>
                            <p>Instructor</p>
                          </div>
                        </div>
                        <div
                          class="course-share d-flex align-items-center justify-content-center"
                        >
                          <a href="javascript:;"><i class="fa-regular fa-heart"></i></a>
                        </div>
                      </div>
                      <h3 class="title">
                        <router-link to="course-details"
                          >Learn and Understand AngularJS to become a ...</router-link
                        >
                      </h3>
                      <div class="course-info d-flex align-items-center">
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
                      <div class="all-btn all-category d-flex align-items-center">
                        <router-link to="checkout" class="btn btn-primary"
                          >BUY NOW</router-link
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-4 col-md-6 d-flex">
                <div class="course-box course-design d-flex">
                  <div class="product">
                    <div class="product-img">
                      <router-link to="course-details">
                        <img
                          class="img-fluid"
                          alt=""
                          src="@/assets/img/course/course-17.jpg"
                        />
                      </router-link>
                      <div class="price">
                        <h3 class="free-color">FREE</h3>
                      </div>
                    </div>
                    <div class="product-content">
                      <div class="course-group d-flex">
                        <div class="course-group-img d-flex">
                          <router-link to="instructor-profile"
                            ><img
                              src="@/assets/img/user/user6.jpg"
                              alt=""
                              class="img-fluid"
                          /></router-link>
                          <div class="course-name">
                            <h4>
                              <router-link to="instructor-profile"
                                >Monroe Parker</router-link
                              >
                            </h4>
                            <p>Instructor</p>
                          </div>
                        </div>
                        <div
                          class="course-share d-flex align-items-center justify-content-center"
                        >
                          <a href="javascript:;"><i class="fa-regular fa-heart"></i></a>
                        </div>
                      </div>
                      <h3 class="title">
                        <router-link to="course-details"
                          >Responsive Web Design Essentials HTML5 CSS3 ...</router-link
                        >
                      </h3>
                      <div class="course-info d-flex align-items-center">
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
                      <div class="all-btn all-category d-flex align-items-center">
                        <router-link to="checkout" class="btn btn-primary"
                          >BUY NOW</router-link
                        >
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <pagination></pagination>
          </div>
          <gridlistsidebar></gridlistsidebar>
        </div>
      </div>
    </section>
    <!-- /Course -->

    <layouts1></layouts1>
  </div>
  <!-- /Main Wrapper -->
</template>
