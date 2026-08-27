<?php $page = 'instructor-reviews'; ?>

<?php $__env->startSection('content'); ?>
    <!-- Page Wrapper -->
    <div class="page-content">
        <div class="container">
            <div class="row">
                <?php $__env->startComponent('components.sidebar'); ?>
                <?php echo $__env->renderComponent(); ?>
                <!-- Instructor Dashboard -->
                <div class="col-xl-9 col-lg-8 col-md-12">
                    <div class="row">
                        <div class="col-md-12">
                            <div class="settings-widget">
                                <div class="settings-inner-blk p-0">
                                    <div class="sell-course-head comman-space">
                                        <h3>Reviews</h3>
                                        <p>You have full control to manage your own account setting.</p>
                                    </div>
                                    <div class="comman-space pb-0">
                                        <div class="instruct-search-blk mb-0">
                                            <div class="show-filter all-select-blk">
                                                <form action="#">
                                                    <?php
$__split = function ($name, $params = []) {
    return [$name, $params];
};
[$__name, $__params] = $__split('select2-instructor-reviews');

$__html = app('livewire')->mount($__name, $__params, 'A463IDC', $__slots ?? [], get_defined_vars());

echo $__html;

unset($__html);
unset($__name);
unset($__params);
unset($__split);
if (isset($__slots)) unset($__slots);
?>
                                                </form>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="comman-space bdr-bottom-line">
                                        <div class="instruct-review-blk ">
                                            <div class="review-item">
                                                <div class="instructor-wrap border-0 m-0">
                                                    <div class="about-instructor">
                                                        <div class="abt-instructor-img">
                                                            <a href="<?php echo e(url('instructor-profile')); ?>"><img
                                                                    src="<?php echo e(URL::asset('/assets/img/user/user1.jpg')); ?>"
                                                                    alt="img" class="img-fluid"></a>
                                                        </div>
                                                        <div class="instructor-detail">
                                                            <h5><a href="<?php echo e(url('instructor-profile')); ?>">Nicole Brown</a>
                                                            </h5>
                                                            <p>UX/UI Designer</p>
                                                        </div>
                                                    </div>
                                                    <div class="rating">
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star"></i>
                                                    </div>
                                                </div>
                                                <p class="rev-info">“ This is the second Photoshop course I have completed
                                                    with Cristian. Worth every penny and recommend it highly. To get the
                                                    most out of this course, its best to to take the Beginner to Advanced
                                                    course first. The sound and video quality is of a good standard. Thank
                                                    you Cristian. “</p>
                                                <a href="javascript:;" class="btn btn-reply"><i
                                                        class="feather-corner-up-left"></i> Respond</a>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="comman-space bdr-bottom-line">
                                        <div class="instruct-review-blk ">
                                            <div class="review-item">
                                                <div class="instructor-wrap border-0 m-0">
                                                    <div class="about-instructor">
                                                        <div class="abt-instructor-img">
                                                            <a href="<?php echo e(url('instructor-profile')); ?>"><img
                                                                    src="<?php echo e(URL::asset('/assets/img/user/user2.jpg')); ?>"
                                                                    alt="img" class="img-fluid"></a>
                                                        </div>
                                                        <div class="instructor-detail">
                                                            <h5><a href="<?php echo e(url('instructor-profile')); ?>">Jesse Stevens</a>
                                                            </h5>
                                                            <p>UX/UI Designer</p>
                                                        </div>
                                                    </div>
                                                    <div class="rating">
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                    </div>
                                                </div>
                                                <p class="rev-info">“ This is the second Photoshop course I have completed
                                                    with Cristian. Worth every penny and recommend it highly. To get the
                                                    most out of this course, its best to to take the Beginner to Advanced
                                                    course first. The sound and video quality is of a good standard. Thank
                                                    you Cristian. “</p>
                                                <a href="javascript:;" class="btn btn-reply"><i
                                                        class="feather-corner-up-left"></i> Respond</a>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="comman-space bdr-bottom-line">
                                        <div class="instruct-review-blk ">
                                            <div class="review-item">
                                                <div class="instructor-wrap border-0 m-0">
                                                    <div class="about-instructor">
                                                        <div class="abt-instructor-img">
                                                            <a href="<?php echo e(url('instructor-profile')); ?>"><img
                                                                    src="<?php echo e(URL::asset('/assets/img/user/user3.jpg')); ?>"
                                                                    alt="img" class="img-fluid"></a>
                                                        </div>
                                                        <div class="instructor-detail">
                                                            <h5><a href="<?php echo e(url('instructor-profile')); ?>">John Smith</a>
                                                            </h5>
                                                            <p>UX/UI Designer</p>
                                                        </div>
                                                    </div>
                                                    <div class="rating">
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star"></i>
                                                    </div>
                                                </div>
                                                <p class="rev-info">“ This is the second Photoshop course I have completed
                                                    with Cristian. Worth every penny and recommend it highly. To get the
                                                    most out of this course, its best to to take the Beginner to Advanced
                                                    course first. The sound and video quality is of a good standard. Thank
                                                    you Cristian. “</p>
                                                <a href="javascript:;" class="btn btn-reply"><i
                                                        class="feather-corner-up-left"></i> Respond</a>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="comman-space">
                                        <div class="instruct-review-blk ">
                                            <div class="review-item">
                                                <div class="instructor-wrap border-0 m-0">
                                                    <div class="about-instructor">
                                                        <div class="abt-instructor-img">
                                                            <a href="<?php echo e(url('instructor-profile')); ?>"><img
                                                                    src="<?php echo e(URL::asset('/assets/img/user/user4.jpg')); ?>"
                                                                    alt="img" class="img-fluid"></a>
                                                        </div>
                                                        <div class="instructor-detail">
                                                            <h5><a href="<?php echo e(url('instructor-profile')); ?>">Stella
                                                                    Johnson</a></h5>
                                                            <p>UX/UI Designer</p>
                                                        </div>
                                                    </div>
                                                    <div class="rating">
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star"></i>
                                                    </div>
                                                </div>
                                                <p class="rev-info">“ This is the second Photoshop course I have completed
                                                    with Cristian. Worth every penny and recommend it highly. To get the
                                                    most out of this course, its best to to take the Beginner to Advanced
                                                    course first. The sound and video quality is of a good standard. Thank
                                                    you Cristian. “</p>
                                                <a href="javascript:;" class="btn btn-reply"><i
                                                        class="feather-corner-up-left"></i> Respond</a>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- /Instructor Dashboard -->

            </div>
        </div>
    </div>
    <!-- /Page Wrapper -->
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/instructor-reviews.blade.php ENDPATH**/ ?>