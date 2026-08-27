<?php if(!Route::is(['course-grid', 'course-list', 'course-student', 'course-wishlist'])): ?>
    <!-- Filter -->
    <div class="showing-list">
        <div class="row">
            <div class="col-lg-6">
                <div class="d-flex align-items-center">
                    <div class="view-icons">
                        <?php if(!Route::is(['students-grid', 'students-grid2', 'students-list'])): ?>
                            <a href="<?php echo e(url('instructor-grid')); ?>"
                                class="grid-view <?php echo e(Request::is('instructor-grid', 'instructor-grid-2') ? 'active' : ''); ?>"><i
                                    class="feather-grid"></i></a>
                            <a href="<?php echo e(url('instructor-list')); ?>"
                                class="list-view <?php echo e(Request::is('instructor-list') ? 'active' : ''); ?>"><i
                                    class="feather-list"></i></a>
                        <?php endif; ?>
                        <?php if(Route::is(['students-grid', 'students-grid2', 'students-list'])): ?>
                            <a href="<?php echo e(url('students-grid')); ?>"
                                class="grid-view <?php echo e(Request::is('students-grid', 'students-grid2') ? 'active' : ''); ?>"><i
                                    class="feather-grid"></i></a>
                            <a href="<?php echo e(url('students-list')); ?>"
                                class="list-view <?php echo e(Request::is('students-list') ? 'active' : ''); ?>"><i
                                    class="feather-list"></i></a>
                        <?php endif; ?>
                    </div>
                    <div class="show-result">
                        <h4>Showing 1-9 of 50 results</h4>
                    </div>
                </div>
            </div>
            <?php if(!Route::is(['students-grid', 'students-grid2', 'students-list'])): ?>
                <div class="col-lg-6">
                    <div class="show-filter add-course-info">
                        <form action="#">
                            <div class="row gx-2 align-items-center">
                                <div class="col-md-6 col-item">
                                    <div class=" search-group">
                                        <i class="feather-search"></i>
                                        <input type="text" class="form-control" placeholder="Search our courses">
                                    </div>
                                </div>
                                <div class="col-md-6 col-lg-6 col-item">
                                    <div class="form-group select-form mb-0">
                                        <?php
$__split = function ($name, $params = []) {
    return [$name, $params];
};
[$__name, $__params] = $__split('select2-component-filter');

$__html = app('livewire')->mount($__name, $__params, '23leR3R', $__slots ?? [], get_defined_vars());

echo $__html;

unset($__html);
unset($__name);
unset($__params);
unset($__split);
if (isset($__slots)) unset($__slots);
?>
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            <?php endif; ?>
        </div>
    </div>
    <!-- /Filter -->
<?php endif; ?>
<?php if(Route::is(['course-grid', 'course-list'])): ?>
    <!-- Filter -->
    <div class="showing-list">
        <div class="row">
            <div class="col-lg-6">
                <div class="d-flex align-items-center">
                    <div class="view-icons">
                        <a href="<?php echo e(url('course-details')); ?>"
                            class="grid-view <?php echo e(Request::is('course-grid') ? 'active' : ''); ?>"><i
                                class="feather-grid"></i></a>
                        <a href="<?php echo e(url('course-list')); ?>"
                            class="list-view <?php echo e(Request::is('course-list') ? 'active' : ''); ?>"><i
                                class="feather-list"></i></a>
                    </div>
                    <div class="show-result">
                        <h4>Showing 1-9 of 50 results</h4>
                    </div>
                </div>
            </div>
            <div class="col-lg-6">
                <div class="show-filter add-course-info">
                    <form action="#">
                        <div class="row gx-2 align-items-center">
                            <div class="col-md-6 col-item">
                                <div class=" search-group">
                                    <i class="feather-search"></i>
                                    <input type="text" class="form-control" placeholder="Search our courses">
                                </div>
                            </div>
                            <div class="col-md-6 col-lg-6 col-item">
                                <div class="form-group select-form mb-0">
                                    <select class="form-select select" id="sel1" name="sellist1">
                                        <option>Newly published </option>
                                        <option>published 1</option>
                                        <option>published 2</option>
                                        <option>published 3</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <!-- /Filter -->
<?php endif; ?>
<?php if(Route::is(['course-student', 'course-wishlist'])): ?>
    <!-- Filter -->
    <div class="showing-list">
        <div class="row">
            <div class="col-lg-12">
                <div class="show-filter choose-search-blk">
                    <form action="#">
                        <div class="mycourse-student align-items-center">
                            <div class="student-search">
                                <div class=" search-group">
                                    <i class="feather-search"></i>
                                    <input type="text" class="form-control" placeholder="Search our courses">
                                </div>
                            </div>
                            <div class="student-filter">
                                <div class="form-group select-form mb-0">
                                    <select class="form-select select" name="sellist1">
                                        <option>Newly published </option>
                                        <option>Angular</option>
                                        <option>React</option>
                                        <option>Node</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
    <!-- /Filter -->
<?php endif; ?>
<?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/components/filter.blade.php ENDPATH**/ ?>