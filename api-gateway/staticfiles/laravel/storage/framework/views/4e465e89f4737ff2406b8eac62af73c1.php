<?php $page = 'register'; ?>

<?php $__env->startSection('content'); ?>
    <div class="row">
        <?php $__env->startComponent('components.loginbanner'); ?>
        <?php echo $__env->renderComponent(); ?>
        <div class="col-md-6 login-wrap-bg">
            <!-- Login -->
            <div class="login-wrapper">
                <div class="loginbox">
                    <div class="img-logo">
                        <img src="<?php echo e(URL::asset('/assets/img/logo.svg')); ?>" class="img-fluid" alt="Logo">
                        <div class="back-home">
                            <a href="<?php echo e(url('index')); ?>">Back to Home</a>
                        </div>
                    </div>
                    <h1>Sign up</h1>
                    <form action="<?php echo e(route('register.custom')); ?>" method="POST">
                        <?php echo csrf_field(); ?>
                        <div class="form-group">
                            <label class="form-control-label">Full Name</label>
                            <input type="text" class="form-control" placeholder="Enter your Full Name">
                            <div class="text-danger pt-2">
                                <?php $__errorArgs = ['name'];
$__bag = $errors->getBag($__errorArgs[1] ?? 'default');
if ($__bag->has($__errorArgs[0])) :
if (isset($message)) { $__messageOriginal = $message; }
$message = $__bag->first($__errorArgs[0]); ?>
                                    <?php echo e($message); ?>

                                <?php unset($message);
if (isset($__messageOriginal)) { $message = $__messageOriginal; }
endif;
unset($__errorArgs, $__bag); ?>
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="form-control-label">Email</label>
                            <input type="email" class="form-control" placeholder="Enter your email address">
                            <div class="text-danger pt-2">
                                <?php $__errorArgs = ['email'];
$__bag = $errors->getBag($__errorArgs[1] ?? 'default');
if ($__bag->has($__errorArgs[0])) :
if (isset($message)) { $__messageOriginal = $message; }
$message = $__bag->first($__errorArgs[0]); ?>
                                    <?php echo e($message); ?>

                                <?php unset($message);
if (isset($__messageOriginal)) { $message = $__messageOriginal; }
endif;
unset($__errorArgs, $__bag); ?>
                            </div>
                        </div>
                        <div class="form-group">
                            <label class="form-control-label">Password</label>
                            <div class="pass-group" id="passwordInput">
                                <input type="password" class="form-control pass-input" placeholder="Enter your password">
                                <span class="toggle-password feather-eye-off"></span>
                                <span class="pass-checked"><i class="feather-check"></i></span>
                            </div>
                            <div class="text-danger pt-2">
                                <?php $__errorArgs = ['password'];
$__bag = $errors->getBag($__errorArgs[1] ?? 'default');
if ($__bag->has($__errorArgs[0])) :
if (isset($message)) { $__messageOriginal = $message; }
$message = $__bag->first($__errorArgs[0]); ?>
                                    <?php echo e($message); ?>

                                <?php unset($message);
if (isset($__messageOriginal)) { $message = $__messageOriginal; }
endif;
unset($__errorArgs, $__bag); ?>
                            </div>
                            <div class="password-strength" id="passwordStrength">
                                <span id="poor"></span>
                                <span id="weak"></span>
                                <span id="strong"></span>
                                <span id="heavy"></span>
                            </div>
                            <div id="passwordInfo"></div>
                        </div>

                        <div class="form-check remember-me">
                            <label class="form-check-label mb-0">
                                <input class="form-check-input" type="checkbox" name="remember"> I agree to the <a
                                    href="<?php echo e(url('term-condition')); ?>">Terms of Service</a> and <a
                                    href="<?php echo e(url('privacy-policy')); ?>">Privacy Policy.</a>
                            </label>
                        </div>
                        <div class="d-grid">
                            <button class="btn btn-primary btn-start" type="submit">Create Account</button>
                        </div>
                    </form>
                </div>
                <div class="google-bg text-center">
                    <span><a href="#">Or sign in with</a></span>
                    <div class="sign-google">
                        <ul>
                            <li><a href="#"><img src="<?php echo e(URL::asset('/assets/img/net-icon-01.png')); ?>"
                                        class="img-fluid" alt="Logo"> Sign In using Google</a></li>
                            <li><a href="#"><img src="<?php echo e(URL::asset('/assets/img/net-icon-02.png')); ?>"
                                        class="img-fluid" alt="Logo">Sign In using Facebook</a></li>
                        </ul>
                    </div>
                    <p class="mb-0">Already have an account? <a href="<?php echo e(url('login')); ?>">Sign in</a></p>
                </div>
            </div>
            <!-- /Login -->

        </div>

    </div>
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/register.blade.php ENDPATH**/ ?>