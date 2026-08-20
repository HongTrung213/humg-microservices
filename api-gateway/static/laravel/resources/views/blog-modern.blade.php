<?php $page = 'blog-modern'; ?>
@extends('layout.mainlayout')
@section('content')
    @component('components.breadcrumb')
        @slot('title')
            Home
        @endslot
        @slot('li1')
            Pages
        @endslot
        @slot('li2')
            Blog Modern
        @endslot
    @endcomponent
    <!-- Blog Modern -->
    <section class="course-content">
        <div class="container">
            <div class="row">
                <div class="col-lg-12 col-md-12">
                    <div class="row">
                        <div class="col-md-4 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-modern">
                                <div class="blog-image">
                                    <a href="{{ url('blog-details') }}"><img class="img-fluid"
                                            src="{{ URL::asset('/assets/img/blog/blog-14.jpg') }}" alt=""></a>
                                </div>
                                <div class="blog-modern-box">
                                    <h3 class="blog-title"><a href="{{ url('blog-details') }}">Learn Webs Applications
                                            Development from Experts</a></h3>
                                    <div class="blog-info clearfix mb-0">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-22.svg') }}"
                                                        alt="">Jun 20, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-24.svg') }}"
                                                        alt="">Programming, Angular</li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                        <div class="col-md-4 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-modern">
                                <div class="blog-image">
                                    <a href="{{ url('blog-details') }}"><img class="img-fluid"
                                            src="{{ URL::asset('/assets/img/blog/blog-15.jpg') }}" alt=""></a>
                                </div>
                                <div class="blog-modern-box">
                                    <h3 class="blog-title"><a href="{{ url('blog-details') }}">Expand Your Career
                                            Opportunities With Python</a></h3>
                                    <div class="blog-info clearfix mb-0">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-22.svg') }}"
                                                        alt="">Jun 10, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-24.svg') }}"
                                                        alt="">Programming, Web Design</li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                        <div class="col-md-4 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-modern">
                                <div class="blog-image">
                                    <a href="{{ url('blog-details') }}"><img class="img-fluid"
                                            src="{{ URL::asset('/assets/img/blog/blog-16.jpg') }}" alt=""></a>
                                </div>
                                <div class="blog-modern-box">
                                    <h3 class="blog-title"><a href="{{ url('blog-details') }}">Learn Mobile Applications
                                            Development from Experts</a></h3>
                                    <div class="blog-info clearfix mb-0">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-22.svg') }}"
                                                        alt="">May 14, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-24.svg') }}"
                                                        alt="">Programming, React</li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                        <div class="col-md-4 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-modern">
                                <div class="blog-image">
                                    <a href="{{ url('blog-details') }}"><img class="img-fluid"
                                            src="{{ URL::asset('/assets/img/blog/blog-17.jpg') }}" alt=""></a>
                                </div>
                                <div class="blog-modern-box">
                                    <h3 class="blog-title"><a href="{{ url('blog-details') }}">Complete PHP Programming
                                            Career Guideline</a></h3>
                                    <div class="blog-info clearfix mb-0">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-22.svg') }}"
                                                        alt="">Jun 19, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-24.svg') }}"
                                                        alt="">Programming, Web Design</li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                        <div class="col-md-4 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-modern">
                                <div class="blog-image">
                                    <a href="{{ url('blog-details') }}"><img class="img-fluid"
                                            src="{{ URL::asset('/assets/img/blog/blog-18.jpg') }}" alt=""></a>
                                </div>
                                <div class="blog-modern-box">
                                    <h3 class="blog-title"><a href="{{ url('blog-details') }}">Programming Content
                                            Guideline For Beginners</a></h3>
                                    <div class="blog-info clearfix mb-0">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-22.svg') }}"
                                                        alt="">Jun 05, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-24.svg') }}"
                                                        alt="">Programming, Php</li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                        <div class="col-md-4 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-modern">
                                <div class="blog-image">
                                    <a href="{{ url('blog-details') }}"><img class="img-fluid"
                                            src="{{ URL::asset('/assets/img/blog/blog-19.jpg') }}" alt=""></a>
                                </div>
                                <div class="blog-modern-box">
                                    <h3 class="blog-title"><a href="{{ url('blog-details') }}">The Complete JavaScript
                                            Course for Beginners</a></h3>
                                    <div class="blog-info clearfix mb-0">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-22.svg') }}"
                                                        alt="">Jun 11, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-24.svg') }}"
                                                        alt="">Programming, Web Design</li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                        <div class="col-md-4 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-modern">
                                <div class="blog-image">
                                    <a href="{{ url('blog-details') }}"><img class="img-fluid"
                                            src="{{ URL::asset('/assets/img/blog/blog-14.jpg') }}" alt=""></a>
                                </div>
                                <div class="blog-modern-box">
                                    <h3 class="blog-title"><a href="{{ url('blog-details') }}">Learn Webs Applications
                                            Development from Experts</a></h3>
                                    <div class="blog-info clearfix mb-0">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-22.svg') }}"
                                                        alt="">Jun 14, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-24.svg') }}"
                                                        alt="">Programming, Course</li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                        <div class="col-md-4 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-modern">
                                <div class="blog-image">
                                    <a href="{{ url('blog-details') }}"><img class="img-fluid"
                                            src="{{ URL::asset('/assets/img/blog/blog-15.jpg') }}" alt=""></a>
                                </div>
                                <div class="blog-modern-box">
                                    <h3 class="blog-title"><a href="{{ url('blog-details') }}">Expand Your Career
                                            Opportunities With Python</a></h3>
                                    <div class="blog-info clearfix mb-0">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-22.svg') }}"
                                                        alt="">May 18, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-24.svg') }}"
                                                        alt="">Programming, Web Design</li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                        <div class="col-md-4 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-modern">
                                <div class="blog-image">
                                    <a href="{{ url('blog-details') }}"><img class="img-fluid"
                                            src="{{ URL::asset('/assets/img/blog/blog-16.jpg') }}" alt=""></a>
                                </div>
                                <div class="blog-modern-box">
                                    <h3 class="blog-title"><a href="{{ url('blog-details') }}">Learn Mobile Applications
                                            Development from Experts</a></h3>
                                    <div class="blog-info clearfix mb-0">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-22.svg') }}"
                                                        alt="">Jun 23, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-24.svg') }}"
                                                        alt="">Programming, Course</li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                    </div>

                    @component('components.pagination')
                    @endcomponent

                </div>
            </div>
        </div>
    </section>
    <!-- /Blog Modern -->
@endsection
