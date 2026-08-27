<template>
  <!-- Feature Instructors -->
  <div class="feature-instructors-sec">
    <div class="container">
      <div class="header-two-title text-center" data-aos="fade-up">
        <p class="tagline">New Courses</p>
        <h2>Featured Instructor</h2>
        <div class="header-two-text aos" data-aos="fade-up">
          <p class="mb-0">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Eget aenean accumsan
            bibendum gravida maecenas augue elementum et neque. Suspendisse imperdiet.
          </p>
        </div>
      </div>
      <!-- Featured Instructor -->
      <div class="featured-instructor-two">
        <div class="row">
          <div
            v-for="(instructor, index) in instructorstwo"
            :key="index"
            class="col-xl-3 col-lg-6 col-md-6 col-sm-12"
            data-aos="fade-up"
          >
            <div class="instructors-widget">
              <div class="instructors-img">
                <router-link to="instructor-list">
                  <img
                    class="img-fluid"
                    :src="require(`@/assets/img/instructor/${instructor.image}`)"
                    alt=""
                  />
                </router-link>
                <div class="featured-border">
                  <div class="featured-img">
                    <img
                      :src="require(`@/assets/img/category/${instructor.category}`)"
                      alt=""
                      class="img-fluid"
                    />
                  </div>
                </div>
              </div>
              <div class="course-details-two">
                <div class="instructors-content text-center">
                  <h5>
                    <router-link to="instructor-profile">{{ instructor.name }}</router-link>
                  </h5>
                  <p>{{ instructor.expertise }}</p>
                </div>
                <div class="course-info"></div>
                <div class="student-count d-flex justify-content-center">
                  <i class="fa-solid fa-user-group"></i>
                  <span>{{ instructor.studentCount }} Students</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Featured Instructor -->

      <!-- View all Category -->
      <div class="col-lg-12">
        <div class="more-details text-center" data-aos="fade-up">
          <router-link to="instructor-list" class="discover-btn discover-btn"
            >View all Instructors <i class="fas fa-arrow-right ms-2"></i
          ></router-link>
        </div>
      </div>
      <!-- /View all Category -->
    </div>
  </div>
  <!-- /Feature Instructors -->

  <!-- Leading Companies -->
  <section class="real-reviews-sec">
    <div class="container">
      <div class="header-two-title text-center" data-aos="fade-up">
        <p class="tagline">Check out these real reviews</p>
        <h2>Users-love-us Don't take it from us</h2>
        <div class="header-two-text text-center m-auto">
          <p class="mb-0">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Eget aenean accumsan
            bibendum gravida maecenas augue elementum et neque. Suspendisse imperdiet.
          </p>
        </div>
      </div>
      <div class="real-reviews-group">
        <div class="row align-items-center">
          <div class="col-lg-6 col-md-12 col-sm-12" data-aos="fade-up">
            <div class="reviews-img">
              <img src="@/assets/img/reviews-img-two.png" alt="" class="img-fluid" />
            </div>
          </div>
          <div class="col-lg-6 col-md-12 col-md-12" data-aos="fade-up">
            <div class="owl-carousel real-reviews owl-theme">
              <Carousel
                :wrap-around="true"
                :settings="settings"
                :breakpoints="breakpoints"
              >
                <Slide v-for="(review, index) in reviews" :key="index" class="item">
                  <div class="real-reviews-grid">
                    <div class="review-content">
                      <h3>{{ review.title }}</h3>
                      <p>{{ review.description }}</p>
                    </div>
                    <div class="review-top">
                      <div class="review-info">
                        <h3 data-aos="fade-up">{{ review.name }}</h3>
                        <h5 data-aos="fade-up">{{ review.role }}</h5>
                      </div>
                    </div>
                  </div>
                </Slide>
                <template #addons>
                  <Navigation />
                </template>
              </Carousel>
            </div>
            <div class="row">
              <div class="col-md-12 d-flex justify-content-between align-items-center">
                <div class="owl-nav slide-nav-8 nav-control"></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="client-two-carousel">
        <Carousel
          :autoplay="2000"
          :loop="true"
          :wrap-around="true"
          :settings="settingslead"
          :breakpoints="breakpointslead"
        >
          <Slide
            v-for="item in landingcompany"
            :key="item.id"
            class="lead-group-slider owl-carousel owl-theme"
          >
            <div class="carousel__item item">
              <div class="lead-img">
                <img
                  class="img-fluid"
                  alt=""
                  :src="require(`@/assets/img/${item.img}`)"
                />
              </div>
            </div>
          </Slide>
        </Carousel>
      </div>
    </div>
  </section>
  <!-- /Leading Companies -->

  <!-- Latest Blog -->
  <section class="latest-blog-sec">
    <div class="container">
      <div class="header-two-title text-center" data-aos="fade-up">
        <p class="tagline">News & Events</p>
        <h2>Our Latest Updates</h2>
        <div class="header-two-text text-center aos" data-aos="fade-up">
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Eget aenean accumsan
            bibendum gravida maecenas augue elementum et neque. Suspendisse imperdiet.
          </p>
        </div>
      </div>
      <div class="award-winning-two">
        <div class="row justify-content-center">
          <div
            v-for="(blog, index) in indextwoblogs"
            :key="index"
            class="col-xl-4 col-lg-6 col-md-6"
            data-aos="fade-down"
          >
            <div class="event-blog-main">
              <div class="latest-blog-img">
                <router-link to="blog-list">
                  <img
                    class="img-fluid"
                    alt=""
                    :src="require(`@/assets/img/blog/${blog.imageSrc}`)"
                  />
                </router-link>
              </div>
              <div class="latest-blog-content">
                <div class="event-content-title">
                  <div class="event-span">
                    <span class="span-name">{{ blog.category }}</span>
                  </div>
                  <h5>
                    <router-link to="blog-list">{{ blog.title }}</router-link>
                  </h5>
                  <div class="blog-student-count">
                    <i class="fa-solid fa-calendar-days me-1"></i>
                    <span>{{ blog.date }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- View all  Events -->
      <div class="col-lg-12">
        <div class="more-details text-center" data-aos="fade-down">
          <router-link to="blog-grid" class="discover-btn"
            >View all Events<i class="fas fa-arrow-right ms-2"></i
          ></router-link>
        </div>
      </div>
      <!-- /View all  Events -->
    </div>
  </section>
  <!-- /Latest Blog -->
</template>
<script>
import AOS from "aos";
import "aos/dist/aos.css";
import { Carousel, Pagination, Navigation, Slide } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
import instructorstwo from "@/assets/json/instructorstwo.json";
import landingcompany from "@/assets/json/landingcompany.json";
import indextwoblogs from "@/assets/json/indextwoblogs.json";
import reviews from "@/assets/json/reviews.json";
export default {
  data() {
    return {
      instructorstwo: instructorstwo,
      landingcompany: landingcompany,
      indextwoblogs: indextwoblogs,
      reviews: reviews,
      settings: {
        itemsToShow: 1,
        snapAlign: "center",
      },

      breakpoints: {
        575: {
          itemsToShow: 1,
          snapAlign: "center",
        },
        767: {
          itemsToShow: 1,
          snapAlign: "center",
        },
        991: {
          itemsToShow: 1,
          snapAlign: "center",
        },
        1024: {
          itemsToShow: 1,
          snapAlign: "start",
        },
      },
      settingslead: {
        itemsToShow: 1,
        snapAlign: "center",
      },

      breakpointslead: {
        // 700px and up
        700: {
          itemsToShow: 2,
          snapAlign: "center",
        },
        // 1024 and up
        1024: {
          itemsToShow: 5,
          snapAlign: "start",
        },
      },
    };
  },
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
  mounted() {
    this.$nextTick(() => {
      AOS.init();
    });
  },
};
</script>
