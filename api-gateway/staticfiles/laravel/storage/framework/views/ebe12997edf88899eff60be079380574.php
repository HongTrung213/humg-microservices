<?php if(!Route::is(['index-two', 'index-three', 'index-four'])): ?>
    <!-- Footer -->
    <footer class="footer">

        <!-- Footer Top -->
        <div class="footer-top">
            <div class="container">
                <div class="row">
                    <div class="col-lg-4 col-md-6">

                        <!-- Footer Widget -->
                        <div class="footer-widget footer-about">
                            <div class="footer-logo">
                                <img src="<?php echo e(URL::asset('/assets/img/logo.svg')); ?>" alt="logo">
                            </div>
                            <div class="footer-about-content">
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat mauris Lorem
                                    ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat mauris</p>
                            </div>
                        </div>
                        <!-- /Footer Widget -->

                    </div>

                    <div class="col-lg-2 col-md-6">

                        <!-- Footer Widget -->
                        <div class="footer-widget footer-menu">
                            <h2 class="footer-title">For Instructor</h2>
                            <ul>
                                <li><a href="<?php echo e(url('instructor-profile')); ?>">Profile</a></li>
                                <li><a href="<?php echo e(url('login')); ?>">Login</a></li>
                                <li><a href="<?php echo e(url('register')); ?>">Register</a></li>
                                <li><a href="<?php echo e(url('instructor-list')); ?>">Instructor</a></li>
                                <li><a href="<?php echo e(url('deposit-instructor-dashboard')); ?>"> Dashboard</a></li>
                            </ul>
                        </div>
                        <!-- /Footer Widget -->

                    </div>

                    <div class="col-lg-2 col-md-6">

                        <!-- Footer Widget -->
                        <div class="footer-widget footer-menu">
                            <h2 class="footer-title">For Student</h2>
                            <ul>
                                <li><a href="<?php echo e(url('student-profile')); ?>">Profile</a></li>
                                <li><a href="<?php echo e(url('login')); ?>">Login</a></li>
                                <li><a href="<?php echo e(url('register')); ?>">Register</a></li>
                                <li><a href="<?php echo e(url('students-list')); ?>">Student</a></li>
                                <li><a href="<?php echo e(url('deposit-student-dashboard')); ?>"> Dashboard</a></li>
                            </ul>
                        </div>
                        <!-- /Footer Widget -->

                    </div>

                    <div class="col-lg-4 col-md-6">

                        <!-- Footer Widget -->
                        <div class="footer-widget footer-contact">
                            <h2 class="footer-title">News letter</h2>
                            <div class="news-letter">
                                <form>
                                    <input type="text" class="form-control" placeholder="Enter your email address"
                                        name="email">
                                </form>
                            </div>
                            <div class="footer-contact-info">
                                <div class="footer-address">
                                    <img src="<?php echo e(URL::asset('/assets/img/icon/icon-20.svg')); ?>" alt=""
                                        class="img-fluid">
                                    <p> 3556 Beech Street, San Francisco,<br> California, CA 94108 </p>
                                </div>
                                <p>
                                    <img src="<?php echo e(URL::asset('/assets/img/icon/icon-19.svg')); ?>" alt=""
                                        class="img-fluid">
                                    dreamslms@example.com
                                </p>
                                <p class="mb-0">
                                    <img src="<?php echo e(URL::asset('/assets/img/icon/icon-21.svg')); ?>" alt=""
                                        class="img-fluid">
                                    +19 123-456-7890
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
                        <div class="col-md-6">
                            <div class="privacy-policy">
                                <ul>
                                    <li><a href="<?php echo e(url('term-condition')); ?>">Terms</a></li>
                                    <li><a href="<?php echo e(url('privacy-policy')); ?>">Privacy</a></li>
                                </ul>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="copyright-text">
                                <p class="mb-0">&copy;
                                    <script>
                                        document.write(new Date().getFullYear())
                                    </script> DreamsLMS. All rights reserved.
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
<?php endif; ?>
<?php if(Route::is(['index-two'])): ?>
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
                                <img src="assets/img/logo.svg" alt="logo">
                            </div>
                            <div class="footer-about-content">
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat mauris Lorem
                                    ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat mauris</p>
                            </div>
                            <div class="social-icon">
                                <ul>
                                    <li>
                                        <a href="#" target="_blank"><i class="feather-facebook"></i></a>
                                    </li>
                                    <li>
                                        <a href="#" target="_blank"><i class="feather-twitter"></i></a>
                                    </li>
                                    <li>
                                        <a href="#" target="_blank"><i class="feather-instagram"></i></a>
                                    </li>
                                    <li>
                                        <a href="#" target="_blank"><i class="feather-linkedin"></i></a>
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
                                <li><a href="<?php echo e(url('instructor-profile')); ?>">Profile</a></li>
                                <li><a href="<?php echo e(url('login')); ?>">Login</a></li>
                                <li><a href="<?php echo e(url('register')); ?>">Register</a></li>
                                <li><a href="<?php echo e(url('instructor-list')); ?>">Instructor</a></li>
                                <li><a href="<?php echo e(url('deposit-instructor-dashboard')); ?>"> Dashboard</a></li>
                            </ul>
                        </div>
                        <!-- /Footer Widget -->

                    </div>

                    <div class="col-lg-2 col-md-6 col-sm-6 col-12">

                        <!-- Footer Widget -->
                        <div class="footer-widget footer-menu footer-menu-two">
                            <h2 class="footer-title">For Student</h2>
                            <ul>
                                <li><a href="<?php echo e(url('student-profile')); ?>">Profile</a></li>
                                <li><a href="<?php echo e(url('login')); ?>">Login</a></li>
                                <li><a href="<?php echo e(url('register')); ?>">Register</a></li>
                                <li><a href="<?php echo e(url('students-list')); ?>">Student</a></li>
                                <li><a href="<?php echo e(url('deposit-student-dashboard')); ?>"> Dashboard</a></li>
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
                                    <p> 3556 Beech Street, San Francisco,<br> California, CA 94108 </p>
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
                                <p class="mb-0">&copy;
                                    <script>
                                        document.write(new Date().getFullYear())
                                    </script> DreamsLMS. All rights reserved.
                                </p>
                            </div>
                        </div>
                        <div class="col-md-6 col-sm-12">
                            <div class="privacy-policy">
                                <ul>
                                    <li><a href="<?php echo e(url('term-condition')); ?>">Terms & Condition</a></li>
                                    <li><a href="<?php echo e(url('privacy-policy')); ?>">Privacy Policy</a></li>
                                    <li><a href="<?php echo e(url('support')); ?>">Contact Us</a></li>
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
<?php endif; ?>
<?php if(Route::is(['index-three'])): ?>
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
                                    <img class="img-fluid" src="<?php echo e(URL::asset('/assets/img/logo/logo.png')); ?>"
                                        alt="logo">
                                </div>
                                <div class="footer-three-about">
                                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sit nulla gravida ut
                                        elit arcu egestas felis. Scelerisque at in magna dolor massa ipsum arcu lacus.
                                        Lobortis posuere justo nunc diam ac massa. Maecenas tellus adipiscing ac fames
                                        ut ac posuere. Aliquam, integer proin hendrerit euismod et. </p>
                                </div>
                                <div class="newsletter-title">
                                    <h6>Get Updates</h6>
                                </div>
                                <div class="box-form-newsletter">
                                    <form class="form-newsletter">
                                        <input class="input-newsletter" type="text"
                                            placeholder="Enter your email here">
                                        <button class="btn btn-default font-heading icon-send-letter">Subscribe
                                            Now</button>
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
                                    <li><a href="<?php echo e(url('instructor-profile')); ?>">Profile</a></li>
                                    <li><a href="<?php echo e(url('login')); ?>">Login</a></li>
                                    <li><a href="<?php echo e(url('register')); ?>">Register</a></li>
                                    <li><a href="<?php echo e(url('instructor-list')); ?>">Instructor</a></li>
                                    <li><a href="<?php echo e(url('deposit-instructor-dashboard')); ?>"> Dashboard</a></li>
                                </ul>
                            </div>
                            <!-- /Footer Widget -->

                        </div>

                        <div class="col-lg-3 col-md-3 col-12">

                            <!-- Footer Widget -->
                            <div class="footer-widget-three footer-menu-three">
                                <h6 class="footer-three-title">For Student</h6>
                                <ul>
                                    <li><a href="<?php echo e(url('student-profile')); ?>">Profile</a></li>
                                    <li><a href="<?php echo e(url('login')); ?>">Login</a></li>
                                    <li><a href="<?php echo e(url('register')); ?>">Register</a></li>
                                    <li><a href="<?php echo e(url('students-list')); ?>">Student</a></li>
                                    <li><a href="<?php echo e(url('deposit-student-dashboard')); ?>"> Dashboard</a></li>
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
                                        <a href="#" target="_blank" class="feather-facebook-icon">
                                            <i class="feather-facebook"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#" target="_blank" class="feather-twitter-icon">
                                            <i class="feather-twitter"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#" target="_blank" class="feather-linkedin-icon">
                                            <i class="feather-linkedin"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#" target="_blank" class="feather-youtube-icon">
                                            <i class="feather-youtube"></i>
                                        </a>
                                    </li>
                                </ul>
                            </div>
                            <div class="privacy-policy-three">
                                <ul>
                                    <li><a href="<?php echo e(url('term-condition')); ?>">Terms & Condition</a></li>
                                    <li><a href="<?php echo e(url('privacy-policy')); ?>">Privacy Policy</a></li>
                                    <li><a href="<?php echo e(url('support')); ?>">Contact Us</a></li>
                                </ul>
                            </div>
                            <div class="copyright-text-three">
                                <p class="mb-0">&copy;
                                    <script>
                                        document.write(new Date().getFullYear())
                                    </script> DreamsLMS. All rights reserved.
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
<?php endif; ?>
<?php if(Route::is(['index-four'])): ?>
    <!-- Footer -->
    <footer class="footer footer-five">
        <!-- Footer Top -->
        <div class="footer-top-five">
            <div class="container">

                <div class="footer-five-left">
                    <img src="assets/img/bg/footer-left.svg" alt="">
                </div>

                <div class="row">

                    <div class="col-xl-4 col-lg-6 col-md-6 col-sm-12">

                        <!-- Footer Widget -->
                        <div class="footer-contact footer-menu-five">
                            <h2 class="footer-title footer-title-five">Get in touch</h2>
                            <div class="footer-contact-info">
                                <div class="footer-address">
                                    <span><i class="feather-map-pin"></i></span>
                                    <p> 3556 Beech Street, San Francisco,<br> California, CA 94108 </p>
                                </div>
                                <p class="mb-0">
                                    <span class="phone-icon"><i class="fa-solid fa-phone-volume"></i></span>
                                    +19 123-456-7890
                                </p>
                            </div>
                        </div>
                        <!-- /Footer Widget -->

                    </div>

                    <div class="col-lg-2 col-md-3 col-sm-12">

                        <!-- Footer Widget -->
                        <div class="footer-menu footer-menu-five">
                            <h2 class="footer-title footer-title-five"><i class="fa-sharp fa-solid fa-dash"></i>For
                                Instructor</h2>
                            <ul>
                                <li><a href="<?php echo e(url('instructor-profile')); ?>">Profile</a></li>
                                <li><a href="<?php echo e(url('login')); ?>">Login</a></li>
                                <li><a href="<?php echo e(url('register')); ?>">Register</a></li>
                                <li><a href="<?php echo e(url('instructor-list')); ?>">Instructor</a></li>
                                <li><a href="<?php echo e(url('deposit-instructor-dashboard')); ?>"> Dashboard</a></li>
                            </ul>
                        </div>
                        <!-- /Footer Widget -->

                    </div>

                    <div class="col-lg-2 col-md-3 col-sm-12">

                        <!-- Footer Widget -->
                        <div class="footer-menu footer-menu-five">
                            <h2 class="footer-title footer-title-five">For Student</h2>
                            <ul>
                                <li><a href="<?php echo e(url('student-profile')); ?>">Profile</a></li>
                                <li><a href="<?php echo e(url('login')); ?>">Login</a></li>
                                <li><a href="<?php echo e(url('register')); ?>">Register</a></li>
                                <li><a href="<?php echo e(url('students-list')); ?>">Student</a></li>
                                <li><a href="<?php echo e(url('deposit-student-dashboard')); ?>"> Dashboard</a></li>
                            </ul>
                        </div>
                        <!-- /Footer Widget -->

                    </div>

                    <div class="col-lg-4 col-md-6 col-sm-6 col-12">
                        <h2 class="footer-title footer-title-five">Get More Updates</h2>
                        <!-- Footer Widget -->
                        <div class="footer-widget-five">
                            <div class="footer-news-five">
                                <form>
                                    <div class="form-group mb-0">
                                        <input type="text" class="form-control"
                                            placeholder="Enter Your Email Address">
                                        <button type="submit" class="btn btn-one">Subscribe</button>
                                    </div>
                                </form>
                            </div>
                            <div class="footer-about-five">
                                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat mauris Lorem
                                    ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat mauris</p>
                            </div>
                        </div>
                        <!-- /Footer Widget -->

                    </div>

                </div>

                <div class="footer-five-right">
                    <img src="assets/img/bg/footer-right.svg" alt="">
                </div>

            </div>
        </div>
        <!-- /Footer Top -->

        <!-- Footer Bottom -->
        <div class="footer-bottom footer-bottom-five">
            <div class="container">

                <!-- Copyright -->
                <div class="copyright-five">
                    <div class="row align-items-center">
                        <div class="col-md-4">
                            <div class="footer-logo-five">
                                <a href="<?php echo e(url('index')); ?>">
                                    <img src="<?php echo e(URL::asset('/assets/img/logo/logo-five.svg')); ?>" class="img-fluid"
                                        alt="Footer Logo">
                                </a>

                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="copyright-text">
                                <p>&copy;
                                    <script>
                                        document.write(new Date().getFullYear())
                                    </script> DreamsLMS. All rights reserved.
                                </p>
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="social-icon-five">
                                <ul class="nav">
                                    <li>
                                        <a href="#" target="_blank" class="twitter-icon">
                                            <i class="fab fa-twitter"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#" target="_blank" class="linked-icon">
                                            <i class="fab fa-linkedin-in"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#" target="_blank" class="facebook-icon">
                                            <i class="fab fa-facebook-f"></i>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="#" target="_blank" class="youtube-icon">
                                            <i class="fab fa-youtube"></i>
                                        </a>
                                    </li>
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
<?php endif; ?>
<?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\dreams-lms_laravel\resources\views/layout/partials/footer.blade.php ENDPATH**/ ?>