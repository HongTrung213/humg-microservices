<template>
  <!-- Home Banner -->
  <section class="home-slide d-flex align-items-center">
    <div class="container">
      <div class="row">
        <div class="col-md-7">
          <div class="home-slide-face aos" data-aos="fade-up">
            <div class="home-slide-text">
              <h5>The Leader in Online Learning</h5>
              <h1>Engaging & Accessible Online Courses For All</h1>
              <p>Own your future learning new skills online</p>
            </div>
            <div class="banner-content">
              <form class="form" @submit.prevent="submitForm">
                <div class="form-inner">
                  <div class="input-group">
                    <i class="fa-solid fa-magnifying-glass search-icon"></i>
                    <input
                      type="email"
                      class="form-control"
                      placeholder="Search School, Online eductional centers, etc"
                    />
                    <span class="drop-detail">
                      <vue-select
                        :options="Category"
                        placeholder="Category"
                        class="vueselect"
                      />
                    </span>
                    <button class="btn btn-primary sub-btn" type="submit">
                      <i class="fas fa-arrow-right"></i>
                    </button>
                  </div>
                </div>
              </form>
            </div>
            <div class="trust-user">
              <p>Trusted by over 15K Users <br />worldwide since 2023</p>
              <div class="trust-rating d-flex align-items-center">
                <div class="rate-head">
                  <h2>
                    <span
                      ><vue3-autocounter
                        class="counter"
                        ref="counter"
                        :startAmount="200"
                        :delay="3"
                        :endAmount="1000"
                        :duration="5"
                        :autoinit="true" /></span
                    >+
                  </h2>
                </div>
                <div class="rating d-flex align-items-center">
                  <h2 class="d-inline-block average-rating">4.4</h2>
                  <i class="fas fa-star filled me-1"></i>
                  <i class="fas fa-star filled me-1"></i>
                  <i class="fas fa-star filled me-1"></i>
                  <i class="fas fa-star filled me-1"></i>
                  <i class="fas fa-star filled me-1"></i>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-5 d-flex align-items-center">
          <div class="girl-slide-img aos" data-aos="fade-up">
            <img src="@/assets/img/object.png" alt="" />
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- /Home Banner -->
  <section class="section student-course">
    <div class="container">
      <div class="course-widget">
        <div class="row">
          <div class="col-lg-3 col-md-6">
            <div class="course-full-width">
              <div
                class="blur-border course-radius align-items-center aos"
                data-aos="fade-up"
              >
                <div class="online-course d-flex align-items-center">
                  <div class="course-img">
                    <img src="@/assets/img/pencil-icon.svg" alt="" />
                  </div>
                  <div class="course-inner-content">
                    <h4>
                      <span
                        ><vue3-autocounter
                          class="counter"
                          ref="counter"
                          :startAmount="1"
                          :delay="3"
                          :endAmount="10"
                          :duration="5"
                          :autoinit="true" /></span
                      >K
                    </h4>
                    <p>Online Courses</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 d-flex">
            <div class="course-full-width">
              <div class="blur-border course-radius aos" data-aos="fade-up">
                <div class="online-course d-flex align-items-center">
                  <div class="course-img">
                    <img src="@/assets/img/cources-icon.svg" alt="" />
                  </div>
                  <div class="course-inner-content">
                    <h4>
                      <span
                        ><vue3-autocounter
                          class="counter"
                          ref="counter"
                          :startAmount="10"
                          :delay="3"
                          :endAmount="200"
                          :duration="5"
                          :autoinit="true" /></span
                      >+
                    </h4>
                    <p>Expert Tutors</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 d-flex">
            <div class="course-full-width">
              <div class="blur-border course-radius aos" data-aos="fade-up">
                <div class="online-course d-flex align-items-center">
                  <div class="course-img">
                    <img src="@/assets/img/certificate-icon.svg" alt="" />
                  </div>
                  <div class="course-inner-content">
                    <h4>
                      <span
                        ><vue3-autocounter
                          class="counter"
                          ref="counter"
                          :startAmount="1"
                          :delay="3"
                          :endAmount="6"
                          :duration="5"
                          :autoinit="true" /></span
                      >K+
                    </h4>
                    <p>Ceritified Courses</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 d-flex">
            <div class="course-full-width">
              <div class="blur-border course-radius aos" data-aos="fade-up">
                <div class="online-course d-flex align-items-center">
                  <div class="course-img">
                    <img src="@/assets/img/gratuate-icon.svg" alt="" />
                  </div>
                  <div class="course-inner-content">
                    <h4>
                      <span
                        ><vue3-autocounter
                          class="counter"
                          ref="counter"
                          :startAmount="5"
                          :delay="3"
                          :endAmount="60"
                          :duration="5"
                          :autoinit="true" /></span
                      >K +
                    </h4>
                    <p>Online Students</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- Home Banner -->

  <!-- Top Categories -->
  <section class="section how-it-works">
    <div class="container">
      <div class="section-header aos" data-aos="fade-up">
        <div class="section-sub-head">
          <span>Favourite Course</span>
          <h2>Top Category</h2>
        </div>
        <div class="all-btn all-category d-flex align-items-center">
          <router-link to="job-category" class="btn btn-primary"
            >All Categories</router-link
          >
        </div>
      </div>
      <div class="section-text aos" data-aos="fade-up">
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Eget aenean accumsan
          bibendum gravida maecenas augue elementum et neque. Suspendisse imperdiet.
        </p>
      </div>
      <Carousel :settings="settings" :breakpoints="breakpoints">
        <Slide
          v-for="item in dashboard"
          :key="item.id"
          class="owl-carousel mentoring-course owl-theme"
        >
          <div class="carousel__item feature-box text-center">
            <div class="feature-bg">
              <div class="feature-header">
                <div class="feature-icon">
                  <img :src="require(`@/assets/img/${item.img}`)" alt="" />
                </div>
                <div class="feature-cont">
                  <div class="feature-text">{{ item.Development }}</div>
                </div>
              </div>
              <p>{{ item.Instructors }}</p>
            </div>
          </div>
        </Slide>
        <template #addons>
          <Pagination />
        </template>
      </Carousel>
    </div>
  </section>
  <!-- /Top Categories -->
</template>
<script>
import { Carousel, Pagination, Slide } from "vue3-carousel";
import dashboard from "@/assets/json/dashboard.json";
import "vue3-carousel/dist/carousel.css";
import AOS from "aos";
import "aos/dist/aos.css";
export default {
  components: {
    Carousel,
    Slide,
    Pagination,
  },
  data() {
    return {
      Category: ["Category", "Angular", "Node Js", "React", "Python"],
      dashboard: dashboard,
    };
  },
  setup() {
    return {
      // carousel settings
      settings: {
        itemsToShow: 1,
        snapAlign: "center",
      },

      breakpoints: {
        // 700px and up
        700: {
          itemsToShow: 3.5,
          snapAlign: "center",
        },
        // 1024 and up
        1024: {
          itemsToShow: 4,
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
