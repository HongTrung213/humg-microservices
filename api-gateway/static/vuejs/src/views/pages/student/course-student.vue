<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layouts></layouts>
    <courseheader></courseheader>
    <!-- My Course -->
    <section class="course-content">
      <div class="container">
        <div class="student-widget">
          <div class="student-widget-group">
            <div class="row">
              <div class="col-lg-12">
                <studentfilter></studentfilter>

                <div class="row">
                  <div class="col-xl-3 col-lg-4 col-md-6 d-flex">
                    <div class="course-box course-design d-flex">
                      <div class="product">
                        <div class="product-img">
                          <router-link to="course-details">
                            <img
                              class="img-fluid"
                              alt=""
                              src="@/assets/img/course/course-10.jpg"
                            />
                          </router-link>
                        </div>
                        <div class="product-content">
                          <h3 class="title">
                            <router-link to="course-details"
                              >Information About UI/UX Design Degree</router-link
                            >
                          </h3>
                          <div class="rating-student">
                            <div class="rating">
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star me-1"></i>
                              <span class="d-inline-block average-rating"
                                ><span>4.0</span></span
                              >
                            </div>
                            <div class="edit-rate">
                              <a href="javascript:;">Edit rating</a>
                            </div>
                          </div>
                          <div class="progress-stip">
                            <div
                              class="progress-bar bg-success progress-bar-striped active-stip"
                            ></div>
                          </div>
                          <div class="student-percent">
                            <p>35% Completed</p>
                          </div>
                          <div class="start-leason d-flex align-items-center">
                            <router-link to="course-lesson" class="btn btn-primary"
                              >Start Lesson</router-link
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-xl-3 col-lg-4 col-md-6 d-flex">
                    <div class="course-box course-design d-flex">
                      <div class="product">
                        <div class="product-img">
                          <router-link to="course-details">
                            <img
                              class="img-fluid"
                              alt=""
                              src="@/assets/img/course/course-11.jpg"
                            />
                          </router-link>
                        </div>
                        <div class="product-content">
                          <h3 class="title">
                            <router-link to="course-details"
                              >Wordpress for Beginners - Master Wordpress
                              Quickly</router-link
                            >
                          </h3>
                          <div class="rating-student">
                            <div class="rating">
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star me-1"></i>
                              <span class="d-inline-block average-rating"
                                ><span>4.0</span>
                              </span>
                            </div>
                            <div class="edit-rate">
                              <a href="javascript:;">Edit rating</a>
                            </div>
                          </div>
                          <div class="progress-stip">
                            <div
                              class="progress-bar bg-success progress-bar-striped"
                            ></div>
                          </div>
                          <div class="student-percent">
                            <p>0% Completed</p>
                          </div>
                          <div class="start-leason d-flex align-items-center">
                            <router-link to="course-lesson" class="btn btn-primary"
                              >Start Lesson</router-link
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-xl-3 col-lg-4 col-md-6 d-flex">
                    <div class="course-box course-design d-flex">
                      <div class="product">
                        <div class="product-img">
                          <router-link to="course-details">
                            <img
                              class="img-fluid"
                              alt=""
                              src="@/assets/img/course/course-12.jpg"
                            />
                          </router-link>
                        </div>
                        <div class="product-content">
                          <h3 class="title">
                            <router-link to="course-details"
                              >Sketch from A to Z (2023): Become an app
                              designer</router-link
                            >
                          </h3>
                          <div class="rating-student">
                            <div class="rating">
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star me-1"></i>
                              <span class="d-inline-block average-rating"
                                ><span>4.0</span></span
                              >
                            </div>
                            <div class="edit-rate">
                              <a href="javascript:;">Edit rating</a>
                            </div>
                          </div>
                          <div class="progress-stip">
                            <div
                              class="progress-bar bg-success progress-bar-striped"
                            ></div>
                          </div>
                          <div class="student-percent">
                            <p>0% Completed</p>
                          </div>
                          <div class="start-leason d-flex align-items-center">
                            <router-link to="course-lesson" class="btn btn-primary"
                              >Start Lesson</router-link
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-xl-3 col-lg-4 col-md-6 d-flex">
                    <div class="course-box course-design d-flex">
                      <div class="product">
                        <div class="product-img">
                          <router-link to="course-details">
                            <img
                              class="img-fluid"
                              alt=""
                              src="@/assets/img/course/course-13.jpg"
                            />
                          </router-link>
                        </div>
                        <div class="product-content">
                          <h3 class="title">
                            <router-link to="course-details"
                              >Learn Angular Fundamentals From ...</router-link
                            >
                          </h3>
                          <div class="rating-student">
                            <div class="rating">
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star me-1"></i>
                              <span class="d-inline-block average-rating"
                                ><span>4.0</span></span
                              >
                            </div>
                            <div class="edit-rate">
                              <a href="javascript:;">Edit rating</a>
                            </div>
                          </div>
                          <div class="progress-stip">
                            <div
                              class="progress-bar bg-success progress-bar-striped"
                            ></div>
                          </div>
                          <div class="student-percent">
                            <p>0% Completed</p>
                          </div>
                          <div class="start-leason d-flex align-items-center">
                            <router-link to="course-lesson" class="btn btn-primary"
                              >Start Lesson</router-link
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-xl-3 col-lg-4 col-md-6 d-flex">
                    <div class="course-box course-design d-flex">
                      <div class="product">
                        <div class="product-img">
                          <router-link to="course-details">
                            <img
                              class="img-fluid"
                              alt=""
                              src="@/assets/img/course/course-14.jpg"
                            />
                          </router-link>
                        </div>
                        <div class="product-content">
                          <h3 class="title">
                            <router-link to="course-details"
                              >Build Responsive Real World Websites with...</router-link
                            >
                          </h3>
                          <div class="rating-student">
                            <div class="rating">
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star me-1"></i>
                              <span class="d-inline-block average-rating"
                                ><span>4.0</span></span
                              >
                            </div>
                            <div class="edit-rate">
                              <a href="javascript:;">Edit rating</a>
                            </div>
                          </div>
                          <div class="progress-stip">
                            <div
                              class="progress-bar bg-success progress-bar-striped"
                            ></div>
                          </div>
                          <div class="student-percent">
                            <p>0% Completed</p>
                          </div>
                          <div class="start-leason d-flex align-items-center">
                            <router-link to="course-lesson" class="btn btn-primary"
                              >Start Lesson</router-link
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-xl-3 col-lg-4 col-md-6 d-flex">
                    <div class="course-box course-design d-flex">
                      <div class="product">
                        <div class="product-img">
                          <router-link to="course-details">
                            <img
                              class="img-fluid"
                              alt=""
                              src="@/assets/img/course/course-15.jpg"
                            />
                          </router-link>
                        </div>
                        <div class="product-content">
                          <h3 class="title">
                            <router-link to="course-details"
                              >C# Developers Double Your Coding Speed with
                              ...</router-link
                            >
                          </h3>
                          <div class="rating-student">
                            <div class="rating">
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star me-1"></i>
                              <span class="d-inline-block average-rating"
                                ><span>4.0</span></span
                              >
                            </div>
                            <div class="edit-rate">
                              <a href="javascript:;">Edit rating</a>
                            </div>
                          </div>
                          <div class="progress-stip">
                            <div
                              class="progress-bar bg-success progress-bar-striped"
                            ></div>
                          </div>
                          <div class="student-percent">
                            <p>0% Completed</p>
                          </div>
                          <div class="start-leason d-flex align-items-center">
                            <router-link to="course-lesson" class="btn btn-primary"
                              >Start Lesson</router-link
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-xl-3 col-lg-4 col-md-6 d-flex">
                    <div class="course-box course-design d-flex">
                      <div class="product">
                        <div class="product-img">
                          <router-link to="course-details">
                            <img
                              class="img-fluid"
                              alt=""
                              src="@/assets/img/course/course-16.jpg"
                            />
                          </router-link>
                        </div>
                        <div class="product-content">
                          <h3 class="title">
                            <router-link to="course-details"
                              >Learn JavaScript and Express to become a ...</router-link
                            >
                          </h3>
                          <div class="rating-student">
                            <div class="rating">
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star me-1"></i>
                              <span class="d-inline-block average-rating"
                                ><span>4.0</span></span
                              >
                            </div>
                            <div class="edit-rate">
                              <a href="javascript:;">Edit rating</a>
                            </div>
                          </div>
                          <div class="progress-stip">
                            <div
                              class="progress-bar bg-success progress-bar-striped"
                            ></div>
                          </div>
                          <div class="student-percent">
                            <p>0% Completed</p>
                          </div>
                          <div class="start-leason d-flex align-items-center">
                            <router-link to="course-lesson" class="btn btn-primary"
                              >Start Lesson</router-link
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="col-xl-3 col-lg-4 col-md-6 d-flex">
                    <div class="course-box course-design d-flex">
                      <div class="product">
                        <div class="product-img">
                          <router-link to="course-details">
                            <img
                              class="img-fluid"
                              alt=""
                              src="@/assets/img/course/course-17.jpg"
                            />
                          </router-link>
                        </div>
                        <div class="product-content">
                          <h3 class="title">
                            <router-link to="course-details"
                              >Responsive Web Design Essentials HTML5 CSS3
                              ...</router-link
                            >
                          </h3>
                          <div class="rating-student">
                            <div class="rating">
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star filled me-1"></i>
                              <i class="fas fa-star me-1"></i>
                              <span class="d-inline-block average-rating"
                                ><span>4.0</span></span
                              >
                            </div>
                            <div class="edit-rate">
                              <a id="edit-rating">Edit rating</a>
                            </div>
                          </div>
                          <div class="publish-rate">
                            <form action="#">
                              <vue-select
                                :options="Out"
                                placeholder="4 Out of 5"
                                name="sellist1"
                              />
                              <div class="form-group mt-3">
                                <textarea
                                  class="form-control"
                                  rows="4"
                                  name="text"
                                ></textarea>
                              </div>
                              <div class="group-btn mb-3">
                                <button
                                  type="submit"
                                  class="btn btn-primary publish-btn mb-3"
                                >
                                  Publish Rating
                                </button>
                                <button type="submit" class="btn btn-primary cancel-btn">
                                  Cancel
                                </button>
                              </div>
                            </form>
                          </div>
                          <div class="stip-grp">
                            <div class="progress-stip">
                              <div
                                class="progress-bar bg-success progress-bar-striped"
                              ></div>
                            </div>
                            <div class="student-percent">
                              <p>0% Completed</p>
                            </div>
                            <div class="start-leason d-flex align-items-center">
                              <router-link to="course-lesson" class="btn btn-primary"
                                >Start Lesson</router-link
                              >
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
        </div>
      </div>
    </section>
    <!-- /My Course -->

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
      Out: ["4 Out of 5", "3 Out of 5", "2 Out of 5", "1 Out of 5"],
    };
  },
};
</script>
