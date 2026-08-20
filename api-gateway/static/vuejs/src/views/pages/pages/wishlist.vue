<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layoutsloginborder></layoutsloginborder>

    <wishlistbreadcrumb></wishlistbreadcrumb>
    <!-- Pricing Plan -->
    <section class="course-content">
      <div class="container">
        <div class="card wish-card">
          <div class="card-header">
            <h5>Your Wishlist (03 items)</h5>
          </div>
          <div class="card-body">
            <div class="row">
              <div class="col-md-12">
                <div class="wishlist-item">
                  <div class="row align-items-center">
                    <div class="col-md-9">
                      <div class="wishlist-detail">
                        <div class="wishlist-img">
                          <router-link to="course-details">
                            <img alt="" src="@/assets/img/course/course-01.jpg" />
                          </router-link>
                          <div class="price-amt">
                            <h4>$300</h4>
                          </div>
                        </div>
                        <div class="wishlist-info">
                          <h5>
                            <router-link to="course-details"
                              >Information About UI/UX Design Degree</router-link
                            >
                          </h5>
                          <div
                            class="course-info d-flex align-items-center border-bottom-0 pb-0"
                          >
                            <div class="rating-img d-flex align-items-center">
                              <img src="@/assets/img/icon/icon-01.svg" alt="" />
                              <p>12+ Lesson</p>
                            </div>
                            <div class="course-view d-flex align-items-center">
                              <img src="@/assets/img/icon/icon-02.svg" alt="" />
                              <p>9hr 30min</p>
                            </div>
                          </div>
                          <div class="rating">
                            <i class="fas fa-star filled me-1"></i>
                            <i class="fas fa-star filled me-1"></i>
                            <i class="fas fa-star filled me-1"></i>
                            <i class="fas fa-star filled me-1"></i>
                            <i class="fas fa-star me-1"></i>
                            <span class="d-inline-block average-rating"
                              ><span>4.0</span> (15)</span
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="col-md-3">
                      <div class="remove-btn">
                        <a href="javascript:;" class="btn">Remove</a>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="wishlist-item">
                  <div class="row align-items-center">
                    <div class="col-md-9">
                      <div class="wishlist-detail">
                        <div class="wishlist-img">
                          <router-link to="course-details">
                            <img alt="" src="@/assets/img/course/course-02.jpg" />
                          </router-link>
                          <div class="price-amt">
                            <h4>$300</h4>
                          </div>
                        </div>
                        <div class="wishlist-info">
                          <h5>
                            <router-link to="course-details"
                              >Wordpress for Beginners - Master Wordpress
                              Quickly</router-link
                            >
                          </h5>
                          <div
                            class="course-info d-flex align-items-center border-bottom-0 pb-0"
                          >
                            <div class="rating-img d-flex align-items-center">
                              <img src="@/assets/img/icon/icon-01.svg" alt="" />
                              <p>12+ Lesson</p>
                            </div>
                            <div class="course-view d-flex align-items-center">
                              <img src="@/assets/img/icon/icon-02.svg" alt="" />
                              <p>9hr 30min</p>
                            </div>
                          </div>
                          <div class="rating">
                            <i class="fas fa-star filled me-1"></i>
                            <i class="fas fa-star filled me-1"></i>
                            <i class="fas fa-star filled me-1"></i>
                            <i class="fas fa-star filled me-1"></i>
                            <i class="fas fa-star me-1"></i>
                            <span class="d-inline-block average-rating"
                              ><span>4.0</span> (15)</span
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="col-md-3">
                      <div class="remove-btn">
                        <a href="javascript:;" class="btn">Remove</a>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="wishlist-item">
                  <div class="row align-items-center">
                    <div class="col-md-9">
                      <div class="wishlist-detail">
                        <div class="wishlist-img">
                          <router-link to="course-details">
                            <img alt="" src="@/assets/img/course/course-03.jpg" />
                          </router-link>
                          <div class="price-amt">
                            <h4>$300</h4>
                          </div>
                        </div>
                        <div class="wishlist-info">
                          <h5>
                            <router-link to="course-details"
                              >Sketch from A to Z (2023): Become an app
                              designer</router-link
                            >
                          </h5>
                          <div
                            class="course-info d-flex align-items-center border-bottom-0 pb-0"
                          >
                            <div class="rating-img d-flex align-items-center">
                              <img src="@/assets/img/icon/icon-01.svg" alt="" />
                              <p>12+ Lesson</p>
                            </div>
                            <div class="course-view d-flex align-items-center">
                              <img src="@/assets/img/icon/icon-02.svg" alt="" />
                              <p>9hr 30min</p>
                            </div>
                          </div>
                          <div class="rating">
                            <i class="fas fa-star filled me-1"></i>
                            <i class="fas fa-star filled me-1"></i>
                            <i class="fas fa-star filled me-1"></i>
                            <i class="fas fa-star filled me-1"></i>
                            <i class="fas fa-star me-1"></i>
                            <span class="d-inline-block average-rating"
                              ><span>4.0</span> (15)</span
                            >
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="col-md-3">
                      <div class="remove-btn">
                        <a href="javascript:;" class="btn">Remove</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <!-- /Plan Type -->
          </div>
        </div>
      </div>
    </section>
    <!-- /Pricing Plan -->
    <layouts1></layouts1>
  </div>
  <!-- /Main Wrapper -->
</template>
