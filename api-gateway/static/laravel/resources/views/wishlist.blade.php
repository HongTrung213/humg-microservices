<?php $page = 'wishlist'; ?>
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
            Wishlists
        @endslot
    @endcomponent
    <!-- Pricing Plan -->
    <section class="course-content">
        <div class="container">
            <div class="card wish-card">
                <div class="card-header">
                    <h5>Your Wishlist (03 items)</h5>
                </div>
                <div class="card-body">
                    <div class="row">
                        <div class="col-md-12">
                            <div class="wishlist-item">
                                <div class="row align-items-center">
                                    <div class="col-md-9">
                                        <div class="wishlist-detail">
                                            <div class="wishlist-img">
                                                <a href="{{ url('course-details') }}">
                                                    <img alt=""
                                                        src="{{ URL::asset('/assets/img/course/course-01.jpg') }}">
                                                </a>
                                                <div class="price-amt">
                                                    <h4>$300</h4>
                                                </div>
                                            </div>
                                            <div class="wishlist-info">
                                                <h5><a href="{{ url('course-details') }}">Information About UI/UX Design
                                                        Degree</a></h5>
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
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-3">
                                        <div class="remove-btn">
                                            <a href="javascript:;" class="btn">Remove</a>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="wishlist-item">
                                <div class="row align-items-center">
                                    <div class="col-md-9">
                                        <div class="wishlist-detail">
                                            <div class="wishlist-img">
                                                <a href="{{ url('course-details') }}">
                                                    <img alt=""
                                                        src="{{ URL::asset('/assets/img/course/course-02.jpg') }}">
                                                </a>
                                                <div class="price-amt">
                                                    <h4>$300</h4>
                                                </div>
                                            </div>
                                            <div class="wishlist-info">
                                                <h5><a href="{{ url('course-details') }}">Wordpress for Beginners - Master
                                                        Wordpress Quickly</a></h5>
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
                                                    <i class="fas fa-star filled"></i>
                                                    <span class="d-inline-block average-rating"><span>5.0</span> (15)</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-3">
                                        <div class="remove-btn">
                                            <a href="javascript:;" class="btn">Remove</a>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <div class="wishlist-item">
                                <div class="row align-items-center">
                                    <div class="col-md-9">
                                        <div class="wishlist-detail">
                                            <div class="wishlist-img">
                                                <a href="{{ url('course-details') }}">
                                                    <img alt=""
                                                        src="{{ URL::asset('/assets/img/course/course-03.jpg') }}">
                                                </a>
                                                <div class="price-amt">
                                                    <h4>$300</h4>
                                                </div>
                                            </div>
                                            <div class="wishlist-info">
                                                <h5><a href="{{ url('course-details') }}">Sketch from A to Z (2023): Become
                                                        an app designer</a></h5>
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
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-3">
                                        <div class="remove-btn">
                                            <a href="javascript:;" class="btn">Remove</a>
                                        </div>
                                    </div>
                                </div>
                            </div>

                        </div>
                    </div>
                    <!-- /Plan Type -->

                </div>
            </div>
        </div>
    </section>
    <!-- /Pricing Plan -->
@endsection
