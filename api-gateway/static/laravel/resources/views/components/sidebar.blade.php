@if (
    !Route::is([
        'setting-edit-profile',
        'setting-student-accounts',
        'setting-student-billing',
        'setting-student-delete-profile',
        'setting-student-invoice',
        'setting-student-notification',
        'setting-student-payment',
        'setting-student-privacy',
        'setting-student-referral',
        'setting-student-security',
        'setting-student-social-profile',
        'setting-student-subscription',
        'setting-support-tickets',
    ]))
    <!-- Sidebar -->
    <div class="col-xl-3 col-lg-4 col-md-12 theiaStickySidebar">
        <div class="settings-widget dash-profile">
            <div class="settings-menu p-0">
                <div class="profile-bg">
                    <h5>Beginner</h5>
                    <img src="{{ URL::asset('/assets/img/instructor-profile-bg.jpg') }}" alt="">
                    <div class="profile-img">
                        <a href="{{ url('instructor-profile') }}"><img
                                src="{{ URL::asset('/assets/img/user/user15.jpg') }}" alt=""></a>
                    </div>
                </div>
                <div class="profile-group">
                    <div class="profile-name text-center">
                        <h4><a href="{{ url('instructor-profile') }}">Jenny Wilson</a></h4>
                        <p>Instructor</p>
                    </div>
                    <div class="go-dashboard text-center">
                        <a href="{{ url('add-course') }}" class="btn btn-primary">Create New Course</a>
                    </div>
                </div>
            </div>
        </div>
        <div class="settings-widget account-settings">
            <div class="settings-menu">
                <h3>DASHBOARD</h3>
                <ul>
                    <li class="nav-item ">
                        <a class="{{ Request::is('instructor-dashboard') ? 'active' : '' }}"
                            href="{{ url('instructor-dashboard') }}" class="nav-link">
                            <i class="feather-home"></i> My Dashboard
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('instructor-course') ? 'active' : '' }}"
                            href="{{ url('instructor-course') }}" class="nav-link">
                            <i class="feather-book"></i> My Courses
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('instructor-reviews') ? 'active' : '' }}"
                            href="{{ url('instructor-reviews') }}" class="nav-link">
                            <i class="feather-star"></i> Reviews
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('instructor-earnings') ? 'active' : '' }}"
                            href="{{ url('instructor-earnings') }}" class="nav-link">
                            <i class="feather-pie-chart"></i> Earnings
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('instructor-orders') ? 'active' : '' }}" href="instructor-orders"
                            class="nav-link">
                            <i class="feather-shopping-bag"></i> Orders
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('instructor-student-grid', 'instructor-student-list') ? 'active' : '' }}"
                            href="{{ url('instructor-student-grid') }}" class="nav-link">
                            <i class="feather-users"></i> Students
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('instructor-payouts') ? 'active' : '' }}"
                            href="{{ url('instructor-payouts') }}" class="nav-link">
                            <i class="feather-dollar-sign"></i> Payouts
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('instructor-tickets') ? 'active' : '' }}"
                            href="{{ url('instructor-tickets') }}" class="nav-link">
                            <i class="feather-server"></i> Support Tickets
                        </a>
                    </li>
                </ul>
                <div class="instructor-title">
                    <h3>ACCOUNT SETTINGS</h3>
                </div>
                <ul>
                    <li class="nav-item">
                        <a class="{{ Request::is('instructor-edit-profile') ? 'active' : '' }}"
                            href="{{ url('instructor-edit-profile') }}" class="nav-link ">
                            <i class="feather-settings"></i> Edit Profile
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('instructor-security') ? 'active' : '' }}"
                            href="{{ url('instructor-security') }}" class="nav-link">
                            <i class="feather-user"></i> Security
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('instructor-social-profiles') ? 'active' : '' }}"
                            href="{{ url('instructor-social-profiles') }}" class="nav-link">
                            <i class="feather-refresh-cw"></i> Social Profiles
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('instructor-notification') ? 'active' : '' }}"
                            href="{{ url('instructor-notification') }}" class="nav-link">
                            <i class="feather-bell"></i> Notifications
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('instructor-profile-privacy') ? 'active' : '' }}"
                            href="{{ url('instructor-profile-privacy') }}" class="nav-link">
                            <i class="feather-lock"></i> Profile Privacy
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('instructor-delete-profile') ? 'active' : '' }}"
                            href="{{ url('instructor-delete-profile') }}" class="nav-link">
                            <i class="feather-trash-2"></i> Delete Profile
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('instructor-linked-account') ? 'active' : '' }}"
                            href="{{ url('instructor-linked-account') }}" class="nav-link">
                            <i class="feather-user"></i> Linked Accounts
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('index') ? 'active' : '' }}" href="{{ url('index') }}"
                            class="nav-link">
                            <i class="feather-power"></i> Sign Out
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <!-- /Sidebar -->
@endif
@if (Route::is([
        'setting-edit-profile',
        'setting-student-accounts',
        'setting-student-billing',
        'setting-student-delete-profile',
        'setting-student-invoice',
        'setting-student-notification',
        'setting-student-payment',
        'setting-student-privacy',
        'setting-student-referral',
        'setting-student-security',
        'setting-student-social-profile',
        'setting-student-subscription',
        'setting-support-tickets',
    ]))
    <!-- sidebar -->
    <div class="col-xl-3 col-md-4 theiaStickySidebar">
        <div class="settings-widget dash-profile mb-3">
            <div class="settings-menu p-0">
                <div class="profile-bg">
                    <h5>Beginner</h5>
                    <img src="{{ URL::asset('/assets/img/profile-bg.jpg') }}" alt="">
                    <div class="profile-img">
                        <a href="{{ url('student-profile') }}"><img
                                src="{{ URL::asset('/assets/img/user/user11.jpg') }}" alt=""></a>
                    </div>
                </div>
                <div class="profile-group">
                    <div class="profile-name text-center">
                        <h4><a href="{{ url('student-profile') }}">Rolands R</a></h4>
                        <p>Student</p>
                    </div>
                    <div class="go-dashboard text-center">
                        <a href="{{ url('deposit-student-dashboard') }}" class="btn btn-primary">Go to Dashboard</a>
                    </div>
                </div>
            </div>
        </div>
        <div class="settings-widget account-settings">
            <div class="settings-menu">
                <h3>ACCOUNT SETTINGS</h3>
                <ul>
                    <li class="nav-item">
                        <a class="{{ Request::is('setting-edit-profile') ? 'active' : '' }}"
                            href="{{ url('setting-edit-profile') }}" class="nav-link">
                            <i class="feather-settings"></i> Edit Profile
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('setting-student-security') ? 'active' : '' }}"
                            href="{{ url('setting-student-security') }}" class="nav-link">
                            <i class="feather-user"></i> Security
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('setting-student-social-profile') ? 'active' : '' }}"
                            href="{{ url('setting-student-social-profile') }}" class="nav-link">
                            <i class="feather-refresh-cw"></i> Social Profiles
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('setting-student-notification') ? 'active' : '' }}"
                            href="{{ url('setting-student-notification') }}" class="nav-link">
                            <i class="feather-bell"></i> Notifications
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('setting-student-privacy') ? 'active' : '' }}"
                            href="{{ url('setting-student-privacy') }}" class="nav-link">
                            <i class="feather-lock"></i> Profile Privacy
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('setting-student-delete-profile') ? 'active' : '' }}"
                            href="{{ url('setting-student-delete-profile') }}" class="nav-link">
                            <i class="feather-trash-2"></i> Delete Profile
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('setting-student-accounts') ? 'active' : '' }}"
                            href="{{ url('setting-student-accounts') }}" class="nav-link">
                            <i class="feather-user"></i> Linked Accounts
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('setting-student-referral') ? 'active' : '' }}"
                            href="{{ url('setting-student-referral') }}" class="nav-link">
                            <i class="feather-user-plus"></i> Referrals
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('login') ? 'active' : '' }}" href="{{ url('login') }}"
                            class="nav-link">
                            <i class="feather-power"></i> Sign Out
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('setting-support-tickets') ? 'active' : '' }}"
                            href="{{ url('setting-support-tickets') }}" class="nav-link">
                            <i class="feather-clipboard"></i> Support Tickets
                        </a>
                    </li>

                </ul>
                <h3>SUBSCRIPTION</h3>
                <ul>
                    <li class="nav-item">
                        <a class="{{ Request::is('setting-student-subscription') ? 'active' : '' }}"
                            href="{{ url('setting-student-subscription') }}" class="nav-link ">
                            <i class="feather-calendar"></i> My Subscriptions
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('setting-student-billing') ? 'active' : '' }}"
                            href="{{ url('setting-student-billing') }}" class="nav-link">
                            <i class="feather-credit-card"></i> Billing Info
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('setting-student-payment') ? 'active' : '' }}"
                            href="{{ url('setting-student-payment') }}" class="nav-link">
                            <i class="feather-credit-card"></i> Payment
                        </a>
                    </li>
                    <li class="nav-item">
                        <a class="{{ Request::is('setting-student-invoice') ? 'active' : '' }}"
                            href="{{ url('setting-student-invoice') }}" class="nav-link">
                            <i class="feather-clipboard"></i> Invoice
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <!-- /sidebar -->
@endif
