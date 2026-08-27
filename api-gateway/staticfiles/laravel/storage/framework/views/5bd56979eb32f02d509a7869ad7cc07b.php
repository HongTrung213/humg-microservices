<?php if(
    !Route::is([
        'dashboard-instructor',
        'deposit-instructor-dashboard',
        'deposit-instructor',
        'transactions-instructor',
        'withdrawal-instructor',
    ])): ?>
    <!-- Breadcrumb -->
    <div class="breadcrumb-bar">
        <div class="container">
            <div class="row">
                <div class="col-md-12 col-12">
                    <div class="breadcrumb-list">
                        <nav aria-label="breadcrumb" class="page-breadcrumb">
                            <ol class="breadcrumb">
                                <li class="breadcrumb-item"><a href="<?php echo e(url('index')); ?>"><?php echo e($title); ?></a></li>
                                <li class="breadcrumb-item" aria-current="page"><?php echo e($li1); ?></li>
                                <li class="breadcrumb-item" aria-current="page"><?php echo e($li2); ?></li>
                                <?php if(Route::is(['course-details', 'course-details1', 'course-details2', 'instructor-edit', 'instructor-profile'])): ?>
                                    <li class="breadcrumb-item" aria-current="page"><?php echo e($li3); ?></li>
                                <?php endif; ?>
                            </ol>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- /Breadcrumb -->
<?php endif; ?>
<?php if(Route::is([
        'dashboard-instructor',
        'deposit-instructor-dashboard',
        'deposit-instructor',
        'transactions-instructor',
        'withdrawal-instructor',
    ])): ?>
    <!-- Breadcrumb -->
    <div class="page-banner instructor-bg-blk">
        <div class="container">
            <?php if(
                !Route::is([
                    'deposit-instructor-dashboard',
                    'deposit-instructor',
                    'transactions-instructor',
                    'withdrawal-instructor',
                ])): ?>
                <div class="row align-items-center">
            <?php endif; ?>
            <?php if(Route::is([
                    'deposit-instructor-dashboard',
                    'deposit-instructor',
                    'transactions-instructor',
                    'withdrawal-instructor',
                ])): ?>
                <div class="row align-items-center student-group">
            <?php endif; ?>
            <div class="col-lg-6 col-md-12">
                <div class="instructor-profile d-flex align-items-center">
                    <div class="instructor-profile-pic">
                        <a href="<?php echo e(url('instructor-profile')); ?>">
                            <img src="<?php echo e(URL::asset('/assets/img/instructor/profile-avatar.jpg')); ?>" alt=""
                                class="img-fluid">
                        </a>
                    </div>
                    <div class="instructor-profile-content">
                        <h4><a href="<?php echo e(url('instructor-profile')); ?>">Jenny Wilson <span>Beginner</span></a></h4>
                        <p>Instructor</p>
                    </div>
                </div>
            </div>
            <div class="col-lg-6 col-md-12">
                <div class="instructor-profile-menu">
                    <ul class="nav">
                        <li>
                            <div class="d-flex align-items-center">
                                <div class="instructor-profile-menu-img">
                                    <img src="<?php echo e(URL::asset('/assets/img/icon/icon-25.svg')); ?>" alt="">
                                </div>
                                <div class="instructor-profile-menu-content">
                                    <h4>32</h4>
                                    <p>Courses</p>
                                </div>
                            </div>
                        </li>
                        <li>
                            <div class="d-flex align-items-center">
                                <div class="instructor-profile-menu-img">
                                    <img src="<?php echo e(URL::asset('/assets/img/icon/icon-26.svg')); ?>" alt="">
                                </div>
                                <div class="instructor-profile-menu-content">
                                    <h4>11,604</h4>
                                    <p>Total Students</p>
                                </div>
                            </div>
                        </li>
                        <li>
                            <div class="d-flex align-items-center">
                                <div class="instructor-profile-menu-img">
                                    <img src="<?php echo e(URL::asset('/assets/img/icon/icon-27.svg')); ?>" alt="">
                                </div>
                                <div class="instructor-profile-menu-content">
                                    <h4>12,230</h4>
                                    <p>Reviews</p>
                                </div>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="row">
            <div class="col-md-12">
                <?php if(
                    !Route::is([
                        'deposit-instructor-dashboard',
                        'deposit-instructor',
                        'transactions-instructor',
                        'withdrawal-instructor',
                    ])): ?>
                    <div class="instructor-profile-text">
                        <p>I am an Innovation designer focussing on UX/UI based in Berlin. As a creative resident at
                            Figma explored the city of the future and how new technologies like AI, voice control, and
                            augmented reality will change our interfaces.</p>
                    </div>
                <?php endif; ?>
                <?php if(Route::is([
                        'deposit-instructor-dashboard',
                        'deposit-instructor',
                        'transactions-instructor',
                        'withdrawal-instructor',
                    ])): ?>
                    <div class="my-student-list">
                        <ul>
                            <li><a class="<?php echo e(Request::is('deposit-instructor-dashboard') ? 'active' : ''); ?>"
                                    href="<?php echo e(url('deposit-instructor-dashboard')); ?>">Dashboard</a></li>
                            <li><a class="<?php echo e(Request::is('dashboard-instructor') ? 'active' : ''); ?>"
                                    href="<?php echo e(url('dashboard-instructor')); ?>">Courses</a></li>
                            <li><a class="<?php echo e(Request::is('withdrawal-instructor') ? 'active' : ''); ?>"
                                    href="<?php echo e(url('withdrawal-instructor')); ?>">Withdrawal</a></li>
                            <li><a href="#">Purchase history</a></li>
                            <li><a class="<?php echo e(Request::is('deposit-instructor') ? 'active' : ''); ?>"
                                    href="<?php echo e(url('dashboard-instructor')); ?>">Deposit</a></li>
                            <li class="mb-0"><a class="<?php echo e(Request::is('transactions-instructor') ? 'active' : ''); ?>"
                                    href="<?php echo e(url('transactions-instructor')); ?>">Transactions</a></li>
                        </ul>
                    </div>
                <?php endif; ?>
            </div>
        </div>
    </div>
    </div>
    <!-- /Breadcrumb -->
<?php endif; ?>
<?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\dreams-lms_laravel\resources\views/components/breadcrumb.blade.php ENDPATH**/ ?>