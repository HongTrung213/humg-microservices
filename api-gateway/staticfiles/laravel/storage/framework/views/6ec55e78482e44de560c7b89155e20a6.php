<?php $page = 'setting-student-notification'; ?>

<?php $__env->startSection('content'); ?>
    <!--Dashbord Student -->
    <div class="page-content">
        <div class="container">
            <div class="row">
                <?php $__env->startComponent('components.sidebar'); ?>
                <?php echo $__env->renderComponent(); ?>
                <!-- Notifications -->
                <div class="col-xl-9 col-md-8">
                    <div class="settings-widget profile-details">
                        <div class="settings-menu p-0">
                            <div class="profile-heading">
                                <h3>Notifications</h3>
                                <p>You will get only notification what have enabled.</p>
                            </div>
                            <div class="checkout-form personal-address secure-alert border-line">
                                <div class="personal-info-head">
                                    <h4>Security Alerts</h4>
                                    <p>You will get only those email notification what you want.</p>
                                </div>
                                <div class="form-check form-switch check-on">
                                    <input class="form-check-input" type="checkbox" checked>
                                    <label class="form-check-label">Email me whenever encounter unusual activity</label>
                                </div>
                                <div class="form-check form-switch check-on">
                                    <input class="form-check-input" type="checkbox">
                                    <label class="form-check-label">Email me if new browser is used to sign in</label>
                                </div>
                            </div>
                            <div class="checkout-form personal-address secure-alert border-line">
                                <div class="personal-info-head">
                                    <h4>News</h4>
                                    <p>You will get only those email notification what you want.</p>
                                </div>
                                <div class="form-check form-switch check-on">
                                    <input class="form-check-input" type="checkbox">
                                    <label class="form-check-label">Notify me by email about sales and latest news</label>
                                </div>
                                <div class="form-check form-switch check-on">
                                    <input class="form-check-input" type="checkbox">
                                    <label class="form-check-label">Email me about new features and updates</label>
                                </div>
                                <div class="form-check form-switch check-on">
                                    <input class="form-check-input" type="checkbox">
                                    <label class="form-check-label">Email me about tips on using account</label>
                                </div>
                            </div>
                            <div class="checkout-form personal-address secure-alert border-line">
                                <div class="personal-info-head">
                                    <h4>Courses</h4>
                                    <p>You will get only those email notification what you want.</p>
                                </div>
                                <div class="form-check form-switch check-on">
                                    <input class="form-check-input" type="checkbox">
                                    <label class="form-check-label">Updates from Classes You're Taking</label>
                                </div>
                                <div class="form-check form-switch check-on">
                                    <input class="form-check-input" type="checkbox">
                                    <label class="form-check-label">Updates from Teacher Discussions</label>
                                </div>
                                <div class="form-check form-switch check-on">
                                    <input class="form-check-input" type="checkbox">
                                    <label class="form-check-label">Personalized Class Recommendations</label>
                                </div>
                                <div class="form-check form-switch check-on">
                                    <input class="form-check-input" type="checkbox">
                                    <label class="form-check-label">Featured content</label>
                                </div>
                                <div class="form-check form-switch check-on">
                                    <input class="form-check-input" type="checkbox">
                                    <label class="form-check-label">Product updates</label>
                                </div>
                                <div class="form-check form-switch check-on mb-0">
                                    <input class="form-check-input" type="checkbox">
                                    <label class="form-check-label">Events and offers</label>
                                </div>
                            </div>
                            <div class="un-subscribe">
                                <a href="#" class="btn btn-danger">Unsubscribe from all of the above</a>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Notifications -->

            </div>
        </div>
    </div>
    <!-- /Dashbord Student -->
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/setting-student-notification.blade.php ENDPATH**/ ?>