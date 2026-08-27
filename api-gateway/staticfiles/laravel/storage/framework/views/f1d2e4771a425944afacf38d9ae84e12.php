<?php $page = 'blog-list'; ?>

<?php $__env->startSection('content'); ?>
    <?php $__env->startComponent('components.breadcrumb'); ?>
        <?php $__env->slot('title'); ?>
            Home
        <?php $__env->endSlot(); ?>
        <?php $__env->slot('li1'); ?>
            Pages
        <?php $__env->endSlot(); ?>
        <?php $__env->slot('li2'); ?>
            Blog List
        <?php $__env->endSlot(); ?>
    <?php echo $__env->renderComponent(); ?>
    <!-- Course -->
    <section class="course-content">
        <div class="container">
            <div class="row">
                <div class="col-lg-9 col-md-12">

                    <!-- Blog Post -->
                    <div class="blog">
                        <div class="blog-image">
                            <a href="<?php echo e(url('blog-details')); ?>"><img class="img-fluid"
                                    src="<?php echo e(URL::asset('/assets/img/blog/blog-05.jpg')); ?>" alt="Post Image"></a>
                        </div>
                        <div class="blog-info clearfix">
                            <div class="post-left">
                                <ul>
                                    <li>
                                        <div class="post-author">
                                            <a href="<?php echo e(url('instructor-profile')); ?>"><img
                                                    src="<?php echo e(URL::asset('/assets/img/user/user.jpg')); ?>" alt="Post Author">
                                                <span>Ruby Perrin</span></a>
                                        </div>
                                    </li>
                                    <li><img class="img-fluid" src="<?php echo e(URL::asset('/assets/img/icon/icon-22.svg')); ?>"
                                            alt="">April 20, 2023</li>
                                    <li><img class="img-fluid" src="<?php echo e(URL::asset('/assets/img/icon/icon-23.svg')); ?>"
                                            alt="">Programming, Web Design</li>
                                </ul>
                            </div>
                        </div>
                        <h3 class="blog-title"><a href="<?php echo e(url('blog-details')); ?>">Learn Webs Applications Development from
                                Experts</a></h3>
                        <div class="blog-content blog-read">
                            <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit. Pellentesque
                                aliquet nibh nec urna. In nisi neque, aliquet vel, dapibus id, mattis vel, nisi. Sed
                                pretium, ligula sollicitudin laoreet viverra, tortor libero sodales leo, eget blandit nunc
                                tortor eu nibh. Nullam mollis. Ut justo. Suspendisse potenti. Sed egestas, ante et vulputate
                                volutpat, eros pede […]</p>
                            <a href="<?php echo e(url('blog-details')); ?>" class="read-more btn btn-primary">Read More</a>
                        </div>
                    </div>
                    <!-- /Blog Post -->

                    <!-- Blog Post -->
                    <div class="blog">
                        <div class="blog-image">
                            <a href="<?php echo e(url('blog-details')); ?>"><img class="img-fluid"
                                    src="<?php echo e(URL::asset('/assets/img/blog/blog-06.jpg')); ?>" alt="Post Image"></a>
                        </div>
                        <div class="blog-info clearfix">
                            <div class="post-left">
                                <ul>
                                    <li>
                                        <div class="post-author">
                                            <a href="<?php echo e(url('instructor-profile')); ?>"><img
                                                    src="<?php echo e(URL::asset('/assets/img/user/user1.jpg')); ?>" alt="Post Author">
                                                <span>Jenis R.</span></a>
                                        </div>
                                    </li>
                                    <li><img class="img-fluid" src="<?php echo e(URL::asset('/assets/img/icon/icon-22.svg')); ?>"
                                            alt="">June 20, 2023</li>
                                    <li><img class="img-fluid" src="<?php echo e(URL::asset('/assets/img/icon/icon-23.svg')); ?>"
                                            alt="">Programming, Courses</li>
                                </ul>
                            </div>
                        </div>
                        <h3 class="blog-title"><a href="<?php echo e(url('blog-details')); ?>">Expand Your Career Opportunities With
                                Python</a></h3>
                        <div class="blog-content blog-read">
                            <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit. Pellentesque
                                aliquet nibh nec urna. In nisi neque, aliquet vel, dapibus id, mattis vel, nisi. Sed
                                pretium, ligula sollicitudin laoreet viverra, tortor libero sodales leo, eget blandit nunc
                                tortor eu nibh. Nullam mollis. Ut justo. Suspendisse potenti. Sed egestas, ante et vulputate
                                volutpat, eros pede […]</p>
                            <a href="<?php echo e(url('blog-details')); ?>" class="read-more btn btn-primary">Read More</a>
                        </div>
                    </div>
                    <!-- /Blog Post -->

                    <!-- Blog Post -->
                    <div class="blog">
                        <div class="blog-image">
                            <a href="<?php echo e(url('blog-details')); ?>"><img class="img-fluid"
                                    src="<?php echo e(URL::asset('/assets/img/blog/blog-07.jpg')); ?>" alt="Post Image"></a>
                        </div>
                        <div class="blog-info clearfix">
                            <div class="post-left">
                                <ul>
                                    <li>
                                        <div class="post-author">
                                            <a href="<?php echo e(url('instructor-profile')); ?>"><img
                                                    src="<?php echo e(URL::asset('/assets/img/user/user3.jpg')); ?>" alt="Post Author">
                                                <span>Rolands R</span></a>
                                        </div>
                                    </li>
                                    <li><img class="img-fluid" src="<?php echo e(URL::asset('/assets/img/icon/icon-22.svg')); ?>"
                                            alt="">June 14, 2023</li>
                                    <li><img class="img-fluid" src="<?php echo e(URL::asset('/assets/img/icon/icon-23.svg')); ?>"
                                            alt="">Programming, Web Design</li>
                                </ul>
                            </div>
                        </div>
                        <h3 class="blog-title"><a href="<?php echo e(url('blog-details')); ?>">Complete PHP Programming Career
                                Guideline</a></h3>
                        <div class="blog-content blog-read">
                            <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit. Pellentesque
                                aliquet nibh nec urna. In nisi neque, aliquet vel, dapibus id, mattis vel, nisi. Sed
                                pretium, ligula sollicitudin laoreet viverra, tortor libero sodales leo, eget blandit nunc
                                tortor eu nibh. Nullam mollis. Ut justo. Suspendisse potenti. Sed egestas, ante et vulputate
                                volutpat, eros pede […]</p>
                            <a href="<?php echo e(url('blog-details')); ?>" class="read-more btn btn-primary">Read More</a>
                        </div>
                    </div>
                    <!-- /Blog Post -->

                    <?php $__env->startComponent('components.pagination'); ?>
                    <?php echo $__env->renderComponent(); ?>

                </div>

                <?php $__env->startComponent('components.blogsidebar'); ?>
                <?php echo $__env->renderComponent(); ?>

            </div>
        </div>
    </section>
    <!-- /Course -->
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\dreams-lms_laravel\resources\views/blog-list.blade.php ENDPATH**/ ?>