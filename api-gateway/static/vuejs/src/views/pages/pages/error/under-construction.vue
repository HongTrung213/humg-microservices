<template>
    <div class="error-page">
        <!-- Main Wrapper -->
        <div class="main-wrapper">
            
            <div class="error-box">
                <div class="error-logo">
                    <router-link to="/">
                        <img src="@/assets/img/logo.svg" class="img-fluid" alt="Logo">
                    </router-link>
                </div>
                <div class="error-box-img">
                    <img src="@/assets/img/error-02.png" alt="" class="img-fluid" >
                </div>
                <h3 class="h2 mb-3"> The Website is Under Construction</h3>
                <p class="h4 font-weight-normal">We are working on fixing the problem. We back soon</p>
                <router-link to="/" class="btn btn-primary">Back to Home</router-link>
            </div>
        
        </div>
        <!-- /Main Wrapper -->
    </div>
</template>
