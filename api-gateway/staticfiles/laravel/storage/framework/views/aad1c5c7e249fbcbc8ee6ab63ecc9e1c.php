<?php $page = 'error-500'; ?>

<?php $__env->startSection('content'); ?>
    <div class="error-box">
        <div class="error-logo">
            <a href="<?php echo e(url('index')); ?>">
                <img src="<?php echo e(URL::asset('/assets/img/logo.svg')); ?>" class="img-fluid" alt="Logo">
            </a>
        </div>
        <div class="error-box-img">
            <img src="<?php echo e(URL::asset('/assets/img/error.png')); ?>" alt="" class="img-fluid">
        </div>
        <h3 class="h2 mb-3"> Oops! 500 Internal Server Error</h3>
        <p class="h4 font-weight-normal">We are working on fixing the problem. We back soon</p>
        <a href="<?php echo e(url('index')); ?>" class="btn btn-primary">Back to Home</a>
    </div>
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/error-500.blade.php ENDPATH**/ ?>