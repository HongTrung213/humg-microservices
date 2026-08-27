<?php $page = 'instructor-delete-profile'; ?>

<?php $__env->startSection('content'); ?>
    <!--Dashbord Student -->
    <div class="page-content">
        <div class="container">
            <div class="row">
                <?php $__env->startComponent('components.sidebar'); ?>
                <?php echo $__env->renderComponent(); ?>
                <!-- Profile Details -->
                <div class="col-xl-9 col-md-8">
                    <div class="settings-widget profile-details">
                        <div class="settings-menu p-0">
                            <div class="profile-heading">
                                <h3>Delete your account</h3>
                                <p>Delete or Close your account permanently.</p>
                            </div>
                            <div class="checkout-form personal-address">
                                <div class="personal-info-head">
                                    <h4>Warning</h4>
                                    <p>If you close your account, you will be unsubscribed from all your 0 courses, and will
                                        lose access forever.</p>
                                </div>
                                <div class="un-subscribe p-0">
                                    <a href="#" class="btn btn-danger">Delete My Account</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Profile Details -->

            </div>
        </div>
    </div>
    <!-- /Dashbord Student -->
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/instructor-delete-profile.blade.php ENDPATH**/ ?>