<template>
  <!-- Experienced Course Five -->
  <section class="experienced-course-five">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6" data-aos="fade-down">
          <div class="experienced-five-group">
            <div class="instructor-vector-left">
              <img src="@/assets/img/bg/instructor-vector-left.svg" alt="" />
            </div>
            <div class="developer-five-list">
              <ul>
                <li class="column-img" v-for="(profile, index) in profile" :key="index">
                  <div class="developer-profile-five">
                    <div class="developer-image">
                      <img
                        :src="require(`@/assets/img/profiles/${profile.imageSrc}`)"
                        :alt="profile.altText"
                      />
                    </div>
                    <div class="profile-five-ovelay">
                      <h5>{{ profile.name }}</h5>
                      <p>{{ profile.expertise }}</p>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
            <div class="instructor-vector-right">
              <img src="@/assets/img/bg/instructor-vector-right.svg" alt="" />
            </div>
          </div>
        </div>
        <div class="col-lg-6" data-aos="fade-down">
          <div class="experienced-five-sub">
            <div class="header-five-title header-five-title-inner">
              <h2 class="ex-five-title">Experienced Course Instructor</h2>
            </div>
            <div class="career-five-content">
              <p class="ex-five-content">
                Get certified, master modern tech skills, and level up your career —
                whether you’re starting out or a seasoned pro. 95% . Get certified, master
                modern tech skills, and level up your career — whether you’re starting out
                or a seasoned pro. 95% of eLearning learners report our hands-on content
                directly helped their careers.
              </p>
            </div>
            <router-link to="instructor-list" class="learn-more-five"
              >Start Learning</router-link
            >
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- Experienced Course Five -->

  <!-- Share your knowledge -->
  <section class="share-knowledge-five">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6 col-md-6 col-sm-12" data-aos="fade-down">
          <div class="section-five-sub">
            <div class="header-five-title">
              <h2>Want to share your knowledge? Join us a Mentor</h2>
            </div>
            <div class="career-five-content">
              <p>
                High-definition video is video of higher resolution and quality than
                standard-definition. While there is no standardized meaning for
                high-definition, generally any video.While there is no standardized
                meaning for high-definition, generally any video.
              </p>
            </div>
            <div class="knowledge-list-five">
              <ul>
                <li>
                  <div class="knowledge-list-group">
                    <img src="@/assets/img/icon/award-new.svg" alt="" />
                    <p>Best Courses</p>
                  </div>
                </li>
                <li class="mb-0">
                  <div class="knowledge-list-group">
                    <img src="@/assets/img/icon/award-new.svg" alt="" />
                    <p>Best Courses</p>
                  </div>
                </li>
              </ul>
            </div>
            <!-- Start Teaching Today -->
            <router-link to="course-list" class="learn-more-five"
              >Start Teaching Today</router-link
            >
            <!-- /Start Teaching Today -->
          </div>
        </div>
        <div class="col-lg-6 col-md-6 col-sm-12" data-aos="fade-down">
          <div class="joing-count-five text-center">
            <img src="@/assets/img/joing-us-skill.png" alt="" />
            <div class="joing-count-five-one course-count">
              <h3 class="joing-count-number">
                <span class="counterUp"
                  ><vue3-autocounter
                    class="counter"
                    ref="counter"
                    :startAmount="1"
                    :delay="3"
                    :endAmount="55"
                    :duration="5"
                    :autoinit="true" /></span
                >K<span>+</span>
              </h3>
              <p class="joing-count-text">Courses</p>
            </div>
            <div class="joing-count-five-two course-count">
              <h3 class="joing-count-number">
                <span class="counterUp"
                  ><vue3-autocounter
                    class="counter"
                    ref="counter"
                    :startAmount="1"
                    :delay="3"
                    :endAmount="50"
                    :duration="5"
                    :autoinit="true" /></span
                >K
              </h3>
              <p class="joing-count-text">Appreciations</p>
            </div>
            <div class="joing-count-five-three course-count">
              <h3 class="joing-count-number">
                <span class="counterUp"
                  ><vue3-autocounter
                    class="counter"
                    ref="counter"
                    :startAmount="10"
                    :delay="3"
                    :endAmount="100"
                    :duration="5"
                    :autoinit="true"
                /></span>
              </h3>
              <p class="joing-count-text">Countries</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- /Share your knowledge -->

  <!-- Achieve your Goals -->
  <section class="goals-section-five">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-x-4 col-lg-3 col-md-12 col-sm-12" data-aos="fade-down">
          <div class="header-five-title mb-0">
            <h2 class="mb-0">Achieve your Goals with DreamsLMS</h2>
          </div>
        </div>
        <div class="col-x-8 col-lg-9 col-md-12 col-sm-12">
          <div class="row text-center align-items-center">
            <!-- col -->
            <div class="col-lg-3 col-sm-3" data-aos="fade-down">
              <div class="goals-count-five goals-five-one">
                <div class="goals-content-five course-count ms-0">
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
            <div class="col-lg-3 col-sm-3" data-aos="fade-down">
              <div class="goals-count-five goals-five-two">
                <div class="goals-content-five course-count ms-0">
                  <h4>
                    <span class="counterUp"
                      ><vue3-autocounter
                        class="counter"
                        ref="counter"
                        :startAmount="1000"
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
            <div class="col-lg-3 col-sm-3" data-aos="fade-down">
              <div class="goals-count-five goals-five-three">
                <div class="goals-content-five course-count ms-0">
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
            <div class="col-lg-3 col-sm-3" data-aos="fade-down">
              <div class="goals-count-five goals-five-four goals-five-last">
                <div class="goals-content-five course-count ms-0">
                  <h4>
                    <span class="counterUp"
                      ><vue3-autocounter
                        class="counter"
                        ref="counter"
                        :startAmount="1000"
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
      </div>
    </div>
  </section>
  <!-- /Achieve your Goals -->

  <!-- Share your knowledge -->
  <section class="transform-section-five">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6 col-md-6 col-sm-12" data-aos="fade-down">
          <div class="joing-count-five">
            <img src="@/assets/img/education.png" alt="" />
            <div class="transform-count-five-one course-count">
              <h3 class="joing-count-number">
                <span class="counterUp"
                  ><vue3-autocounter
                    class="counter"
                    ref="counter"
                    :startAmount="10"
                    :delay="3"
                    :endAmount="100"
                    :duration="5"
                    :autoinit="true"
                /></span>
              </h3>
              <p class="joing-count-text">Countries</p>
            </div>
            <div class="transform-count-five-two course-count">
              <h3 class="joing-count-number">
                <span class="counterUp"
                  ><vue3-autocounter
                    class="counter"
                    ref="counter"
                    :startAmount="1"
                    :delay="3"
                    :endAmount="55"
                    :duration="5"
                    :autoinit="true" /></span
                >K<span>+</span>
              </h3>
              <p class="joing-count-text">Courses</p>
            </div>
            <div class="transform-count-five-three course-count">
              <h3 class="joing-count-number">
                <span class="counterUp"
                  ><vue3-autocounter
                    class="counter"
                    ref="counter"
                    :startAmount="1"
                    :delay="3"
                    :endAmount="50"
                    :duration="5"
                    :autoinit="true" /></span
                >K<span>+</span>
              </h3>
              <p class="joing-count-text">Appreciations</p>
            </div>
          </div>
        </div>
        <div class="col-lg-6 col-md-6 col-sm-12" data-aos="fade-down">
          <div class="transform-access-content">
            <div class="header-five-title">
              <h2>Transform Access To Education</h2>
            </div>
            <div class="career-five-content">
              <p class="mb-0">
                Create an account to receive our newsletter, course recommendations and
                promotions. Create an account to receive our newsletter, course
                recommendations and promotions. Create an account to receive our
                newsletter, course recommendations and promotions.
              </p>
            </div>
            <div class="knowledge-list-five">
              <ul>
                <li>
                  <div class="knowledge-list-group">
                    <img src="@/assets/img/icon/award-new.svg" alt="" />
                    <p>Award Winning Course Management</p>
                  </div>
                </li>
                <li>
                  <div class="knowledge-list-group">
                    <img src="@/assets/img/icon/award-new.svg" alt="" />
                    <p>Learn anything from anywhere anytime</p>
                  </div>
                </li>
                <li class="mb-0">
                  <div class="knowledge-list-group">
                    <img src="@/assets/img/icon/award-new.svg" alt="" />
                    <p>Certification for solid development of your Carrer</p>
                  </div>
                </li>
              </ul>
            </div>
            <!-- Start Teaching Today -->
            <router-link to="instructor-course" class="learn-more-five"
              >Start Teaching Today</router-link
            >
            <!-- /Start Teaching Today -->
          </div>
        </div>
      </div>
    </div>
  </section>
  <!-- /Share your knowledge -->
</template>
<script>
import AOS from "aos";
import "aos/dist/aos.css";
import profile from "@/assets/json/profile.json";
export default {
  data() {
    return {
      profile: profile,
    };
  },

  mounted() {
    this.$nextTick(() => {
      AOS.init();
    });
  },
};
</script>
