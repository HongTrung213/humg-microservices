<?php $page = 'blog-grid'; ?>

<?php $__env->startSection('content'); ?>
    <?php $__env->startComponent('components.breadcrumb'); ?>
        <?php $__env->slot('title'); ?>
            Home
        <?php $__env->endSlot(); ?>
        <?php $__env->slot('li1'); ?>
            Pages
        <?php $__env->endSlot(); ?>
        <?php $__env->slot('li2'); ?>
            Blog Grid
        <?php $__env->endSlot(); ?>
    <?php echo $__env->renderComponent(); ?>
    <!-- Blog Grid -->
    <section class="course-content">
        <div class="container">
            <div class="row">
                <div class="col-lg-9 col-md-12">
                    <div class="row">
                        <div class="col-md-6 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-blog">
                                <div class="blog-image">
                                    <a href="<?php echo e(url('blog-details')); ?>"><img class="img-fluid"
                                            src="<?php echo e(URL::asset('/assets/img/blog/blog-08.jpg')); ?>" alt="Post Image"></a>
                                </div>
                                <div class="blog-grid-box">
                                    <div class="blog-info clearfix">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="<?php echo e(URL::asset('/assets/img/icon/icon-22.svg')); ?>"
                                                        alt="">Jun 14, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="<?php echo e(URL::asset('/assets/img/icon/icon-23.svg')); ?>"
                                                        alt="">Programming, Web Design</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <h3 class="blog-title"><a href="<?php echo e(url('blog-details')); ?>">Learn Webs Applications
                                            Development from Experts</a></h3>
                                    <div class="blog-content blog-read">
                                        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit.
                                            Sed egestas, ante et vulputate volutpat, eros pede […]</p>
                                        <a href="<?php echo e(url('blog-details')); ?>" class="read-more btn btn-primary">Read More</a>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                        <div class="col-md-6 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-blog">
                                <div class="blog-image">
                                    <a href="<?php echo e(url('blog-details')); ?>"><img class="img-fluid"
                                            src="<?php echo e(URL::asset('/assets/img/blog/blog-09.jpg')); ?>" alt="Post Image"></a>
                                </div>
                                <div class="blog-grid-box">
                                    <div class="blog-info clearfix">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="<?php echo e(URL::asset('/assets/img/icon/icon-22.svg')); ?>"
                                                        alt="">May 24, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="<?php echo e(URL::asset('/assets/img/icon/icon-23.svg')); ?>"
                                                        alt="">Programming, Courses</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <h3 class="blog-title"><a href="<?php echo e(url('blog-details')); ?>">Expand Your Career
                                            Opportunities With Python</a></h3>
                                    <div class="blog-content blog-read">
                                        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit.
                                            Sed egestas, ante et vulputate volutpat, eros pede […]</p>
                                        <a href="<?php echo e(url('blog-details')); ?>" class="read-more btn btn-primary">Read More</a>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                        <div class="col-md-6 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-blog">
                                <div class="blog-image">
                                    <a href="<?php echo e(url('blog-details')); ?>"><img class="img-fluid"
                                            src="<?php echo e(URL::asset('/assets/img/blog/blog-10.jpg')); ?>" alt="Post Image"></a>
                                </div>
                                <div class="blog-grid-box">
                                    <div class="blog-info clearfix">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="<?php echo e(URL::asset('/assets/img/icon/icon-22.svg')); ?>"
                                                        alt="">Jun 14, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="<?php echo e(URL::asset('/assets/img/icon/icon-23.svg')); ?>"
                                                        alt="">Programming, Web Design</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <h3 class="blog-title"><a href="<?php echo e(url('blog-details')); ?>">Complete PHP Programming
                                            Career Guideline</a></h3>
                                    <div class="blog-content blog-read">
                                        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit.
                                            Sed egestas, ante et vulputate volutpat, eros pede […]</p>
                                        <a href="<?php echo e(url('blog-details')); ?>" class="read-more btn btn-primary">Read More</a>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                        <div class="col-md-6 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-blog">
                                <div class="blog-image">
                                    <a href="<?php echo e(url('blog-details')); ?>"><img class="img-fluid"
                                            src="<?php echo e(URL::asset('/assets/img/blog/blog-11.jpg')); ?>" alt="Post Image"></a>
                                </div>
                                <div class="blog-grid-box">
                                    <div class="blog-info clearfix">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="<?php echo e(URL::asset('/assets/img/icon/icon-22.svg')); ?>"
                                                        alt="">Jun 18, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="<?php echo e(URL::asset('/assets/img/icon/icon-23.svg')); ?>"
                                                        alt="">Programming, Courses</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <h3 class="blog-title"><a href="<?php echo e(url('blog-details')); ?>">Programming Content
                                            Guideline For Beginners</a></h3>
                                    <div class="blog-content blog-read">
                                        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit.
                                            Sed egestas, ante et vulputate volutpat, eros pede […]</p>
                                        <a href="<?php echo e(url('blog-details')); ?>" class="read-more btn btn-primary">Read More</a>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                        <div class="col-md-6 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-blog">
                                <div class="blog-image">
                                    <a href="<?php echo e(url('blog-details')); ?>"><img class="img-fluid"
                                            src="<?php echo e(URL::asset('/assets/img/blog/blog-12.jpg')); ?>" alt="Post Image"></a>
                                </div>
                                <div class="blog-grid-box">
                                    <div class="blog-info clearfix">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="<?php echo e(URL::asset('/assets/img/icon/icon-22.svg')); ?>"
                                                        alt="">Jun 26, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="<?php echo e(URL::asset('/assets/img/icon/icon-23.svg')); ?>"
                                                        alt="">Programming, Web Design</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <h3 class="blog-title"><a href="<?php echo e(url('blog-details')); ?>">The Complete JavaScript
                                            Course for Beginners</a></h3>
                                    <div class="blog-content blog-read">
                                        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit.
                                            Sed egestas, ante et vulputate volutpat, eros pede […]</p>
                                        <a href="<?php echo e(url('blog-details')); ?>" class="read-more btn btn-primary">Read
                                            More</a>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                        <div class="col-md-6 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-blog">
                                <div class="blog-image">
                                    <a href="<?php echo e(url('blog-details')); ?>"><img class="img-fluid"
                                            src="<?php echo e(URL::asset('/assets/img/blog/blog-13.jpg')); ?>" alt="Post Image"></a>
                                </div>
                                <div class="blog-grid-box">
                                    <div class="blog-info clearfix">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="<?php echo e(URL::asset('/assets/img/icon/icon-22.svg')); ?>"
                                                        alt="">Feb 14, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="<?php echo e(URL::asset('/assets/img/icon/icon-23.svg')); ?>"
                                                        alt="">Programming, Courses</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <h3 class="blog-title"><a href="<?php echo e(url('blog-details')); ?>">Learn Mobile Applications
                                            Development from Experts</a></h3>
                                    <div class="blog-content blog-read">
                                        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit.
                                            Sed egestas, ante et vulputate volutpat, eros pede […]</p>
                                        <a href="<?php echo e(url('blog-details')); ?>" class="read-more btn btn-primary">Read
                                            More</a>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                    </div>

                    <?php $__env->startComponent('components.pagination'); ?>
                    <?php echo $__env->renderComponent(); ?>

                </div>

                <?php $__env->startComponent('components.blogsidebar'); ?>
                <?php echo $__env->renderComponent(); ?>

            </div>
        </div>
    </section>
    <!-- /Blog Grid -->
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/blog-grid.blade.php ENDPATH**/ ?>