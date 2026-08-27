<template>
  <!-- Home Banner -->
  <section class="home-two-slide d-flex align-items-center">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-12" data-aos="fade-up">
          <div class="home-slide-face">
            <div class="home-slide-text">
              <h5>The Leader in Online Learning</h5>
              <h1>Engaging & Accessible Online Courses For All</h1>
            </div>
            <div class="banner-content">
              <form
                class="form"
                name="store"
                id="store"
                method="post"
                @submit.prevent="submitForm"
              >
                <div class="form-inner">
                  <div class="input-group">
                    <span class="drop-detail">
                      <vue-select :options="Category" placeholder="Select Category" />
                    </span>
                    <input
                      type="email"
                      class="form-control"
                      placeholder="Search School, Online eductional centers, etc"
                    />
                    <button class="btn btn-primary sub-btn" type="submit">Search</button>
                  </div>
                </div>
              </form>
            </div>
            <div class="trust-user-two">
              <p>Trusted by over 15K Users worldwide since 2023</p>
              <div class="rating-two">
                <span>4.4</span>
                <i class="fas fa-star filled ms-1 me-1"></i>
                <i class="fas fa-star filled me-1"></i>
                <i class="fas fa-star filled me-1"></i>
                <i class="fas fa-star filled me-1"></i>
                <i class="fas fa-star filled"></i>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Shapes -->
      <div class="shapes">
        <img class="shapes-one" src="@/assets/img/bg/home-right.png" alt="" />
        <img class="shapes-two" src="@/assets/img/bg/home-right-bottom.png" alt="" />
        <img class="shapes-middle" src="@/assets/img/bg/home-middle.png" alt="" />
        <img
          class="shapes-four wow animate__animated animate__slideInLeft"
          src="@/assets/img/bg/home-left.png"
          alt=""
        />
      </div>
      <!-- /Shapes -->
    </div>
  </section>
  <!-- /Home Banner -->

  <!-- About Section -->
  <section class="about-section">
    <div class="container">
      <div class="row">
        <div
          class="col-lg-6 wow fadeInLeft order-lg-1 order-xs-2 order-sm-2"
          data-aos="fade-up"
        >
          <div class="header-two-title">
            <p class="tagline">Learn with DreamLMS</p>
            <h2 class="mb-0">Get Trained By Experts & Professionals around the World</h2>
          </div>
          <div class="header-two-title">
            <p class="about-text">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quam dolor
              fermentum massa viverra congue proin. A volutpat eget ultrices velit nunc
              orci. Commodo quis integer a felis ac vel mauris a morbi. Scelerisque nunc
              accumsan elementum aenean nisl lacinia. Congue enim aliquet ac vitae turpis.
              Neque, bibendum imperdiet sed ullamcorper morbi amet. Facilisi odio amet,
              nunc quam ut nulla purus adipiscing pharetra.
            </p>
            <div class="about-button more-details">
              <router-link to="course-list" class="discover-btn"
                >Learn more <i class="fas fa-arrow-right ms-2"></i
              ></router-link>
            </div>
          </div>
        </div>

        <div class="col-lg-6 order-lg-2 order-xs-1 order-sm-1">
          <div class="stylist-gallery">
            <div class="row">
              <div class="col-lg-6 col-md-6 col-sm-12 col-12" data-aos="fade-down">
                <div
                  class="about-image count-one d-flex align-items-center justify-content-center flex-fill project-details"
                >
                  <div class="about-count">
                    <div class="course-img">
                      <img src="@/assets/img/icon/count-one.svg" alt="" />
                    </div>
                    <div class="count-content-three course-count ms-0">
                      <h4>
                        <span class="counterUp"
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
                      <p class="mb-0">Online Courses</p>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-lg-6 col-md-6 col-sm-12 col-12" data-aos="fade-down">
                <div
                  class="about-image count-two d-flex align-items-center justify-content-center flex-fill project-details"
                >
                  <div class="about-count">
                    <div class="course-img">
                      <img src="@/assets/img/icon/count-two.svg" alt="" />
                    </div>
                    <div class="count-content-three course-count ms-0">
                      <h4>
                        <span class="counterUp"
                          ><vue3-autocounter
                            class="counter"
                            ref="counter"
                            :startAmount="10"
                            :delay="3"
                            :endAmount="215"
                            :duration="5"
                            :autoinit="true" /></span
                        >+
                      </h4>
                      <p class="mb-0">Expert Tutors</p>
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-6 col-md-6 col-sm-12 col-12"
                data-aos="fade-right"
                data-wow-delay="1.5"
              >
                <div
                  class="about-image count-three d-flex align-items-center justify-content-center flex-fill project-details"
                >
                  <div class="about-count">
                    <div class="course-img">
                      <img src="@/assets/img/icon/count-three.svg" alt="" />
                    </div>
                    <div class="count-content-three course-count ms-0">
                      <h4>
                        <span class="counterUp"
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
                      <p class="mb-0">Ceritified Courses</p>
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="col-lg-6 col-md-6 col-sm-12 col-12"
                data-aos="fade-left"
                data-wow-delay="0.5"
              >
                <div
                  class="about-image count-four d-flex align-items-center justify-content-center flex-fill project-details"
                >
                  <div class="about-count">
                    <div class="course-img">
                      <img src="@/assets/img/icon/count-four.svg" alt="" />
                    </div>
                    <div class="count-content-three course-count ms-0">
                      <h4>
                        <span class="counterUp"
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
                      <p class="mb-0">Online Students</p>
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
  <!-- /About us -->

  <!-- Top Categories -->
  <section class="topcategory-sec">
    <div class="container">
      <div class="header-two-title text-center" data-aos="fade-up">
        <p class="tagline">Favourite Course</p>
        <h2>Top Category</h2>
        <div class="header-two-text">
          <p class="mb-0">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Eget aenean accumsan
            bibendum gravida maecenas augue elementum et neque. Suspendisse imperdiet.
          </p>
        </div>
      </div>
      <div class="top-category-group">
        <div class="row">
          <div
            v-for="category in catogoriestwo"
            :key="category.id"
            class="col-xl-3 col-lg-6 col-md-6 col-sm-12 d-flex"
            data-aos="fade-down"
          >
            <div class="categories-item flex-fill">
              <div class="categories-icon">
                <img
                  :src="require(`@/assets/img/category/${category.icon}`)"
                  :alt="category.name"
                />
              </div>
              <div class="categories-content">
                <h3>{{ category.name }}</h3>
                <p>{{ category.instructors }} Instructors</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- View all Category -->
      <div class="col-lg-12">
        <div class="more-details text-center" data-aos="fade-down">
          <router-link to="job-category" class="discover-btn"
            >View all Category <i class="fas fa-arrow-right ms-2"></i
          ></router-link>
        </div>
      </div>
      <!-- /View all Category -->
    </div>
  </section>
  <!-- /Top Categories -->
</template>
<script>
import AOS from "aos";
import "aos/dist/aos.css";
import catogoriestwo from "@/assets/json/catogoriestwo.json";
export default {
  data() {
    return {
      Category: ["Select Category", "Category One", "Category Two"],
      catogoriestwo: catogoriestwo,
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
