<template>
<!-- Footer Top -->
<div class="footer-top">
    <div class="container">
        <div class="row">
            <div class="col-lg-4 col-md-6">
            
                <!-- Footer Widget -->
                <div class="footer-widget footer-about">
                    <div class="footer-logo">
                        <img src="@/assets/img/logo.svg" alt="logo">
                    </div>
                    <div class="footer-about-content">
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat mauris Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consequat mauris</p>
                    </div>
                </div>
                <!-- /Footer Widget -->
                
            </div>
            
            <div class="col-lg-2 col-md-6">
            
                <!-- Footer Widget -->
                <div class="footer-widget footer-menu">
                    <h2 class="footer-title">For Instructor</h2>
                    <ul>
                        <li><router-link to="instructor-profile">Profile</router-link></li>
                        <li><router-link to="login">Login</router-link></li>
                        <li><router-link to="register">Register</router-link></li>
                        <li><router-link to="instructor-list">Instructor</router-link></li>
                        <li><router-link to="deposit-instructor-dashboard"> Dashboard</router-link></li>
                    </ul>
                </div>
                <!-- /Footer Widget -->
                
            </div>
            
            <div class="col-lg-2 col-md-6">
            
                <!-- Footer Widget -->
                <div class="footer-widget footer-menu">
                    <h2 class="footer-title">For Student</h2>
                    <ul>
                        <li><router-link to="student-profile">Profile</router-link></li>
                        <li><router-link to="login">Login</router-link></li>
                        <li><router-link to="register">Register</router-link></li>
                        <li><router-link to="students-list">Student</router-link></li>
                        <li><router-link to="deposit-student-dashboard"> Dashboard</router-link></li>
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
                            <input type="text" class="form-control" placeholder="Enter your email address" name="email">
                        </form>
                    </div>
                    <div class="footer-contact-info">
                        <div class="footer-address">
                            <img src="@/assets/img/icon/icon-20.svg" alt="" class="img-fluid">
                            <p> 3556  Beech Street, San Francisco,<br> California, CA 94108 </p>
                        </div>
                        <p>
                            <img src="@/assets/img/icon/icon-19.svg" alt="" class="img-fluid">
                            dreamslms@example.com
                        </p>
                        <p class="mb-0">
                            <img src="@/assets/img/icon/icon-21.svg" alt="" class="img-fluid">
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
</template>