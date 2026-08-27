<?php $page = 'instructor-orders'; ?>
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
                    <div class="row">
                        <div class="col-md-12">
                            <div class="settings-widget">
                                <div class="settings-inner-blk p-0">
                                    <div class="sell-course-head comman-space">
                                        <h3>Orders</h3>
                                        <p>Order Dashboard is a quick overview of all current orders.</p>
                                    </div>
                                    <div class="comman-space pb-0">
                                        <div class="settings-tickets-blk course-instruct-blk table-responsive">

                                            <!-- Referred Users-->
                                            <table class="table table-nowrap mb-0">
                                                <thead>
                                                    <tr>
                                                        <th>COURSES</th>
                                                        <th>SALES</th>
                                                        <th>INVOICE</th>
                                                        <th>DATE</th>
                                                        <th>METHOD</th>
                                                        <th></th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <td class="instruct-orders-info">
                                                            <p><a href="{{ url('course-details') }}">Information About UI/UX
                                                                    Design Degree</a></p>
                                                        </td>
                                                        <td>34</td>
                                                        <td>#10021</td>
                                                        <td>10-05-20</td>
                                                        <td>Mastercard</td>
                                                        <td><a href="javascript:;"><i class="feather-more-vertical"></i></a>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="instruct-orders-info">
                                                            <p><a href="{{ url('course-details') }}">Wordpress for Beginners
                                                                    - Master Wordpress Quickly</a></p>
                                                        </td>
                                                        <td>30</td>
                                                        <td>#12421</td>
                                                        <td>10-05-20</td>
                                                        <td>Visa</td>
                                                        <td><a href="javascript:;"><i class="feather-more-vertical"></i></a>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="instruct-orders-info">
                                                            <p><a href="{{ url('course-details') }}">Sketch from A to Z
                                                                    (2023): Become an app designer</a></p>
                                                        </td>
                                                        <td>24</td>
                                                        <td>#11021</td>
                                                        <td>10-05-20</td>
                                                        <td>Mastercard</td>
                                                        <td><a href="javascript:;"><i class="feather-more-vertical"></i></a>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="instruct-orders-info">
                                                            <p><a href="{{ url('course-details') }}">Learn Angular
                                                                    Fundamentals From beginning to advance lavel</a></p>
                                                        </td>
                                                        <td>34</td>
                                                        <td>#10021</td>
                                                        <td>10-05-20</td>
                                                        <td>Mastercard</td>
                                                        <td><a href="javascript:;"><i class="feather-more-vertical"></i></a>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="instruct-orders-info">
                                                            <p><a href="{{ url('course-details') }}">Build Responsive Real
                                                                    World Websites with HTML5 and CSS3</a></p>
                                                        </td>
                                                        <td>34</td>
                                                        <td>#10021</td>
                                                        <td>10-05-20</td>
                                                        <td>Mastercard</td>
                                                        <td><a href="javascript:;"><i class="feather-more-vertical"></i></a>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="instruct-orders-info">
                                                            <p><a href="{{ url('course-details') }}">C# Developers Double
                                                                    Your Coding Speed with Visual Studio</a></p>
                                                        </td>
                                                        <td>34</td>
                                                        <td>#10021</td>
                                                        <td>10-05-20</td>
                                                        <td>Mastercard</td>
                                                        <td><a href="javascript:;"><i class="feather-more-vertical"></i></a>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="instruct-orders-info">
                                                            <p><a href="{{ url('course-details') }}">Learn JavaScript and
                                                                    Express to become a professional JavaScript</a></p>
                                                        </td>
                                                        <td>34</td>
                                                        <td>#10021</td>
                                                        <td>10-05-20</td>
                                                        <td>Mastercard</td>
                                                        <td><a href="javascript:;"><i class="feather-more-vertical"></i></a>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="instruct-orders-info">
                                                            <p><a href="{{ url('course-details') }}">Learn and Understand
                                                                    AngularJS to become a professional developer</a></p>
                                                        </td>
                                                        <td>34</td>
                                                        <td>#10021</td>
                                                        <td>10-05-20</td>
                                                        <td>Mastercard</td>
                                                        <td><a href="javascript:;"><i class="feather-more-vertical"></i></a>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="instruct-orders-info">
                                                            <p><a href="{{ url('course-details') }}">Responsive Web Design
                                                                    Essentials HTML5 CSS3 and Bootstrap</a></p>
                                                        </td>
                                                        <td>34</td>
                                                        <td>#10021</td>
                                                        <td>10-05-20</td>
                                                        <td>Mastercard</td>
                                                        <td><a href="javascript:;"><i class="feather-more-vertical"></i></a>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="instruct-orders-info">
                                                            <p><a href="{{ url('course-details') }}">The Complete App Design
                                                                    Course - UX, UI and Design Thinking</a></p>
                                                        </td>
                                                        <td>34</td>
                                                        <td>#10021</td>
                                                        <td>10-05-20</td>
                                                        <td>Mastercard</td>
                                                        <td><a href="javascript:;"><i class="feather-more-vertical"></i></a>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                            <!-- /Referred Users-->

                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- /Instructor Dashboard -->

            </div>
        </div>
    </div>
    <!-- /Page Wrapper -->
@endsection
