<?php $page = 'cart'; ?>

<?php $__env->startSection('content'); ?>
    <?php $__env->startComponent('components.breadcrumb'); ?>
        <?php $__env->slot('title'); ?>
            Home
        <?php $__env->endSlot(); ?>
        <?php $__env->slot('li1'); ?>
            Pages
        <?php $__env->endSlot(); ?>
        <?php $__env->slot('li2'); ?>
            Cart
        <?php $__env->endSlot(); ?>
    <?php echo $__env->renderComponent(); ?>
    <!-- Cart -->
    <section class="course-content cart-widget">
        <div class="container">
            <div class="student-widget">
                <div class="student-widget-group">
                    <div class="row">
                        <div class="col-lg-12">
                            <div class="cart-head">
                                <h4>Your cart (03 items)</h4>
                            </div>
                            <div class="cart-group">
                                <div class="row">
                                    <div class="col-lg-12 col-md-12 d-flex">
                                        <div class="course-box course-design list-course d-flex">
                                            <div class="product">
                                                <div class="product-img">
                                                    <a href="<?php echo e(url('course-details')); ?>">
                                                        <img class="img-fluid" alt=""
                                                            src="<?php echo e(URL::asset('/assets/img/course/course-10.jpg')); ?>">
                                                    </a>
                                                    <div class="price">
                                                        <h3 class="free-color">FREE</h3>
                                                    </div>
                                                </div>
                                                <div class="product-content">
                                                    <div class="head-course-title">
                                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">Information
                                                                About UI/UX Design Degree</a></h3>
                                                    </div>
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
                                                        <span class="d-inline-block average-rating"><span>4.0</span>
                                                            (15)</span>
                                                    </div>
                                                </div>
                                                <div class="cart-remove">
                                                    <a href="javascript:;" class="btn btn-primary">Remove</a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-lg-12 col-md-12 d-flex">
                                        <div class="course-box course-design list-course d-flex ">
                                            <div class="product">
                                                <div class="product-img">
                                                    <a href="<?php echo e(url('course-details')); ?>">
                                                        <img class="img-fluid" alt=""
                                                            src="<?php echo e(URL::asset('/assets/img/course/course-11.jpg')); ?>">
                                                    </a>
                                                    <div class="price">
                                                        <h3>$300 <span>$99.00</span></h3>
                                                    </div>
                                                </div>
                                                <div class="product-content">
                                                    <div class="head-course-title">
                                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">Wordpress
                                                                for Beginners - Master Wordpress Quickly</a></h3>
                                                    </div>
                                                    <div class="course-info d-flex align-items-center border-bottom-0 pb-0">
                                                        <div class="rating-img d-flex align-items-center">
                                                            <img src="<?php echo e(URL::asset('/assets/img/icon/icon-01.svg')); ?>"
                                                                alt="">
                                                            <p>10+ Lesson</p>
                                                        </div>
                                                        <div class="course-view d-flex align-items-center">
                                                            <img src="<?php echo e(URL::asset('/assets/img/icon/icon-02.svg')); ?>"
                                                                alt="">
                                                            <p>7hr 20min</p>
                                                        </div>
                                                    </div>
                                                    <div class="rating">
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star"></i>
                                                        <span class="d-inline-block average-rating"><span>4.2</span>
                                                            (15)</span>
                                                    </div>
                                                </div>
                                                <div class="cart-remove">
                                                    <a href="javascript:;" class="btn btn-primary">Remove</a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-lg-12 col-md-12 d-flex">
                                        <div class="course-box course-design list-course d-flex mb-0">
                                            <div class="product">
                                                <div class="product-img">
                                                    <a href="<?php echo e(url('course-details')); ?>">
                                                        <img class="img-fluid" alt=""
                                                            src="<?php echo e(URL::asset('/assets/img/course/course-12.jpg')); ?>">
                                                    </a>
                                                    <div class="price">
                                                        <h3>$300 <span>$99.00</span></h3>
                                                    </div>
                                                </div>
                                                <div class="product-content">
                                                    <div class="head-course-title">
                                                        <h3 class="title"><a href="<?php echo e(url('course-details')); ?>">Sketch
                                                                from A to Z (2023): Become an app designer</a></h3>
                                                    </div>
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
                                                        <span class="d-inline-block average-rating"><span>4.0</span>
                                                            (15)</span>
                                                    </div>
                                                </div>
                                                <div class="cart-remove">
                                                    <a href="javascript:;" class="btn btn-primary">Remove</a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="cart-total">
                                <div class="row">
                                    <div class="col-lg-12 col-md-12">
                                        <div class="cart-subtotal">
                                            <p>Subtotal <span>$600.00</span></p>
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-md-6">
                                        <div class="check-outs">
                                            <a href="<?php echo e(url('checkout')); ?>" class="btn btn-primary">Checkout</a>
                                        </div>
                                    </div>
                                    <div class="col-lg-6 col-md-6">
                                        <div class="condinue-shop">
                                            <a href="<?php echo e(url('course-list')); ?>" class="btn btn-primary">Continue
                                                Shopping</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- /Cart -->
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/cart.blade.php ENDPATH**/ ?>