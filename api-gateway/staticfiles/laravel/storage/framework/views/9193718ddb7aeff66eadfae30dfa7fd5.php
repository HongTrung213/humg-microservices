<?php $page = 'students-grid'; ?>

<?php $__env->startSection('content'); ?>
    <?php $__env->startComponent('components.breadcrumb'); ?>
        <?php $__env->slot('title'); ?>
            Home
        <?php $__env->endSlot(); ?>
        <?php $__env->slot('li1'); ?>
            Pages
        <?php $__env->endSlot(); ?>
        <?php $__env->slot('li2'); ?>
            Students Grid
        <?php $__env->endSlot(); ?>
    <?php echo $__env->renderComponent(); ?>
    <!-- Page Wrapper -->
    <div class="page-content">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <?php $__env->startComponent('components.filter'); ?>
                    <?php echo $__env->renderComponent(); ?>
                    <div class="row">
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box flex-fill">
                                <div class="student-img">
                                    <a href="<?php echo e(url('student-profile')); ?>">
                                        <img class="img-fluid" alt="Students Info"
                                            src="<?php echo e(URL::asset('/assets/img/user/user1.jpg')); ?>">
                                    </a>
                                </div>
                                <div class="student-content pb-0">
                                    <h5><a href="<?php echo e(url('student-profile')); ?>">Charles Dickens</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="<?php echo e(URL::asset('/assets/img/students/loc-icon.svg')); ?>" class="me-1"
                                            alt="">
                                        <p>Iceland</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box flex-fill">
                                <div class="student-img">
                                    <a href="<?php echo e(url('student-profile')); ?>">
                                        <img class="img-fluid" alt="Students Info"
                                            src="<?php echo e(URL::asset('/assets/img/user/user2.jpg')); ?>">
                                    </a>
                                </div>
                                <div class="student-content pb-0">
                                    <h5><a href="<?php echo e(url('student-profile')); ?>">Gabriel Palmer</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="<?php echo e(URL::asset('/assets/img/students/loc-icon.svg')); ?>" class="me-1"
                                            alt="">
                                        <p>France</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box flex-fill">
                                <div class="student-img">
                                    <a href="<?php echo e(url('student-profile')); ?>">
                                        <img class="img-fluid" alt="Students Info"
                                            src="<?php echo e(URL::asset('/assets/img/user/user3.jpg')); ?>">
                                    </a>
                                </div>
                                <div class="student-content pb-0">
                                    <h5><a href="<?php echo e(url('student-profile')); ?>">James Lemire</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="<?php echo e(URL::asset('/assets/img/students/loc-icon.svg')); ?>" class="me-1"
                                            alt="">
                                        <p>Italy</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box flex-fill">
                                <div class="student-img">
                                    <a href="<?php echo e(url('student-profile')); ?>">
                                        <img class="img-fluid" alt="Students Info"
                                            src="<?php echo e(URL::asset('/assets/img/user/user4.jpg')); ?>">
                                    </a>
                                </div>
                                <div class="student-content pb-0">
                                    <h5><a href="<?php echo e(url('student-profile')); ?>">Olivia Murphy</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="<?php echo e(URL::asset('/assets/img/students/loc-icon.svg')); ?>" class="me-1"
                                            alt="">
                                        <p>Brazil</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box flex-fill">
                                <div class="student-img">
                                    <a href="<?php echo e(url('student-profile')); ?>">
                                        <img class="img-fluid" alt="Students Info"
                                            src="<?php echo e(URL::asset('/assets/img/user/user5.jpg')); ?>">
                                    </a>
                                </div>
                                <div class="student-content pb-0">
                                    <h5><a href="<?php echo e(url('student-profile')); ?>">Rebecca Swartz</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="<?php echo e(URL::asset('/assets/img/students/loc-icon.svg')); ?>" class="me-1"
                                            alt="">
                                        <p>Louisiana</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box flex-fill">
                                <div class="student-img">
                                    <a href="<?php echo e(url('student-profile')); ?>">
                                        <img class="img-fluid" alt="Students Info"
                                            src="<?php echo e(URL::asset('/assets/img/user/user6.jpg')); ?>">
                                    </a>
                                </div>
                                <div class="student-content pb-0">
                                    <h5><a href="<?php echo e(url('student-profile')); ?>">Betty Richards</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="<?php echo e(URL::asset('/assets/img/students/loc-icon.svg')); ?>" class="me-1"
                                            alt="">
                                        <p>Iceland</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box flex-fill">
                                <div class="student-img">
                                    <a href="<?php echo e(url('student-profile')); ?>">
                                        <img class="img-fluid" alt="Students Info"
                                            src="<?php echo e(URL::asset('/assets/img/user/user14.jpg')); ?>">
                                    </a>
                                </div>
                                <div class="student-content pb-0">
                                    <h5><a href="<?php echo e(url('student-profile')); ?>">Jeffrey Montgomery</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="<?php echo e(URL::asset('/assets/img/students/loc-icon.svg')); ?>" class="me-1"
                                            alt="">
                                        <p>United Kingdom</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box flex-fill">
                                <div class="student-img">
                                    <a href="<?php echo e(url('student-profile')); ?>">
                                        <img class="img-fluid" alt="Students Info"
                                            src="<?php echo e(URL::asset('/assets/img/user/user11.jpg')); ?>">
                                    </a>
                                </div>
                                <div class="student-content pb-0">
                                    <h5><a href="<?php echo e(url('student-profile')); ?>">Brooke Hayes</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="<?php echo e(URL::asset('/assets/img/students/loc-icon.svg')); ?>" class="me-1"
                                            alt="">
                                        <p>United States</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box flex-fill">
                                <div class="student-img">
                                    <a href="<?php echo e(url('student-profile')); ?>">
                                        <img class="img-fluid" alt="Students Info"
                                            src="<?php echo e(URL::asset('/assets/img/user/user12.jpg')); ?>">
                                    </a>
                                </div>
                                <div class="student-content pb-0">
                                    <h5><a href="<?php echo e(url('student-profile')); ?>">Gertrude D. Shorter</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="<?php echo e(URL::asset('/assets/img/students/loc-icon.svg')); ?>" class="me-1"
                                            alt="">
                                        <p>Louisiana</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box flex-fill">
                                <div class="student-img">
                                    <a href="<?php echo e(url('student-profile')); ?>">
                                        <img class="img-fluid" alt="Students Info"
                                            src="<?php echo e(URL::asset('/assets/img/user/user13.jpg')); ?>">
                                    </a>
                                </div>
                                <div class="student-content pb-0">
                                    <h5><a href="<?php echo e(url('student-profile')); ?>">David L. Garza</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="<?php echo e(URL::asset('/assets/img/students/loc-icon.svg')); ?>" class="me-1"
                                            alt="">
                                        <p>Spain</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box flex-fill">
                                <div class="student-img">
                                    <a href="<?php echo e(url('student-profile')); ?>">
                                        <img class="img-fluid" alt="Students Info"
                                            src="<?php echo e(URL::asset('/assets/img/user/user4.jpg')); ?>">
                                    </a>
                                </div>
                                <div class="student-content pb-0">
                                    <h5><a href="<?php echo e(url('student-profile')); ?>">Vivian E. Winders</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="<?php echo e(URL::asset('/assets/img/students/loc-icon.svg')); ?>" class="me-1"
                                            alt="">
                                        <p>Tunisia</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box flex-fill">
                                <div class="student-img">
                                    <a href="<?php echo e(url('student-profile')); ?>">
                                        <img class="img-fluid" alt="Students Info"
                                            src="<?php echo e(URL::asset('/assets/img/user/user5.jpg')); ?>">
                                    </a>
                                </div>
                                <div class="student-content pb-0">
                                    <h5><a href="<?php echo e(url('student-profile')); ?>">Sean K. Leon</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="<?php echo e(URL::asset('/assets/img/students/loc-icon.svg')); ?>" class="me-1"
                                            alt="">
                                        <p>United States</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <?php $__env->startComponent('components.pagination'); ?>
                    <?php echo $__env->renderComponent(); ?>

                </div>

            </div>
        </div>
    </div>
    <!-- /Page Wrapper -->
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/students-grid.blade.php ENDPATH**/ ?>