<template>
  <!-- Counter Five-->
  <section class="counter-section-five">
    <div class="container">
      <div class="row align-items-center text-center justify-content-between">
        <!-- col -->
        <div class="col-lg-3 col-md-3 col-sm-12" data-aos="fade-down">
          <div class="count-five">
            <div class="count-content-five course-count ms-0">
              <h4>
                <span class="counterUp"
                  ><vue3-autocounter
                    class="counter"
                    ref="counter"
                    :startAmount="10"
                    :delay="3"
                    :endAmount="145"
                    :duration="5"
                    :autoinit="true"
                /></span>
              </h4>
              <p class="mb-0">Expert Tutors</p>
            </div>
          </div>
        </div>
        <!--/ col -->

        <!-- col -->
        <div class="col-lg-3 col-md-3 col-sm-12" data-aos="fade-down">
          <div class="count-five">
            <div class="count-content-five course-count ms-0">
              <h4>
                <span class="counterUp"
                  ><vue3-autocounter
                    class="counter"
                    ref="counter"
                    :startAmount="100"
                    :delay="3"
                    :endAmount="23495"
                    :duration="5"
                    :autoinit="true"
                /></span>
              </h4>
              <p class="mb-0">Cetified Courses</p>
            </div>
          </div>
        </div>
        <!--/ col -->

        <!-- col -->
        <div class="col-lg-3 col-md-3 col-sm-12" data-aos="fade-down">
          <div class="count-five">
            <div class="count-content-five course-count ms-0">
              <h4>
                <span class="counterUp"
                  ><vue3-autocounter
                    class="counter"
                    ref="counter"
                    :startAmount="1"
                    :delay="3"
                    :endAmount="20"
                    :duration="5"
                    :autoinit="true" /></span
                >+
              </h4>
              <p class="mb-0">Online students</p>
            </div>
          </div>
        </div>
        <!--/ col -->

        <!-- col -->
        <div class="col-lg-3 col-md-3 col-sm-12" data-aos="fade-down">
          <div class="count-five count-five-last count-five-0">
            <div class="count-content-five course-count ms-0">
              <h4>
                <span class="counterUp"
                  ><vue3-autocounter
                    class="counter"
                    ref="counter"
                    :startAmount="500"
                    :delay="3"
                    :endAmount="58370"
                    :duration="5"
                    :autoinit="true"
                /></span>
              </h4>
              <p class="mb-0">Online Courses</p>
            </div>
          </div>
        </div>
        <!--/ col -->
      </div>
    </div>
  </section>
  <!-- /Counter Five-->

  <!-- Featured Courses Five-->
  <section class="featured-section-five">
    <div class="container">
      <div class="header-five-title text-center" data-aos="fade-down">
        <h2>Featured Courses</h2>
        <p>Pick Your Favourite Course</p>
      </div>
      <div class="row">
        <div class="featured-courses-five-tab">
          <div class="tab-content">
            <div class="nav tablist-five" role="tablist">
              <a
                class="nav-tab active"
                data-bs-toggle="tab"
                href="#ux-design-tab"
                role="tab"
                >UI/UX Design</a
              >

              <a class="nav-tab" data-bs-toggle="tab" href="#development-tab" role="tab"
                >Development</a
              >

              <a class="nav-tab" data-bs-toggle="tab" href="#marketing-tab" role="tab"
                >Marketing</a
              >

              <a class="nav-tab" data-bs-toggle="tab" href="#business-tab" role="tab"
                >Business</a
              >

              <a class="nav-tab" data-bs-toggle="tab" href="#technology-tab" role="tab"
                >Technology</a
              >

              <a class="nav-tab" data-bs-toggle="tab" href="#all-category-tab" role="tab"
                >All Category</a
              >
            </div>

            <tabcontantfour></tabcontantfour>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- /Featured Courses Five-->

  <!-- Master the skills Five -->
  <section class="master-section-five">
    <div class="container">
      <div class="master-five-vector">
        <img class="ellipse-right" src="@/assets/img/bg/master-vector-left.svg" alt="" />
      </div>
      <div class="row">
        <div class="col-lg-6 col-sm-12" data-aos="fade-down">
          <div class="section-five-sub">
            <div class="header-five-title">
              <h2>Master the skills to drive your career</h2>
              <p>Pick Your Favourite Course</p>
            </div>
            <div class="career-five-content">
              <p data-aos="fade-down">
                Get certified, master modern tech skills, and level up your career —
                whether you’re starting out or a seasoned pro. 95% .
              </p>
              <p class="mb-0" data-aos="fade-down">
                Get certified, master modern tech skills, and level up your career —
                whether you’re starting out or a seasoned pro. 95% of eLearning learners
                report our hands-on content directly helped their careers.
              </p>
            </div>
            <router-link to="course-list" class="learn-more-five">Learn More</router-link>
          </div>
        </div>
        <div class="col-lg-6 col-sm-12">
          <div class="row">
            <div
              v-for="(item, index) in skillfour"
              :key="index"
              class="col-lg-6 col-sm-6"
              data-aos="fade-down"
            >
              <div class="skill-five-item">
                <div class="skill-five-icon">
                  <img
                    :src="require(`@/assets/img/skills/${item.iconSrc}`)"
                    :class="item.iconClass"
                    :alt="item.altText"
                  />
                </div>
                <div class="skill-five-content">
                  <h3>{{ item.title }}</h3>
                  <p>{{ item.description }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- /Master the skills Five -->
</template>
<script>
import AOS from "aos";
import "aos/dist/aos.css";
import skillfour from "@/assets/json/skillfour.json";
export default {
  data() {
    return {
      skillfour: skillfour,
    };
  },

  mounted() {
    this.$nextTick(() => {
      AOS.init();
    });
  },
};
</script>
