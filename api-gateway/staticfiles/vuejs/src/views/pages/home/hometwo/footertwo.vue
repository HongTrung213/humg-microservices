<template>
  <!-- Footer -->
  <footer class="footer footer-two" data-aos="fade-up">
    <!-- Footer Top -->
    <div class="footer-top">
      <div class="container">
        <div class="row">
          <div class="col-lg-4 col-md-6 col-sm-6 col-12">
            <!-- Footer Widget -->
            <div class="footer-widget footer-about">
              <div class="footer-logo">
                <img src="@/assets/img/logo.svg" alt="logo" />
              </div>
              <div class="footer-about-content">
                <p>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat
                  mauris Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut
                  consequat mauris
                </p>
              </div>
              <div class="social-icon">
                <ul>
                  <li>
                    <a href="javascript:;" target="_blank"
                      ><i class="feather-facebook"></i
                    ></a>
                  </li>
                  <li>
                    <a href="javascript:;" target="_blank"
                      ><i class="feather-twitter"></i
                    ></a>
                  </li>
                  <li>
                    <a href="javascript:;" target="_blank"
                      ><i class="feather-instagram"></i
                    ></a>
                  </li>
                  <li>
                    <a href="javascript:;" target="_blank"
                      ><i class="feather-linkedin"></i
                    ></a>
                  </li>
                </ul>
              </div>
            </div>
            <!-- /Footer Widget -->
          </div>

          <div class="col-lg-2 col-md-6 col-sm-6 col-12">
            <!-- Footer Widget -->
            <div class="footer-widget footer-menu footer-menu-two">
              <h2 class="footer-title">For Instructor</h2>
              <ul>
                <li><router-link to="instructor-profile">Profile</router-link></li>
                <li><router-link to="login">Login</router-link></li>
                <li><router-link to="register">Register</router-link></li>
                <li><router-link to="instructor-list">Instructor</router-link></li>
                <li>
                  <router-link to="deposit-instructor-dashboard"> Dashboard</router-link>
                </li>
              </ul>
            </div>
            <!-- /Footer Widget -->
          </div>

          <div class="col-lg-2 col-md-6 col-sm-6 col-12">
            <!-- Footer Widget -->
            <div class="footer-widget footer-menu footer-menu-two">
              <h2 class="footer-title">For Student</h2>
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

          <div class="col-lg-4 col-md-6 col-sm-6 col-12">
            <!-- Footer Widget -->
            <div class="footer-widget footer-contact footer-contact-two">
              <h2 class="footer-title">Address</h2>
              <div class="footer-contact-widget">
                <div class="footer-address">
                  <h6>Location</h6>
                  <p>
                    3556 Beech Street, San Francisco,<br />
                    California, CA 94108
                  </p>
                </div>

                <h6>Email Address</h6>
                <p>
                  <a href="mailto:dreamslms@example.com">dreamslms@example.com</a>
                </p>

                <h6>Phone number</h6>
                <p class="mb-0">
                  <a href="tel:+191234567890">+19 123-456-7890</a>
                </p>
              </div>
            </div>
            <!-- /Footer Widget -->
          </div>
        </div>
      </div>
    </div>
    <!-- /Footer Top -->

    <!-- Footer Bottom -->
    <div class="footer-bottom">
      <div class="container">
        <!-- Copyright -->
        <div class="copyright">
          <div class="row">
            <div class="col-md-6 col-sm-12">
              <div class="copyright-text">
                <p class="mb-0">
                  &copy; {{ new Date().getFullYear() }} DreamsLMS. All rights reserved.
                </p>
              </div>
            </div>
            <div class="col-md-6 col-sm-12">
              <div class="privacy-policy">
                <ul>
                  <li>
                    <router-link to="term-condition">Terms & Condition</router-link>
                  </li>
                  <li><router-link to="privacy-policy">Privacy Policy</router-link></li>
                  <li><router-link to="support">Contact Us</router-link></li>
                </ul>
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
