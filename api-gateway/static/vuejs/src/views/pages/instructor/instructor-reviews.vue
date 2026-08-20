<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layoutsinstructor></layoutsinstructor>

    <!-- Page Wrapper -->
    <div class="page-content">
      <div class="container">
        <div class="row">
          <instructorsidebar></instructorsidebar>

          <!-- Instructor Dashboard -->
          <div class="col-xl-9 col-lg-8 col-md-12">
            <div class="row">
              <div class="col-md-12">
                <div class="settings-widget">
                  <div class="settings-inner-blk p-0">
                    <div class="sell-course-head comman-space">
                      <h3>Reviews</h3>
                      <p>You have full control to manage your own account setting.</p>
                    </div>
                    <div class="comman-space pb-0">
                      <div class="instruct-search-blk mb-0">
                        <div class="show-filter all-select-blk">
                          <form action="#">
                            <div class="row gx-2 align-items-center">
                              <div class="col-md-6 col-lg-3 col-item">
                                <div class="form-group select-form mb-1">
                                  <vue-select :options="All" placeholder="All" />
                                </div>
                              </div>
                              <div class="col-md-6 col-lg-3 col-item">
                                <div class="form-group select-form mb-1">
                                  <vue-select :options="Rating" placeholder="Rating" />
                                </div>
                              </div>
                              <div class="col-md-6 col-lg-3 col-item">
                                <div class="form-group select-form mb-1">
                                  <vue-select :options="Sort" placeholder="Sort" />
                                </div>
                              </div>
                            </div>
                          </form>
                        </div>
                      </div>
                    </div>
                    <div class="comman-space bdr-bottom-line">
                      <div class="instruct-review-blk">
                        <div class="review-item">
                          <div class="instructor-wrap border-0 m-0">
                            <div class="about-instructor">
                              <div class="abt-instructor-img">
                                <router-link to="instructor-profile"
                                  ><img
                                    src="@/assets/img/user/user1.jpg"
                                    alt="img"
                                    class="img-fluid"
                                /></router-link>
                              </div>
                              <div class="instructor-detail">
                                <h5>
                                  <router-link to="instructor-profile"
                                    >Nicole Brown</router-link
                                  >
                                </h5>
                                <p>UX/UI Designer</p>
                              </div>
                            </div>
                            <div class="rating">
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star"></i>
                            </div>
                          </div>
                          <p class="rev-info">
                            “ This is the second Photoshop course I have completed with
                            Cristian. Worth every penny and recommend it highly. To get
                            the most out of this course, its best to to take the Beginner
                            to Advanced course first. The sound and video quality is of a
                            good standard. Thank you Cristian. “
                          </p>
                          <a href="javascript:;" class="btn btn-reply"
                            ><i class="feather-corner-up-left"></i> Respond</a
                          >
                        </div>
                      </div>
                    </div>
                    <div class="comman-space bdr-bottom-line">
                      <div class="instruct-review-blk">
                        <div class="review-item">
                          <div class="instructor-wrap border-0 m-0">
                            <div class="about-instructor">
                              <div class="abt-instructor-img">
                                <router-link to="instructor-profile"
                                  ><img
                                    src="@/assets/img/user/user2.jpg"
                                    alt="img"
                                    class="img-fluid"
                                /></router-link>
                              </div>
                              <div class="instructor-detail">
                                <h5>
                                  <router-link to="instructor-profile"
                                    >Jesse Stevens</router-link
                                  >
                                </h5>
                                <p>UX/UI Designer</p>
                              </div>
                            </div>
                            <div class="rating">
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star"></i>
                            </div>
                          </div>
                          <p class="rev-info">
                            “ This is the second Photoshop course I have completed with
                            Cristian. Worth every penny and recommend it highly. To get
                            the most out of this course, its best to to take the Beginner
                            to Advanced course first. The sound and video quality is of a
                            good standard. Thank you Cristian. “
                          </p>
                          <a href="javascript:;" class="btn btn-reply"
                            ><i class="feather-corner-up-left"></i> Respond</a
                          >
                        </div>
                      </div>
                    </div>
                    <div class="comman-space bdr-bottom-line">
                      <div class="instruct-review-blk">
                        <div class="review-item">
                          <div class="instructor-wrap border-0 m-0">
                            <div class="about-instructor">
                              <div class="abt-instructor-img">
                                <router-link to="instructor-profile"
                                  ><img
                                    src="@/assets/img/user/user3.jpg"
                                    alt="img"
                                    class="img-fluid"
                                /></router-link>
                              </div>
                              <div class="instructor-detail">
                                <h5>
                                  <router-link to="instructor-profile"
                                    >John Smith</router-link
                                  >
                                </h5>
                                <p>UX/UI Designer</p>
                              </div>
                            </div>
                            <div class="rating">
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star"></i>
                            </div>
                          </div>
                          <p class="rev-info">
                            “ This is the second Photoshop course I have completed with
                            Cristian. Worth every penny and recommend it highly. To get
                            the most out of this course, its best to to take the Beginner
                            to Advanced course first. The sound and video quality is of a
                            good standard. Thank you Cristian. “
                          </p>
                          <a href="javascript:;" class="btn btn-reply"
                            ><i class="feather-corner-up-left"></i> Respond</a
                          >
                        </div>
                      </div>
                    </div>
                    <div class="comman-space">
                      <div class="instruct-review-blk">
                        <div class="review-item">
                          <div class="instructor-wrap border-0 m-0">
                            <div class="about-instructor">
                              <div class="abt-instructor-img">
                                <router-link to="instructor-profile"
                                  ><img
                                    src="@/assets/img/user/user4.jpg"
                                    alt="img"
                                    class="img-fluid"
                                /></router-link>
                              </div>
                              <div class="instructor-detail">
                                <h5>
                                  <router-link to="instructor-profile"
                                    >Stella Johnson</router-link
                                  >
                                </h5>
                                <p>UX/UI Designer</p>
                              </div>
                            </div>
                            <div class="rating">
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star"></i>
                            </div>
                          </div>
                          <p class="rev-info">
                            “ This is the second Photoshop course I have completed with
                            Cristian. Worth every penny and recommend it highly. To get
                            the most out of this course, its best to to take the Beginner
                            to Advanced course first. The sound and video quality is of a
                            good standard. Thank you Cristian. “
                          </p>
                          <a href="javascript:;" class="btn btn-reply"
                            ><i class="feather-corner-up-left"></i> Respond</a
                          >
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /Instructor Dashboard -->
        </div>
      </div>
    </div>
    <!-- /Page Wrapper -->

    <layouts1></layouts1>
  </div>
  <!-- /Main Wrapper -->
</template>
<script>
import Vue from "vue";
export default {
  components: {},
  data() {
    return {
      All: ["All", "review 1", "review 2", "review 3"],
      Rating: ["Rating", "5", "4", "3"],
      Sort: ["Sort", "Sort 1", "Sort 2", "Sort 3"],
    };
  },
};
</script>
