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
                            <li class="breadcrumb-item" aria-current="page">Student</li>
                            <li class="breadcrumb-item active" aria-current="page">Student Profile</li>
                        </ol>
                    </nav>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- /Breadcrumb -->

<!-- Breadcrumb -->
<div class="page-banner student-bg-blk">
    <div class="container">
        <div class="row">
            <div class="col-md-12 col-12">
                <div class="profile-info-blk">
                    <a href="javascript:;" class="profile-info-img">
                        <img src="@/assets/img/students/profile-avatar.png" alt="Profile Avatar" class="img-fluid">
                    </a>
                    <h4><a href="javascript:;">Gabriel Palmer</a><span>Beginner</span></h4>
                    <p>Student</p>
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