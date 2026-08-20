<?php $page = 'withdrawal-instructor'; ?>
@extends('layout.mainlayout')
@section('content')
    @component('components.breadcrumb')
    @endcomponent
    <!--Dashbord Student -->
    <div class="page-content">
        <div class="container">
            <div class="row">
                <!-- Profile Details -->
                <div class="col-xl-12 col-md-12">
                    <div class="settings-widget">
                        <div class="settings-inner-blk p-0">
                            <div class="comman-space pb-0">
                                <div class="filter-grp ticket-grp d-flex align-items-center justify-content-between">
                                    <div>
                                        <h3>Deposit History</h3>
                                    </div>
                                    <div class="ticket-btn-grp">
                                        <a href="javascript:;" data-bs-toggle="modal"
                                            data-bs-target="#depositMethod">Withdrawal Money</a>
                                    </div>
                                </div>
                                <div class="settings-tickets-blk table-responsive">

                                    <!-- Referred Users-->
                                    <table class="table table-nowrap mb-0">
                                        <thead>
                                            <tr>
                                                <th>Referred ID</th>
                                                <th>Gateway</th>
                                                <th>Amount</th>
                                                <th>Time</th>
                                                <th>Status</th>
                                                <th>&nbsp;</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td><a href="javascript:;">K2WX7JJ6R1UA</a></td>
                                                <td>Stripe </td>
                                                <td><span class="text-success">+ $45.00</span></td>
                                                <td>2023-05-18 01:12 AM </td>
                                                <td><span class="badge info-low">Complete</span></td>
                                                <td><a href="javascript:;" class="btn-style"><i class="feather-eye"></i></a>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td><a href="javascript:;">9RVE1N1TA1H3</a></td>
                                                <td>Bank </td>
                                                <td><span class="text-success">+ $75.00</span></td>
                                                <td>2023-05-08 01:12 AM </td>
                                                <td><span class="badge info-low">Complete</span></td>
                                                <td><a href="javascript:;" class="btn-style"><i class="feather-eye"></i></a>
                                                </td>
                                            </tr>
                                            <tr>
                                                <td><a href="javascript:;">C83Z7EQ4A1WX</a></td>
                                                <td>Stripe </td>
                                                <td><span class="text-success">+ $100.00</span></td>
                                                <td>2023-06-20 01:12 AM </td>
                                                <td><span class="badge info-low">Complete</span></td>
                                                <td><a href="javascript:;" class="btn-style"><i class="feather-eye"></i></a>
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
                <!-- Profile Details -->

            </div>
        </div>
    </div>
    <!-- /Dashbord Student -->
    @component('components.modalpopup')
    @endcomponent
@endsection
