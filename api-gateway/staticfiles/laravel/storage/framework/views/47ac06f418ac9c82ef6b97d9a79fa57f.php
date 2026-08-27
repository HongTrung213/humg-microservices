<?php $page = 'setting-student-invoice'; ?>

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
                        <div class="settings-inner-blk p-0">
                            <div class="profile-heading">
                                <h3>Invoices</h3>
                                <p>You can find all of your order Invoices.</p>
                            </div>
                            <div class="comman-space pb-0">
                                <div class="settings-invoice-blk table-responsive">

                                    <!-- Invoice info-->
                                    <table class="table table-borderless mb-0">
                                        <thead>
                                            <tr>
                                                <th>order id</th>
                                                <th>date</th>
                                                <th>amount</th>
                                                <th>status</th>
                                                <th>&nbsp;</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td><a href="<?php echo e(url('view-invoice')); ?>" class="invoice-no">#1001</a></td>
                                                <td>15-01-2020, 10:45pm</td>
                                                <td>$50.00</td>
                                                <td><span class="badge status-due">Due</span></td>
                                                <td><a href="javascript:;" class="btn-style"><i
                                                            class="feather-download"></i></a></td>
                                            </tr>
                                            <tr>
                                                <td><a href="<?php echo e(url('view-invoice')); ?>" class="invoice-no">#1002</a></td>
                                                <td>15-02-2020, 10:45pm</td>
                                                <td>$50.00</td>
                                                <td><span class="badge status-completed">Completed</span></td>
                                                <td><a href="javascript:;" class="btn-style"><i
                                                            class="feather-download"></i></a></td>
                                            </tr>
                                            <tr>
                                                <td><a href="<?php echo e(url('view-invoice')); ?>" class="invoice-no">#1003</a></td>
                                                <td>15-03-2020, 10:45pm</td>
                                                <td>$50.00</td>
                                                <td><span class="badge status-completed">Completed</span></td>
                                                <td><a href="javascript:;" class="btn-style"><i
                                                            class="feather-download"></i></a></td>
                                            </tr>
                                            <tr>
                                                <td><a href="<?php echo e(url('view-invoice')); ?>" class="invoice-no">#1004</a></td>
                                                <td>15-04-2020, 10:45pm</td>
                                                <td>$50.00</td>
                                                <td><span class="badge status-completed">Completed</span></td>
                                                <td><a href="javascript:;" class="btn-style"><i
                                                            class="feather-download"></i></a></td>
                                            </tr>
                                            <tr>
                                                <td><a href="<?php echo e(url('view-invoice')); ?>" class="invoice-no">#1005</a></td>
                                                <td>15-05-2020, 10:45pm</td>
                                                <td>$50.00</td>
                                                <td><span class="badge status-completed">Completed</span></td>
                                                <td><a href="javascript:;" class="btn-style"><i
                                                            class="feather-download"></i></a></td>
                                            </tr>
                                            <tr>
                                                <td><a href="<?php echo e(url('view-invoice')); ?>" class="invoice-no">#1006</a></td>
                                                <td>15-06-2020, 10:45pm</td>
                                                <td>$50.00</td>
                                                <td><span class="badge status-completed">Completed</span></td>
                                                <td><a href="javascript:;" class="btn-style"><i
                                                            class="feather-download"></i></a></td>
                                            </tr>
                                            <tr>
                                                <td><a href="<?php echo e(url('view-invoice')); ?>" class="invoice-no">#1007</a></td>
                                                <td>15-07-2020, 10:45pm</td>
                                                <td>$50.00</td>
                                                <td><span class="badge status-completed">Completed</span></td>
                                                <td><a href="javascript:;" class="btn-style"><i
                                                            class="feather-download"></i></a></td>
                                            </tr>
                                            <tr>
                                                <td><a href="<?php echo e(url('view-invoice')); ?>" class="invoice-no">#1008</a></td>
                                                <td>15-08-2020, 10:45pm</td>
                                                <td>$50.00</td>
                                                <td><span class="badge status-completed">Completed</span></td>
                                                <td><a href="javascript:;" class="btn-style"><i
                                                            class="feather-download"></i></a></td>
                                            </tr>
                                            <tr>
                                                <td><a href="<?php echo e(url('view-invoice')); ?>" class="invoice-no">#1009</a></td>
                                                <td>15-09-2020, 10:45pm</td>
                                                <td>$50.00</td>
                                                <td><span class="badge status-completed">Completed</span></td>
                                                <td><a href="javascript:;" class="btn-style"><i
                                                            class="feather-download"></i></a></td>
                                            </tr>
                                            <tr>
                                                <td><a href="<?php echo e(url('view-invoice')); ?>" class="invoice-no">#1010</a></td>
                                                <td>15-10-2020, 10:45pm</td>
                                                <td>$50.00</td>
                                                <td><span class="badge status-completed">Completed</span></td>
                                                <td><a href="javascript:;" class="btn-style"><i
                                                            class="feather-download"></i></a></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <!-- /Invoice info-->

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
    <?php $__env->startComponent('components.modalpopup'); ?>
    <?php echo $__env->renderComponent(); ?>
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/setting-student-invoice.blade.php ENDPATH**/ ?>