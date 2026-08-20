<?php $page = 'course-student'; ?>
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
                                                        src="{{ URL::asset('/assets/img/course/course-10.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="product-content">
                                                <h3 class="title"><a href="{{ url('course-details') }}">Information About
                                                        UI/UX Design Degree</a></h3>
                                                <div class="rating-student">
                                                    <div class="rating">
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star"></i>
                                                        <span class="d-inline-block average-rating"><span>4.0</span></span>
                                                    </div>
                                                    <div class="edit-rate">
                                                        <a href="javascript:;">Edit rating</a>
                                                    </div>
                                                </div>
                                                <div class="progress-stip">
                                                    <div class="progress-bar bg-success progress-bar-striped active-stip">
                                                    </div>
                                                </div>
                                                <div class="student-percent">
                                                    <p>35% Completed</p>
                                                </div>
                                                <div class="start-leason d-flex align-items-center">
                                                    <a href="{{ url('course-lesson') }}" class="btn btn-primary">Start
                                                        Lesson</a>
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
                                                        src="{{ URL::asset('/assets/img/course/course-11.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="product-content">
                                                <h3 class="title"><a href="{{ url('course-details') }}">Wordpress for
                                                        Beginners - Master Wordpress Quickly</a></h3>
                                                <div class="rating-student">
                                                    <div class="rating">
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star"></i>
                                                        <span class="d-inline-block average-rating"><span>4.0</span> </span>
                                                    </div>
                                                    <div class="edit-rate">
                                                        <a href="javascript:;">Edit rating</a>
                                                    </div>
                                                </div>
                                                <div class="progress-stip">
                                                    <div class="progress-bar bg-success progress-bar-striped "></div>
                                                </div>
                                                <div class="student-percent">
                                                    <p>0% Completed</p>
                                                </div>
                                                <div class="start-leason d-flex align-items-center">
                                                    <a href="{{ url('course-lesson') }}" class="btn btn-primary">Start
                                                        Lesson</a>
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
                                                        src="{{ URL::asset('/assets/img/course/course-12.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="product-content">
                                                <h3 class="title"><a href="{{ url('course-details') }}">Sketch from A to Z
                                                        (2023): Become an app designer</a></h3>
                                                <div class="rating-student">
                                                    <div class="rating">
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star"></i>
                                                        <span class="d-inline-block average-rating"><span>4.0</span></span>
                                                    </div>
                                                    <div class="edit-rate">
                                                        <a href="javascript:;">Edit rating</a>
                                                    </div>
                                                </div>
                                                <div class="progress-stip">
                                                    <div class="progress-bar bg-success progress-bar-striped"></div>
                                                </div>
                                                <div class="student-percent">
                                                    <p>0% Completed</p>
                                                </div>
                                                <div class="start-leason d-flex align-items-center">
                                                    <a href="{{ url('course-lesson') }}" class="btn btn-primary">Start
                                                        Lesson</a>
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
                                                        src="{{ URL::asset('/assets/img/course/course-13.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="product-content">
                                                <h3 class="title"><a href="{{ url('course-details') }}">Learn Angular
                                                        Fundamentals From ...</a></h3>
                                                <div class="rating-student">
                                                    <div class="rating">
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star"></i>
                                                        <span class="d-inline-block average-rating"><span>4.0</span></span>
                                                    </div>
                                                    <div class="edit-rate">
                                                        <a href="javascript:;">Edit rating</a>
                                                    </div>
                                                </div>
                                                <div class="progress-stip">
                                                    <div class="progress-bar bg-success progress-bar-striped "></div>
                                                </div>
                                                <div class="student-percent">
                                                    <p>0% Completed</p>
                                                </div>
                                                <div class="start-leason d-flex align-items-center">
                                                    <a href="{{ url('course-lesson') }}" class="btn btn-primary">Start
                                                        Lesson</a>
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
                                            </div>
                                            <div class="product-content">
                                                <h3 class="title"><a href="{{ url('course-details') }}">Build Responsive
                                                        Real World Websites with...</a></h3>
                                                <div class="rating-student">
                                                    <div class="rating">
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star"></i>
                                                        <span class="d-inline-block average-rating"><span>4.0</span></span>
                                                    </div>
                                                    <div class="edit-rate">
                                                        <a href="javascript:;">Edit rating</a>
                                                    </div>
                                                </div>
                                                <div class="progress-stip">
                                                    <div class="progress-bar bg-success progress-bar-striped "></div>
                                                </div>
                                                <div class="student-percent">
                                                    <p>0% Completed</p>
                                                </div>
                                                <div class="start-leason d-flex align-items-center">
                                                    <a href="{{ url('course-lesson') }}" class="btn btn-primary">Start
                                                        Lesson</a>
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
                                            </div>
                                            <div class="product-content">
                                                <h3 class="title"><a href="{{ url('course-details') }}">C# Developers
                                                        Double Your Coding Speed with ...</a></h3>
                                                <div class="rating-student">
                                                    <div class="rating">
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star"></i>
                                                        <span class="d-inline-block average-rating"><span>4.0</span></span>
                                                    </div>
                                                    <div class="edit-rate">
                                                        <a href="javascript:;">Edit rating</a>
                                                    </div>
                                                </div>
                                                <div class="progress-stip">
                                                    <div class="progress-bar bg-success progress-bar-striped "></div>
                                                </div>
                                                <div class="student-percent">
                                                    <p>0% Completed</p>
                                                </div>
                                                <div class="start-leason d-flex align-items-center">
                                                    <a href="{{ url('course-lesson') }}" class="btn btn-primary">Start
                                                        Lesson</a>
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
                                                        src="{{ URL::asset('/assets/img/course/course-16.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="product-content">
                                                <h3 class="title"><a href="{{ url('course-details') }}">Learn JavaScript
                                                        and Express to become a ...</a></h3>
                                                <div class="rating-student">
                                                    <div class="rating">
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star"></i>
                                                        <span class="d-inline-block average-rating"><span>4.0</span></span>
                                                    </div>
                                                    <div class="edit-rate">
                                                        <a href="javascript:;">Edit rating</a>
                                                    </div>
                                                </div>
                                                <div class="progress-stip">
                                                    <div class="progress-bar bg-success progress-bar-striped "></div>
                                                </div>
                                                <div class="student-percent">
                                                    <p>0% Completed</p>
                                                </div>
                                                <div class="start-leason d-flex align-items-center">
                                                    <a href="{{ url('course-lesson') }}" class="btn btn-primary">Start
                                                        Lesson</a>
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
                                                        src="{{ URL::asset('/assets/img/course/course-17.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="product-content">
                                                <h3 class="title"><a href="{{ url('course-details') }}">Responsive Web
                                                        Design Essentials HTML5 CSS3 ...</a></h3>
                                                <div class="rating-student">
                                                    <div class="rating">
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star filled"></i>
                                                        <i class="fas fa-star"></i>
                                                        <span class="d-inline-block average-rating"><span>4.0</span></span>
                                                    </div>
                                                    <div class="edit-rate">
                                                        <a id="edit-rating">Edit rating</a>
                                                    </div>
                                                </div>
                                                <div class="publish-rate">
                                                    <form action="#">
                                                        <select class="form-select" name="sellist1">
                                                            <option>4 Out of 5</option>
                                                            <option>3 Out of 5</option>
                                                            <option>2 Out of 5</option>
                                                            <option>1 Out of 5</option>
                                                        </select>
                                                        <div class="form-group mt-3">
                                                            <textarea class="form-control" rows="4" name="text"></textarea>
                                                        </div>
                                                        <div class="group-btn mb-3">
                                                            <button type="submit"
                                                                class="btn btn-primary publish-btn mb-3">Publish
                                                                Rating</button>
                                                            <button type="submit"
                                                                class="btn btn-primary cancel-btn">Cancel</button>
                                                        </div>
                                                    </form>
                                                </div>
                                                <div class="stip-grp">
                                                    <div class="progress-stip">
                                                        <div class="progress-bar bg-success progress-bar-striped "></div>
                                                    </div>
                                                    <div class="student-percent">
                                                        <p>0% Completed</p>
                                                    </div>
                                                    <div class="start-leason d-flex align-items-center">
                                                        <a href="{{ url('course-lesson') }}"
                                                            class="btn btn-primary">Start Lesson</a>
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
    <!-- /My Course -->
@endsection
