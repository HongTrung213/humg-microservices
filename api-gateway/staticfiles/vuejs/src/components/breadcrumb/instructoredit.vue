<template>
<!-- Breadcrumb -->
<div class="breadcrumb-bar">
    <div class="container">
        <div class="row">
            <div class="col-md-12 col-12">
                <div class="breadcrumb-list">
                    <nav aria-label="breadcrumb" class="page-breadcrumb">
                        <ol class="breadcrumb">
                            <li class="breadcrumb-item"><router-link to="/">Home</router-link></li>
                            <li class="breadcrumb-item" aria-current="page">Courses</li>
                            <li class="breadcrumb-item" aria-current="page">All Courses</li>
                            <li class="breadcrumb-item" aria-current="page">The Complete Web Developer Course 2.0</li>
                        </ol>
                    </nav>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- /Breadcrumb -->

<!-- Breadcrumb -->
<div class="page-banner instructor-bg-blk">
    <div class="container">
        <div class="row">
            <div class="col-md-12 col-12">
                <div class="profile-info-blk">
                    <router-link to="instructor-dashboard" class="profile-info-img">
                        <img src="@/assets/img/instructor/profile-avatar.jpg" alt="" class="img-fluid">
                    </router-link>
                    <h4><router-link to="instructor-dashboard">Jenny Wilson</router-link><span>Beginner</span></h4>
                    <p>Instructor</p>
                    <ul class="list-unstyled inline-inline profile-info-social">
                        <li class="list-inline-item">
                            <a href="javascript:;">
                                <i class="fa-brands fa-facebook me-1"></i>
                            </a>
                        </li>
                        <li class="list-inline-item">
                            <a href="javascript:;">
                                <i class="fa-brands fa-twitter me-1"></i>
                            </a>
                        </li>
                        <li class="list-inline-item">
                            <a href="javascript:;">
                                <i class="fa-brands fa-instagram me-1"></i>
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
<!-- /Breadcrumb -->	
</template>