<?php $page = 'faq'; ?>

<?php $__env->startSection('content'); ?>
    <?php $__env->startComponent('components.breadcrumb'); ?>
        <?php $__env->slot('title'); ?>
            Home
        <?php $__env->endSlot(); ?>
        <?php $__env->slot('li1'); ?>
            Pages
        <?php $__env->endSlot(); ?>
        <?php $__env->slot('li2'); ?>
            FAQ
        <?php $__env->endSlot(); ?>
    <?php echo $__env->renderComponent(); ?>
    <?php $__env->startComponent('components.pagebanner'); ?>
        <?php $__env->slot('title'); ?>
            Most frequently asked questions
        <?php $__env->endSlot(); ?>
    <?php echo $__env->renderComponent(); ?>

    <!-- Help Details -->
    <div class="help-sec">
        <div class="container">
            <div class="row">
                <div class="col-lg-6">
                    <div class="help-title">
                        <h1>Most frequently asked questions</h1>
                        <p>Here are the most frequently asked questions you may check before getting started</p>
                    </div>
                </div>
            </div>
            <div class="row">
                <div class="col-lg-6">
                    <!-- Faq -->
                    <div class="faq-card">
                        <h6 class="faq-title">
                            <a class="collapsed" data-bs-toggle="collapse" href="#faqone" aria-expanded="false">Is there a
                                14-days trial?</a>
                        </h6>
                        <div id="faqone" class="collapse">
                            <div class="faq-detail">
                                <p>Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad
                                    squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck
                                    quinoa nesciunt laborum eiusmod.</p>
                                <p>If several languages coalesce, the grammar of the resulting language is more simple and
                                    regular than that of the individual languages. The new common language will be more
                                    simple and regular than the existing European languages.</p>
                            </div>
                        </div>
                    </div>


                    <div class="faq-card">
                        <h6 class="faq-title">
                            <a class="collapsed" data-bs-toggle="collapse" href="#faqtwo" aria-expanded="false">How much
                                time I will need to learn this app?</a>
                        </h6>
                        <div id="faqtwo" class="collapse">
                            <div class="faq-detail">
                                <p>Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad
                                    squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck
                                    quinoa nesciunt laborum eiusmod.</p>
                                <p>If several languages coalesce, the grammar of the resulting language is more simple and
                                    regular than that of the individual languages. The new common language will be more
                                    simple and regular than the existing European languages.</p>
                            </div>
                        </div>
                    </div>


                    <div class="faq-card">
                        <h6 class="faq-title">
                            <a class="collapsed" data-bs-toggle="collapse" href="#faqthree" aria-expanded="false">Is there a
                                month-to-month payment option?</a>
                        </h6>
                        <div id="faqthree" class="collapse">
                            <div class="faq-detail">
                                <p>Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad
                                    squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck
                                    quinoa nesciunt laborum eiusmod.</p>
                                <p>If several languages coalesce, the grammar of the resulting language is more simple and
                                    regular than that of the individual languages. The new common language will be more
                                    simple and regular than the existing European languages.</p>
                            </div>
                        </div>
                    </div>
                    <!-- /Faq -->

                </div>

                <div class="col-lg-6">

                    <!-- Faq -->
                    <div class="faq-card">
                        <h6 class="faq-title">
                            <a class="collapsed" data-bs-toggle="collapse" href="#faqfour" aria-expanded="false">What’s the
                                benefits of the Premium Membership?</a>
                        </h6>
                        <div id="faqfour" class="collapse">
                            <div class="faq-detail">
                                <p>Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad
                                    squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck
                                    quinoa nesciunt laborum eiusmod.</p>
                                <p>If several languages coalesce, the grammar of the resulting language is more simple and
                                    regular than that of the individual languages. The new common language will be more
                                    simple and regular than the existing European languages.</p>
                            </div>
                        </div>
                    </div>


                    <div class="faq-card">
                        <h6 class="faq-title">
                            <a class="collapsed" data-bs-toggle="collapse" href="#faqfive" aria-expanded="false">Are there
                                any free tutorials available?</a>
                        </h6>
                        <div id="faqfive" class="collapse">
                            <div class="faq-detail">
                                <p>Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad
                                    squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck
                                    quinoa nesciunt laborum eiusmod.</p>
                                <p>If several languages coalesce, the grammar of the resulting language is more simple and
                                    regular than that of the individual languages. The new common language will be more
                                    simple and regular than the existing European languages.</p>
                            </div>
                        </div>
                    </div>


                    <div class="faq-card">
                        <h6 class="faq-title">
                            <a class="collapsed" data-bs-toggle="collapse" href="#faqsix" aria-expanded="false">How can I
                                cancel my subscription plan?</a>
                        </h6>
                        <div id="faqsix" class="collapse">
                            <div class="faq-detail">
                                <p>Anim pariatur cliche reprehenderit, enim eiusmod high life accusamus terry richardson ad
                                    squid. 3 wolf moon officia aute, non cupidatat skateboard dolor brunch. Food truck
                                    quinoa nesciunt laborum eiusmod.</p>
                                <p>If several languages coalesce, the grammar of the resulting language is more simple and
                                    regular than that of the individual languages. The new common language will be more
                                    simple and regular than the existing European languages.</p>
                            </div>
                        </div>
                    </div>
                    <!-- /Faq -->

                </div>
            </div>
        </div>
    </div>
    <!-- /Help Details -->
<?php $__env->stopSection(); ?>

<?php echo $__env->make('layout.mainlayout', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?><?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/faq.blade.php ENDPATH**/ ?>