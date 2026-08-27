<?php $page = 'register-step-one'; ?>

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
                                    <div class="circle-graph1" data-percent="25">
                                        <p>25% <span>1 of 4</span></p>
                                    </div>
                                </div>
                                <h3>Profile Compleation</h3>
                                <div class="personal-detail d-flex align-items-center">
                                    <span class="active-color active-bar">1</span>
                                    <div class="personal-text">
                                        <h4>Personal Details</h4>
                                        <p class="mb-0">Setup Your personal details</p>
                                    </div>
                                </div>
                                <div class="personal-detail d-flex align-items-center">
                                    <span>2</span>
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
                                <h4>Personal Details</h4>
                                <form action="register-step-two">
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label">First Name</label>
                                                <input type="text" class="form-control"
                                                    placeholder="Enter your first Name">
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label">Last Name</label>
                                                <input type="text" class="form-control"
                                                    placeholder="Enter your last Name">
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label">Email</label>
                                                <input type="email" class="form-control"
                                                    placeholder="Enter your email address">
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label">Phone</label>
                                                <input type="text" class="form-control"
                                                    placeholder="Enter your phone number">
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label">Website</label>
                                                <input type="text" class="form-control"
                                                    placeholder="Enter your website url">
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label for="sel1" class="form-label">Country</label>
                                                <select class="form-select" id="sel1" name="sellist1">
                                                    <option>Select country</option>
                                                    <option>India</option>
                                                    <option>America</option>
                                                    <option>London</option>
                                                </select>
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label">Address Line1</label>
                                                <input type="text" class="form-control" placeholder="Address Line1">
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label">Address Line2</label>
                                                <input type="text" class="form-control" placeholder="Address Line2">
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label">City</label>
                                                <input type="text" class="form-control" placeholder="Enter your city">
                                            </div>
                                        </div>
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label class="form-control-label">Zipcode</label>
                                                <input type="text" class="form-control" placeholder="Enter your zipcode">
                                            </div>
                                        </div>
                                        <div class="col-lg-12">
                                            <div class="form-check form-switch check-on">
                                                <input class="form-check-input" type="checkbox" id="flexSwitchCheckChecked"
                                                    checked>
                                                <label class="form-check-label" for="flexSwitchCheckChecked">Use same
                                                    address for Billing.</label>
                                            </div>
                                            <div class="next-btn">
                                                <button class="btn btn-primary btn-start" type="submit">Next</button>
                                            </div>
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

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\dreams-lms_laravel\resources\views/register-step-one.blade.php ENDPATH**/ ?>