<!DOCTYPE html>
<html lang="en">

<head>
    <?php echo $__env->make('layout.partials.head', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?>
    <?php echo \Livewire\Mechanisms\FrontendAssets\FrontendAssets::styles(); ?>

</head>

<body>
    <?php if(Route::is(['index-two'])): ?>

        <body class="home-two">
    <?php endif; ?>
    <?php if(Route::is(['index-three'])): ?>

        <body class="home-three">
    <?php endif; ?>
    <?php if(Route::is(['index-four'])): ?>

        <body class="home-five">
    <?php endif; ?>
    <?php if(Route::is(['come-soon', 'error-404', 'error-500', 'under-construction'])): ?>

        <body class="error-page">
    <?php endif; ?>
    <!-- Main Wrapper -->
    <?php if(!Route::is(['login', 'register'])): ?>
        <div class="main-wrapper">
    <?php endif; ?>
    <?php if(Route::is(['login', 'register'])): ?>
        <div class="main-wrapper log-wrap">
    <?php endif; ?>
    <?php if(
        !Route::is([
            'come-soon',
            'error-404',
            'error-500',
            'forgot-password',
            'login',
            'new-password',
            'register-step-five',
            'register-step-four',
            'register-step-one',
            'register-step-three',
            'register-step-two',
            'register',
            'under-construction',
            'verification-code',
        ])): ?>
        <?php echo $__env->make('layout.partials.header', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?>
    <?php endif; ?>
    <?php echo $__env->yieldContent('content'); ?>
    <?php if(
        !Route::is([
            'come-soon',
            'error-404',
            'error-500',
            'forgot-password',
            'login',
            'new-password',
            'register-step-five',
            'register-step-four',
            'register-step-one',
            'register-step-three',
            'register-step-two',
            'register',
            'under-construction',
            'verification-code',
        ])): ?>
        <?php echo $__env->make('layout.partials.footer', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?>
    <?php endif; ?>
    </div>
    <!-- /Main Wrapper -->
    <?php echo $__env->make('layout.partials.footer-scripts', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?>

</body>

</html>
<?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\dreams-lms_laravel\resources\views/layout/mainlayout.blade.php ENDPATH**/ ?>