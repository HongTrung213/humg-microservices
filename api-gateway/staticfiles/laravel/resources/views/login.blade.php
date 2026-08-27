<?php $page = 'login'; ?>
@extends('layout.mainlayout')
@section('content')
    <div class="row">
        @component('components.loginbanner')
        @endcomponent
        <div class="col-md-6 login-wrap-bg">
            <!-- Login -->
            <div class="login-wrapper">
                <div class="loginbox">
                    <div class="w-100">
                        <div class="img-logo">
                            <img src="{{ URL::asset('/assets/img/logo.svg') }}" class="img-fluid" alt="Logo">
                            <div class="back-home">
                                <a href="{{ url('index') }}">Back to Home</a>
                            </div>
                        </div>
                        <h1>Sign into Your Account</h1>
                        <form method="post" action="{{ route('login.custom') }}">
                            @csrf
                            <div class="form-group">
                                <label class="form-control-label">Email</label>
                                <input type="email" class="form-control" value="admin@example.com" name="email"
                                    id="email">
                                <div class="text-danger pt-2">
                                    @error('0')
                                        {{ $message }}
                                    @enderror
                                    @error('email')
                                        {{ $message }}
                                    @enderror
                                </div>
                            </div>
                            <div class="form-group">
                                <label class="form-control-label">Password</label>
                                <div class="pass-group">
                                    <input type="password" class="form-control pass-input" value="12345678" name="password"
                                        id="password">
                                    <span class="feather-eye-off toggle-password"></span>
                                    <div class="text-danger pt-2">
                                        @error('0')
                                            {{ $message }}
                                        @enderror
                                        @error('password')
                                            {{ $message }}
                                        @enderror
                                    </div>
                                </div>
                            </div>
                            <div class="forgot">
                                <span><a class="forgot-link" href="{{ url('forgot-password') }}">Forgot Password
                                        ?</a></span>
                            </div>
                            <div class="remember-me">
                                <label class="custom_check mr-2 mb-0 d-inline-flex remember-me"> Remember me
                                    <input type="checkbox" name="radio">
                                    <span class="checkmark"></span>
                                </label>
                            </div>
                            <div class="d-grid">
                                <button class="btn btn-primary btn-start" type="submit">Sign In</button>
                            </div>
                        </form>
                    </div>
                </div>
                <div class="google-bg text-center">
                    <span><a href="#">Or sign in with</a></span>
                    <div class="sign-google">
                        <ul>
                            <li><a href="#"><img src="{{ URL::asset('/assets/img/net-icon-01.png') }}"
                                        class="img-fluid" alt="Logo"> Sign In using Google</a></li>
                            <li><a href="#"><img src="{{ URL::asset('/assets/img/net-icon-02.png') }}"
                                        class="img-fluid" alt="Logo">Sign In using Facebook</a></li>
                        </ul>
                    </div>
                    <p class="mb-0">New User ? <a href="{{ url('register') }}">Create an Account</a></p>
                </div>
            </div>
            <!-- /Login -->

        </div>

    </div>
@endsection
