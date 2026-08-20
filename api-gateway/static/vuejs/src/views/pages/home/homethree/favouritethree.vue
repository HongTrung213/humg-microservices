<template>
  <!-- Favourite Course -->
  <section class="home-three-favourite">
    <div class="container">
      <div class="row">
        <div class="container">
          <div class="home-three-head section-header-title">
            <div class="row align-items-center d-flex justify-content-between">
              <div class="col-lg-8 col-sm-12">
                <h2>Choose favourite Course from top Category</h2>
              </div>
              <div class="col-lg-4 col-sm-12">
                <div class="see-all">
                  <router-link to="course-details"
                    >See all<span class="see-all-icon"
                      ><i class="fas fa-arrow-right"></i></span
                  ></router-link>
                </div>
              </div>
            </div>
          </div>

          <Carousel
            class="home-three-favourite-carousel"
            :settings="settings"
            :breakpoints="breakpoints"
          >
            <Slide v-for="course in coursethree" :key="course.name" class="favourite-box">
              <div class="carousel__item favourite-item flex-fill text-start">
                <div class="categories-icon">
                  <img
                    class="img-fluid"
                    :src="require(`@/assets/img/category/${course.icon}`)"
                    :alt="course.name"
                  />
                </div>
                <div class="categories-content course-info">
                  <h3>{{ course.name }}</h3>
                </div>
                <div class="course-instructors">
                  <div class="instructors-info">
                    <p class="me-4">Instructors</p>
                    <ul class="instructors-list">
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
                      <li class="more-set">
                        <a href="javascript:;">80+</a>
                      </li>
                    </ul>
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
      <!-- /Favourite Course -->
    </div>
  </section>
  <!-- Feature Course -->

  <!-- Courses -->
  <section class="home-three-courses">
    <div class="container">
      <div class="favourite-course-sec">
        <div class="row">
          <div class="home-three-head section-header-title" data-aos="fade-up">
            <div class="row align-items-center d-flex justify-content-between">
              <div class="col-lg-6 col-sm-8">
                <h2>Courses</h2>
              </div>
              <div class="col-lg-6 col-sm-4">
                <div class="see-all">
                  <a href="javascript:void(0);"
                    >See all<span class="see-all-icon"
                      ><i class="fas fa-arrow-right"></i></span
                  ></a>
                </div>
              </div>
            </div>
          </div>

          <div class="all-corses-main">
            <div class="tab-content">
              <div class="nav tablist-three" role="tablist">
                <a
                  class="nav-tab active me-3"
                  data-bs-toggle="tab"
                  href="#alltab"
                  role="tab"
                  >All</a
                >

                <a
                  class="nav-tab me-3"
                  data-bs-toggle="tab"
                  href="#mostpopulartab"
                  role="tab"
                  >Most popular</a
                >

                <a
                  class="nav-tab me-3"
                  data-bs-toggle="tab"
                  href="#businesstab"
                  role="tab"
                  >Business</a
                >

                <a class="nav-tab me-3" data-bs-toggle="tab" href="#designtab" role="tab"
                  >Design</a
                >

                <a class="nav-tab me-3" data-bs-toggle="tab" href="#designtab" role="tab"
                  >Music</a
                >

                <a
                  class="nav-tab me-3"
                  data-bs-toggle="tab"
                  href="#programmingtab"
                  role="tab"
                  >Programming</a
                >

                <a
                  class="nav-tab me-3"
                  data-bs-toggle="tab"
                  href="#databasetab"
                  role="tab"
                  >Database</a
                >
              </div>
              <coursestabcontent></coursestabcontent>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- /Courses -->

  <!-- Call to Action -->
  <section class="home-three-transform">
    <div class="container" data-aos="fade-up">
      <div class="row align-items-center">
        <div class="col-lg-9 col-md-8 col-sm-12">
          <div class="cta-content">
            <h2>Transform Access To Education</h2>
            <p>
              Create an account to receive our newsletter, course recommendations and
              promotions.
            </p>
          </div>
        </div>
        <div class="col-lg-3 col-md-4 col-sm-12">
          <div class="transform-button-three">
            <router-link to="register" class="btn btn-action"
              >Get Started Now</router-link
            >
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- Call to Action -->
</template>
<script>
import AOS from "aos";
import "aos/dist/aos.css";
import skillsthree from "@/assets/json/skillsthree.json";
import coursethree from "@/assets/json/coursethree.json";
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
      skillsthree: skillsthree,
      coursethree: coursethree,
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
          itemsToShow: 5.4,
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
