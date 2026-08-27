<?php $page = 'wishlist'; ?>

<?php $__env->startSection('content'); ?>
    <?php $__env->startComponent('components.breadcrumb'); ?>
        <?php $__env->slot('title'); ?>
            Home
        <?php $__env->endSlot(); ?>
        <?php $__env->slot('li1'); ?>
            Pages
        <?php $__env->endSlot(); ?>
        <?php $__env->slot('li2'); ?>
            Wishlists
        <?php $__env->endSlot(); ?>
    <?php echo $__env->renderComponent(); ?>
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
                                                <a href="<?php echo e(url('course-details')); ?>">
                                                    <img alt=""
                                                        src="<?php echo e(URL::asset('/assets/img/course/course-01.jpg')); ?>">
                                                </a>
                                                <div class="price-amt">
                                                    <h4>$300</h4>
                                                </div>
                                            </div>
                                            <div class="wishlist-info">
                                                <h5><a href="<?php echo e(url('course-details')); ?>">Information About UI/UX Design
                                                        Degree</a></h5>
                                                <div class="course-info d-flex align-items-center border-bottom-0 pb-0">
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
                                                <a href="<?php echo e(url('course-details')); ?>">
                                                    <img alt=""
                                                        src="<?php echo e(URL::asset('/assets/img/course/course-02.jpg')); ?>">
                                                </a>
                                                <div class="price-amt">
                                                    <h4>$300</h4>
                                                </div>
                                            </div>
                                            <div class="wishlist-info">
                                                <h5><a href="<?php echo e(url('course-details')); ?>">Wordpress for Beginners - Master
                                                        Wordpress Quickly</a></h5>
                                                <div class="course-info d-flex align-items-center border-bottom-0 pb-0">
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
                                                <a href="<?php echo e(url('course-details')); ?>">
                                                    <img alt=""
                                                        src="<?php echo e(URL::asset('/assets/img/course/course-03.jpg')); ?>">
                                                </a>
                                                <div class="price-amt">
                                                    <h4>$300</h4>
                                                </div>
                                            </div>
                                            <div class="wishlist-info">
                                                <h5><a href="<?php echo e(url('course-details')); ?>">Sketch from A to Z (2023): Become
                                                        an app designer</a></h5>
                                                <div class="course-info d-flex align-items-center border-bottom-0 pb-0">
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
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/wishlist.blade.php ENDPATH**/ ?>