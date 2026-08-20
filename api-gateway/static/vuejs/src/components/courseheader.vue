<template>
<!-- Course Header -->
<div class="course-student-header">
    <div class="container">
        <div class="student-group">
            <div class="course-group ">
                <div class="course-group-img d-flex">
                    <router-link to="student-profile"><img src="@/assets/img/user/user11.jpg" alt="" class="img-fluid"></router-link>
                    <div class="d-flex align-items-center">
                        <div class="course-name">
                            <h4><router-link to="student-profile">Rolands R</router-link><span>Beginner</span></h4>
                            <p>Student</p>
                        </div>
                    </div>
                </div>
                <div class="course-share ">
                    <a href="javascript:;" class="btn btn-primary">Account Settings</a>
                </div>
            </div>
        </div>
        <div class="my-student-list">
            <ul>
                <li :class="currentPath == 'course-student' ? 'active' : 'notactive'"><router-link to="course-student">Courses</router-link></li>
                <li :class="currentPath == 'course-wishlist' ? 'active' : 'notactive'"><router-link to="course-wishlist">Wishlists</router-link></li>
                <li :class="currentPath == 'course-message' ? 'active' : 'notactive'"><router-link to="course-message">Messages</router-link></li>
                <li :class="currentPath == 'purchase-history' ? 'active' : 'notactive'" class="mb-0"><router-link to="purchase-history">Purchase history</router-link></li>
            </ul>
        </div>
    </div>
</div>
<!-- /Course Header -->
</template> 
<script>
    export default {
        computed:{
            currentPath() {
                return this.$route.name;
            }
        }
    }
    </script>