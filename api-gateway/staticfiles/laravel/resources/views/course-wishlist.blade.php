<?php $page = 'course-wishlist'; ?>
@extends('layout.mainlayout')
@section('content')
    @component('components.courseheader')
    @endcomponent
    <!-- My Course -->
    <section class="course-content">
        <div class="container">
            <div class="student-widget">
                <div class="student-widget-group">
                    <div class="row">
                        <div class="col-lg-12">
                            @component('components.filter')
                            @endcomponent
                            <div class="row">
                                <div class="col-xl-3 col-lg-4 col-md-6 d-flex">
                                    <div class="course-box course-design d-flex ">
                                        <div class="product">
                                            <div class="product-img">
                                                <a href="{{ url('course-details') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/course/course-13.jpg') }}">
                                                </a>
                                                <div class="price">
                                                    <h3 class="free-color">FREE</h3>
                                                </div>
                                            </div>
                                            <div class="product-content">
                                                <div class="course-group d-flex">
                                                    <div class="course-group-img d-flex">
                                                        <a href="{{ url('student-profile') }}"><img
                                                                src="{{ URL::asset('/assets/img/user/user1.jpg') }}"
                                                                alt="" class="img-fluid"></a>
                                                        <div class="course-name">
                                                            <h4><a href="{{ url('student-profile') }}">Rolands R</a></h4>
                                                            <p>Instructor</p>
                                                        </div>
                                                    </div>
                                                    <div
                                                        class="course-share d-flex align-items-center justify-content-center">
                                                        <a href="#rate"><i class="fa-regular fa-heart"></i></a>
                                                    </div>
                                                </div>
                                                <h3 class="title"><a href="{{ url('course-details') }}">Information About
                                                        UI/UX Design Degree</a></h3>
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
                                                <div class="all-btn all-category d-flex align-items-center">
                                                    <a href="{{ url('checkout') }}" class="btn btn-primary">BUY NOW</a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xl-3 col-lg-4 col-md-6 d-flex">
                                    <div class="course-box course-design d-flex ">
                                        <div class="product">
                                            <div class="product-img">
                                                <a href="{{ url('course-details') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/course/course-14.jpg') }}">
                                                </a>
                                                <div class="price">
                                                    <h3>$300 <span>$99.00</span></h3>
                                                </div>
                                            </div>
                                            <div class="product-content">
                                                <div class="course-group d-flex">
                                                    <div class="course-group-img d-flex">
                                                        <a href="{{ url('student-profile') }}"><img
                                                                src="{{ URL::asset('/assets/img/user/user1.jpg') }}"
                                                                alt="" class="img-fluid"></a>
                                                        <div class="course-name">
                                                            <h4><a href="{{ url('student-profile') }}">Rolands R</a></h4>
                                                            <p>Instructor</p>
                                                        </div>
                                                    </div>
                                                    <div
                                                        class="course-share d-flex align-items-center justify-content-center">
                                                        <a href="#rate"><i class="fa-regular fa-heart"></i></a>
                                                    </div>
                                                </div>
                                                <h3 class="title"><a href="{{ url('course-details') }}">Information About
                                                        UI/UX Design Degree</a></h3>
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
                                                <div class="all-btn all-category d-flex align-items-center">
                                                    <a href="{{ url('checkout') }}" class="btn btn-primary">BUY NOW</a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-xl-3 col-lg-4 col-md-6 d-flex">
                                    <div class="course-box course-design d-flex ">
                                        <div class="product">
                                            <div class="product-img">
                                                <a href="{{ url('course-details') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/course/course-15.jpg') }}">
                                                </a>
                                                <div class="price">
                                                    <h3>$300 <span>$99.00</span></h3>
                                                </div>
                                            </div>
                                            <div class="product-content">
                                                <div class="course-group d-flex">
                                                    <div class="course-group-img d-flex">
                                                        <a href="{{ url('student-profile') }}"><img
                                                                src="{{ URL::asset('/assets/img/user/user1.jpg') }}"
                                                                alt="" class="img-fluid"></a>
                                                        <div class="course-name">
                                                            <h4><a href="{{ url('student-profile') }}">Rolands R</a></h4>
                                                            <p>Instructor</p>
                                                        </div>
                                                    </div>
                                                    <div
                                                        class="course-share d-flex align-items-center justify-content-center">
                                                        <a href="#rate"><i class="fa-regular fa-heart"></i></a>
                                                    </div>
                                                </div>
                                                <h3 class="title"><a href="{{ url('course-details') }}">Information
                                                        About UI/UX Design Degree</a></h3>
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
                                                <div class="all-btn all-category d-flex align-items-center">
                                                    <a href="{{ url('checkout') }}" class="btn btn-primary">BUY NOW</a>
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
    <!-- /My Course -->
@endsection
