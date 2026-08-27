<?php $page = 'dashboard-instructor'; ?>

<?php $__env->startSection('content'); ?>
    <?php $__env->startComponent('components.breadcrumb'); ?>
    <?php echo $__env->renderComponent(); ?>
    <!-- Instructor Dashboard -->
    <section class="page-content course-sec">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="card instructor-card">
                        <div class="card-header">
                            <h4>My Courses</h4>
                            <a href="<?php echo e(url('add-course')); ?>" class="btn btn-dark">Create New Course</a>
                        </div>
                        <div class="card-body">
                            <div class="instructor-grid">
                                <div class="product-img">
                                    <a href="<?php echo e(url('course-details')); ?>">
                                        <img src="<?php echo e(URL::asset('/assets/img/course/course-10.jpg')); ?>" class="img-fluid"
                                            alt="">
                                    </a>
                                </div>
                                <div class="instructor-product-content">
                                    <div class="head-course-title">
                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">Information About UI/UX
                                                Design Degree</a></h3>
                                    </div>
                                    <div class="course-info d-flex align-items-center border-bottom-0 pb-0">
                                        <div class="rating-img d-flex align-items-center">
                                            <img src="<?php echo e(URL::asset('/assets/img/icon/icon-01.svg')); ?>" alt="">
                                            <p>12+ Lesson</p>
                                        </div>
                                        <div class="course-view d-flex align-items-center">
                                            <img src="<?php echo e(URL::asset('/assets/img/icon/icon-02.svg')); ?>" alt="">
                                            <p>9hr 30min</p>
                                        </div>
                                    </div>
                                    <div class="rating mb-0">
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star"></i>
                                        <span class="d-inline-block average-rating"><span>4.0</span> (15)</span>
                                    </div>
                                </div>
                            </div>
                            <div class="instructor-grid">
                                <div class="product-img">
                                    <a href="<?php echo e(url('course-details')); ?>">
                                        <img src="<?php echo e(URL::asset('/assets/img/course/course-11.jpg')); ?>" class="img-fluid"
                                            alt="">
                                    </a>
                                </div>
                                <div class="instructor-product-content">
                                    <div class="head-course-title">
                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">Wordpress for Beginners -
                                                Master Wordpress Quickly</a></h3>
                                    </div>
                                    <div class="course-info d-flex align-items-center border-bottom-0 pb-0">
                                        <div class="rating-img d-flex align-items-center">
                                            <img src="<?php echo e(URL::asset('/assets/img/icon/icon-01.svg')); ?>" alt="">
                                            <p>10+ Lesson</p>
                                        </div>
                                        <div class="course-view d-flex align-items-center">
                                            <img src="<?php echo e(URL::asset('/assets/img/icon/icon-02.svg')); ?>" alt="">
                                            <p>7hr 20min</p>
                                        </div>
                                    </div>
                                    <div class="rating mb-0">
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star"></i>
                                        <span class="d-inline-block average-rating"><span>4.2</span> (20)</span>
                                    </div>
                                </div>
                            </div>
                            <div class="instructor-grid">
                                <div class="product-img">
                                    <a href="<?php echo e(url('course-details')); ?>">
                                        <img src="<?php echo e(URL::asset('/assets/img/course/course-12.jpg')); ?>" class="img-fluid"
                                            alt="">
                                    </a>
                                </div>
                                <div class="instructor-product-content">
                                    <div class="head-course-title">
                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">Sketch from A to Z (2023):
                                                Become an app designer</a></h3>
                                    </div>
                                    <div class="course-info d-flex align-items-center border-bottom-0 pb-0">
                                        <div class="rating-img d-flex align-items-center">
                                            <img src="<?php echo e(URL::asset('/assets/img/icon/icon-01.svg')); ?>" alt="">
                                            <p>05+ Lesson</p>
                                        </div>
                                        <div class="course-view d-flex align-items-center">
                                            <img src="<?php echo e(URL::asset('/assets/img/icon/icon-02.svg')); ?>" alt="">
                                            <p>8hr 00min</p>
                                        </div>
                                    </div>
                                    <div class="rating mb-0">
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star"></i>
                                        <span class="d-inline-block average-rating"><span>4.0</span> (10)</span>
                                    </div>
                                </div>
                            </div>
                            <div class="instructor-grid">
                                <div class="product-img">
                                    <a href="<?php echo e(url('course-details')); ?>">
                                        <img src="<?php echo e(URL::asset('/assets/img/course/course-13.jpg')); ?>" class="img-fluid"
                                            alt="">
                                    </a>
                                </div>
                                <div class="instructor-product-content">
                                    <div class="head-course-title">
                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">Learn Angular Fundamentals
                                                From beginning to advance lavel</a></h3>
                                    </div>
                                    <div class="course-info d-flex align-items-center border-bottom-0 pb-0">
                                        <div class="rating-img d-flex align-items-center">
                                            <img src="<?php echo e(URL::asset('/assets/img/icon/icon-01.svg')); ?>" alt="">
                                            <p>30+ Lesson</p>
                                        </div>
                                        <div class="course-view d-flex align-items-center">
                                            <img src="<?php echo e(URL::asset('/assets/img/icon/icon-02.svg')); ?>" alt="">
                                            <p>10hr 30min</p>
                                        </div>
                                    </div>
                                    <div class="rating mb-0">
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star"></i>
                                        <span class="d-inline-block average-rating"><span>4.3</span> (25)</span>
                                    </div>
                                </div>
                            </div>
                            <div class="instructor-grid">
                                <div class="product-img">
                                    <a href="<?php echo e(url('course-details')); ?>">
                                        <img src="<?php echo e(URL::asset('/assets/img/course/course-14.jpg')); ?>" class="img-fluid"
                                            alt="">
                                    </a>
                                </div>
                                <div class="instructor-product-content">
                                    <div class="head-course-title">
                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">Build Responsive Real
                                                World Websites with HTML5 and CSS3</a></h3>
                                    </div>
                                    <div class="course-info d-flex align-items-center border-bottom-0 pb-0">
                                        <div class="rating-img d-flex align-items-center">
                                            <img src="<?php echo e(URL::asset('/assets/img/icon/icon-01.svg')); ?>" alt="">
                                            <p>20+ Lesson</p>
                                        </div>
                                        <div class="course-view d-flex align-items-center">
                                            <img src="<?php echo e(URL::asset('/assets/img/icon/icon-02.svg')); ?>" alt="">
                                            <p>7hr 00min</p>
                                        </div>
                                    </div>
                                    <div class="rating mb-0">
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star"></i>
                                        <span class="d-inline-block average-rating"><span>4.0</span> (15)</span>
                                    </div>
                                </div>
                            </div>
                            <div class="instructor-grid mb-0">
                                <div class="product-img">
                                    <a href="<?php echo e(url('course-details')); ?>">
                                        <img src="<?php echo e(URL::asset('/assets/img/course/course-15.jpg')); ?>" class="img-fluid"
                                            alt="">
                                    </a>
                                </div>
                                <div class="instructor-product-content">
                                    <div class="head-course-title">
                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">C# Developers Double
                                                Your Coding Speed with Visual Studio</a></h3>
                                    </div>
                                    <div class="course-info d-flex align-items-center border-bottom-0 pb-0">
                                        <div class="rating-img d-flex align-items-center">
                                            <img src="<?php echo e(URL::asset('/assets/img/icon/icon-01.svg')); ?>" alt="">
                                            <p>50+ Lesson</p>
                                        </div>
                                        <div class="course-view d-flex align-items-center">
                                            <img src="<?php echo e(URL::asset('/assets/img/icon/icon-02.svg')); ?>" alt="">
                                            <p>10hr 30min</p>
                                        </div>
                                    </div>
                                    <div class="rating mb-0">
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star filled"></i>
                                        <i class="fas fa-star"></i>
                                        <span class="d-inline-block average-rating"><span>4.5</span> (30)</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- /Instructor Dashboard -->
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\dreams-lms_laravel\resources\views/dashboard-instructor.blade.php ENDPATH**/ ?>