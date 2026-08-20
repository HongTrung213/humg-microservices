<?php $page = 'notifications'; ?>
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
            Notifications
        @endslot
    @endcomponent
    <!-- Notification -->
    <section class="course-content">
        <div class="container">
            <div class="title-sec">
                <div class="row">
                    <div class="col-sm-6 col-lg-5">
                        <h2>Notifications</h2>
                        <p>Improve the way your work, discover a brand new tool and drop the hassle once and for all.</p>
                    </div>
                    <div class="col-sm-6 col-lg-7">
                        <div class="text-end">
                            <a href="javascript:;" class="btn btn-mark">Mark All as Read</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Notifications List -->
            <div class="notify-sec">
                <div class="row">
                    <div class="col-md-12">
                        <h5>Today</h5>
                        <div class="notify-item">
                            <div class="row align-items-center">
                                <div class="col-md-9">
                                    <div class="notify-content">
                                        <a href="{{ url('instructor-profile') }}">
                                            <img class="avatar-img semirounded-circle"
                                                src="{{ URL::asset('/assets/img/user/user2.jpg') }}" alt="User Image">
                                        </a>
                                        <div class="notify-detail">
                                            <h6><a href="{{ url('instructor-profile') }}">Rolands R </a><span>Today at 9:42
                                                    AM</span></h6>
                                            <p>It is a long established fact that a reader will be distracted by the
                                                readable content of a page when looking at its layout. The point of using
                                                Lorem Ipsum is that it has a more-or-less normal distribution of letters, as
                                                opposed to using 'Content here,</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-3">
                                    <div class="text-md-end">
                                        <a href="javascript:;" class="btn">Mark as Read</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <div class="notify-item">
                            <div class="row align-items-center">
                                <div class="col-md-9">
                                    <div class="notify-content">
                                        <a href="{{ url('instructor-profile') }}">
                                            <img class="avatar-img semirounded-circle"
                                                src="{{ URL::asset('/assets/img/user/user1.jpg') }}" alt="User Image">
                                        </a>
                                        <div class="notify-detail">
                                            <h6><a href="{{ url('instructor-profile') }}">Jenis R. </a><span>Today at 10:08
                                                    AM</span></h6>
                                            <p>It is a long established fact that a reader will be distracted by the
                                                readable content of a page when looking at its layout. The point of using
                                                Lorem Ipsum is that it has a more-or-less normal distribution of letters, as
                                                opposed to using 'Content here,</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-3">
                                    <div class="text-md-end">
                                        <a href="javascript:;" class="btn">Mark as Read</a>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <h5>Yesterday</h5>
                        <div class="notify-item">
                            <div class="row align-items-center">
                                <div class="col-md-9">
                                    <div class="notify-content">
                                        <a href="{{ url('instructor-profile') }}">
                                            <img class="avatar-img semirounded-circle"
                                                src="{{ URL::asset('/assets/img/user/user3.jpg') }}" alt="User Image">
                                        </a>
                                        <div class="notify-detail">
                                            <h6><a href="{{ url('instructor-profile') }}">Jesse Stevens</a> <span>Yesterday
                                                    at 9:42 AM</span></h6>
                                            <p>It is a long established fact that a reader will be distracted by the
                                                readable content of a page when looking at its layout. The point of using
                                                Lorem Ipsum is that it has a more-or-less normal distribution of letters, as
                                                opposed to using 'Content here,</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-3">
                                    <div class="text-md-end">
                                        <a href="javascript:;" class="btn">Mark as Read</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="notify-item">
                            <div class="row align-items-center">
                                <div class="col-md-9">
                                    <div class="notify-content">
                                        <a href="{{ url('instructor-profile') }}">
                                            <img class="avatar-img semirounded-circle"
                                                src="{{ URL::asset('/assets/img/user/user7.jpg') }}" alt="User Image">
                                        </a>
                                        <div class="notify-detail">
                                            <h6><a href="{{ url('instructor-profile') }}">Rolands R</a> <span>Yesterday at
                                                    5:40 AM</span></h6>
                                            <p>It is a long established fact that a reader will be distracted by the
                                                readable content of a page when looking at its layout. The point of using
                                                Lorem Ipsum is that it has a more-or-less normal distribution of letters, as
                                                opposed to using 'Content here,</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-3">
                                    <div class="text-md-end">
                                        <a href="javascript:;" class="btn">Mark as Read</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="notify-item">
                            <div class="row align-items-center">
                                <div class="col-md-9">
                                    <div class="notify-content">
                                        <a href="{{ url('instructor-profile') }}">
                                            <img class="avatar-img semirounded-circle"
                                                src="{{ URL::asset('/assets/img/user/user11.jpg') }}" alt="User Image">
                                        </a>
                                        <div class="notify-detail">
                                            <h6><a href="{{ url('instructor-profile') }}">John Michael</a> <span>Yesterday
                                                    at 7:40 AM</span></h6>
                                            <p>It is a long established fact that a reader will be distracted by the
                                                readable content of a page when looking at its layout. The point of using
                                                Lorem Ipsum is that it has a more-or-less normal distribution of letters, as
                                                opposed to using 'Content here,</p>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-md-3">
                                    <div class="text-md-end">
                                        <a href="javascript:;" class="btn">Mark as Read</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- /Notifications List -->

        </div>
    </section>
    <!-- /Notification -->
@endsection
