<template>
  <!-- Feature Course -->
  <section class="section new-course">
    <div class="container">
      <div class="section-header aos" data-aos="fade-up">
        <div class="section-sub-head">
          <span>What’s New</span>
          <h2>Featured Courses</h2>
        </div>
        <div class="all-btn all-category d-flex align-items-center">
          <router-link to="course-list" class="btn btn-primary">All Courses</router-link>
        </div>
      </div>
      <div class="section-text aos" data-aos="fade-up">
        <p class="mb-0">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Eget aenean accumsan
          bibendum gravida maecenas augue elementum et neque. Suspendisse imperdiet.
        </p>
      </div>
      <div class="course-feature">
        <div class="row">
          <div class="col-lg-4 col-md-6 d-flex">
            <div class="course-box d-flex aos" data-aos="fade-up">
              <div class="product">
                <div class="product-img">
                  <router-link to="course-details">
                    <img
                      class="img-fluid"
                      alt=""
                      src="@/assets/img/course/course-01.jpg"
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
                          <router-link to="instructor-profile">Nicole Brown</router-link>
                        </h4>
                        <p>Instructor</p>
                      </div>
                    </div>
                    <div
                      class="course-share d-flex align-items-center justify-content-center"
                    >
                      <a href="javascript:void(0);"
                        ><i class="fa-regular fa-heart"></i
                      ></a>
                    </div>
                  </div>
                  <h3 class="title instructor-text">
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
            <div class="course-box d-flex aos" data-aos="fade-up">
              <div class="product">
                <div class="product-img">
                  <router-link to="course-details">
                    <img
                      class="img-fluid"
                      alt=""
                      src="@/assets/img/course/course-02.jpg"
                    />
                  </router-link>
                  <div class="price">
                    <h3>$400 <span>$99.00</span></h3>
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
                      <a href="javascript:void(0);"
                        ><i class="fa-regular fa-heart"></i
                      ></a>
                    </div>
                  </div>
                  <h3 class="title instructor-text">
                    <router-link to="course-details"
                      >Wordpress for Beginners - Master Wordpress Quickly</router-link
                    >
                  </h3>
                  <div class="course-info d-flex align-items-center">
                    <div class="rating-img d-flex align-items-center">
                      <img src="@/assets/img/icon/icon-01.svg" alt="" />
                      <p>11+ Lesson</p>
                    </div>
                    <div class="course-view d-flex align-items-center">
                      <img src="@/assets/img/icon/icon-02.svg" alt="" />
                      <p>6hr 30min</p>
                    </div>
                  </div>
                  <div class="rating">
                    <i class="fas fa-star filled me-1"></i>
                    <i class="fas fa-star filled me-1"></i>
                    <i class="fas fa-star filled me-1"></i>
                    <i class="fas fa-star filled me-1"></i>
                    <i class="fas fa-star me-1"></i>
                    <span class="d-inline-block average-rating"
                      ><span>4.3</span> (15)</span
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
            <div class="course-box d-flex aos" data-aos="fade-up">
              <div class="product">
                <div class="product-img">
                  <router-link to="course-details">
                    <img
                      class="img-fluid"
                      alt=""
                      src="@/assets/img/course/course-03.jpg"
                    />
                  </router-link>
                  <div class="price combo">
                    <h3>FREE</h3>
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
                          <router-link to="instructor-profile">Jesse Stevens</router-link>
                        </h4>
                        <p>Instructor</p>
                      </div>
                    </div>
                    <div
                      class="course-share d-flex align-items-center justify-content-center"
                    >
                      <a href="javascript:void(0);"
                        ><i class="fa-regular fa-heart"></i
                      ></a>
                    </div>
                  </div>
                  <h3 class="title instructor-text">
                    <router-link to="course-details"
                      >Sketch from A to Z (2023): Become an app designer</router-link
                    >
                  </h3>
                  <div class="course-info d-flex align-items-center">
                    <div class="rating-img d-flex align-items-center">
                      <img src="@/assets/img/icon/icon-01.svg" alt="" />
                      <p>16+ Lesson</p>
                    </div>
                    <div class="course-view d-flex align-items-center">
                      <img src="@/assets/img/icon/icon-02.svg" alt="" />
                      <p>12hr 30min</p>
                    </div>
                  </div>
                  <div class="rating">
                    <i class="fas fa-star filled me-1"></i>
                    <i class="fas fa-star filled me-1"></i>
                    <i class="fas fa-star filled me-1"></i>
                    <i class="fas fa-star filled me-1"></i>
                    <i class="fas fa-star me-1"></i>
                    <span class="d-inline-block average-rating"
                      ><span>4.5</span> (15)</span
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
            <div class="course-box d-flex aos" data-aos="fade-up">
              <div class="product">
                <div class="product-img">
                  <router-link to="course-details">
                    <img
                      class="img-fluid"
                      alt=""
                      src="@/assets/img/course/course-04.jpg"
                    />
                  </router-link>
                  <div class="price">
                    <h3>$500 <span>$99.00</span></h3>
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
                          <router-link to="instructor-profile">Nicole Brown</router-link>
                        </h4>
                        <p>Instructor</p>
                      </div>
                    </div>
                    <div
                      class="course-share d-flex align-items-center justify-content-center"
                    >
                      <a href="javascript:void(0);"
                        ><i class="fa-regular fa-heart"></i
                      ></a>
                    </div>
                  </div>
                  <h3 class="title instructor-text">
                    <router-link to="course-details"
                      >Learn Angular Fundamentals From beginning to advance
                      lavel</router-link
                    >
                  </h3>
                  <div class="course-info d-flex align-items-center">
                    <div class="rating-img d-flex align-items-center">
                      <img src="@/assets/img/icon/icon-01.svg" alt="" />
                      <p>10+ Lesson</p>
                    </div>
                    <div class="course-view d-flex align-items-center">
                      <img src="@/assets/img/icon/icon-02.svg" alt="" />
                      <p>8hr 30min</p>
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
            <div class="course-box d-flex aos" data-aos="fade-up">
              <div class="product">
                <div class="product-img">
                  <router-link to="course-details">
                    <img
                      class="img-fluid"
                      alt=""
                      src="@/assets/img/course/course-05.jpg"
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
                          src="@/assets/img/user/user3.jpg"
                          alt=""
                          class="img-fluid"
                      /></router-link>
                      <div class="course-name">
                        <h4>
                          <router-link to="instructor-profile">John Smith</router-link>
                        </h4>
                        <p>Instructor</p>
                      </div>
                    </div>
                    <div
                      class="course-share d-flex align-items-center justify-content-center"
                    >
                      <a href="javascript:void(0);"
                        ><i class="fa-regular fa-heart"></i
                      ></a>
                    </div>
                  </div>
                  <h3 class="title instructor-text">
                    <router-link to="course-details"
                      >Build Responsive Real World Websites with HTML5 and
                      CSS3</router-link
                    >
                  </h3>
                  <div class="course-info d-flex align-items-center">
                    <div class="rating-img d-flex align-items-center">
                      <img src="@/assets/img/icon/icon-01.svg" alt="" />
                      <p>13+ Lesson</p>
                    </div>
                    <div class="course-view d-flex align-items-center">
                      <img src="@/assets/img/icon/icon-02.svg" alt="" />
                      <p>10hr 30min</p>
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
            <div class="course-box d-flex aos" data-aos="fade-up">
              <div class="product">
                <div class="product-img">
                  <router-link to="course-details">
                    <img
                      class="img-fluid"
                      alt=""
                      src="@/assets/img/course/course-06.jpg"
                    />
                  </router-link>
                  <div class="price combo">
                    <h3>FREE</h3>
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
                      <a href="javascript:void(0);"
                        ><i class="fa-regular fa-heart"></i
                      ></a>
                    </div>
                  </div>
                  <h3 class="title instructor-text">
                    <router-link to="course-details"
                      >C# Developers Double Your Coding Speed with Visual
                      Studio</router-link
                    >
                  </h3>
                  <div class="course-info d-flex align-items-center">
                    <div class="rating-img d-flex align-items-center">
                      <img src="@/assets/img/icon/icon-01.svg" alt="" />
                      <p>7+ Lesson</p>
                    </div>
                    <div class="course-view d-flex align-items-center">
                      <img src="@/assets/img/icon/icon-02.svg" alt="" />
                      <p>7hr 30min</p>
                    </div>
                  </div>
                  <div class="rating">
                    <i class="fas fa-star filled me-1"></i>
                    <i class="fas fa-star filled me-1"></i>
                    <i class="fas fa-star filled me-1"></i>
                    <i class="fas fa-star filled me-1"></i>
                    <i class="fas fa-star me-1"></i>
                    <span class="d-inline-block average-rating"
                      ><span>4.6</span> (15)</span
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
      </div>
    </div>
  </section>
  <!-- /Feature Course -->

  <!-- Master Skill -->
  <section class="section master-skill">
    <div class="container">
      <div class="row">
        <div class="col-lg-7 col-md-12">
          <div class="section-header aos" data-aos="fade-up">
            <div class="section-sub-head">
              <span>What’s New</span>
              <h2>Master the skills to drive your career</h2>
            </div>
          </div>
          <div class="section-text aos" data-aos="fade-up">
            <p>
              Get certified, master modern tech skills, and level up your career — whether
              you’re starting out or a seasoned pro. 95% of eLearning learners report our
              hands-on content directly helped their careers.
            </p>
          </div>
          <div class="career-group aos" data-aos="fade-up">
            <div class="row">
              <div class="col-lg-6 col-md-6 d-flex">
                <div class="certified-group blur-border d-flex">
                  <div class="get-certified d-flex align-items-center">
                    <div class="blur-box">
                      <div class="certified-img">
                        <img
                          src="@/assets/img/icon/icon-1.svg"
                          alt=""
                          class="img-fluid"
                        />
                      </div>
                    </div>
                    <p>Stay motivated with engaging instructors</p>
                  </div>
                </div>
              </div>
              <div class="col-lg-6 col-md-6 d-flex">
                <div class="certified-group blur-border d-flex">
                  <div class="get-certified d-flex align-items-center">
                    <div class="blur-box">
                      <div class="certified-img">
                        <img
                          src="@/assets/img/icon/icon-2.svg"
                          alt=""
                          class="img-fluid"
                        />
                      </div>
                    </div>
                    <p>Keep up with in the latest in cloud</p>
                  </div>
                </div>
              </div>
              <div class="col-lg-6 col-md-6 d-flex">
                <div class="certified-group blur-border d-flex">
                  <div class="get-certified d-flex align-items-center">
                    <div class="blur-box">
                      <div class="certified-img">
                        <img
                          src="@/assets/img/icon/icon-3.svg"
                          alt=""
                          class="img-fluid"
                        />
                      </div>
                    </div>
                    <p>Get certified with 100+ certification courses</p>
                  </div>
                </div>
              </div>
              <div class="col-lg-6 col-md-6 d-flex">
                <div class="certified-group blur-border d-flex">
                  <div class="get-certified d-flex align-items-center">
                    <div class="blur-box">
                      <div class="certified-img">
                        <img
                          src="@/assets/img/icon/icon-4.svg"
                          alt=""
                          class="img-fluid"
                        />
                      </div>
                    </div>
                    <p>Build skills your way, from labs to courses</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-5 col-md-12 d-flex align-items-end">
          <div class="career-img aos" data-aos="fade-up">
            <img src="@/assets/img/join.png" alt="" class="img-fluid" />
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- /Master Skill -->
</template>
<script>
import AOS from "aos";
import "aos/dist/aos.css";
export default {
  data() {
    return {};
  },

  mounted() {
    this.$nextTick(() => {
      AOS.init();
    });
  },
};
</script>
