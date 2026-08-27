<?php $page = 'course-grid'; ?>

<?php $__env->startSection('content'); ?>
    <?php $__env->startComponent('components.breadcrumb'); ?>
        <?php $__env->slot('title'); ?>
            Home
        <?php $__env->endSlot(); ?>
        <?php $__env->slot('li1'); ?>
            Courses
        <?php $__env->endSlot(); ?>
        <?php $__env->slot('li2'); ?>
            All Courses
        <?php $__env->endSlot(); ?>
    <?php echo $__env->renderComponent(); ?>
    <!-- Course -->
    <section class="course-content">
        <div class="container">
            <div class="row">
                <div class="col-lg-9">
                    <?php $__env->startComponent('components.filter'); ?>
                    <?php echo $__env->renderComponent(); ?>
                    <div class="row">
                        <div class="col-lg-4 col-md-6 d-flex">
                            <div class="course-box course-design d-flex ">
                                <div class="product">
                                    <div class="product-img">
                                        <a href="<?php echo e(url('course-details')); ?>">
                                            <img class="img-fluid" alt=""
                                                src="<?php echo e(URL::asset('/assets/img/course/course-10.jpg')); ?>">
                                        </a>
                                        <div class="price">
                                            <h3>$300 <span>$99.00</span></h3>
                                        </div>
                                    </div>
                                    <div class="product-content">
                                        <div class="course-group d-flex">
                                            <div class="course-group-img d-flex">
                                                <a href="<?php echo e(url('instructor-profile')); ?>"><img
                                                        src="<?php echo e(URL::asset('/assets/img/user/user1.jpg')); ?>" alt=""
                                                        class="img-fluid"></a>
                                                <div class="course-name">
                                                    <h4><a href="<?php echo e(url('instructor-profile')); ?>">Rolands R</a></h4>
                                                    <p>Instructor</p>
                                                </div>
                                            </div>
                                            <div class="course-share d-flex align-items-center justify-content-center">
                                                <a href="#rate"><i class="fa-regular fa-heart"></i></a>
                                            </div>
                                        </div>
                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">Information About UI/UX
                                                Design Degree</a></h3>
                                        <div class="course-info d-flex align-items-center">
                                            <div class="rating-img d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-01.svg')); ?>" alt="">
                                                <p>12+ Lesson</p>
                                            </div>
                                            <div class="course-view d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-02.svg')); ?>" alt="">
                                                <p>9hr 30min</p>
                                            </div>
                                        </div>
                                        <div class="rating">
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star"></i>
                                            <span class="d-inline-block average-rating"><span>4.0</span> (15)</span>
                                        </div>
                                        <div class="all-btn all-category d-flex align-items-center">
                                            <a href="<?php echo e(url('checkout')); ?>" class="btn btn-primary">BUY NOW</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 d-flex">
                            <div class="course-box course-design d-flex ">
                                <div class="product">
                                    <div class="product-img">
                                        <a href="<?php echo e(url('course-details')); ?>">
                                            <img class="img-fluid" alt=""
                                                src="<?php echo e(URL::asset('/assets/img/course/course-11.jpg')); ?>">
                                        </a>
                                        <div class="price">
                                            <h3>$200 <span>$99.00</span></h3>
                                        </div>
                                    </div>
                                    <div class="product-content">
                                        <div class="course-group d-flex">
                                            <div class="course-group-img d-flex">
                                                <a href="<?php echo e(url('instructor-profile')); ?>"><img
                                                        src="<?php echo e(URL::asset('/assets/img/user/user2.jpg')); ?>" alt=""
                                                        class="img-fluid"></a>
                                                <div class="course-name">
                                                    <h4><a href="<?php echo e(url('instructor-profile')); ?>">Jenis R.</a></h4>
                                                    <p>Instructor</p>
                                                </div>
                                            </div>
                                            <div class="course-share d-flex align-items-center justify-content-center">
                                                <a href="#rate"><i class="fa-regular fa-heart"></i></a>
                                            </div>
                                        </div>
                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">Wordpress for Beginners -
                                                Master Wordpress Quickly</a></h3>
                                        <div class="course-info d-flex align-items-center">
                                            <div class="rating-img d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-01.svg')); ?>" alt="">
                                                <p>12+ Lesson</p>
                                            </div>
                                            <div class="course-view d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-02.svg')); ?>" alt="">
                                                <p>9hr 30min</p>
                                            </div>
                                        </div>
                                        <div class="rating">
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <span class="d-inline-block average-rating"><span>5.0</span> (15)</span>
                                        </div>
                                        <div class="all-btn all-category d-flex align-items-center">
                                            <a href="<?php echo e(url('checkout')); ?>" class="btn btn-primary">BUY NOW</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 d-flex">
                            <div class="course-box course-design d-flex ">
                                <div class="product">
                                    <div class="product-img">
                                        <a href="<?php echo e(url('course-details')); ?>">
                                            <img class="img-fluid" alt=""
                                                src="<?php echo e(URL::asset('/assets/img/course/course-12.jpg')); ?>">
                                        </a>
                                        <div class="price">
                                            <h3 class="free-color">FREE</h3>
                                        </div>
                                    </div>
                                    <div class="product-content">
                                        <div class="course-group d-flex">
                                            <div class="course-group-img d-flex">
                                                <a href="<?php echo e(url('instructor-profile')); ?>"><img
                                                        src="<?php echo e(URL::asset('/assets/img/user/user3.jpg')); ?>"
                                                        alt="" class="img-fluid"></a>
                                                <div class="course-name">
                                                    <h4><a href="<?php echo e(url('instructor-profile')); ?>">Jesse Stevens</a></h4>
                                                    <p>Instructor</p>
                                                </div>
                                            </div>
                                            <div class="course-share d-flex align-items-center justify-content-center">
                                                <a href="#rate"><i class="fa-regular fa-heart"></i></a>
                                            </div>
                                        </div>
                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">Sketch from A to Z
                                                (2023): Become an app designer</a></h3>
                                        <div class="course-info d-flex align-items-center">
                                            <div class="rating-img d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-01.svg')); ?>"
                                                    alt="">
                                                <p>12+ Lesson</p>
                                            </div>
                                            <div class="course-view d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-02.svg')); ?>"
                                                    alt="">
                                                <p>9hr 30min</p>
                                            </div>
                                        </div>
                                        <div class="rating">
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star"></i>
                                            <span class="d-inline-block average-rating"><span>4.0</span> (15)</span>
                                        </div>
                                        <div class="all-btn all-category d-flex align-items-center">
                                            <a href="<?php echo e(url('checkout')); ?>" class="btn btn-primary">BUY NOW</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 d-flex">
                            <div class="course-box course-design d-flex ">
                                <div class="product">
                                    <div class="product-img">
                                        <a href="<?php echo e(url('course-details')); ?>">
                                            <img class="img-fluid" alt=""
                                                src="<?php echo e(URL::asset('/assets/img/course/course-13.jpg')); ?>">
                                        </a>
                                        <div class="price">
                                            <h3 class="free-color">FREE</h3>
                                        </div>
                                    </div>
                                    <div class="product-content">
                                        <div class="course-group d-flex">
                                            <div class="course-group-img d-flex">
                                                <a href="<?php echo e(url('instructor-profile')); ?>"><img
                                                        src="<?php echo e(URL::asset('/assets/img/user/user4.jpg')); ?>"
                                                        alt="" class="img-fluid"></a>
                                                <div class="course-name">
                                                    <h4><a href="<?php echo e(url('instructor-profile')); ?>">Nicole Brown</a></h4>
                                                    <p>Instructor</p>
                                                </div>
                                            </div>
                                            <div class="course-share d-flex align-items-center justify-content-center">
                                                <a href="#rate" class="active-heart"><i
                                                        class="fa-regular fa-heart"></i></a>
                                            </div>
                                        </div>
                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">Learn Angular
                                                Fundamentals From ...</a></h3>
                                        <div class="course-info d-flex align-items-center">
                                            <div class="rating-img d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-01.svg')); ?>"
                                                    alt="">
                                                <p>12+ Lesson</p>
                                            </div>
                                            <div class="course-view d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-02.svg')); ?>"
                                                    alt="">
                                                <p>9hr 30min</p>
                                            </div>
                                        </div>
                                        <div class="rating">
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <span class="d-inline-block average-rating"><span>5.0</span> (15)</span>
                                        </div>
                                        <div class="all-btn all-category d-flex align-items-center">
                                            <a href="<?php echo e(url('checkout')); ?>" class="btn btn-primary">BUY NOW</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 d-flex">
                            <div class="course-box course-design d-flex ">
                                <div class="product">
                                    <div class="product-img">
                                        <a href="<?php echo e(url('course-details')); ?>">
                                            <img class="img-fluid" alt=""
                                                src="<?php echo e(URL::asset('/assets/img/course/course-14.jpg')); ?>">
                                        </a>
                                        <div class="price">
                                            <h3>$29.99</h3>
                                        </div>
                                    </div>
                                    <div class="product-content">
                                        <div class="course-group d-flex">
                                            <div class="course-group-img d-flex">
                                                <a href="<?php echo e(url('instructor-profile')); ?>"><img
                                                        src="<?php echo e(URL::asset('/assets/img/user/user5.jpg')); ?>"
                                                        alt="" class="img-fluid"></a>
                                                <div class="course-name">
                                                    <h4><a href="<?php echo e(url('instructor-profile')); ?>">John Smith</a></h4>
                                                    <p>Instructor</p>
                                                </div>
                                            </div>
                                            <div class="course-share d-flex align-items-center justify-content-center">
                                                <a href="#rate" class="active-heart"><i
                                                        class="fa-regular fa-heart"></i></a>
                                            </div>
                                        </div>
                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">Build Responsive Real
                                                World Websites with ...</a></h3>
                                        <div class="course-info d-flex align-items-center">
                                            <div class="rating-img d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-01.svg')); ?>"
                                                    alt="">
                                                <p>12+ Lesson</p>
                                            </div>
                                            <div class="course-view d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-02.svg')); ?>"
                                                    alt="">
                                                <p>9hr 30min</p>
                                            </div>
                                        </div>
                                        <div class="rating">
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star"></i>
                                            <span class="d-inline-block average-rating"><span>4.0</span> (15)</span>
                                        </div>
                                        <div class="all-btn all-category d-flex align-items-center">
                                            <a href="<?php echo e(url('checkout')); ?>" class="btn btn-primary">BUY NOW</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 d-flex">
                            <div class="course-box course-design d-flex ">
                                <div class="product">
                                    <div class="product-img">
                                        <a href="<?php echo e(url('course-details')); ?>">
                                            <img class="img-fluid" alt=""
                                                src="<?php echo e(URL::asset('/assets/img/course/course-15.jpg')); ?>">
                                        </a>
                                        <div class="price">
                                            <h3>$300 <span>$99.00</span></h3>
                                        </div>
                                    </div>
                                    <div class="product-content">
                                        <div class="course-group d-flex">
                                            <div class="course-group-img d-flex">
                                                <a href="<?php echo e(url('instructor-profile')); ?>"><img
                                                        src="<?php echo e(URL::asset('/assets/img/user/user6.jpg')); ?>"
                                                        alt="" class="img-fluid"></a>
                                                <div class="course-name">
                                                    <h4><a href="<?php echo e(url('instructor-profile')); ?>">Stella Johnson</a></h4>
                                                    <p>Instructor</p>
                                                </div>
                                            </div>
                                            <div class="course-share d-flex align-items-center justify-content-center">
                                                <a href="#rate" class="active-heart"><i
                                                        class="fa-regular fa-heart"></i></a>
                                            </div>
                                        </div>
                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">C# Developers Double
                                                Your Coding Speed with ...</a></h3>
                                        <div class="course-info d-flex align-items-center">
                                            <div class="rating-img d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-01.svg')); ?>"
                                                    alt="">
                                                <p>12+ Lesson</p>
                                            </div>
                                            <div class="course-view d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-02.svg')); ?>"
                                                    alt="">
                                                <p>9hr 30min</p>
                                            </div>
                                        </div>
                                        <div class="rating">
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <span class="d-inline-block average-rating"><span>5.0</span> (15)</span>
                                        </div>
                                        <div class="all-btn all-category d-flex align-items-center">
                                            <a href="<?php echo e(url('checkout')); ?>" class="btn btn-primary">BUY NOW</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 d-flex">
                            <div class="course-box course-design d-flex ">
                                <div class="product">
                                    <div class="product-img">
                                        <a href="<?php echo e(url('course-details')); ?>">
                                            <img class="img-fluid" alt=""
                                                src="<?php echo e(URL::asset('/assets/img/course/course-16.jpg')); ?>">
                                        </a>
                                        <div class="price">
                                            <h3>$200 <span>$99.00</span></h3>
                                        </div>
                                    </div>
                                    <div class="product-content">
                                        <div class="course-group d-flex">
                                            <div class="course-group-img d-flex">
                                                <a href="<?php echo e(url('instructor-profile')); ?>"><img
                                                        src="<?php echo e(URL::asset('/assets/img/user/user.jpg')); ?>"
                                                        alt="" class="img-fluid"></a>
                                                <div class="course-name">
                                                    <h4><a href="<?php echo e(url('instructor-profile')); ?>">John Michael</a></h4>
                                                    <p>Instructor</p>
                                                </div>
                                            </div>
                                            <div class="course-share d-flex align-items-center justify-content-center">
                                                <a href="#rate"><i class="fa-regular fa-heart"></i></a>
                                            </div>
                                        </div>
                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">Learn JavaScript and
                                                Express to become a...</a></h3>
                                        <div class="course-info d-flex align-items-center">
                                            <div class="rating-img d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-01.svg')); ?>"
                                                    alt="">
                                                <p>12+ Lesson</p>
                                            </div>
                                            <div class="course-view d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-02.svg')); ?>"
                                                    alt="">
                                                <p>9hr 30min</p>
                                            </div>
                                        </div>
                                        <div class="rating">
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star"></i>
                                            <span class="d-inline-block average-rating"><span>4.0</span> (15)</span>
                                        </div>
                                        <div class="all-btn all-category d-flex align-items-center">
                                            <a href="<?php echo e(url('checkout')); ?>" class="btn btn-primary">BUY NOW</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 d-flex">
                            <div class="course-box course-design d-flex ">
                                <div class="product">
                                    <div class="product-img">
                                        <a href="<?php echo e(url('course-details')); ?>">
                                            <img class="img-fluid" alt=""
                                                src="<?php echo e(URL::asset('/assets/img/course/course-13.jpg')); ?>">
                                        </a>
                                        <div class="price">
                                            <h3>$300 <span>$99.00</span></h3>
                                        </div>
                                    </div>
                                    <div class="product-content">
                                        <div class="course-group d-flex">
                                            <div class="course-group-img d-flex">
                                                <a href="<?php echo e(url('instructor-profile')); ?>"><img
                                                        src="<?php echo e(URL::asset('/assets/img/user/user4.jpg')); ?>"
                                                        alt="" class="img-fluid"></a>
                                                <div class="course-name">
                                                    <h4><a href="<?php echo e(url('instructor-profile')); ?>">Jesse Stevens</a></h4>
                                                    <p>Instructor</p>
                                                </div>
                                            </div>
                                            <div class="course-share d-flex align-items-center justify-content-center">
                                                <a href="#rate"><i class="fa-regular fa-heart"></i></a>
                                            </div>
                                        </div>
                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">Learn and Understand
                                                AngularJS to become a ...</a></h3>
                                        <div class="course-info d-flex align-items-center">
                                            <div class="rating-img d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-01.svg')); ?>"
                                                    alt="">
                                                <p>12+ Lesson</p>
                                            </div>
                                            <div class="course-view d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-02.svg')); ?>"
                                                    alt="">
                                                <p>9hr 30min</p>
                                            </div>
                                        </div>
                                        <div class="rating">
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <span class="d-inline-block average-rating"><span>5.0</span> (15)</span>
                                        </div>
                                        <div class="all-btn all-category d-flex align-items-center">
                                            <a href="<?php echo e(url('checkout')); ?>" class="btn btn-primary">BUY NOW</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-4 col-md-6 d-flex">
                            <div class="course-box course-design d-flex ">
                                <div class="product">
                                    <div class="product-img">
                                        <a href="<?php echo e(url('course-details')); ?>">
                                            <img class="img-fluid" alt=""
                                                src="<?php echo e(URL::asset('/assets/img/course/course-17.jpg')); ?>">
                                        </a>
                                        <div class="price">
                                            <h3 class="free-color">FREE</h3>
                                        </div>
                                    </div>
                                    <div class="product-content">
                                        <div class="course-group d-flex">
                                            <div class="course-group-img d-flex">
                                                <a href="<?php echo e(url('instructor-profile')); ?>"><img
                                                        src="<?php echo e(URL::asset('/assets/img/user/user6.jpg')); ?>"
                                                        alt="" class="img-fluid"></a>
                                                <div class="course-name">
                                                    <h4><a href="<?php echo e(url('instructor-profile')); ?>">Monroe Parker</a></h4>
                                                    <p>Instructor</p>
                                                </div>
                                            </div>
                                            <div class="course-share d-flex align-items-center justify-content-center">
                                                <a href="#rate"><i class="fa-regular fa-heart"></i></a>
                                            </div>
                                        </div>
                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">Responsive Web Design
                                                Essentials HTML5 CSS3 ...</a></h3>
                                        <div class="course-info d-flex align-items-center">
                                            <div class="rating-img d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-01.svg')); ?>"
                                                    alt="">
                                                <p>12+ Lesson</p>
                                            </div>
                                            <div class="course-view d-flex align-items-center">
                                                <img src="<?php echo e(URL::asset('/assets/img/icon/icon-02.svg')); ?>"
                                                    alt="">
                                                <p>9hr 30min</p>
                                            </div>
                                        </div>
                                        <div class="rating">
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star"></i>
                                            <span class="d-inline-block average-rating"><span>4.0</span> (15)</span>
                                        </div>
                                        <div class="all-btn all-category d-flex align-items-center">
                                            <a href="<?php echo e(url('checkout')); ?>" class="btn btn-primary">BUY NOW</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <?php $__env->startComponent('components.pagination'); ?>
                    <?php echo $__env->renderComponent(); ?>

                </div>
                <div class="col-lg-3 theiaStickySidebar">
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
                                            <input type="checkbox" name="select_specialist">
                                            <span class="checkmark"></span> Backend (3)

                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist">
                                            <span class="checkmark"></span> CSS (2)
                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist">
                                            <span class="checkmark"></span> Frontend (2)
                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist" checked>
                                            <span class="checkmark"></span> General (2)
                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist" checked>
                                            <span class="checkmark"></span> IT & Software (2)
                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist">
                                            <span class="checkmark"></span> Photography (2)
                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist">
                                            <span class="checkmark"></span> Programming Language (3)
                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check mb-0">
                                            <input type="checkbox" name="select_specialist">
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
                                            <input type="checkbox" name="select_specialist">
                                            <span class="checkmark"></span> Keny White (10)

                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist">
                                            <span class="checkmark"></span> Hinata Hyuga (5)
                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist">
                                            <span class="checkmark"></span> John Doe (3)
                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check mb-0">
                                            <input type="checkbox" name="select_specialist" checked>
                                            <span class="checkmark"></span> Nicole Brown
                                        </label>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- /Search Filter -->

                        <!-- Search Filter -->
                        <div class="card search-filter ">
                            <div class="card-body">
                                <div class="filter-widget mb-0">
                                    <div class="categories-head d-flex align-items-center">
                                        <h4>Price</h4>
                                        <i class="fas fa-angle-down"></i>
                                    </div>
                                    <div>
                                        <label class="custom_check custom_one">
                                            <input type="radio" name="select_specialist">
                                            <span class="checkmark"></span> All (18)

                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check custom_one">
                                            <input type="radio" name="select_specialist">
                                            <span class="checkmark"></span> Free (3)

                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check custom_one mb-0">
                                            <input type="radio" name="select_specialist" checked>
                                            <span class="checkmark"></span> Paid (15)
                                        </label>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- /Search Filter -->

                        <!-- Latest Posts -->
                        <div class="card post-widget ">
                            <div class="card-body">
                                <div class="latest-head">
                                    <h4 class="card-title">Latest Courses</h4>
                                </div>
                                <ul class="latest-posts">
                                    <li>
                                        <div class="post-thumb">
                                            <a href="<?php echo e(url('course-details')); ?>">
                                                <img class="img-fluid"
                                                    src="<?php echo e(URL::asset('/assets/img/blog/blog-01.jpg')); ?>"
                                                    alt="">
                                            </a>
                                        </div>
                                        <div class="post-info free-color">
                                            <h4>
                                                <a href="<?php echo e(url('course-details')); ?>">Introduction LearnPress – LMS
                                                    plugin</a>
                                            </h4>
                                            <p>FREE</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="post-thumb">
                                            <a href="<?php echo e(url('course-details')); ?>">
                                                <img class="img-fluid"
                                                    src="<?php echo e(URL::asset('/assets/img/blog/blog-02.jpg')); ?>"
                                                    alt="">
                                            </a>
                                        </div>
                                        <div class="post-info">
                                            <h4>
                                                <a href="<?php echo e(url('course-details')); ?>">Become a PHP Master and Make
                                                    Money</a>
                                            </h4>
                                            <p>$200</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="post-thumb">
                                            <a href="<?php echo e(url('course-details')); ?>">
                                                <img class="img-fluid"
                                                    src="<?php echo e(URL::asset('/assets/img/blog/blog-03.jpg')); ?>"
                                                    alt="">
                                            </a>
                                        </div>
                                        <div class="post-info free-color">
                                            <h4>
                                                <a href="<?php echo e(url('course-details')); ?>">Learning jQuery Mobile for
                                                    Beginners</a>
                                            </h4>
                                            <p>FREE</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="post-thumb">
                                            <a href="<?php echo e(url('course-details')); ?>">
                                                <img class="img-fluid"
                                                    src="<?php echo e(URL::asset('/assets/img/blog/blog-01.jpg')); ?>"
                                                    alt="">
                                            </a>
                                        </div>
                                        <div class="post-info">
                                            <h4>
                                                <a href="<?php echo e(url('course-details')); ?>">Improve Your CSS Workflow with
                                                    SASS</a>
                                            </h4>
                                            <p>$200</p>
                                        </div>
                                    </li>
                                    <li>
                                        <div class="post-thumb ">
                                            <a href="<?php echo e(url('course-details')); ?>">
                                                <img class="img-fluid"
                                                    src="<?php echo e(URL::asset('/assets/img/blog/blog-02.jpg')); ?>"
                                                    alt="">
                                            </a>
                                        </div>
                                        <div class="post-info free-color">
                                            <h4>
                                                <a href="<?php echo e(url('course-details')); ?>">HTML5/CSS3 Essentials in 4-Hours</a>
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
        </div>
    </section>
    <!-- /Course -->
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/course-grid.blade.php ENDPATH**/ ?>