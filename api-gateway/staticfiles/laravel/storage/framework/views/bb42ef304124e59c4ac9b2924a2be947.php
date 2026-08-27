<?php $page = 'forgot-password'; ?>

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
                    <h1>Forgot Password ?</h1>
                    <div class="reset-password">
                        <p>Enter your email to reset your password.</p>
                    </div>
                    <form action="login">
                        <div class="form-group">
                            <label class="form-control-label">Email</label>
                            <input type="email" class="form-control" placeholder="Enter your email address">
                        </div>
                        <div class="d-grid">
                            <button class="btn btn-start" type="submit">Submit</button>
                        </div>
                    </form>
                </div>
            </div>
            <!-- /Login -->

        </div>

    </div>
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/forgot-password.blade.php ENDPATH**/ ?>