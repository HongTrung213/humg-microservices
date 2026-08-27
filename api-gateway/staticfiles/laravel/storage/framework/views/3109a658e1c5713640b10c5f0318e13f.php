<?php $page = 'register-step-two'; ?>

<?php $__env->startSection('content'); ?>
    <div class="row">
        <?php $__env->startComponent('components.loginbanner'); ?>
        <?php echo $__env->renderComponent(); ?>
        <div class="col-lg-8 col-md-6 login-wrap-bg">
            <!-- Login -->
            <div class="login-wrapper">
                <div class="loginbox register-box">
                    <div class="img-logo">
                        <img src="<?php echo e(URL::asset('/assets/img/logo.svg')); ?>" class="img-fluid" alt="Logo">
                        <div class="back-home">
                            <a href="<?php echo e(url('login')); ?>">Back to Home</a>
                        </div>
                    </div>
                    <h1>Become An Instructor</h1>
                    <div class="row">
                        <div class="col-lg-5">
                            <div class="profile-box">
                                <div class="circle-bar circle-bar1 text-center">
                                    <div class="circle-graph1" data-percent="50">
                                        <p>50% <span>2 of 4</span></p>
                                    </div>
                                </div>
                                <h3>Profile Compleation</h3>
                                <div class="personal-detail d-flex align-items-center">
                                    <span class="active-color"><i class="fa-solid fa-check"></i></span>
                                    <div class="personal-text">
                                        <h4>Personal Details</h4>
                                        <p class="mb-0">Setup Your personal details</p>
                                    </div>
                                </div>
                                <div class="personal-detail d-flex align-items-center">
                                    <span class="active-color active-bar">2</span>
                                    <div class="personal-text">
                                        <h4>Social Profiles</h4>
                                        <p class="mb-0">Setup Your Social Profiles links</p>
                                    </div>
                                </div>
                                <div class="personal-detail d-flex align-items-center">
                                    <span>3</span>
                                    <div class="personal-text">
                                        <h4>Profile Privacy Settings</h4>
                                        <p class="mb-0">Setup Your Profile Privacy Settings</p>
                                    </div>
                                </div>
                                <div class="personal-detail d-flex align-items-center">
                                    <span>4</span>
                                    <div class="personal-text">
                                        <h4>Link Accounts</h4>
                                        <p class="mb-0">Setup Your Linked Accounts</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-7">
                            <div class="personal-form">
                                <h4>Social Profiles</h4>
                                <form action="register-step-three">
                                    <div class="form-group">
                                        <label class="form-control-label">Twitter</label>
                                        <input type="text" class="form-control" placeholder="Twitter Profile URL">
                                    </div>
                                    <div class="form-group">
                                        <label class="form-control-label">Facebook</label>
                                        <input type="text" class="form-control" placeholder="Facebook Profile URL">
                                    </div>
                                    <div class="form-group">
                                        <label class="form-control-label">Instagram</label>
                                        <input type="text" class="form-control" placeholder="Instagram Profile URL">
                                    </div>
                                    <div class="form-group">
                                        <label class="form-control-label">LinkedIn Profile URL</label>
                                        <input type="text" class="form-control" placeholder="LinkedIn Profile URL">
                                    </div>
                                    <div class="form-group">
                                        <label class="form-control-label">YouTube</label>
                                        <input type="text" class="form-control" placeholder="Youtube URL">
                                    </div>
                                    <div class="btn-group d-flex">
                                        <div class="back-btn">
                                            <a href="<?php echo e(url('register-step-one')); ?>" class="btn btn-back"
                                                type="submit">back</a>
                                        </div>
                                        <div class="next-btn">
                                            <button class="btn btn-primary btn-start">Next</button>
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- /Login -->

        </div>

    </div>
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\dreams-lms_laravel\resources\views/register-step-two.blade.php ENDPATH**/ ?>