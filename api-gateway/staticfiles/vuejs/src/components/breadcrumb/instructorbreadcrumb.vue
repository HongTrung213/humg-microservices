<template>
  <!-- Breadcrumb -->
  <div class="page-banner instructor-bg-blk">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6 col-md-12">
          <div class="instructor-profile d-flex align-items-center">
            <div class="instructor-profile-pic">
              <router-link to="instructor-profile">
                <img
                  src="@/assets/img/instructor/profile-avatar.jpg"
                  alt=""
                  class="img-fluid"
                />
              </router-link>
            </div>
            <div class="instructor-profile-content">
              <h4>
                <router-link to="instructor-profile"
                  >Jenny Wilson <span>Beginner</span></router-link
                >
              </h4>
              <p>Instructor</p>
            </div>
          </div>
        </div>
        <div class="col-lg-6 col-md-12">
          <div class="instructor-profile-menu">
            <ul class="nav">
              <li>
                <div class="d-flex align-items-center">
                  <div class="instructor-profile-menu-img">
                    <img src="@/assets/img/icon/icon-25.svg" alt="" />
                  </div>
                  <div class="instructor-profile-menu-content">
                    <h4>32</h4>
                    <p>Courses</p>
                  </div>
                </div>
              </li>
              <li>
                <div class="d-flex align-items-center">
                  <div class="instructor-profile-menu-img">
                    <img src="@/assets/img/icon/icon-26.svg" alt="" />
                  </div>
                  <div class="instructor-profile-menu-content">
                    <h4>11,604</h4>
                    <p>Total Students</p>
                  </div>
                </div>
              </li>
              <li>
                <div class="d-flex align-items-center">
                  <div class="instructor-profile-menu-img">
                    <img src="@/assets/img/icon/icon-27.svg" alt="" />
                  </div>
                  <div class="instructor-profile-menu-content">
                    <h4>12,230</h4>
                    <p>Reviews</p>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <div class="instructor-profile-text">
            <p>
              I am an Innovation designer focussing on UX/UI based in Berlin. As a
              creative resident at Figma explored the city of the future and how new
              technologies like AI, voice control, and augmented reality will change our
              interfaces.
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Breadcrumb -->
</template>
