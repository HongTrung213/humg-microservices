<?php $page = 'deposit-instructor-dashboard'; ?>

<?php $__env->startSection('content'); ?>
    <?php $__env->startComponent('components.breadcrumb'); ?>
    <?php echo $__env->renderComponent(); ?>
    <!--Dashbord Student -->
    <div class="page-content">
        <div class="container">
            <div class="row">
                <!-- Profile Details -->
                <div class="col-xl-12 col-md-12">
                    <div class="settings-top-widget student-deposit-blk">
                        <div class="row">
                            <div class="col-lg-4 col-md-6 d-flex">
                                <div class="card stat-info ttl-tickets">
                                    <div class="card-body">
                                        <div class="view-all-grp d-flex">
                                            <div class="student-ticket-view">
                                                <h3>50</h3>
                                                <p>Purchased Courses</p>
                                                <a href="<?php echo e(url('dashboard-instructor')); ?>">View All</a>
                                            </div>
                                            <div class="img-deposit-ticket">
                                                <img src="<?php echo e(URL::asset('/assets/img/students/book.svg')); ?>" alt="">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-6 d-flex">
                                <div class="card stat-info open-tickets">
                                    <div class="card-body">
                                        <div class="view-all-grp d-flex">
                                            <div class="student-ticket-view">
                                                <h3>30</h3>
                                                <p>Total Transactions</p>
                                                <a href="<?php echo e(url('transactions-instructor')); ?>">View All</a>
                                            </div>
                                            <div class="img-deposit-ticket">
                                                <img src="<?php echo e(URL::asset('/assets/img/students/receipt-text.svg')); ?>"
                                                    alt="">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-6 d-flex">
                                <div class="card stat-info close-tickets">
                                    <div class="card-body">
                                        <div class="view-all-grp d-flex">
                                            <div class="student-ticket-view">
                                                <h3>20</h3>
                                                <p>Total Deposit</p>
                                                <a href="<?php echo e(url('deposit-student')); ?>">View All</a>
                                            </div>
                                            <div class="img-deposit-ticket">
                                                <img src="<?php echo e(URL::asset('/assets/img/students/empty-wallet-tick.svg')); ?>"
                                                    alt="">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-6 d-flex">
                                <div class="card stat-info medium-tickets">
                                    <div class="card-body">
                                        <div class="view-all-grp d-flex">
                                            <div class="student-ticket-view">
                                                <h3>$2055</h3>
                                                <p>Total Withdraw</p>
                                                <a href="<?php echo e(url('withdrawal-instructor')); ?>">View All</a>
                                            </div>
                                            <div class="img-deposit-ticket">
                                                <img src="<?php echo e(URL::asset('/assets/img/students/empty-wallet-change.svg')); ?>"
                                                    alt="">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-6 d-flex">
                                <div class="card stat-info blue-tickets">
                                    <div class="card-body">
                                        <div class="view-all-grp d-flex">
                                            <div class="student-ticket-view">
                                                <h3>30</h3>
                                                <p>Total Student</p>
                                            </div>
                                            <div class="img-deposit-ticket">
                                                <img src="<?php echo e(URL::asset('/assets/img/students/profile-user.svg')); ?>"
                                                    alt="">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-6 d-flex">
                                <div class="card stat-info ttl-tickets">
                                    <div class="card-body">
                                        <div class="view-all-grp d-flex">
                                            <div class="student-ticket-view">
                                                <h3>50</h3>
                                                <p>Total Approved Course</p>
                                                <a href="<?php echo e(url('dashboard-instructor')); ?>">View All</a>
                                            </div>
                                            <div class="img-deposit-ticket">
                                                <img src="<?php echo e(URL::asset('/assets/img/students/book.svg')); ?>"
                                                    alt="">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="settings-widget">
                        <div class="settings-inner-blk p-0">
                            <div class="comman-space pb-0">
                                <div class="filter-grp ticket-grp d-flex align-items-center justify-content-between">
                                    <h3>Latest Transactions</h3>
                                </div>
                                <div class="settings-tickets-blk table-responsive">

                                    <!-- Referred Users-->
                                    <table class="table table-nowrap mb-0">
                                        <thead>
                                            <tr>
                                                <th>Referred ID</th>
                                                <th>Details</th>
                                                <th>Amount</th>
                                                <th>Post Balance</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td><a href="javascript:;">K2WX7JJ6R1UA</a></td>
                                                <td>10 USD Refunded from withdrawal rejection </td>
                                                <td><span class="text-success">+ $45.00</span></td>
                                                <td>$45.00</td>
                                            </tr>
                                            <tr>
                                                <td><a href="javascript:;">9RVE1N1TA1H3</a></td>
                                                <td>Deposit Via Stripe Hosted - USD </td>
                                                <td><span class="text-success">+ $75.00</span></td>
                                                <td>$75.00</td>
                                            </tr>
                                            <tr>
                                                <td><a href="javascript:;">C83Z7EQ4A1WX</a></td>
                                                <td>Deposit Via Stripe Hosted - USD </td>
                                                <td><span class="text-success">+ $100.00</span></td>
                                                <td>$100.00</td>
                                            </tr>
                                            <tr>
                                                <td><a href="javascript:;">1C6A5M4YPV39</a></td>
                                                <td>Withdraw Via Bank withdrawal </td>
                                                <td><span class="text-danger">- $5.00</span></td>
                                                <td>$5.00</td>
                                            </tr>
                                            <tr>
                                                <td><a href="javascript:;">K2WX7JJ6R1UA</a></td>
                                                <td>10 USD Refunded from withdrawal rejection </td>
                                                <td><span class="text-danger">- $25.00</span></td>
                                                <td>$25.00</td>
                                            </tr>
                                            <tr>
                                                <td><a href="javascript:;">KSM5CW4EOEGQ</a></td>
                                                <td>Added Balance Via Admin </td>
                                                <td><span class="text-success">+ $160.00</span></td>
                                                <td>S160.00</td>
                                            </tr>
                                            <tr>
                                                <td><a href="javascript:;">K2WX7JJ6R1UA</a></td>
                                                <td>10 USD Refunded from withdrawal rejection </td>
                                                <td><span class="text-success">+ $150.00</span></td>
                                                <td> $150.00</td>
                                            </tr>
                                            <tr>
                                                <td><a href="javascript:;">9RVE1N1TA1H3</a></td>
                                                <td>Deposit Via Stripe Hosted - USD </td>
                                                <td><span class="text-success">+ $45.00</span></td>
                                                <td>$45.00</td>
                                            </tr>
                                            <tr>
                                                <td><a href="javascript:;">C83Z7EQ4A1WX</a></td>
                                                <td>Deposit Via Stripe Hosted - USD </td>
                                                <td><span class="text-success">+ $10.00</span></td>
                                                <td>$10.00</td>
                                            </tr>
                                            <tr>
                                                <td><a href="javascript:;">1C6A5M4YPV39</a></td>
                                                <td>Withdraw Via Bank withdrawal </td>
                                                <td><span class="text-danger">- $10.00</span></td>
                                                <td>$10.00</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    <!-- /Referred Users-->

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

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\dreams-lms_laravel\resources\views/deposit-instructor-dashboard.blade.php ENDPATH**/ ?>