<?php $page = 'login'; ?>

<?php $__env->startSection('content'); ?>
    <div class="row">
        <?php $__env->startComponent('components.loginbanner'); ?>
        <?php echo $__env->renderComponent(); ?>
        <div class="col-md-6 login-wrap-bg">
            <!-- Login -->
            <div class="login-wrapper">
                <div class="loginbox">
                    <div class="w-100">
                        <div class="img-logo">
                            <img src="<?php echo e(URL::asset('/assets/img/logo.svg')); ?>" class="img-fluid" alt="Logo">
                            <div class="back-home">
                                <a href="<?php echo e(url('index')); ?>">Back to Home</a>
                            </div>
                        </div>
                        <h1>Sign into Your Account</h1>
                        <form method="post" action="<?php echo e(route('login.custom')); ?>">
                            <?php echo csrf_field(); ?>
                            <div class="form-group">
                                <label class="form-control-label">Email</label>
                                <input type="email" class="form-control" value="admin@example.com" name="email"
                                    id="email">
                                <div class="text-danger pt-2">
                                    <?php $__errorArgs = ['0'];
$__bag = $errors->getBag($__errorArgs[1] ?? 'default');
if ($__bag->has($__errorArgs[0])) :
if (isset($message)) { $__messageOriginal = $message; }
$message = $__bag->first($__errorArgs[0]); ?>
                                        <?php echo e($message); ?>

                                    <?php unset($message);
if (isset($__messageOriginal)) { $message = $__messageOriginal; }
endif;
unset($__errorArgs, $__bag); ?>
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
                                <div class="pass-group">
                                    <input type="password" class="form-control pass-input" value="12345678" name="password"
                                        id="password">
                                    <span class="feather-eye-off toggle-password"></span>
                                    <div class="text-danger pt-2">
                                        <?php $__errorArgs = ['0'];
$__bag = $errors->getBag($__errorArgs[1] ?? 'default');
if ($__bag->has($__errorArgs[0])) :
if (isset($message)) { $__messageOriginal = $message; }
$message = $__bag->first($__errorArgs[0]); ?>
                                            <?php echo e($message); ?>

                                        <?php unset($message);
if (isset($__messageOriginal)) { $message = $__messageOriginal; }
endif;
unset($__errorArgs, $__bag); ?>
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
                                </div>
                            </div>
                            <div class="forgot">
                                <span><a class="forgot-link" href="<?php echo e(url('forgot-password')); ?>">Forgot Password
                                        ?</a></span>
                            </div>
                            <div class="remember-me">
                                <label class="custom_check mr-2 mb-0 d-inline-flex remember-me"> Remember me
                                    <input type="checkbox" name="radio">
                                    <span class="checkmark"></span>
                                </label>
                            </div>
                            <div class="d-grid">
                                <button class="btn btn-primary btn-start" type="submit">Sign In</button>
                            </div>
                        </form>
                    </div>
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
                    <p class="mb-0">New User ? <a href="<?php echo e(url('register')); ?>">Create an Account</a></p>
                </div>
            </div>
            <!-- /Login -->

        </div>

    </div>
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\dreams-lms_laravel\resources\views/login.blade.php ENDPATH**/ ?>