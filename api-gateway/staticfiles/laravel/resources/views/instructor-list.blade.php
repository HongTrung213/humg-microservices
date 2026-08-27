<?php $page = 'instructor-list'; ?>
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
            Instructors List
        @endslot
    @endcomponent
    <!-- Page Wrapper -->
    <div class="page-content">
        <div class="container">
            <div class="row">
                <div class="col-lg-9">
                    @component('components.filter')
                    @endcomponent
                    <div class="row">
                        <!-- Instructor List -->
                        <div class="col-lg-12 d-flex">
                            <div class="instructor-list flex-fill">
                                <div class="instructor-img">
                                    <a href="{{ url('instructor-profile') }}">
                                        <img class="img-fluid" alt=""
                                            src="{{ URL::asset('/assets/img/user/user11.jpg') }}">
                                    </a>
                                </div>
                                <div class="instructor-content">
                                    <h5><a href="{{ url('instructor-profile') }}">Rolands R</a></h5>
                                    <h6>Instructor</h6>
                                    <div class="instructor-info">
                                        <div class="rating-img d-flex align-items-center">
                                            <img src="{{ URL::asset('/assets/img/icon/icon-01.svg') }}" class="me-1"
                                                alt="">
                                            <p>12+ Lesson</p>
                                        </div>
                                        <div class="course-view d-flex align-items-center ms-0">
                                            <img src="{{ URL::asset('/assets/img/icon/icon-02.svg') }}" class="me-1"
                                                alt="">
                                            <p>9hr 30min</p>
                                        </div>
                                        <div class="rating-img d-flex align-items-center">
                                            <img src="{{ URL::asset('/assets/img/icon/user-icon.svg') }}" class="me-1"
                                                alt="">
                                            <p>50 Students</p>
                                        </div>
                                        <div class="rating">
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star"></i>
                                            <span class="d-inline-block average-rating"><span>4.0</span> (15)</span>
                                        </div>
                                        <div class="course-share rating-count">
                                            <a href="#rate"><i class="fa-regular fa-heart"></i></a>
                                        </div>
                                    </div>
                                    <div class="instructor-badge">
                                        <span class="web-badge">Web Design</span>
                                        <span class="web-badge">web development</span>
                                        <span class="web-badge">UI Design</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- /Instructor List -->

                        <!-- Instructor List -->
                        <div class="col-lg-12 d-flex">
                            <div class="instructor-list flex-fill">
                                <div class="instructor-img">
                                    <a href="{{ url('instructor-profile') }}">
                                        <img class="img-fluid" alt=""
                                            src="{{ URL::asset('/assets/img/user/user.jpg') }}">
                                    </a>
                                </div>
                                <div class="instructor-content">
                                    <h5><a href="{{ url('instructor-profile') }}">Jenis R.</a></h5>
                                    <h6>Instructor</h6>
                                    <div class="instructor-info">
                                        <div class="rating-img d-flex align-items-center justify-content-center">
                                            <img src="{{ URL::asset('/assets/img/icon/icon-01.svg') }}" class="me-1"
                                                alt="">
                                            <p>12+ Lesson</p>
                                        </div>
                                        <div class="course-view d-flex align-items-center justify-content-center">
                                            <img src="{{ URL::asset('/assets/img/icon/icon-02.svg') }}" class="me-1"
                                                alt="">
                                            <p>9hr 30min</p>
                                        </div>
                                        <div class="rating-img d-flex align-items-center">
                                            <img src="{{ URL::asset('/assets/img/icon/user-icon.svg') }}" class="me-1"
                                                alt="">
                                            <p>50 Students</p>
                                        </div>
                                        <div class="rating">
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <span class="d-inline-block average-rating"><span>5.0</span> (15)</span>
                                        </div>
                                        <div class="course-share rating-count">
                                            <a href="#rate"><i class="fa-regular fa-heart"></i></a>
                                        </div>
                                    </div>
                                    <div class="instructor-badge">
                                        <span class="web-badge">Web Design</span>
                                        <span class="web-badge">web development</span>
                                        <span class="web-badge">UI Design</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- /Instructor List -->

                        <!-- Instructor List -->
                        <div class="col-lg-12 d-flex">
                            <div class="instructor-list flex-fill">
                                <div class="instructor-img">
                                    <a href="{{ url('instructor-profile') }}">
                                        <img class="img-fluid" alt=""
                                            src="{{ URL::asset('/assets/img/user/user4.jpg') }}">
                                    </a>
                                </div>
                                <div class="instructor-content">
                                    <h5><a href="{{ url('instructor-profile') }}">Jesse Stevens</a></h5>
                                    <h6>Instructor</h6>
                                    <div class="instructor-info">
                                        <div class="rating-img d-flex align-items-center justify-content-center">
                                            <img src="{{ URL::asset('/assets/img/icon/icon-01.svg') }}" class="me-1"
                                                alt="">
                                            <p>12+ Lesson</p>
                                        </div>
                                        <div class="course-view d-flex align-items-center justify-content-center">
                                            <img src="{{ URL::asset('/assets/img/icon/icon-02.svg') }}" class="me-1"
                                                alt="">
                                            <p>9hr 30min</p>
                                        </div>
                                        <div class="rating-img d-flex align-items-center">
                                            <img src="{{ URL::asset('/assets/img/icon/user-icon.svg') }}" class="me-1"
                                                alt="">
                                            <p>50 Students</p>
                                        </div>
                                        <div class="rating">
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star"></i>
                                            <span class="d-inline-block average-rating"><span>4.0</span> (15)</span>
                                        </div>
                                        <div class="course-share rating-count">
                                            <a href="#rate"><i class="fa-regular fa-heart"></i></a>
                                        </div>
                                    </div>
                                    <div class="instructor-badge">
                                        <span class="web-badge">Web Design</span>
                                        <span class="web-badge">web development</span>
                                        <span class="web-badge">UI Design</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- /Instructor List -->

                        <!-- Instructor List -->
                        <div class="col-lg-12 d-flex">
                            <div class="instructor-list flex-fill">
                                <div class="instructor-img">
                                    <a href="{{ url('instructor-profile') }}">
                                        <img class="img-fluid" alt=""
                                            src="{{ URL::asset('/assets/img/user/user2.jpg') }}">
                                    </a>
                                </div>
                                <div class="instructor-content">
                                    <h5><a href="{{ url('instructor-profile') }}">Stevens Jes</a></h5>
                                    <h6>Instructor</h6>
                                    <div class="instructor-info">
                                        <div class="rating-img d-flex align-items-center justify-content-center">
                                            <img src="{{ URL::asset('/assets/img/icon/icon-01.svg') }}" class="me-1"
                                                alt="">
                                            <p>12+ Lesson</p>
                                        </div>
                                        <div class="course-view d-flex align-items-center justify-content-center">
                                            <img src="{{ URL::asset('/assets/img/icon/icon-02.svg') }}" class="me-1"
                                                alt="">
                                            <p>9hr 30min</p>
                                        </div>
                                        <div class="rating-img d-flex align-items-center">
                                            <img src="{{ URL::asset('/assets/img/icon/user-icon.svg') }}" class="me-1"
                                                alt="">
                                            <p>50 Students</p>
                                        </div>
                                        <div class="rating">
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <span class="d-inline-block average-rating"><span>5.0</span> (15)</span>
                                        </div>
                                        <div class="course-share rating-count">
                                            <a href="#rate"><i class="fa-regular fa-heart"></i></a>
                                        </div>
                                    </div>
                                    <div class="instructor-badge">
                                        <span class="web-badge">Web Design</span>
                                        <span class="web-badge">web development</span>
                                        <span class="web-badge">UI Design</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- /Instructor List -->

                        <!-- Instructor List -->
                        <div class="col-lg-12 d-flex">
                            <div class="instructor-list flex-fill">
                                <div class="instructor-img">
                                    <a href="{{ url('instructor-profile') }}">
                                        <img class="img-fluid" alt=""
                                            src="{{ URL::asset('/assets/img/user/user3.jpg') }}">
                                    </a>
                                </div>
                                <div class="instructor-content">
                                    <h5><a href="{{ url('instructor-profile') }}">John Smith</a></h5>
                                    <h6>Instructor</h6>
                                    <div class="instructor-info">
                                        <div class="rating-img d-flex align-items-center justify-content-center">
                                            <img src="{{ URL::asset('/assets/img/icon/icon-01.svg') }}" class="me-1"
                                                alt="">
                                            <p>12+ Lesson</p>
                                        </div>
                                        <div class="course-view d-flex align-items-center justify-content-center">
                                            <img src="{{ URL::asset('/assets/img/icon/icon-02.svg') }}" class="me-1"
                                                alt="">
                                            <p>9hr 30min</p>
                                        </div>
                                        <div class="rating-img d-flex align-items-center">
                                            <img src="{{ URL::asset('/assets/img/icon/user-icon.svg') }}" class="me-1"
                                                alt="">
                                            <p>50 Students</p>
                                        </div>
                                        <div class="rating">
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star"></i>
                                            <span class="d-inline-block average-rating"><span>4.0</span> (15)</span>
                                        </div>
                                        <div class="course-share rating-count">
                                            <a href="#rate"><i class="fa-regular fa-heart"></i></a>
                                        </div>
                                    </div>
                                    <div class="instructor-badge">
                                        <span class="web-badge">Web Design</span>
                                        <span class="web-badge">web development</span>
                                        <span class="web-badge">UI Design</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- /Instructor List -->

                        <!-- Instructor List -->
                        <div class="col-lg-12 d-flex">
                            <div class="instructor-list flex-fill">
                                <div class="instructor-img">
                                    <a href="{{ url('instructor-profile') }}">
                                        <img class="img-fluid" alt=""
                                            src="{{ URL::asset('/assets/img/user/user5.jpg') }}">
                                    </a>
                                </div>
                                <div class="instructor-content">
                                    <h5><a href="{{ url('instructor-profile') }}">Stella Johnson</a></h5>
                                    <h6>Instructor</h6>
                                    <div class="instructor-info">
                                        <div class="rating-img d-flex align-items-center justify-content-center">
                                            <img src="{{ URL::asset('/assets/img/icon/icon-01.svg') }}" class="me-1"
                                                alt="">
                                            <p>12+ Lesson</p>
                                        </div>
                                        <div class="course-view d-flex align-items-center justify-content-center">
                                            <img src="{{ URL::asset('/assets/img/icon/icon-02.svg') }}" class="me-1"
                                                alt="">
                                            <p>9hr 30min</p>
                                        </div>
                                        <div class="rating-img d-flex align-items-center">
                                            <img src="{{ URL::asset('/assets/img/icon/user-icon.svg') }}" class="me-1"
                                                alt="">
                                            <p>50 Students</p>
                                        </div>
                                        <div class="rating">
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star"></i>
                                            <span class="d-inline-block average-rating"><span>4.0</span> (15)</span>
                                        </div>
                                        <div class="course-share rating-count">
                                            <a href="#rate"><i class="fa-regular fa-heart"></i></a>
                                        </div>
                                    </div>
                                    <div class="instructor-badge">
                                        <span class="web-badge">Web Design</span>
                                        <span class="web-badge">web development</span>
                                        <span class="web-badge">UI Design</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- /Instructor List -->

                        <!-- Instructor List -->
                        <div class="col-lg-12 d-flex">
                            <div class="instructor-list flex-fill">
                                <div class="instructor-img">
                                    <a href="{{ url('instructor-profile') }}">
                                        <img class="img-fluid" alt=""
                                            src="{{ URL::asset('/assets/img/user/user12.jpg') }}">
                                    </a>
                                </div>
                                <div class="instructor-content">
                                    <h5><a href="{{ url('instructor-profile') }}">John Michael</a></h5>
                                    <h6>Instructor</h6>
                                    <div class="instructor-info">
                                        <div class="rating-img d-flex align-items-center justify-content-center">
                                            <img src="{{ URL::asset('/assets/img/icon/icon-01.svg') }}" class="me-1"
                                                alt="">
                                            <p>12+ Lesson</p>
                                        </div>
                                        <div class="course-view d-flex align-items-center justify-content-center">
                                            <img src="{{ URL::asset('/assets/img/icon/icon-02.svg') }}" class="me-1"
                                                alt="">
                                            <p>9hr 30min</p>
                                        </div>
                                        <div class="rating-img d-flex align-items-center">
                                            <img src="{{ URL::asset('/assets/img/icon/user-icon.svg') }}" class="me-1"
                                                alt="">
                                            <p>50 Students</p>
                                        </div>
                                        <div class="rating">
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <i class="fas fa-star filled"></i>
                                            <span class="d-inline-block average-rating"><span>5.0</span> (15)</span>
                                        </div>
                                        <div class="course-share rating-count">
                                            <a href="#rate"><i class="fa-regular fa-heart"></i></a>
                                        </div>
                                    </div>
                                    <div class="instructor-badge">
                                        <span class="web-badge">Web Design</span>
                                        <span class="web-badge">web development</span>
                                        <span class="web-badge">UI Design</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- /Instructor List -->

                    </div>

                    @component('components.pagination')
                    @endcomponent

                </div>

                <div class="col-lg-3">
                    <div class="filter-clear">
                        <div class="clear-filter d-flex align-items-center">
                            <h4><i class="feather-filter"></i>Filters</h4>
                            <div class="clear-text">
                                <p>CLEAR</p>
                            </div>
                        </div>

                        <!-- Search Filter -->
                        <div class="card search-filter">
                            <div class="card-body">
                                <div class="filter-widget mb-0">
                                    <div class="categories-head d-flex align-items-center">
                                        <h4>Course categories</h4>
                                        <i class="fas fa-angle-down"></i>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist">
                                            <span class="checkmark"></span> Backend (3)

                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist">
                                            <span class="checkmark"></span> CSS (2)
                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist">
                                            <span class="checkmark"></span> Frontend (2)
                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist" checked>
                                            <span class="checkmark"></span> General (2)
                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist" checked>
                                            <span class="checkmark"></span> IT & Software (2)
                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist">
                                            <span class="checkmark"></span> Photography (2)
                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist">
                                            <span class="checkmark"></span> Programming Language (3)
                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check mb-0">
                                            <input type="checkbox" name="select_specialist">
                                            <span class="checkmark"></span> Technology (2)
                                        </label>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- /Search Filter -->

                        <!-- Search Filter -->
                        <div class="card search-filter">
                            <div class="card-body">
                                <div class="filter-widget mb-0">
                                    <div class="categories-head d-flex align-items-center">
                                        <h4>Instructors</h4>
                                        <i class="fas fa-angle-down"></i>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist">
                                            <span class="checkmark"></span> Keny White (10)

                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist">
                                            <span class="checkmark"></span> Hinata Hyuga (5)
                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check">
                                            <input type="checkbox" name="select_specialist">
                                            <span class="checkmark"></span> John Doe (3)
                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check mb-0">
                                            <input type="checkbox" name="select_specialist" checked>
                                            <span class="checkmark"></span> Nicole Brown
                                        </label>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- /Search Filter -->

                        <!-- Search Filter -->
                        <div class="card search-filter ">
                            <div class="card-body">
                                <div class="filter-widget mb-0">
                                    <div class="categories-head d-flex align-items-center">
                                        <h4>Price</h4>
                                        <i class="fas fa-angle-down"></i>
                                    </div>
                                    <div>
                                        <label class="custom_check custom_one">
                                            <input type="radio" name="select_specialist">
                                            <span class="checkmark"></span> All (18)

                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check custom_one">
                                            <input type="radio" name="select_specialist">
                                            <span class="checkmark"></span> Free (3)

                                        </label>
                                    </div>
                                    <div>
                                        <label class="custom_check custom_one mb-0">
                                            <input type="radio" name="select_specialist" checked>
                                            <span class="checkmark"></span> Paid (15)
                                        </label>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- /Search Filter -->

                    </div>
                </div>

            </div>
        </div>
    </div>
    <!-- /Page Wrapper -->
@endsection
