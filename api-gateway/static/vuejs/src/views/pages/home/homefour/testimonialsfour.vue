<template>
  <!-- Testimonials -->
  <section class="testimonial-section-five">
    <div class="container">
      <div class="header-five-title text-center" data-aos="fade-down">
        <h2 class="text-warning">Testimonials</h2>
        <p class="text-white">We are a very happy because we have a happy customer</p>
      </div>
      <div class="testimonial-slider-five">
        <div class="testimonial-five lazy slider">
          <Carousel :wrap-around="true" :settings="settings" :breakpoints="breakpoints">
            <Slide
              class="testimonial-carousel"
              v-for="(testimonial, index) in testimonialfour"
              :key="index"
            >
              <div class="testimonial-item">
                <div class="testimonial-content-five">
                  <div class="testimonial-text">
                    <p>{{ testimonial.text }}</p>
                  </div>
                  <div
                    class="testimonial-users-group d-flex align-items-center justify-content-between"
                  >
                    <div class="testimonial-users text-start">
                      <h5>{{ testimonial.name }}</h5>
                      <p>{{ testimonial.role }}</p>
                    </div>
                    <div
                      class="testimonial-ratings-five d-inline-flex align-items-center"
                    >
                      <div class="rating">
                        <i
                          v-for="n in testimonial.rating"
                          :key="n"
                          class="fas fa-star filled me-1"
                        ></i>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="testimonial-image">
                  <img
                    :src="require(`@/assets/img/testimonial/${testimonial.image}`)"
                    alt=""
                  />
                </div>
              </div>
            </Slide>
            <template #addons>
              <Navigation />
            </template>
          </Carousel>
        </div>
      </div>
    </div>
  </section>
  <!-- /Testimonials -->

  <!-- Unlimited access -->
  <section class="leading-section-five">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-4 col-sm-6" data-aos="fade-down">
          <div class="leading-five-content">
            <h2>Unlimited access</h2>
            <p>to 360+ courses and 1,600+ hands-on labs</p>
          </div>
        </div>
        <div class="col-lg-8 col-sm-6" data-aos="fade-down">
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
  <!-- /Unlimited access -->

  <!-- Latest Blogs -->
  <section class="blogs-section-five">
    <div class="container">
      <div class="header-five-title text-center" data-aos="fade-down">
        <h2>Latest Blogs</h2>
        <p>Follow the latest and most useful articles on that student's blog</p>
      </div>
      <div class="owl-carousel home-five-blog owl-theme">
        <Carousel :settings="settingsblog" :breakpoints="breakpointsblog">
          <Slide class="blog-five-item" v-for="(item, index) in blogfour" :key="index">
            <div class="product-img-five">
              <router-link to="blog-details">
                <img
                  class="img-fluid"
                  :src="require(`@/assets/img/blog/${item.image}`)"
                  alt=""
                />
              </router-link>
            </div>
            <div class="blog-box-content">
              <div
                class="blog-five-header d-flex align-items-center justify-content-between"
              >
                <div class="blog-five-text">
                  <p>{{ item.category }}</p>
                </div>
                <div class="blog-five-year">
                  <span class="me-2"><i class="fa-solid fa-calendar-days"></i></span>
                  <span>{{ item.date }}</span>
                </div>
              </div>
              <div class="blog-five-footer text-start">
                <h3>
                  <router-link to="blog-details">{{ item.title }}</router-link>
                </h3>
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
  <!-- Latest Blogs -->
</template>
<script>
import AOS from "aos";
import "aos/dist/aos.css";
import leading from "@/assets/json/leading.json";
import testimonialfour from "@/assets/json/testimonialfour.json";
import blogfour from "@/assets/json/blogfour.json";
import { Carousel, Pagination, Navigation, Slide } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
export default {
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
  data() {
    return {
      leading: leading,
      testimonialfour: testimonialfour,
      blogfour: blogfour,
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
          itemsToShow: 1,
          snapAlign: "center",
        },
        // 1024 and up
        1024: {
          itemsToShow: 0.9,
          snapAlign: "start",
        },
      },
      settingsblog: {
        itemsToShow: 1,
        snapAlign: "center",
      },
      breakpointsblog: {
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
          itemsToShow: 3.1,
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
