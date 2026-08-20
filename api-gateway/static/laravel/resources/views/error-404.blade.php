<?php $page = 'error-404'; ?>
@extends('layout.mainlayout')
@section('content')
    <div class="error-box">
        <div class="error-logo">
            <a href="{{ url('index') }}">
                <img src="{{ URL::asset('/assets/img/logo.svg') }}" class="img-fluid" alt="Logo">
            </a>
        </div>
        <div class="error-box-img">
            <img src="{{ URL::asset('/assets/img/error-01.png') }}" alt="" class="img-fluid">
        </div>
        <h3 class="h2 mb-3"> Oh No! Error 404</h3>
        <p class="h4 font-weight-normal">This page you requested counld not found. May the force be with you!</p>
        <a href="{{ url('index') }}" class="btn btn-primary">Back to Home</a>
    </div>
@endsection
