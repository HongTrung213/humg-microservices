<template>
  <!-- Become An Instructor -->
  <section class="home-three-become">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-8 col-md-8" data-aos="fade-up">
          <div class="become-content-three">
            <h2>Become An Instructor</h2>
            <p>
              Top instructors from around the world teach millions of students on
              DreamsLMS.
            </p>
          </div>
        </div>
        <div class="col-lg-4 col-md-4" data-aos="fade-up">
          <div class="become-button-three">
            <router-link to="register" class="btn btn-become"
              >Get Started Now</router-link
            >
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- /Become An Instructor -->

  <!-- Leading Companies -->
  <section class="lead-companies-three">
    <div class="container">
      <div class="home-three-head section-header-title aos-init aos-animate">
        <div class="row align-items-center d-flex justify-content-between">
          <div class="col-lg-12" data-aos="fade-up">
            <h2>500+ Leading Universities And Companies</h2>
          </div>
        </div>
      </div>
      <div class="m-0 p-0 lead-group aos" data-aos="fade-up">
        <Carousel
          :autoplay="2000"
          :loop="true"
          :wrap-around="true"
          :settings="settingsland"
          :breakpoints="breakpointsland"
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

  <!-- Testimonial -->
  <section class="testimonial-three">
    <div class="container">
      <div class="testimonial-pattern">
        <img class="pattern-left img-fluid" alt="" src="@/assets/img/bg/pattern-05.svg" />
        <img
          class="pattern-right img-fluid"
          alt=""
          src="@/assets/img/bg/pattern-06.svg"
        />
      </div>
      <div class="testimonial-three-content">
        <div class="row align-items-center">
          <div class="col-xl-6 col-lg-12 col-md-12" data-aos="fade-down">
            <div class="become-content">
              <h2 class="aos-init aos-animate">They Trusted us</h2>
              <h4 class="aos-init aos-animate">
                We are a very happy because we have a happy customer
              </h4>
            </div>

            <!-- View all Testimonail -->
            <router-link
              to="instructor-profile"
              class="btn btn-action aos-init aos-animate"
              data-aos="fade-up"
              >View all Testimonail</router-link
            >
            <!-- View all Testimonail -->
          </div>
          <div class="col-xl-6 col-lg-12 col-md-12" data-aos="fade-down">
            <div class="swiper-testimonial-three">
              <div class="swiper-wrapper">
                <div
                  class="swiper-slide"
                  v-for="(slide, index) in swiperthree"
                  :key="index"
                >
                  <div class="testimonial-item-five">
                    <div class="testimonial-quote">
                      <img
                        class="quote img-fluid"
                        alt=""
                        src="@/assets/img/bg/quote.svg"
                      />
                    </div>
                    <div class="testimonial-content">
                      <p>{{ slide.content }}</p>
                    </div>
                    <div class="testimonial-ratings">
                      <div class="rating">
                        <i
                          v-for="(star, starIndex) in slide.ratings"
                          :key="starIndex"
                          class="fas fa-star me-1"
                          :class="{ filled: starIndex < slide.filledStars }"
                        ></i>
                        <p class="d-inline-block">
                          {{ slide.rating }}<span>ratings</span>
                        </p>
                      </div>
                    </div>
                    <div class="testimonial-users">
                      <div class="imgbx">
                        <img
                          class="img-fluid"
                          alt=""
                          :src="require(`@/assets/img/profiles/${slide.avatar}`)"
                        />
                      </div>
                      <div class="d-block">
                        <h6>{{ slide.name }}</h6>
                        <p>{{ slide.profession }}</p>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="testimonial-bottom-nav">
                <div class="slide-next-btn testimonial-next-pre">
                  <i class="fas fa-arrow-left"></i>
                </div>
                <div class="slide-prev-btn testimonial-next-pre">
                  <i class="fas fa-arrow-right"></i>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!--/Testimonial -->

  <!-- Latest Blog -->
  <section class="latest-blog-three">
    <div class="container">
      <div class="home-three-head section-header-title" data-aos="fade-up">
        <div class="row align-items-center d-flex justify-content-between">
          <div class="col-lg-6 col-md-8">
            <h2>Latest news & Events</h2>
          </div>
          <div class="col-lg-6 col-md-4">
            <div class="see-all">
              <router-link to="blog-list"
                >See all<span class="see-all-icon"
                  ><i class="fas fa-arrow-right"></i></span
              ></router-link>
            </div>
          </div>
        </div>
      </div>
      <div class="latest-blog-main">
        <div class="row">
          <div class="col-xl-6 col-lg-12 col-md-12">
            <div class="row">
              <div
                class="col-md-12"
                data-aos="fade-down"
                v-for="blog in blogthree"
                :key="blog.id"
              >
                <div :class="'event-blog-three blog-three-' + blog.id">
                  <div class="blog-img-three">
                    <router-link to="blog-list">
                      <img
                        class="img-fluid"
                        :src="require(`@/assets/img/blog/${blog.image}`)"
                        alt=""
                      />
                    </router-link>
                  </div>
                  <div class="latest-blog-content">
                    <div class="event-three-title">
                      <div class="event-span-three">
                        <span class="span-name-three" :class="blog.class">{{
                          blog.category
                        }}</span>
                      </div>
                      <router-link to="blog-list">
                        <h5>{{ blog.title }}</h5>
                        <p>{{ blog.description }}</p>
                      </router-link>
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
          <div class="col-xl-6 col-lg-12 col-md-12">
            <div class="row">
              <div
                class="col-md-12"
                data-aos="fade-down"
                v-for="(blog, index) in blogsthree"
                :key="index"
              >
                <div :class="'event-blog-three blog-three-' + (index + 1)">
                  <div class="blog-img-three">
                    <router-link to="blog-list">
                      <img
                        class="img-fluid"
                        :src="require(`@/assets/img/blog/${blog.image}`)"
                        alt=""
                      />
                    </router-link>
                  </div>
                  <div class="latest-blog-content">
                    <div class="event-three-title">
                      <div class="event-span-three">
                        <span class="span-name-three" :class="blog.class">{{
                          blog.category
                        }}</span>
                      </div>
                      <router-link to="blog-list">
                        <h5>{{ blog.title }}</h5>
                        <p>{{ blog.description }}</p>
                      </router-link>
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
        </div>
      </div>
    </div>
  </section>
  <!-- /Latest Blog -->
</template>
<script>
import AOS from "aos";
import "aos/dist/aos.css";
import landingcompany from "@/assets/json/landingcompany.json";
import swiperthree from "@/assets/json/swiperthree.json";
import blogthree from "@/assets/json/blogthree.json";
import blogsthree from "@/assets/json/blogsthree.json";
import { Carousel, Pagination, Slide } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
import Swiper from "swiper";
import "swiper/css/swiper.min.css";
export default {
  components: {
    Carousel,
    Slide,
    Pagination,
  },
  data() {
    return {
      landingcompany: landingcompany,
      swiperthree: swiperthree,
      blogsthree: blogsthree,
      blogthree: blogthree,
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
          itemsToShow: 5,
          snapAlign: "start",
        },
      },
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
          itemsToShow: 4.2,
          snapAlign: "start",
        },
      },
    };
  },

  mounted() {
    const swiper = new Swiper(".swiper-testimonial-three", {
      effect: "coverflow",
      loop: false,
      grabCursor: true,
      center: true,
      centeredSlides: true,
      slidesPerView: "auto",
      initialSlide: 2,
      navigation: {
        prevEl: ".slide-prev-btn",
        nextEl: ".slide-next-btn",
        speed: 400,
        spaceBetween: 100,
      },
      coverflowEffect: {
        rotate: 0,
        stretch: 0,
        depth: 100,
        modifier: 10,
        slideShadows: true,
      },
      pagination: {
        el: ".swiper-pagination",
        clickable: true,
      },
    });

    this.$nextTick(() => {
      AOS.init();
    });
  },
};
</script>
