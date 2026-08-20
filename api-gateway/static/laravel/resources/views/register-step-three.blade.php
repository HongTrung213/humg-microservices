<?php $page = 'register-step-three'; ?>
@extends('layout.mainlayout')
@section('content')
    <div class="row">
        @component('components.loginbanner')
        @endcomponent
        <div class="col-lg-8 col-md-6 login-wrap-bg">
            <!-- Login -->
            <div class="login-wrapper">
                <div class="loginbox register-box">
                    <div class="img-logo">
                        <img src="{{ URL::asset('/assets/img/logo.svg') }}" class="img-fluid" alt="Logo">
                        <div class="back-home">
                            <a href="{{ url('login') }}">Back to Home</a>
                        </div>
                    </div>
                    <h1>Become An Instructor</h1>
                    <div class="row">
                        <div class="col-lg-5">
                            <div class="profile-box">
                                <div class="circle-bar circle-bar1 text-center">
                                    <div class="circle-graph1" data-percent="75">
                                        <p>75% <span>3 of 4</span></p>
                                    </div>
                                </div>
                                <h3>Profile Compleation</h3>
                                <div class="personal-detail d-flex align-items-center">
                                    <span class="active-color"><i class="fa-solid fa-check"></i></span>
                                    <div class="personal-text">
                                        <h4>Personal Details</h4>
                                        <p class="mb-0">Setup Your personal details</p>
                                    </div>
                                </div>
                                <div class="personal-detail d-flex align-items-center">
                                    <span class="active-color"><i class="fa-solid fa-check"></i></span>
                                    <div class="personal-text">
                                        <h4>Social Profiles</h4>
                                        <p class="mb-0">Setup Your Social Profiles links</p>
                                    </div>
                                </div>
                                <div class="personal-detail d-flex align-items-center">
                                    <span class="active-color active-bar">3</span>
                                    <div class="personal-text">
                                        <h4>Profile Privacy Settings</h4>
                                        <p class="mb-0">Setup Your Profile Privacy Settings</p>
                                    </div>
                                </div>
                                <div class="personal-detail d-flex align-items-center">
                                    <span>4</span>
                                    <div class="personal-text">
                                        <h4>Link Accounts</h4>
                                        <p class="mb-0">Setup Your Linked Accounts</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-7">
                            <div class="personal-form">
                                <h4>Profile Privacy Settings</h4>
                                <form action="register-step-four">
                                    <div class="row">
                                        <div class="col-lg-6">
                                            <div class="form-group">
                                                <label for="sel1" class="form-label">Privacy levels</label>
                                                <select class="form-select" id="sel1" name="sellist1">
                                                    <option>Select </option>
                                                    <option>India</option>
                                                    <option>America</option>
                                                    <option>London</option>
                                                </select>
                                            </div>
                                        </div>
                                        <div class="col-lg-12">
                                            <label>Profile settings</label>
                                            <div class="form-check form-switch check-on">
                                                <input class="form-check-input" type="checkbox" checked>
                                                <label class="form-check-label">Show your profile on search engines</label>
                                            </div>
                                            <div class="form-check form-switch check-on">
                                                <input class="form-check-input" type="checkbox">
                                                <label class="form-check-label">Show courses you're taking on your profile
                                                    page</label>
                                            </div>
                                            <div class="form-check form-switch check-on">
                                                <input class="form-check-input" type="checkbox">
                                                <label class="form-check-label">Show your profile on public</label>
                                            </div>
                                            <div class="form-check form-switch check-on">
                                                <input class="form-check-input" type="checkbox">
                                                <label class="form-check-label">Currently learning</label>
                                            </div>
                                            <div class="form-check form-switch check-on">
                                                <input class="form-check-input" type="checkbox">
                                                <label class="form-check-label">Completed courses</label>
                                            </div>
                                            <div class="form-check form-switch check-on">
                                                <input class="form-check-input" type="checkbox">
                                                <label class="form-check-label">Your Interests</label>
                                            </div>
                                            <div class="btn-group d-flex">
                                                <div class="back-btn">
                                                    <a href="{{ url('register-step-two') }}" class="btn btn-back">back</a>
                                                </div>
                                                <div class="next-btn">
                                                    <button class="btn btn-primary btn-start">Next</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- /Login -->

        </div>

    </div>
@endsection
