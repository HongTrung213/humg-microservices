<template>
  <!-- Inner Banner -->
  <div class="inner-banner">
    <div class="container">
      <div class="row">
        <div class="col-lg-8">
          <div class="instructor-wrap border-bottom-0 m-0">
            <div class="about-instructor align-items-center">
              <div class="abt-instructor-img">
                <router-link to="instructor-profile"
                  ><img
                    src="@/assets/img/user/user1.jpg"
                    alt="img"
                    class="img-fluid"
                /></router-link>
              </div>
              <div class="instructor-detail me-3">
                <h5><router-link to="instructor-profile">Nicole Brown</router-link></h5>
                <p>UX/UI Designer</p>
              </div>
              <div class="rating mb-0">
                <i class="fas fa-star filled me-1"></i>
                <i class="fas fa-star filled me-1"></i>
                <i class="fas fa-star filled me-1"></i>
                <i class="fas fa-star filled me-1"></i>
                <i class="fas fa-star me-1"></i>
                <span class="d-inline-block average-rating"><span>4.5</span> (15)</span>
              </div>
            </div>
            <span class="web-badge mb-3">WEB DEVELPMENT</span>
          </div>
          <h2>The Complete Web Developer Course 2.0</h2>
          <p>
            Learn Web Development by building 25 websites and mobile apps using HTML, CSS,
            Javascript, PHP, Python, MySQL & more!
          </p>
          <div class="course-info d-flex align-items-center border-bottom-0 m-0 p-0">
            <div class="cou-info">
              <img src="@/assets/img/icon/icon-01.svg" alt="" />
              <p>12+ Lesson</p>
            </div>
            <div class="cou-info">
              <img src="@/assets/img/icon/timer-icon.svg" alt="" />
              <p>9hr 30min</p>
            </div>
            <div class="cou-info">
              <img src="@/assets/img/icon/people.svg" alt="" />
              <p>32 students enrolled</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Inner Banner -->
</template>
