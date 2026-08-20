<?php $page = 'students-grid2'; ?>
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
            Students Grid
        @endslot
    @endcomponent

    <!-- Page Wrapper -->
    <div class="page-content">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    @component('components.filter')
                    @endcomponent
                    <div class="row">
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box student-grid flex-fill">
                                <div class="student-img">
                                    <a href="{{ url('student-profile') }}">
                                        <img class="img-fluid" alt="Students Info"
                                            src="{{ URL::asset('/assets/img/user/user1.jpg') }}">
                                    </a>
                                </div>
                                <div class="student-content">
                                    <h5><a href="{{ url('student-profile') }}">Charles Dickens</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}" class="me-1"
                                            alt="">
                                        <p>Louisiana</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box student-grid flex-fill">
                                <div class="student-img">
                                    <a href="{{ url('student-profile') }}">
                                        <img class="img-fluid" alt="Students Info"
                                            src="{{ URL::asset('/assets/img/user/user2.jpg') }}">
                                    </a>
                                </div>
                                <div class="student-content">
                                    <h5><a href="{{ url('student-profile') }}">Gabriel Palmer</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}" class="me-1"
                                            alt="">
                                        <p>Tunisia</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box student-grid flex-fill">
                                <div class="student-img">
                                    <a href="{{ url('student-profile') }}">
                                        <img class="img-fluid" alt="Students Info"
                                            src="{{ URL::asset('/assets/img/user/user3.jpg') }}">
                                    </a>
                                </div>
                                <div class="student-content">
                                    <h5><a href="{{ url('student-profile') }}">James Lemire</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}" class="me-1"
                                            alt="">
                                        <p>Louisiana</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box student-grid flex-fill">
                                <div class="student-img">
                                    <a href="{{ url('student-profile') }}">
                                        <img class="img-fluid" alt="Students Info"
                                            src="{{ URL::asset('/assets/img/user/user4.jpg') }}">
                                    </a>
                                </div>
                                <div class="student-content">
                                    <h5><a href="{{ url('student-profile') }}">Olivia Murphy</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}" class="me-1"
                                            alt="">
                                        <p>Spain</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box student-grid flex-fill">
                                <div class="student-img">
                                    <a href="{{ url('student-profile') }}">
                                        <img class="img-fluid" alt="Students Info"
                                            src="{{ URL::asset('/assets/img/user/user5.jpg') }}">
                                    </a>
                                </div>
                                <div class="student-content">
                                    <h5><a href="{{ url('student-profile') }}">Rebecca Swartz</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}" class="me-1"
                                            alt="">
                                        <p>Tunisia</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box student-grid flex-fill">
                                <div class="student-img">
                                    <a href="{{ url('student-profile') }}">
                                        <img class="img-fluid" alt="Students Info"
                                            src="{{ URL::asset('/assets/img/user/user6.jpg') }}">
                                    </a>
                                </div>
                                <div class="student-content">
                                    <h5><a href="{{ url('student-profile') }}">Betty Richards</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}" class="me-1"
                                            alt="">
                                        <p>United States</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box student-grid flex-fill">
                                <div class="student-img">
                                    <a href="{{ url('student-profile') }}">
                                        <img class="img-fluid" alt="Students Info"
                                            src="{{ URL::asset('/assets/img/user/user11.jpg') }}">
                                    </a>
                                </div>
                                <div class="student-content">
                                    <h5><a href="{{ url('student-profile') }}">Jeffrey Montgomery</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}" class="me-1"
                                            alt="">
                                        <p>Louisiana</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box student-grid flex-fill">
                                <div class="student-img">
                                    <a href="{{ url('student-profile') }}">
                                        <img class="img-fluid" alt="Students Info"
                                            src="{{ URL::asset('/assets/img/user/user12.jpg') }}">
                                    </a>
                                </div>
                                <div class="student-content">
                                    <h5><a href="{{ url('student-profile') }}">Brooke Hayes</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}" class="me-1"
                                            alt="">
                                        <p>Louisiana</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box student-grid flex-fill">
                                <div class="student-img">
                                    <a href="{{ url('student-profile') }}">
                                        <img class="img-fluid" alt="Students Info"
                                            src="{{ URL::asset('/assets/img/user/user13.jpg') }}">
                                    </a>
                                </div>
                                <div class="student-content">
                                    <h5><a href="{{ url('student-profile') }}">Gertrude D. Shorter</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}" class="me-1"
                                            alt="">
                                        <p>Brazil</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box student-grid flex-fill">
                                <div class="student-img">
                                    <a href="{{ url('student-profile') }}">
                                        <img class="img-fluid" alt="Students Info"
                                            src="{{ URL::asset('/assets/img/user/user14.jpg') }}">
                                    </a>
                                </div>
                                <div class="student-content">
                                    <h5><a href="{{ url('student-profile') }}">David L. Garza</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}" class="me-1"
                                            alt="">
                                        <p>Italy</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box student-grid flex-fill">
                                <div class="student-img">
                                    <a href="{{ url('student-profile') }}">
                                        <img class="img-fluid" alt="Students Info"
                                            src="{{ URL::asset('/assets/img/user/user3.jpg') }}">
                                    </a>
                                </div>
                                <div class="student-content">
                                    <h5><a href="{{ url('student-profile') }}">Vivian E. Winders</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}" class="me-1"
                                            alt="">
                                        <p>France</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-3 col-md-6 d-flex">
                            <div class="student-box student-grid flex-fill">
                                <div class="student-img">
                                    <a href="{{ url('student-profile') }}">
                                        <img class="img-fluid" alt="Students Info"
                                            src="{{ URL::asset('/assets/img/user/user5.jpg') }}">
                                    </a>
                                </div>
                                <div class="student-content">
                                    <h5><a href="{{ url('student-profile') }}">Sean K. Leon</a></h5>
                                    <h6>Student</h6>
                                    <div class="loc-blk d-flex align-items-center justify-content-center">
                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}" class="me-1"
                                            alt="">
                                        <p>Iceland</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    @component('components.pagination')
                    @endcomponent

                </div>

            </div>
        </div>
    </div>
    <!-- /Page Wrapper -->
@endsection
