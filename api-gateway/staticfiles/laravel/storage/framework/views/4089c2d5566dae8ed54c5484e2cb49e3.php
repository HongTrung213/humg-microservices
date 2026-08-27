<?php $page = 'instructor-dashboard'; ?>

<?php $__env->startSection('content'); ?>
    <!-- Page Wrapper -->
    <div class="page-content instructor-page-content">
        <div class="container">
            <div class="row">
                <?php $__env->startComponent('components.sidebar'); ?>
                <?php echo $__env->renderComponent(); ?>
                <!-- Instructor Dashboard -->
                <div class="col-xl-9 col-lg-8 col-md-12">
                    <div class="row">
                        <div class="col-md-4 d-flex">
                            <div class="card instructor-card w-100">
                                <div class="card-body">
                                    <div class="instructor-inner">
                                        <h6>REVENUE</h6>
                                        <h4 class="instructor-text-success">$467.34</h4>
                                        <p>Earning this month</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-4 d-flex">
                            <div class="card instructor-card w-100">
                                <div class="card-body">
                                    <div class="instructor-inner">
                                        <h6>STUDENTS ENROLLMENTS</h6>
                                        <h4 class="instructor-text-info">12,000</h4>
                                        <p>New this month</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-md-4 d-flex">
                            <div class="card instructor-card w-100">
                                <div class="card-body">
                                    <div class="instructor-inner">
                                        <h6>COURSES RATING</h6>
                                        <h4 class="instructor-text-warning">4.80</h4>
                                        <p>Rating this month</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-12">
                            <div class="card instructor-card">
                                <div class="card-header">
                                    <h4>Earnings</h4>
                                </div>
                                <div class="card-body">
                                    <div id="instructor_chart"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-12">
                            <div class="card instructor-card">
                                <div class="card-header">
                                    <h4>Order</h4>
                                </div>
                                <div class="card-body">
                                    <div id="order_chart"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-12">
                            <div class="settings-widget">
                                <div class="settings-inner-blk p-0">
                                    <div class="sell-course-head comman-space">
                                        <h3>Best Selling Courses</h3>
                                    </div>
                                    <div class="comman-space pb-0">
                                        <div class="settings-tickets-blk course-instruct-blk table-responsive">

                                            <!-- Referred Users-->
                                            <table class="table table-nowrap mb-0">
                                                <thead>
                                                    <tr>
                                                        <th>COURSES</th>
                                                        <th>SALES</th>
                                                        <th>AMOUNT</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <td>
                                                            <div class="sell-table-group d-flex align-items-center">
                                                                <div class="sell-group-img">
                                                                    <a href="<?php echo e(url('course-details')); ?>">
                                                                        <img src="<?php echo e(URL::asset('/assets/img/course/course-10.jpg')); ?>"
                                                                            class="img-fluid " alt="">
                                                                    </a>
                                                                </div>
                                                                <div class="sell-tabel-info">
                                                                    </p>
                                                                    <p><a href="<?php echo e(url('course-details')); ?>">Information
                                                                            About UI/UX Design Degree</a>
                                                                </div>
                                                            </div>
                                                        </td>
                                                        <td>34</td>
                                                        <td>$3,145.23</td>
                                                    </tr>
                                                    <tr>
                                                        <td>
                                                            <div class="sell-table-group d-flex align-items-center">
                                                                <div class="sell-group-img">
                                                                    <a href="<?php echo e(url('course-details')); ?>">
                                                                        <img src="<?php echo e(URL::asset('/assets/img/course/course-11.jpg')); ?>"
                                                                            class="img-fluid " alt="">
                                                                    </a>
                                                                </div>
                                                                <div class="sell-tabel-info">
                                                                    <p><a href="<?php echo e(url('course-details')); ?>">Wordpress for
                                                                            Beginners - Master Wordpress Quickly</a></p>
                                                                </div>
                                                            </div>
                                                        </td>
                                                        <td>34</td>
                                                        <td>$3,145.23</td>
                                                    </tr>
                                                    <tr>
                                                        <td>
                                                            <div class="sell-table-group d-flex align-items-center">
                                                                <div class="sell-group-img">
                                                                    <a href="<?php echo e(url('course-details')); ?>">
                                                                        <img src="<?php echo e(URL::asset('/assets/img/course/course-12.jpg')); ?>"
                                                                            class="img-fluid " alt="">
                                                                    </a>
                                                                </div>
                                                                <div class="sell-tabel-info">
                                                                    <p><a href="<?php echo e(url('course-details')); ?>">Sketch from A
                                                                            to Z (2023): Become an app designer</a></p>
                                                                </div>
                                                            </div>
                                                        </td>
                                                        <td>34</td>
                                                        <td>$3,145.23</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                            <!-- /Referred Users-->

                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- /Instructor Dashboard -->

            </div>
        </div>
    </div>
    <!-- /Page Wrapper -->
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\dreams-lms_laravel\resources\views/instructor-dashboard.blade.php ENDPATH**/ ?>