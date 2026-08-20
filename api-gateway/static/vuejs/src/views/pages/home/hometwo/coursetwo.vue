<template>
  <!-- Feature Course -->
  <section class="featured-courses-sec">
    <div class="patter-one-main">
      <img class="patter-one" src="@/assets/img/bg/patter-one.png" alt="" />
    </div>
    <div class="container">
      <div class="header-two-title text-center" data-aos="fade-up">
        <p class="tagline">What’s New</p>
        <h2>Featured Courses</h2>
        <div class="header-two-text m-auto text-center d-block">
          <p class="mb-0">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Eget aenean accumsan
            bibendum gravida maecenas augue elementum et neque. Suspendisse imperdiet.
          </p>
        </div>
      </div>
      <div class="featured-courses-two">
        <div class="row">
          <!-- Featured Courses -->
          <div
            v-for="course in coursetwo"
            :key="course.id"
            class="col-xl-4 col-lg-6 col-md-6 col-sm-12 d-flex"
            data-aos="fade-down"
          >
            <div class="featured-details-two">
              <div class="product-item-two">
                <div class="product-img-two">
                  <router-link to="course-details">
                    <img
                      class="img-fluid"
                      :src="require(`@/assets/img/course/${course.imageSrc}`)"
                      :alt="course.title"
                    />
                  </router-link>
                  <div class="price-text">
                    <h4>
                      <span>{{ course.category }}</span>
                    </h4>
                  </div>
                </div>
                <div class="course-details-content">
                  <div class="image-info">
                    <img
                      class="img-fluid"
                      :src="require(`@/assets/img/profiles/${course.instructor.avatar}`)"
                      :alt="course.instructor.name"
                    />
                  </div>
                  <div class="rating">
                    <i
                      v-for="n in course.rating"
                      :key="n"
                      class="fas fa-star filled me-1"
                    ></i>
                    <span class="ms-3">{{ course.reviews }} reviews</span>
                  </div>
                  <div class="name-text featured-info-two">
                    <h3 class="title instructor-text">
                      <router-link to="course-details">{{ course.title }}</router-link>
                    </h3>
                    <p class="me-3">
                      By<span class="text-danger ms-2">{{ course.instructor.name }}</span>
                    </p>
                  </div>
                  <div class="featured-info-time d-flex align-items-center">
                    <div class="hours-time-two d-flex align-items-center">
                      <span><i class="fa-regular fa-clock me-2"></i></span>
                      <p>{{ course.duration }}</p>
                    </div>
                    <div class="course-view d-inline-flex align-items-center">
                      <div class="course-price">
                        <h3>
                          {{ course.originalPrice }}
                          <span>{{ course.discountedPrice }}</span>
                        </h3>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
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

  <!-- Growup Your Skill Section -->
  <section class="growup-section">
    <div class="home-two-shapes">
      <img src="@/assets/img/bg/home-right-bottom.png" alt="" />
    </div>
    <div class="container">
      <div class="row align-items-center">
        <div class="col-xl-6 col-lg-6 col-md-5 col-12" data-aos="fade-right">
          <div class="growup-images-two">
            <div class="growup-skills-img">
              <img
                class=""
                src="@/assets/img/skil-01.png"
                alt="image-banner"
                title="image-banner"
              />
            </div>
          </div>
        </div>

        <div
          class="col-xl-6 col-lg-6 col-md-7 col-12 wow fadeInLeft"
          data-aos="fade-left"
        >
          <div class="header-two-title">
            <p class="tagline">Growup Your Skill</p>
            <h2 class="text-navy">Learn Anything you want today</h2>
            <div class="header-two-text">
              <p class="mb-0">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quam dolor
                fermentum massa viverra congue proin. A volutpat eget ultrices velit nunc
                orci. Commodo quis integer a felis ac vel mauris a morbi. Scelerisque nunc
                accumsan elementum aenean nisl lacinia. Congue enim aliquet ac vitae
                turpis. Neque, bibendum imperdiet sed ullamcorper morbi amet. Facilisi
                odio amet, nunc quam ut nulla purus adipiscing pharetra.
              </p>
            </div>
          </div>
          <div class="about-button more-details">
            <router-link to="register" class="discover-btn"
              >Join Today <i class="fas fa-arrow-right ms-2"></i
            ></router-link>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- /Growup Your Skill -->

  <!-- Master Skills -->
  <section class="master-skills-sec">
    <div class="container">
      <div class="header-two-title text-center" data-aos="fade-up">
        <p class="tagline">What’s New</p>
        <h2>Master the skills to drive your career</h2>
        <div class="header-two-text" data-aos="fade-up">
          <p class="mb-0">
            Get certified, master modern tech skills, and level up your career — whether
            you’re starting out or a seasoned pro. 95% of eLearning learners report our
            hands-on content directly helped their careers.
          </p>
        </div>
      </div>
      <!-- Course Info-->
      <div class="course-info-two">
        <div class="row align-items-center">
          <!-- Master skills Content -->
          <div
            class="col-lg-6 col-md-12 order-lg-0 order-md-0 order-0"
            data-aos="fade-up"
          >
            <div class="join-title-one">
              <h2>Award Winning Course Management</h2>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quam dolor
                fermentum massa viverra congue proin. A volutpat eget ultrices velit nunc
                orci. Commodo quis integer a felis ac vel mauris a morbi. Scelerisque nunc
                accumsan elementum aenean nisl lacinia. Congue enim aliquet ac vitae
                turpis. Neque, bibendum imperdiet sed ullamcorper morbi amet. Facilisi
                odio amet, nunc quam ut nulla purus adipiscing pharetra.
              </p>
            </div>
          </div>
          <!-- /Master skills Content -->

          <!-- Master skills Image -->
          <div
            class="col-lg-6 col-md-12 order-lg-1 order-md-1 order-1"
            data-aos="fade-up"
          >
            <div class="join-mentor-img">
              <div class="winning-two-one">
                <img src="@/assets/img/skills/skills-01.jpg" alt="" class="img-fluid" />
              </div>
              <div class="joing-icon-award">
                <img
                  src="@/assets/img/bg/skill-icon-01.png"
                  alt=""
                  class="joing-icon-one img-fluid"
                />
              </div>
            </div>
          </div>
          <!-- /Master skills Image -->

          <!-- Master skills Content -->
          <div
            class="col-xl-6 col-lg-7 col-md-12 order-lg-2 order-md-3 order-3"
            data-aos="fade-up"
          >
            <div class="join-mentor-img">
              <div class="winning-two-two">
                <img src="@/assets/img/skills/skills-02.jpg" alt="" class="img-fluid" />
              </div>
            </div>
            <div class="joing-icon-award">
              <img
                src="@/assets/img/bg/skill-icon-02.png"
                alt=""
                class="joing-icon-two img-fluid"
              />
            </div>
          </div>
          <!-- /Master skills Content -->

          <!-- Master skills Image -->
          <div
            class="col-xl-6 col-lg-5 col-md-12 order-lg-3 order-md-2 order-2"
            data-aos="fade-up"
          >
            <div class="join-title-middle">
              <h2>Award Winning Course Management</h2>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quam dolor
                fermentum massa viverra congue proin. A volutpat eget ultrices velit nunc
                orci. Commodo quis integer a felis ac vel mauris a morbi. Scelerisque nunc
                accumsan elementum aenean nisl lacinia. Congue enim aliquet ac vitae
                turpis. Neque, bibendum imperdiet sed ullamcorper morbi amet. Facilisi
                odio amet, nunc quam ut nulla purus adipiscing pharetra.
              </p>
            </div>
          </div>
          <!-- /Master skills Image -->

          <!-- Master skills Content -->
          <div
            class="col-xl-6 col-lg-7 col-md-12 order-lg-4 order-md-4 order-4"
            data-aos="fade-up"
          >
            <div class="join-title-one">
              <h2>Certification for solid development of your Carrer</h2>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quam dolor
                fermentum massa viverra congue proin. A volutpat eget ultrices velit nunc
                orci. Commodo quis integer a felis ac vel mauris a morbi. Scelerisque nunc
                accumsan elementum aenean nisl lacinia. Congue enim aliquet ac vitae
                turpis. Neque, bibendum imperdiet sed ullamcorper morbi amet. Facilisi
                odio amet, nunc quam ut nulla purus adipiscing pharetra.
              </p>
            </div>
          </div>
          <!-- /Master skills Content -->

          <!-- Master skills Image -->
          <div
            class="col-xl-6 col-lg-5 col-md-12 order-lg-5 order-md-5 order-5"
            data-aos="fade-up"
          >
            <div class="join-mentor-img mb-0">
              <div class="winning-two-three">
                <img src="@/assets/img/skills/skills-03.jpg" alt="" class="img-fluid" />
              </div>
            </div>
            <div class="joing-icon-award">
              <img
                src="@/assets/img/bg/skill-icon-03.png"
                alt=""
                class="joing-icon-three img-fluid"
              />
            </div>
          </div>
          <!-- /Master skills Image -->
        </div>
      </div>
      <!-- /Course Info -->
    </div>
  </section>
  <!-- /Master Skills -->
</template>
<script>
import AOS from "aos";
import "aos/dist/aos.css";
import coursetwo from "@/assets/json/coursetwo.json";
export default {
  data() {
    return {
      coursetwo: coursetwo,
    };
  },

  mounted() {
    this.$nextTick(() => {
      AOS.init();
    });
  },
};
</script>
