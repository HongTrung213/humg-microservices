<?php $page = 'instructor-student-grid'; ?>
@extends('layout.mainlayout')
@section('content')
    <!-- Page Wrapper -->
    <div class="page-content">
        <div class="container">
            <div class="row">
                @component('components.sidebar')
                @endcomponent
                <!-- Instructor Dashboard -->
                <div class="col-xl-9 col-lg-8 col-md-12">
                    <div class="tak-instruct-group">
                        <div class="row">
                            <div class="col-md-12">
                                <div class="settings-widget">
                                    <div class="settings-inner-blk p-0">
                                        <div class="sell-course-head student-meet-head comman-space border-0">
                                            <div class="tak-head d-flex align-items-center">
                                                <div>
                                                    <h3>Students</h3>
                                                    <p>Meet people taking your course.</p>
                                                </div>
                                                <div class="view-icons">
                                                    <a href="{{ url('instructor-student-grid') }}"
                                                        class="grid-view active"><i class="feather-grid"></i></a>
                                                    <a href="{{ url('instructor-student-list') }}" class="list-view"><i
                                                            class="feather-list"></i></a>
                                                </div>
                                            </div>
                                            <form>
                                                <div class="student-search-form d-flex ">
                                                    <div class="form-group mb-0">
                                                        <input type="text" class="form-control"
                                                            placeholder="Twitter Profile Name">
                                                    </div>
                                                    <div class="export-cvv-btn">
                                                        <button class="btn btn-primary">Export CSV</button>
                                                    </div>
                                                </div>
                                            </form>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                                <div class="student-box flex-fill">
                                    <div class="student-box-blks">
                                        <div class="message-text-img">
                                            <a href="javascript:;">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/icon/message-text.svg') }}">
                                            </a>
                                        </div>
                                        <div class="student-img">
                                            <a href="{{ url('student-profile') }}">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/user/user1.jpg') }}">
                                            </a>
                                        </div>
                                        <div class="student-content pb-0">
                                            <h5><a href="{{ url('student-profile') }}">Wade Warren</a></h5>
                                            <div class="loc-blk d-flex align-items-center justify-content-center">
                                                <i class="feather-map-pin me-2"></i>
                                                <p>United States</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="enrol-student-foot">
                                        <ul>
                                            <li>Enrolled <span>3/12/2020</span></li>
                                            <li>Progress
                                                <div class="instruct-stip d-flex align-items-center">
                                                    <span>20%</span>
                                                    <div class="course-stip progress-stip">
                                                        <div
                                                            class="progress-bar bg-success progress-bar-striped active-stip">
                                                        </div>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                                <div class="student-box flex-fill">
                                    <div class="student-box-blks">
                                        <div class="message-text-img">
                                            <a href="javascript:;">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/icon/message-text.svg') }}">
                                            </a>
                                        </div>
                                        <div class="student-img">
                                            <a href="{{ url('student-profile') }}">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/user/user3.jpg') }}">
                                            </a>
                                        </div>
                                        <div class="student-content pb-0">
                                            <h5><a href="{{ url('student-profile') }}">Dianna Smiley</a></h5>
                                            <div class="loc-blk d-flex align-items-center justify-content-center">
                                                <i class="feather-map-pin me-2"></i>
                                                <p>Tunisia</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="enrol-student-foot">
                                        <ul>
                                            <li>Enrolled <span>15/06/2023</span></li>
                                            <li>Progress
                                                <div class="instruct-stip d-flex align-items-center">
                                                    <span>20%</span>
                                                    <div class="course-stip progress-stip">
                                                        <div
                                                            class="progress-bar bg-success progress-bar-striped active-stip">
                                                        </div>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                                <div class="student-box flex-fill">
                                    <div class="student-box-blks">
                                        <div class="message-text-img">
                                            <a href="javascript:;">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/icon/message-text.svg') }}">
                                            </a>
                                        </div>
                                        <div class="student-img">
                                            <a href="{{ url('student-profile') }}">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/user/user2.jpg') }}">
                                            </a>
                                        </div>
                                        <div class="student-content pb-0">
                                            <h5><a href="{{ url('student-profile') }}">Esther Howard</a></h5>
                                            <div class="loc-blk d-flex align-items-center justify-content-center">
                                                <i class="feather-map-pin me-2"></i>
                                                <p>Spain</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="enrol-student-foot">
                                        <ul>
                                            <li>Enrolled <span>6/10/2020</span></li>
                                            <li>Progress
                                                <div class="instruct-stip d-flex align-items-center">
                                                    <span>20%</span>
                                                    <div class="course-stip progress-stip">
                                                        <div
                                                            class="progress-bar bg-success progress-bar-striped active-stip">
                                                        </div>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                                <div class="student-box flex-fill">
                                    <div class="student-box-blks">
                                        <div class="message-text-img">
                                            <a href="javascript:;">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/icon/message-text.svg') }}">
                                            </a>
                                        </div>
                                        <div class="student-img">
                                            <a href="{{ url('student-profile') }}">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/user/user5.jpg') }}">
                                            </a>
                                        </div>
                                        <div class="student-content pb-0">
                                            <h5><a href="{{ url('student-profile') }}">Guy Hawkins</a></h5>
                                            <div class="loc-blk d-flex align-items-center justify-content-center">
                                                <i class="feather-map-pin me-2"></i>
                                                <p>United States</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="enrol-student-foot">
                                        <ul>
                                            <li>Enrolled <span>13/1/2020</span></li>
                                            <li>Progress
                                                <div class="instruct-stip d-flex align-items-center">
                                                    <span>20%</span>
                                                    <div class="course-stip progress-stip">
                                                        <div
                                                            class="progress-bar bg-success progress-bar-striped active-stip">
                                                        </div>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                                <div class="student-box flex-fill">
                                    <div class="student-box-blks">
                                        <div class="message-text-img">
                                            <a href="javascript:;">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/icon/message-text.svg') }}">
                                            </a>
                                        </div>
                                        <div class="student-img">
                                            <a href="{{ url('student-profile') }}">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/user/user6.jpg') }}">
                                            </a>
                                        </div>
                                        <div class="student-content pb-0">
                                            <h5><a href="{{ url('student-profile') }}">Jacob Jones</a></h5>
                                            <div class="loc-blk d-flex align-items-center justify-content-center">
                                                <i class="feather-map-pin me-2"></i>
                                                <p>United Kingdom</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="enrol-student-foot">
                                        <ul>
                                            <li>Enrolled <span>2/6/2020</span></li>
                                            <li>Progress
                                                <div class="instruct-stip d-flex align-items-center">
                                                    <span>20%</span>
                                                    <div class="course-stip progress-stip">
                                                        <div
                                                            class="progress-bar bg-success progress-bar-striped active-stip">
                                                        </div>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                                <div class="student-box flex-fill">
                                    <div class="student-box-blks">
                                        <div class="message-text-img">
                                            <a href="javascript:;">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/icon/message-text.svg') }}">
                                            </a>
                                        </div>
                                        <div class="student-img">
                                            <a href="{{ url('student-profile') }}">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/user/user4.jpg') }}">
                                            </a>
                                        </div>
                                        <div class="student-content pb-0">
                                            <h5><a href="{{ url('student-profile') }}">Kristin Watson</a></h5>
                                            <div class="loc-blk d-flex align-items-center justify-content-center">
                                                <i class="feather-map-pin me-2"></i>
                                                <p>Iceland</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="enrol-student-foot">
                                        <ul>
                                            <li>Enrolled <span>22/12/2020</span></li>
                                            <li>Progress
                                                <div class="instruct-stip d-flex align-items-center">
                                                    <span>20%</span>
                                                    <div class="course-stip progress-stip">
                                                        <div
                                                            class="progress-bar bg-success progress-bar-striped active-stip">
                                                        </div>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                                <div class="student-box flex-fill">
                                    <div class="student-box-blks">
                                        <div class="message-text-img">
                                            <a href="javascript:;">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/icon/message-text.svg') }}">
                                            </a>
                                        </div>
                                        <div class="student-img">
                                            <a href="{{ url('student-profile') }}">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/user/user11.jpg') }}">
                                            </a>
                                        </div>
                                        <div class="student-content pb-0">
                                            <h5><a href="{{ url('student-profile') }}">Rivao Luke</a></h5>
                                            <div class="loc-blk d-flex align-items-center justify-content-center">
                                                <i class="feather-map-pin me-2"></i>
                                                <p>Brazil</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="enrol-student-foot">
                                        <ul>
                                            <li>Enrolled <span>3/12/2020</span></li>
                                            <li>Progress
                                                <div class="instruct-stip d-flex align-items-center">
                                                    <span>20%</span>
                                                    <div class="course-stip progress-stip">
                                                        <div
                                                            class="progress-bar bg-success progress-bar-striped active-stip">
                                                        </div>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                                <div class="student-box flex-fill">
                                    <div class="student-box-blks">
                                        <div class="message-text-img">
                                            <a href="javascript:;">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/icon/message-text.svg') }}">
                                            </a>
                                        </div>
                                        <div class="student-img">
                                            <a href="{{ url('student-profile') }}">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/user/user12.jpg') }}">
                                            </a>
                                        </div>
                                        <div class="student-content pb-0">
                                            <h5><a href="{{ url('student-profile') }}">Nia Sikhone</a></h5>
                                            <div class="loc-blk d-flex align-items-center justify-content-center">
                                                <i class="feather-map-pin me-2"></i>
                                                <p>Italy</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="enrol-student-foot">
                                        <ul>
                                            <li>Enrolled <span>10/12/2020</span></li>
                                            <li>Progress
                                                <div class="instruct-stip d-flex align-items-center">
                                                    <span>20%</span>
                                                    <div class="course-stip progress-stip">
                                                        <div
                                                            class="progress-bar bg-success progress-bar-striped active-stip">
                                                        </div>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-4 col-lg-6 col-md-6 d-flex">
                                <div class="student-box flex-fill">
                                    <div class="student-box-blks">
                                        <div class="message-text-img">
                                            <a href="javascript:;">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/icon/message-text.svg') }}">
                                            </a>
                                        </div>
                                        <div class="student-img">
                                            <a href="{{ url('student-profile') }}">
                                                <img class="img-fluid" alt="Students Info"
                                                    src="{{ URL::asset('/assets/img/user/user13.jpg') }}">
                                            </a>
                                        </div>
                                        <div class="student-content pb-0">
                                            <h5><a href="{{ url('student-profile') }}">Xiaon Merry</a></h5>
                                            <div class="loc-blk d-flex align-items-center justify-content-center">
                                                <i class="feather-map-pin me-2"></i>
                                                <p>France</p>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="enrol-student-foot">
                                        <ul>
                                            <li>Enrolled <span>3/12/2020</span></li>
                                            <li>Progress
                                                <div class="instruct-stip d-flex align-items-center">
                                                    <span>20%</span>
                                                    <div class="course-stip progress-stip">
                                                        <div
                                                            class="progress-bar bg-success progress-bar-striped active-stip">
                                                        </div>
                                                    </div>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>

                        @component('components.pagination')
                        @endcomponent

                    </div>
                </div>
                <!-- /Instructor Dashboard -->

            </div>
        </div>
    </div>
    <!-- /Page Wrapper -->
@endsection
