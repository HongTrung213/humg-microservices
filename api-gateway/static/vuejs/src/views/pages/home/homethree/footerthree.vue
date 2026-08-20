<template>
  <!-- Footer -->
  <footer class="footer footer-three">
    <!-- Footer Top -->
    <div class="footer-three-top" data-aos="fade-up">
      <div class="container">
        <div class="footer-three-top-content">
          <div class="row align-items-center">
            <div class="col-lg-6 col-md-6 col-12">
              <!-- Footer Widget -->
              <div class="footer-widget-three footer-about">
                <div class="footer-three-logo">
                  <img class="img-fluid" src="@/assets/img/logo/logo.png" alt="logo" />
                </div>
                <div class="footer-three-about">
                  <p>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sit nulla
                    gravida ut elit arcu egestas felis. Scelerisque at in magna dolor
                    massa ipsum arcu lacus. Lobortis posuere justo nunc diam ac massa.
                    Maecenas tellus adipiscing ac fames ut ac posuere. Aliquam, integer
                    proin hendrerit euismod et.
                  </p>
                </div>
                <div class="newsletter-title">
                  <h6>Get Updates</h6>
                </div>
                <div class="box-form-newsletter">
                  <form class="form-newsletter">
                    <input
                      class="input-newsletter"
                      type="text"
                      placeholder="Enter your email here"
                    />
                    <button class="btn btn-default font-heading icon-send-letter">
                      Subscribe Now
                    </button>
                  </form>
                </div>
              </div>
              <!-- /Footer Widget -->
            </div>

            <div class="col-lg-3 col-md-3 col-12">
              <!-- Footer Widget -->
              <div class="footer-widget-three footer-menu-three footer-three-right">
                <h6 class="footer-three-title">For Instructor</h6>
                <ul>
                  <li><router-link to="instructor-profile">Profile</router-link></li>
                  <li><router-link to="login">Login</router-link></li>
                  <li><router-link to="register">Register</router-link></li>
                  <li><router-link to="instructor-list">Instructor</router-link></li>
                  <li>
                    <router-link to="deposit-instructor-dashboard">
                      Dashboard</router-link
                    >
                  </li>
                </ul>
              </div>
              <!-- /Footer Widget -->
            </div>

            <div class="col-lg-3 col-md-3 col-12">
              <!-- Footer Widget -->
              <div class="footer-widget-three footer-menu-three">
                <h6 class="footer-three-title">For Student</h6>
                <ul>
                  <li><router-link to="student-profile">Profile</router-link></li>
                  <li><router-link to="login">Login</router-link></li>
                  <li><router-link to="register">Register</router-link></li>
                  <li><router-link to="students-list">Student</router-link></li>
                  <li>
                    <router-link to="deposit-student-dashboard"> Dashboard</router-link>
                  </li>
                </ul>
              </div>
              <!-- /Footer Widget -->
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- /Footer Top -->

    <!-- Footer Bottom -->
    <div class="footer-three-bottom" data-aos="fade-up">
      <div class="container">
        <!-- Copyright -->
        <div class="copyright-three">
          <div class="row">
            <div class="col-md-12">
              <div class="social-icon-three">
                <h6>Connect Socially</h6>
                <ul>
                  <li>
                    <a href="javascript:;" target="_blank" class="feather-facebook-icon">
                      <i class="feather-facebook"></i>
                    </a>
                  </li>
                  <li>
                    <a href="javascript:;" target="_blank" class="feather-twitter-icon">
                      <i class="feather-twitter"></i>
                    </a>
                  </li>
                  <li>
                    <a href="javascript:;" target="_blank" class="feather-linkedin-icon">
                      <i class="feather-linkedin"></i>
                    </a>
                  </li>
                  <li>
                    <a href="javascript:;" target="_blank" class="feather-youtube-icon">
                      <i class="feather-youtube"></i>
                    </a>
                  </li>
                </ul>
              </div>
              <div class="privacy-policy-three">
                <ul>
                  <li>
                    <router-link to="term-condition">Terms & Condition</router-link>
                  </li>
                  <li><router-link to="privacy-policy">Privacy Policy</router-link></li>
                  <li><router-link to="support">Contact Us</router-link></li>
                </ul>
              </div>
              <div class="copyright-text-three">
                <p class="mb-0">
                  &copy; {{ new Date().getFullYear() }} DreamsLMS. All rights reserved.
                </p>
              </div>
            </div>
          </div>
        </div>
        <!-- /Copyright -->
      </div>
    </div>
    <!-- /Footer Bottom -->
  </footer>
  <!-- /Footer -->
</template>
