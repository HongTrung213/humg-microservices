<template>
  <!-- Trending Course -->
  <section class="section trend-course">
    <div class="container">
      <div class="section-header aos" data-aos="fade-up">
        <div class="section-sub-head">
          <span>What’s New</span>
          <h2>TRENDING COURSES</h2>
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
      <Carousel :settings="settings" :breakpoints="breakpoints">
        <Slide
          v-for="item in trendingcourse"
          :key="item.id"
          class="owl-carousel trending-course owl-theme"
        >
          <div class="course-box trend-box">
            <div class="product trend-product">
              <div class="product-img">
                <router-link to="course-details">
                  <img
                    class="img-fluid"
                    alt=""
                    :src="require(`@/assets/img/course/${item.img}`)"
                  />
                </router-link>
                <div class="price">
                  <h3>
                    {{ item.amt }} <span>{{ item.amt1 }}</span>
                  </h3>
                </div>
              </div>
              <div class="product-content">
                <div class="course-group d-flex">
                  <div class="course-group-img d-flex">
                    <router-link to="instructor-profile"
                      ><img
                        :src="require(`@/assets/img/user/${item.img1}`)"
                        alt=""
                        class="img-fluid"
                    /></router-link>
                    <div class="course-name">
                      <h4>
                        <router-link to="instructor-profile">{{ item.name }}</router-link>
                      </h4>
                      <p>{{ item.instructor }}</p>
                    </div>
                  </div>
                  <div
                    class="course-share d-flex align-items-center justify-content-center"
                  >
                    <a href="javascript:void(0);"><i class="fa-regular fa-heart"></i></a>
                  </div>
                </div>
                <h3 class="title">
                  <router-link to="course-details">{{ item.title }}</router-link>
                </h3>
                <div class="course-info d-flex align-items-center">
                  <div class="rating-img d-flex align-items-center">
                    <img
                      src="@/assets/img/icon/icon-01.svg"
                      alt=""
                      class="img-fluid"
                    />
                    <p>{{ item.lesson }}</p>
                  </div>
                  <div class="course-view d-flex align-items-center">
                    <img
                      src="@/assets/img/icon/icon-02.svg"
                      alt=""
                      class="img-fluid"
                    />
                    <p>{{ item.min }}</p>
                  </div>
                </div>
                <div class="rating d-flex align-items-center">
                  <i class="fas fa-star filled me-1"></i>
                  <i class="fas fa-star filled me-1"></i>
                  <i class="fas fa-star filled me-1"></i>
                  <i class="fas fa-star filled me-1"></i>
                  <i class="fas fa-star me-1"></i>
                  <span class="d-inline-block average-rating"><span>4.0</span> (15)</span>
                </div>
                <div class="all-btn all-category d-flex align-items-center">
                  <router-link to="checkout" class="btn btn-primary">BUY NOW</router-link>
                </div>
              </div>
            </div>
          </div>
        </Slide>
        <template #addons>
          <Pagination />
        </template>
      </Carousel>
      <featureinstructors></featureinstructors>
    </div>
  </section>
  <!-- /Trending Course -->

  <leadingcompanies></leadingcompanies>
</template>
<script>
import AOS from "aos";
import "aos/dist/aos.css";
import trendingcourse from "@/assets/json/trendingcourse.json";
import { Carousel, Pagination, Slide } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
export default {
  name: "Autoplay",
  components: {
    Carousel,
    Slide,
    Pagination,
  },
  data() {
    return {
      trendingcourse: trendingcourse,
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

  mounted() {
    this.$nextTick(() => {
      AOS.init();
    });
  },
};
</script>
