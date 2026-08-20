<template>
  <!-- Home Banner -->
  <section class="home-slide-five">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6 col-12">
          <div class="home-slide-five-face" data-aos="fade-down">
            <!-- Banner Text -->
            <div class="home-slide-five-text">
              <h5>The Leader in Online Learning</h5>
              <h1>Engaging & Accessible Online Courses For All</h1>
              <p>
                Trusted by over 15K Users worldwide since {{ new Date().getFullYear() }}
              </p>
            </div>
            <!-- /Banner Text -->

            <!-- banner Seach Category -->
            <div class="banner-content-five">
              <form class="form" @submit.prevent="submitForm">
                <div class="form-inner-five">
                  <div class="input-group">
                    <!-- Slect Category -->
                    <span class="drop-detail-five">
                      <vue-select
                        :options="Category"
                        placeholder="Category"
                        class="ms-4"
                      />
                    </span>
                    <!-- Slect Category -->

                    <!-- Search -->
                    <input
                      type="email"
                      class="form-control"
                      placeholder="Search School, Online eductional centers, etc"
                    />
                    <!-- Search -->

                    <!-- Submit Button -->
                    <button class="btn btn-primary sub-btn" type="submit">
                      <span><i class="fa-solid fa-magnifying-glass"></i></span>
                    </button>
                    <!-- Submit Button -->
                  </div>
                </div>
              </form>
            </div>
            <!-- /banner Seach Category -->

            <!-- Review and Experience -->
            <div class="review-five-group">
              <div class="review-user-five d-flex align-items-center">
                <ul class="review-users-list">
                  <li>
                    <a
                      href="javascript:;"
                      data-bs-toggle="tooltip"
                      data-bs-placement="top"
                      title=""
                      data-bs-original-title="leader 1"
                      ><img src="@/assets/img/profiles/avatar-01.jpg" alt="img"
                    /></a>
                  </li>
                  <li>
                    <a
                      href="javascript:;"
                      data-bs-toggle="tooltip"
                      data-bs-placement="top"
                      title=""
                      data-bs-original-title="leader 2"
                      ><img src="@/assets/img/profiles/avatar-02.jpg" alt="img"
                    /></a>
                  </li>
                  <li>
                    <a
                      href="javascript:;"
                      data-bs-toggle="tooltip"
                      data-bs-placement="top"
                      title=""
                      data-bs-original-title="leader 3"
                      ><img src="@/assets/img/profiles/avatar-03.jpg" alt="img"
                    /></a>
                  </li>
                  <li>
                    <a
                      href="javascript:;"
                      data-bs-toggle="tooltip"
                      data-bs-placement="top"
                      title=""
                      data-bs-original-title="leader 3"
                      ><img src="@/assets/img/profiles/avatar-04.jpg" alt="img"
                    /></a>
                  </li>
                </ul>
                <div class="review-rating-five">
                  <div class="rating-star">
                    <p>5.5</p>
                    <i class="fas fa-star filled me-1 ms-1"></i>
                    <i class="fas fa-star filled me-1"></i>
                    <i class="fas fa-star filled me-1"></i>
                    <i class="fas fa-star filled me-1"></i>
                    <i class="fas fa-star filled"></i>
                  </div>
                </div>
              </div>
              <!-- Experience -->
              <div class="rate-head-five d-flex align-items-center course-count">
                <h2>
                  <span class="counterUp"
                    ><vue3-autocounter
                      class="counter"
                      ref="counter"
                      :startAmount="1"
                      :delay="3"
                      :endAmount="10"
                      :duration="5"
                      :autoinit="true" /></span
                  >+
                </h2>
                <p>Years of experience tutors</p>
              </div>
              <!-- /Experience -->
            </div>
            <!-- /Review and Experience -->
          </div>
        </div>
        <div class="col-lg-6 col-12">
          <div class="banner-slider-img">
            <div class="row">
              <div class="col-lg-6 align-self-end">
                <div class="slider-five-one" data-aos="fade-down">
                  <img src="@/assets/img/slider/slider-01.png" alt="" />
                </div>
              </div>
              <div class="col-lg-6">
                <div class="slider-five-two aos" data-aos="fade-down">
                  <img src="@/assets/img/slider/slider-02.png" alt="" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="vector-shapes-five">
        <img src="@/assets/img/bg/banner-vector.svg" alt="" />
      </div>
    </div>
  </section>
  <!-- /Home Banner -->

  <!-- Leading Companies -->
  <section class="leading-section-five">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-4 col-md-6" data-aos="fade-down">
          <div class="leading-five-content course-count">
            <h2>
              Trusted By
              <span class="counterUp"
                ><vue3-autocounter
                  class="counter"
                  ref="counter"
                  :startAmount="50"
                  :delay="3"
                  :endAmount="500"
                  :duration="5"
                  :autoinit="true" /></span
              >+
            </h2>
            <p>Leading Universities And Companies</p>
          </div>
        </div>
        <div class="col-lg-8 col-md-6" data-aos="fade-down">
          <div class="lead-group-five">
            <Carousel
              :autoplay="2000"
              :loop="true"
              :wrap-around="true"
              :settings="settingsland"
              :breakpoints="breakpointsland"
            >
              <Slide
                v-for="item in leading"
                :key="item.id"
                class="leading-slider-five owl-carousel owl-theme"
              >
                <div class="carousel__item item">
                  <div class="lead-img">
                    <img
                      class="img-fluid"
                      alt=""
                      :src="require(`@/assets/img/client/${item.img}`)"
                    />
                  </div>
                </div>
              </Slide>
            </Carousel>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- /Leading Companies -->

  <!-- Course Categories Five -->
  <section class="course-section-five">
    <div class="container">
      <div class="header-five-title text-center" data-aos="fade-down">
        <h2>Course Categories</h2>
        <p>Pick Your Favourite Course</p>
      </div>
      <div class="home-five-course">
        <Carousel :settings="settings" :breakpoints="breakpoints">
          <Slide
            v-for="(item, index) in courseinfo"
            :key="index"
            class="carousel-five-item"
          >
            <div class="course-five-item">
              <div class="course-five-grid">
                <div class="course-icon-five">
                  <div class="icon-five-border">
                    <router-link to="job-category">
                      <img :src="require(`@/assets/img/course/${item.image}`)" alt="" />
                    </router-link>
                  </div>
                </div>
                <div class="course-info-five">
                  <router-link to="job-category">
                    <h3>{{ item.title }}</h3>
                    <p>{{ item.instructors }} Instructors</p>
                  </router-link>
                </div>
                <div class="course-info-btn">
                  <router-link to="job-category" class="btn-five">
                    <i class="fas fa-chevron-right"></i>
                  </router-link>
                </div>
              </div>
            </div>
          </Slide>
          <template #addons>
            <Pagination />
          </template>
        </Carousel>
      </div>
    </div>
  </section>
  <!-- /Course Categories Five-->
</template>
<script>
import AOS from "aos";
import "aos/dist/aos.css";
import leading from "@/assets/json/leading.json";
import courseinfo from "@/assets/json/courseinfo.json";
import { Carousel, Pagination, Slide } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
export default {
  components: {
    Carousel,
    Slide,
    Pagination,
  },
  data() {
    return {
      Category: ["category", "Angular", "Node Js", "React", "Python"],
      leading: leading,
      courseinfo: courseinfo,
      settingsland: {
        itemsToShow: 1,
        snapAlign: "center",
      },

      breakpointsland: {
        // 700px and up
        700: {
          itemsToShow: 2,
          snapAlign: "center",
        },
        // 1024 and up
        1024: {
          itemsToShow: 4,
          snapAlign: "start",
        },
      },
      settings: {
        itemsToShow: 1,
        snapAlign: "center",
      },
      breakpoints: {
        // 700px and up
        575: {
          itemsToShow: 1,
          snapAlign: "center",
        },
        700: {
          itemsToShow: 2,
          snapAlign: "center",
        },
        // 1024 and up
        1024: {
          itemsToShow: 3,
          snapAlign: "start",
        },
      },
    };
  },
  methods: {
    submitForm() {
      this.$router.push("/course-list");
    },
  },
  mounted() {
    this.$nextTick(() => {
      AOS.init();
    });
  },
};
</script>
