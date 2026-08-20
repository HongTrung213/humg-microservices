<?php $page = 'new-password'; ?>
@extends('layout.mainlayout')
@section('content')
    <div class="row">
        @component('components.loginbanner')
        @endcomponent
        <div class="col-md-6 login-wrap-bg">
            <!-- Login -->
            <div class="login-wrapper">
                <div class="loginbox">
                    <div class="img-logo">
                        <img src="{{ URL::asset('/assets/img/logo.svg') }}" class="img-fluid" alt="Logo">
                        <div class="back-home">
                            <a href="#">Back to Home</a>
                        </div>
                    </div>
                    <h1>Setup New Password</h1>
                    <form action="{{ url('login') }}">
                        <div class="form-group">
                            <label class="form-control-label">Password</label>
                            <div class="pass-group" id="passwordInput">
                                <input type="password" class="form-control pass-input" placeholder="Enter your password">
                                <span class="toggle-password feather-eye-off"></span>
                                <span class="pass-checked"><i class="feather-check"></i></span>
                            </div>
                            <div class="password-strength" id="passwordStrength">
                                <span id="poor"></span>
                                <span id="weak"></span>
                                <span id="strong"></span>
                                <span id="heavy"></span>
                            </div>
                            <div id="passwordInfo"></div>
                        </div>
                        <div class="form-group">
                            <label class="form-control-label">Confirm Password</label>
                            <div class="pass-group" id="passwordInputs">
                                <input type="password" class="form-control pass-input" placeholder="Enter your password">
                                <span class="toggle-password feather-eye-off"></span>
                                <span class="pass-checked"><i class="feather-check"></i></span>
                            </div>
                            <div class="password-strength" id="passwordStrengths">
                                <span id="poors"></span>
                                <span id="weaks"></span>
                                <span id="strongs"></span>
                                <span id="heavys"></span>
                            </div>
                            <div id="passwordInfos"></div>
                        </div>
                        <div class="form-check remember-me">
                            <label class="form-check-label mb-0">
                                <input class="form-check-input" type="checkbox" name="remember"> I agree to the <a
                                    href="#">Terms of Service</a> and <a href="#">Privacy Policy.</a>
                            </label>
                        </div>
                        <div class="d-grid">
                            <button class="btn btn-primary btn-start" type="submit">Reset Password</button>
                        </div>
                        <div class="reset-account">
                            <p class="mb-0">Already have an account? <a href="{{ url('login') }}">Sign in</a></p>
                        </div>
                    </form>
                </div>
            </div>
            <!-- /Login -->

        </div>

    </div>
@endsection
