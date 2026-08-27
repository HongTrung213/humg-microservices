<?php $page = 'students-list'; ?>
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
            Students List
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
                        <!-- Instructor List -->
                        <div class="col-lg-12">
                            <div class="student-grid-blk">
                                <!-- Row alignment -->
                                <div class="row">
                                    <div class="col-md-6">
                                        <div class="student-list flex-fill">
                                            <div class="student-img">
                                                <a href="{{ url('student-profile') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/students/student-01.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="student-content">
                                                <h5><a href="{{ url('student-profile') }}">Charles Dickens</a></h5>
                                                <h6>Student</h6>
                                                <div class="student-info">
                                                    <div class="loc-blk d-flex justify-content-center">
                                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}"
                                                            class="me-1" alt="">
                                                        <p>Brazil</p>
                                                    </div>
                                                    <ul class="list-unstyled inline-inline profile-info-social">
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-facebook"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-twitter"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-instagram"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-linkedin"></i>
                                                            </a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="student-list flex-fill">
                                            <div class="student-img">
                                                <a href="{{ url('student-profile') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/students/student-02.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="student-content">
                                                <h5><a href="{{ url('student-profile') }}">Gabriel Palmer</a></h5>
                                                <h6>Student</h6>
                                                <div class="student-info">
                                                    <div class="loc-blk d-flex justify-content-center">
                                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}"
                                                            class="me-1" alt="">
                                                        <p>Italy</p>
                                                    </div>
                                                    <ul class="list-unstyled inline-inline profile-info-social">
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-facebook"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-twitter"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-instagram"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-linkedin"></i>
                                                            </a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- /Row alignment -->

                                <!-- Row alignment -->
                                <div class="row">
                                    <div class="col-md-6">
                                        <div class="student-list flex-fill">
                                            <div class="student-img">
                                                <a href="{{ url('student-profile') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/students/student-03.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="student-content">
                                                <h5><a href="{{ url('student-profile') }}">James Lemire</a></h5>
                                                <h6>Student</h6>
                                                <div class="student-info">
                                                    <div class="loc-blk d-flex justify-content-center">
                                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}"
                                                            class="me-1" alt="">
                                                        <p>Louisiana</p>
                                                    </div>
                                                    <ul class="list-unstyled inline-inline profile-info-social">
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-facebook"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-twitter"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-instagram"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-linkedin"></i>
                                                            </a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="student-list flex-fill">
                                            <div class="student-img">
                                                <a href="{{ url('student-profile') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/students/student-04.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="student-content">
                                                <h5><a href="{{ url('student-profile') }}">Olivia Murphy</a></h5>
                                                <h6>Student</h6>
                                                <div class="student-info">
                                                    <div class="loc-blk d-flex justify-content-center">
                                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}"
                                                            class="me-1" alt="">
                                                        <p>France</p>
                                                    </div>
                                                    <ul class="list-unstyled inline-inline profile-info-social">
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-facebook"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-twitter"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-instagram"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-linkedin"></i>
                                                            </a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- /Row alignment -->

                                <!-- Row alignment -->
                                <div class="row">
                                    <div class="col-md-6">
                                        <div class="student-list flex-fill">
                                            <div class="student-img">
                                                <a href="{{ url('student-profile') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/students/student-05.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="student-content">
                                                <h5><a href="{{ url('student-profile') }}">Rebecca Swartz</a></h5>
                                                <h6>Student</h6>
                                                <div class="student-info">
                                                    <div class="loc-blk d-flex justify-content-center">
                                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}"
                                                            class="me-1" alt="">
                                                        <p>Iceland</p>
                                                    </div>
                                                    <ul class="list-unstyled inline-inline profile-info-social">
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-facebook"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-twitter"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-instagram"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-linkedin"></i>
                                                            </a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="student-list flex-fill">
                                            <div class="student-img">
                                                <a href="{{ url('student-profile') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/students/student-06.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="student-content">
                                                <h5><a href="{{ url('student-profile') }}">Betty Richards</a></h5>
                                                <h6>Student</h6>
                                                <div class="student-info">
                                                    <div class="loc-blk d-flex justify-content-center">
                                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}"
                                                            class="me-1" alt="">
                                                        <p>Louisiana</p>
                                                    </div>
                                                    <ul class="list-unstyled inline-inline profile-info-social">
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-facebook"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-twitter"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-instagram"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-linkedin"></i>
                                                            </a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- /Row alignment -->

                                <!-- Row alignment -->
                                <div class="row">
                                    <div class="col-md-6">
                                        <div class="student-list flex-fill">
                                            <div class="student-img">
                                                <a href="{{ url('student-profile') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/students/student-07.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="student-content">
                                                <h5><a href="{{ url('student-profile') }}">Jeffrey Montgomery</a></h5>
                                                <h6>Student</h6>
                                                <div class="student-info">
                                                    <div class="loc-blk d-flex justify-content-center">
                                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}"
                                                            class="me-1" alt="">
                                                        <p>Brazil</p>
                                                    </div>
                                                    <ul class="list-unstyled inline-inline profile-info-social">
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-facebook"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-twitter"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-instagram"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-linkedin"></i>
                                                            </a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="student-list flex-fill">
                                            <div class="student-img">
                                                <a href="{{ url('student-profile') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/students/student-08.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="student-content">
                                                <h5><a href="{{ url('student-profile') }}">Brooke Hayes</a></h5>
                                                <h6>Student</h6>
                                                <div class="student-info">
                                                    <div class="loc-blk d-flex justify-content-center">
                                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}"
                                                            class="me-1" alt="">
                                                        <p>United States</p>
                                                    </div>
                                                    <ul class="list-unstyled inline-inline profile-info-social">
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-facebook"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-twitter"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-instagram"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-linkedin"></i>
                                                            </a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- /Row alignment -->

                                <!-- Row alignment -->
                                <div class="row">
                                    <div class="col-md-6">
                                        <div class="student-list flex-fill">
                                            <div class="student-img">
                                                <a href="{{ url('student-profile') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/students/student-09.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="student-content">
                                                <h5><a href="{{ url('student-profile') }}">Gertrude Shorter</a></h5>
                                                <h6>Student</h6>
                                                <div class="student-info">
                                                    <div class="loc-blk d-flex justify-content-center">
                                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}"
                                                            class="me-1" alt="">
                                                        <p>Louisiana</p>
                                                    </div>
                                                    <ul class="list-unstyled inline-inline profile-info-social">
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-facebook"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-twitter"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-instagram"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-linkedin"></i>
                                                            </a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="student-list flex-fill">
                                            <div class="student-img">
                                                <a href="{{ url('student-profile') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/students/student-10.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="student-content">
                                                <h5><a href="{{ url('student-profile') }}">David Garza</a></h5>
                                                <h6>Student</h6>
                                                <div class="student-info">
                                                    <div class="loc-blk d-flex justify-content-center">
                                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}"
                                                            class="me-1" alt="">
                                                        <p>Tunisia</p>
                                                    </div>
                                                    <ul class="list-unstyled inline-inline profile-info-social">
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-facebook"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-twitter"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-instagram"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-linkedin"></i>
                                                            </a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- /Row alignment -->

                                <!-- Row alignment -->
                                <div class="row">
                                    <div class="col-md-6">
                                        <div class="student-list flex-fill">
                                            <div class="student-img">
                                                <a href="{{ url('student-profile') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/students/student-11.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="student-content">
                                                <h5><a href="{{ url('student-profile') }}">Vivian Winders</a></h5>
                                                <h6>Student</h6>
                                                <div class="student-info">
                                                    <div class="loc-blk d-flex justify-content-center">
                                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}"
                                                            class="me-1" alt="">
                                                        <p>Louisiana</p>
                                                    </div>
                                                    <ul class="list-unstyled inline-inline profile-info-social">
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-facebook"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-twitter"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-instagram"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-linkedin"></i>
                                                            </a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="col-md-6">
                                        <div class="student-list flex-fill">
                                            <div class="student-img">
                                                <a href="{{ url('student-profile') }}">
                                                    <img class="img-fluid" alt=""
                                                        src="{{ URL::asset('/assets/img/students/student-12.jpg') }}">
                                                </a>
                                            </div>
                                            <div class="student-content">
                                                <h5><a href="{{ url('student-profile') }}">Sean Leon</a></h5>
                                                <h6>Student</h6>
                                                <div class="student-info">
                                                    <div class="loc-blk d-flex justify-content-center">
                                                        <img src="{{ URL::asset('/assets/img/students/loc-icon.svg') }}"
                                                            class="me-1" alt="">
                                                        <p>Spain</p>
                                                    </div>
                                                    <ul class="list-unstyled inline-inline profile-info-social">
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-facebook"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-twitter"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-instagram"></i>
                                                            </a>
                                                        </li>
                                                        <li class="list-inline-item">
                                                            <a href="javascript:;">
                                                                <i class="fa-brands fa-linkedin"></i>
                                                            </a>
                                                        </li>
                                                    </ul>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- /Row alignment -->
                            </div>
                        </div>
                        <!-- /Instructor List -->


                    </div>

                    @component('components.pagination')
                    @endcomponent

                </div>
            </div>
        </div>
    </div>
    <!-- /Page Wrapper -->
@endsection
