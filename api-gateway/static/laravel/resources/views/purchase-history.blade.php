<?php $page = 'purchase-history'; ?>
@extends('layout.mainlayout')
@section('content')
    @component('components.courseheader')
    @endcomponent
    <!-- Purchase History -->
    <section class="course-content purchase-widget">
        <div class="container">
            <div class="student-widget">
                <div class="student-widget-group">
                    <div class="row">
                        <div class="col-lg-12">
                            <div class="row">
                                <div class="col-lg-12 col-md-12 d-flex">
                                    <div class="course-box course-design list-course d-flex">
                                        <div class="product">
                                            <div class="product-img">
                                                <a href="{{ url('course-details') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/course/course-10.jpg') }}">
                                                </a>
                                                <div class="price">
                                                    <h3 class="free-color">FREE</h3>
                                                </div>
                                            </div>
                                            <div class="product-content">
                                                <div class="head-course-title">
                                                    <h3 class="title"><a href="{{ url('course-details') }}">Information
                                                            About UI/UX<br> Design Degree</a></h3>
                                                    <div class="all-btn all-category d-flex align-items-center">
                                                        <a href="{{ url('view-invoice') }}"
                                                            class="btn btn-primary">Invoice</a>
                                                    </div>
                                                </div>
                                                <div class="course-info d-flex align-items-center border-bottom-0 pb-0">
                                                    <div class="rating-img d-flex align-items-center">
                                                        <img src="{{ URL::asset('/assets/img/icon/icon-01.svg') }}"
                                                            alt="">
                                                        <p>12+ Lesson</p>
                                                    </div>
                                                    <div class="course-view d-flex align-items-center">
                                                        <img src="{{ URL::asset('/assets/img/icon/icon-02.svg') }}"
                                                            alt="">
                                                        <p>9hr 30min</p>
                                                    </div>
                                                </div>
                                                <div class="rating">
                                                    <i class="fas fa-star filled"></i>
                                                    <i class="fas fa-star filled"></i>
                                                    <i class="fas fa-star filled"></i>
                                                    <i class="fas fa-star filled"></i>
                                                    <i class="fas fa-star"></i>
                                                    <span class="d-inline-block average-rating"><span>4.0</span> (15)</span>
                                                </div>
                                                <div class="course-group d-flex mb-0">
                                                    <div class="course-group-img d-flex">
                                                        <a href="{{ url('student-profile') }}"><img
                                                                src="{{ URL::asset('/assets/img/user/user1.jpg') }}"
                                                                alt="" class="img-fluid"></a>
                                                        <div class="course-name">
                                                            <h4><a href="{{ url('student-profile') }}">Rolands R</a></h4>
                                                            <p>Instructor</p>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-12 col-md-12 d-flex">
                                    <div class="course-box course-design list-course d-flex ">
                                        <div class="product">
                                            <div class="product-img">
                                                <a href="{{ url('course-details') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/course/course-11.jpg') }}">
                                                </a>
                                                <div class="price">
                                                    <h3>$300 <span>$99.00</span></h3>
                                                </div>
                                            </div>
                                            <div class="product-content">
                                                <div class="head-course-title">
                                                    <h3 class="title"><a href="{{ url('course-details') }}">Wordpress for
                                                            Beginners - Master Wordpress <br> Quickly</a></h3>
                                                    <div class="all-btn all-category d-flex align-items-center">
                                                        <a href="{{ url('view-invoice') }}"
                                                            class="btn btn-primary">Invoice</a>
                                                    </div>
                                                </div>
                                                <div class="course-info d-flex align-items-center border-bottom-0 pb-0">
                                                    <div class="rating-img d-flex align-items-center">
                                                        <img src="{{ URL::asset('/assets/img/icon/icon-01.svg') }}"
                                                            alt="">
                                                        <p>10+ Lesson</p>
                                                    </div>
                                                    <div class="course-view d-flex align-items-center">
                                                        <img src="{{ URL::asset('/assets/img/icon/icon-02.svg') }}"
                                                            alt="">
                                                        <p>7hr 20min</p>
                                                    </div>
                                                </div>
                                                <div class="rating">
                                                    <i class="fas fa-star filled"></i>
                                                    <i class="fas fa-star filled"></i>
                                                    <i class="fas fa-star filled"></i>
                                                    <i class="fas fa-star filled"></i>
                                                    <i class="fas fa-star"></i>
                                                    <span class="d-inline-block average-rating"><span>4.2</span> (15)</span>
                                                </div>
                                                <div class="course-group d-flex mb-0">
                                                    <div class="course-group-img d-flex">
                                                        <a href="{{ url('student-profile') }}"><img
                                                                src="{{ URL::asset('/assets/img/user/user2.jpg') }}"
                                                                alt="" class="img-fluid"></a>
                                                        <div class="course-name">
                                                            <h4><a href="{{ url('student-profile') }}">Jenis R.</a></h4>
                                                            <p>Instructor</p>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-lg-12 col-md-12 d-flex">
                                    <div class="course-box course-design list-course d-flex mb-0">
                                        <div class="product">
                                            <div class="product-img">
                                                <a href="{{ url('course-details') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/course/course-12.jpg') }}">
                                                </a>
                                                <div class="price">
                                                    <h3>$300 <span>$99.00</span></h3>
                                                </div>
                                            </div>
                                            <div class="product-content">
                                                <div class="head-course-title">
                                                    <h3 class="title"><a href="{{ url('course-details') }}">Sketch from A
                                                            to Z (2023): Become an app<br> designer</a></h3>
                                                    <div class="all-btn all-category d-flex align-items-center">
                                                        <a href="{{ url('view-invoice') }}"
                                                            class="btn btn-primary">Invoice</a>
                                                    </div>
                                                </div>
                                                <div class="course-info d-flex align-items-center border-bottom-0 pb-0">
                                                    <div class="rating-img d-flex align-items-center">
                                                        <img src="{{ URL::asset('/assets/img/icon/icon-01.svg') }}"
                                                            alt="">
                                                        <p>12+ Lesson</p>
                                                    </div>
                                                    <div class="course-view d-flex align-items-center">
                                                        <img src="{{ URL::asset('/assets/img/icon/icon-02.svg') }}"
                                                            alt="">
                                                        <p>9hr 30min</p>
                                                    </div>
                                                </div>
                                                <div class="rating">
                                                    <i class="fas fa-star filled"></i>
                                                    <i class="fas fa-star filled"></i>
                                                    <i class="fas fa-star filled"></i>
                                                    <i class="fas fa-star filled"></i>
                                                    <i class="fas fa-star"></i>
                                                    <span class="d-inline-block average-rating"><span>4.0</span>
                                                        (15)</span>
                                                </div>
                                                <div class="course-group d-flex mb-0">
                                                    <div class="course-group-img d-flex">
                                                        <a href="{{ url('student-profile') }}"><img
                                                                src="{{ URL::asset('/assets/img/user/user3.jpg') }}"
                                                                alt="" class="img-fluid"></a>
                                                        <div class="course-name">
                                                            <h4><a href="{{ url('student-profile') }}">Jesse Stevens</a>
                                                            </h4>
                                                            <p>Instructor</p>
                                                        </div>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <!-- /Purchase History -->
@endsection
