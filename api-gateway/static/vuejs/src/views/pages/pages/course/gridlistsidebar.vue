<template>
  <div class="col-lg-3 theiaStickySidebar">
    <div class="stickysidebar">
      <div class="filter-clear">
        <div class="clear-filter d-flex align-items-center">
          <h4><i class="feather-filter"></i>Filters</h4>
          <div class="clear-text">
            <p>CLEAR</p>
          </div>
        </div>

        <!-- Search Filter -->
        <div class="card search-filter">
          <div class="card-body">
            <div class="filter-widget mb-0">
              <div class="categories-head d-flex align-items-center">
                <h4>Course categories</h4>
                <i class="fas fa-angle-down"></i>
              </div>
              <div>
                <label class="custom_check">
                  <input type="checkbox" name="select_specialist" />
                  <span class="checkmark"></span> Backend (3)
                </label>
              </div>
              <div>
                <label class="custom_check">
                  <input type="checkbox" name="select_specialist" />
                  <span class="checkmark"></span> CSS (2)
                </label>
              </div>
              <div>
                <label class="custom_check">
                  <input type="checkbox" name="select_specialist" />
                  <span class="checkmark"></span> Frontend (2)
                </label>
              </div>
              <div>
                <label class="custom_check">
                  <input type="checkbox" name="select_specialist" checked />
                  <span class="checkmark"></span> General (2)
                </label>
              </div>
              <div>
                <label class="custom_check">
                  <input type="checkbox" name="select_specialist" checked />
                  <span class="checkmark"></span> IT & Software (2)
                </label>
              </div>
              <div>
                <label class="custom_check">
                  <input type="checkbox" name="select_specialist" />
                  <span class="checkmark"></span> Photography (2)
                </label>
              </div>
              <div>
                <label class="custom_check">
                  <input type="checkbox" name="select_specialist" />
                  <span class="checkmark"></span> Programming Language (3)
                </label>
              </div>
              <div>
                <label class="custom_check mb-0">
                  <input type="checkbox" name="select_specialist" />
                  <span class="checkmark"></span> Technology (2)
                </label>
              </div>
            </div>
          </div>
        </div>
        <!-- /Search Filter -->

        <!-- Search Filter -->
        <div class="card search-filter">
          <div class="card-body">
            <div class="filter-widget mb-0">
              <div class="categories-head d-flex align-items-center">
                <h4>Instructors</h4>
                <i class="fas fa-angle-down"></i>
              </div>
              <div>
                <label class="custom_check">
                  <input type="checkbox" name="select_specialist" />
                  <span class="checkmark"></span> Keny White (10)
                </label>
              </div>
              <div>
                <label class="custom_check">
                  <input type="checkbox" name="select_specialist" />
                  <span class="checkmark"></span> Hinata Hyuga (5)
                </label>
              </div>
              <div>
                <label class="custom_check">
                  <input type="checkbox" name="select_specialist" />
                  <span class="checkmark"></span> John Doe (3)
                </label>
              </div>
              <div>
                <label class="custom_check mb-0">
                  <input type="checkbox" name="select_specialist" checked />
                  <span class="checkmark"></span> Nicole Brown
                </label>
              </div>
            </div>
          </div>
        </div>
        <!-- /Search Filter -->

        <!-- Search Filter -->
        <div class="card search-filter">
          <div class="card-body">
            <div class="filter-widget mb-0">
              <div class="categories-head d-flex align-items-center">
                <h4>Price</h4>
                <i class="fas fa-angle-down"></i>
              </div>
              <div>
                <label class="custom_check custom_one">
                  <input type="radio" name="select_specialist" />
                  <span class="checkmark"></span> All (18)
                </label>
              </div>
              <div>
                <label class="custom_check custom_one">
                  <input type="radio" name="select_specialist" />
                  <span class="checkmark"></span> Free (3)
                </label>
              </div>
              <div>
                <label class="custom_check custom_one mb-0">
                  <input type="radio" name="select_specialist" checked />
                  <span class="checkmark"></span> Paid (15)
                </label>
              </div>
            </div>
          </div>
        </div>
        <!-- /Search Filter -->

        <!-- Latest Posts -->
        <div class="card post-widget">
          <div class="card-body">
            <div class="latest-head">
              <h4 class="card-title">Latest Courses</h4>
            </div>
            <ul class="latest-posts">
              <li>
                <div class="post-thumb">
                  <router-link to="course-details">
                    <img
                      class="img-fluid"
                      src="@/assets/img/blog/blog-01.jpg"
                      alt=""
                    />
                  </router-link>
                </div>
                <div class="post-info free-color">
                  <h4>
                    <router-link to="course-details"
                      >Introduction LearnPress – LMS plugin</router-link
                    >
                  </h4>
                  <p>FREE</p>
                </div>
              </li>
              <li>
                <div class="post-thumb">
                  <router-link to="course-details">
                    <img
                      class="img-fluid"
                      src="@/assets/img/blog/blog-02.jpg"
                      alt=""
                    />
                  </router-link>
                </div>
                <div class="post-info">
                  <h4>
                    <router-link to="course-details"
                      >Become a PHP Master and Make Money</router-link
                    >
                  </h4>
                  <p>$200</p>
                </div>
              </li>
              <li>
                <div class="post-thumb">
                  <a href="course-details">
                    <img
                      class="img-fluid"
                      src="@/assets/img/blog/blog-03.jpg"
                      alt=""
                    />
                  </a>
                </div>
                <div class="post-info free-color">
                  <h4>
                    <a href="course-details">Learning jQuery Mobile for Beginners</a>
                  </h4>
                  <p>FREE</p>
                </div>
              </li>
              <li>
                <div class="post-thumb">
                  <a href="course-details">
                    <img
                      class="img-fluid"
                      src="@/assets/img/blog/blog-01.jpg"
                      alt=""
                    />
                  </a>
                </div>
                <div class="post-info">
                  <h4>
                    <a href="course-details">Improve Your CSS Workflow with SASS</a>
                  </h4>
                  <p>$200</p>
                </div>
              </li>
              <li>
                <div class="post-thumb">
                  <a href="course-details">
                    <img
                      class="img-fluid"
                      src="@/assets/img/blog/blog-02.jpg"
                      alt=""
                    />
                  </a>
                </div>
                <div class="post-info free-color">
                  <h4>
                    <a href="course-details">HTML5/CSS3 Essentials in 4-Hours</a>
                  </h4>
                  <p>FREE</p>
                </div>
              </li>
            </ul>
          </div>
        </div>
        <!-- /Latest Posts -->
      </div>
    </div>
  </div>
</template>
