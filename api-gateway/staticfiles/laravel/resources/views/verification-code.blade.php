<?php $page = 'verification-code'; ?>
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
                    <h1>Enter Varification Code</h1>
                    <div class="reset-password">
                        <p>We have just sent a verification code to your registed email id</p>
                    </div>
                    <form action="login" class="verification-code">
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="d-flex digit-group">
                                    <input type="text" class="form-control" id="digit-1" name="digit-1"
                                        data-next="digit-2" value="8" />
                                    <input type="text" class="form-control" id="digit-2" name="digit-2"
                                        data-next="digit-3" data-previous="digit-1" />
                                    <input type="text" class="form-control" id="digit-3" name="digit-3"
                                        data-next="digit-4" data-previous="digit-2" />
                                    <input type="text" class="form-control" id="digit-4" name="digit-4"
                                        data-next="digit-5" data-previous="digit-3" />
                                </div>
                            </div>
                            <div class="send-code">
                                <a href="{{ url('verification-code') }}">Send the code again</a>
                            </div>
                            <div class="d-grid">
                                <button class="btn btn-primary btn-start" type="submit">Submit</button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
            <!-- /Login -->

        </div>

    </div>
@endsection
