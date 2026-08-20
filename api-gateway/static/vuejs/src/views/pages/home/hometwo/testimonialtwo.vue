<template>
  <!-- Testimonial -->
  <section class="testimonial-sec">
    <div class="container">
      <div class="testimonial-two-img">
        <img src="@/assets/img/bg/map-user.png" alt="" class="img-fluid" />
      </div>
      <div class="testimonial-subhead-two">
        <div class="col-xl-8 col-lg-10 col-md-10 mx-auto" data-aos="fade-down">
          <div class="testimonial-inner">
            <div class="header-two-title testimonial-head-two text-center">
              <h2 data-aos="fade-down">Join over <span>5 Million</span> Students</h2>
              <div class="header-two-text text-center">
                <p>
                  Get certified, master modern tech skills, and level up your career —
                  whether you’re starting out or a seasoned pro. 95% of eLearning learners
                  report our hands-on content directly helped their careers.
                </p>
              </div>
            </div>
            <div class="row text-center">
              <div class="col-md-4 col-sm-12" data-aos="fade-up">
                <div class="course-count-two course-count">
                  <h4>
                    <span class="counterUp text-orange"
                      ><vue3-autocounter
                        class="counter"
                        ref="counter"
                        :startAmount="20085"
                        :delay="3"
                        :endAmount="253085"
                        :duration="5"
                        :autoinit="true"
                    /></span>
                  </h4>
                  <h5>Students Enrolled</h5>
                </div>
              </div>
              <div class="col-md-4 col-sm-12" data-aos="fade-up">
                <div class="course-count-two course-count">
                  <h4>
                    <span class="counterUp text-green"
                      ><vue3-autocounter
                        class="counter"
                        ref="counter"
                        :startAmount="105"
                        :delay="3"
                        :endAmount="1205"
                        :duration="5"
                        :autoinit="true"
                    /></span>
                  </h4>
                  <h5>Total Courses</h5>
                </div>
              </div>
              <div class="col-md-4 col-sm-12" data-aos="fade-up">
                <div class="course-count-two course-count">
                  <h4>
                    <span class="counterUp text-blue"
                      ><vue3-autocounter
                        class="counter"
                        ref="counter"
                        :startAmount="20005"
                        :delay="3"
                        :endAmount="253085"
                        :duration="5"
                        :autoinit="true"
                    /></span>
                  </h4>
                  <h5>Students Worldwide</h5>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- /Testimonial -->

  <!-- Trending Course -->
  <section class="trending-course-sec">
    <div class="container">
      <div class="header-two-title text-center" data-aos="fade-up">
        <p class="tagline">New Courses</p>
        <h2>Trending Courses</h2>
        <div class="header-two-text m-auto text-center d-block">
          <p class="mb-0">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Eget aenean accumsan
            bibendum gravida maecenas augue elementum et neque. Suspendisse imperdiet.
          </p>
        </div>
      </div>

      <!-- Trending Course Group -->
      <div class="trending-course-main">
        <div class="row">
          <div
            v-for="course in trendingcourese"
            :key="course.id"
            class="col-xl-6 col-lg-12 col-md-12"
            data-aos="fade-down"
          >
            <div class="trending-courses-group">
              <div class="trending-courses-two">
                <div class="product-img course-column-img">
                  <router-link to="instructor-profile">
                    <img
                      class="img-fluid"
                      :src="require(`@/assets/img/skills/${course.imageSrc}`)"
                      alt=""
                    />
                  </router-link>
                  <div class="trending-price">
                    <h4>
                      <span>{{ course.skill }}</span>
                    </h4>
                  </div>
                </div>
                <div class="course-content-column">
                  <div class="trending-two-rating align-items-center">
                    <i
                      v-for="star in course.ratingStars"
                      :key="star"
                      class="fas fa-star filled me-1"
                    ></i>
                    <span class="ms-2">{{ course.reviewCount }} reviews</span>
                  </div>

                  <div class="name-text featured-info-two">
                    <h3 class="title instructor-text">
                      <router-link to="course-details">{{ course.title }}</router-link>
                    </h3>
                    <div class="time-hours-two">
                      <span><i class="fa-regular fa-clock me-2"></i></span>
                      <p>{{ course.duration }}</p>
                    </div>
                  </div>

                  <div class="d-flex align-items-center">
                    <div class="rating-price-two d-flex align-items-center">
                      <p>{{ course.instructor }}</p>
                    </div>
                    <div class="course-view d-inline-flex align-items-center">
                      <div class="course-price-two">
                        <h3>{{ course.price }}</h3>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Trending Course Group -->

      <!-- View all  Courses -->
      <div class="col-lg-12" data-aos="fade-up">
        <div class="more-details text-center">
          <router-link to="course-details" class="discover-btn"
            >View all Courses <i class="fas fa-arrow-right ms-2"></i
          ></router-link>
        </div>
      </div>
      <!-- /View all  Courses -->
    </div>
  </section>
  <!-- /Feature Course -->

  <!-- Share your knowledge -->
  <div class="knowledge-sec">
    <div class="container-fluid">
      <div class="row align-items-center">
        <div class="col-lg-6 col-sm-12 ps-0">
          <div class="featured-img-1"></div>
        </div>
        <div class="col-lg-6 col-sm-12" data-aos="fade-up">
          <div class="joing-group">
            <div class="section-title">
              <h2>Want to share your knowledge? Join us a Mentor</h2>
              <div class="joing-section-text">
                <p class="mb-0">
                  High-definition video is video of higher resolution and quality than
                  standard-definition. While there is no standardized meaning for
                  high-definition, generally any video.
                </p>
              </div>
            </div>
            <div class="joing-list">
              <ul>
                <li
                  v-for="item in testimonialtwo"
                  :key="item.id"
                  data-aos="fade-bottom"
                  :class="{ 'mb-0': item.lastItem }"
                >
                  <div class="joing-header">
                    <span :class="item.iconClass">
                      <img
                        :src="require(`@/assets/img/icon/${item.iconSrc}`)"
                        alt=""
                        class="img-fluid"
                      />
                    </span>
                    <div class="joing-content">
                      <h5 class="joing-title">{{ item.title }}</h5>
                      <div class="joing-para">
                        <p>{{ item.description1 }}</p>
                        <p>{{ item.description2 }}</p>
                      </div>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Share your knowledge -->
</template>
<script>
import AOS from "aos";
import "aos/dist/aos.css";
import trendingcourese from "@/assets/json/trendingcourese.json";
import testimonialtwo from "@/assets/json/testimonialtwo.json";
export default {
  data() {
    return {
      testimonialtwo: testimonialtwo,
      trendingcourese: trendingcourese,
    };
  },

  mounted() {
    this.$nextTick(() => {
      AOS.init();
    });
  },
};
</script>
