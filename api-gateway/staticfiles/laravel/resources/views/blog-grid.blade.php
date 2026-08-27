<?php $page = 'blog-grid'; ?>
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
            Blog Grid
        @endslot
    @endcomponent
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
                                    <a href="{{ url('blog-details') }}"><img class="img-fluid"
                                            src="{{ URL::asset('/assets/img/blog/blog-08.jpg') }}" alt="Post Image"></a>
                                </div>
                                <div class="blog-grid-box">
                                    <div class="blog-info clearfix">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-22.svg') }}"
                                                        alt="">Jun 14, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-23.svg') }}"
                                                        alt="">Programming, Web Design</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <h3 class="blog-title"><a href="{{ url('blog-details') }}">Learn Webs Applications
                                            Development from Experts</a></h3>
                                    <div class="blog-content blog-read">
                                        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit.
                                            Sed egestas, ante et vulputate volutpat, eros pede […]</p>
                                        <a href="{{ url('blog-details') }}" class="read-more btn btn-primary">Read More</a>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                        <div class="col-md-6 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-blog">
                                <div class="blog-image">
                                    <a href="{{ url('blog-details') }}"><img class="img-fluid"
                                            src="{{ URL::asset('/assets/img/blog/blog-09.jpg') }}" alt="Post Image"></a>
                                </div>
                                <div class="blog-grid-box">
                                    <div class="blog-info clearfix">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-22.svg') }}"
                                                        alt="">May 24, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-23.svg') }}"
                                                        alt="">Programming, Courses</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <h3 class="blog-title"><a href="{{ url('blog-details') }}">Expand Your Career
                                            Opportunities With Python</a></h3>
                                    <div class="blog-content blog-read">
                                        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit.
                                            Sed egestas, ante et vulputate volutpat, eros pede […]</p>
                                        <a href="{{ url('blog-details') }}" class="read-more btn btn-primary">Read More</a>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                        <div class="col-md-6 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-blog">
                                <div class="blog-image">
                                    <a href="{{ url('blog-details') }}"><img class="img-fluid"
                                            src="{{ URL::asset('/assets/img/blog/blog-10.jpg') }}" alt="Post Image"></a>
                                </div>
                                <div class="blog-grid-box">
                                    <div class="blog-info clearfix">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-22.svg') }}"
                                                        alt="">Jun 14, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-23.svg') }}"
                                                        alt="">Programming, Web Design</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <h3 class="blog-title"><a href="{{ url('blog-details') }}">Complete PHP Programming
                                            Career Guideline</a></h3>
                                    <div class="blog-content blog-read">
                                        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit.
                                            Sed egestas, ante et vulputate volutpat, eros pede […]</p>
                                        <a href="{{ url('blog-details') }}" class="read-more btn btn-primary">Read More</a>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                        <div class="col-md-6 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-blog">
                                <div class="blog-image">
                                    <a href="{{ url('blog-details') }}"><img class="img-fluid"
                                            src="{{ URL::asset('/assets/img/blog/blog-11.jpg') }}" alt="Post Image"></a>
                                </div>
                                <div class="blog-grid-box">
                                    <div class="blog-info clearfix">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-22.svg') }}"
                                                        alt="">Jun 18, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-23.svg') }}"
                                                        alt="">Programming, Courses</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <h3 class="blog-title"><a href="{{ url('blog-details') }}">Programming Content
                                            Guideline For Beginners</a></h3>
                                    <div class="blog-content blog-read">
                                        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit.
                                            Sed egestas, ante et vulputate volutpat, eros pede […]</p>
                                        <a href="{{ url('blog-details') }}" class="read-more btn btn-primary">Read More</a>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                        <div class="col-md-6 col-sm-12">

                            <!-- Blog Post -->
                            <div class="blog grid-blog">
                                <div class="blog-image">
                                    <a href="{{ url('blog-details') }}"><img class="img-fluid"
                                            src="{{ URL::asset('/assets/img/blog/blog-12.jpg') }}" alt="Post Image"></a>
                                </div>
                                <div class="blog-grid-box">
                                    <div class="blog-info clearfix">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-22.svg') }}"
                                                        alt="">Jun 26, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-23.svg') }}"
                                                        alt="">Programming, Web Design</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <h3 class="blog-title"><a href="{{ url('blog-details') }}">The Complete JavaScript
                                            Course for Beginners</a></h3>
                                    <div class="blog-content blog-read">
                                        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit.
                                            Sed egestas, ante et vulputate volutpat, eros pede […]</p>
                                        <a href="{{ url('blog-details') }}" class="read-more btn btn-primary">Read
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
                                    <a href="{{ url('blog-details') }}"><img class="img-fluid"
                                            src="{{ URL::asset('/assets/img/blog/blog-13.jpg') }}" alt="Post Image"></a>
                                </div>
                                <div class="blog-grid-box">
                                    <div class="blog-info clearfix">
                                        <div class="post-left">
                                            <ul>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-22.svg') }}"
                                                        alt="">Feb 14, 2023</li>
                                                <li><img class="img-fluid"
                                                        src="{{ URL::asset('/assets/img/icon/icon-23.svg') }}"
                                                        alt="">Programming, Courses</li>
                                            </ul>
                                        </div>
                                    </div>
                                    <h3 class="blog-title"><a href="{{ url('blog-details') }}">Learn Mobile Applications
                                            Development from Experts</a></h3>
                                    <div class="blog-content blog-read">
                                        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit.
                                            Sed egestas, ante et vulputate volutpat, eros pede […]</p>
                                        <a href="{{ url('blog-details') }}" class="read-more btn btn-primary">Read
                                            More</a>
                                    </div>
                                </div>
                            </div>
                            <!-- /Blog Post -->

                        </div>
                    </div>

                    @component('components.pagination')
                    @endcomponent

                </div>

                @component('components.blogsidebar')
                @endcomponent

            </div>
        </div>
    </section>
    <!-- /Blog Grid -->
@endsection
