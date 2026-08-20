<template>
<!-- Login Banner -->
<div class="col-md-6 login-bg">
    <div class="owl-carousel login-slide owl-theme">
        <div class="welcome-login">
            <div class="login-banner">
                <img src="@/assets/img/login-img.png" class="img-fluid" alt="Logo">
            </div>
            <Carousel>
                <Slide v-for="slide in 3" :key="slide">
                    <div class="mentor-course text-center">
                        <h2>Welcome to <br>DreamsLMS Courses.</h2>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam.</p>
                    </div>
                </Slide>
                <template #addons>
                    <Pagination />
                </template>
            </Carousel>
        </div>
    </div>
</div>
<!-- /Login Banner -->
</template>
<script>
    import { defineComponent } from 'vue'
    import { Carousel, Pagination, Slide } from 'vue3-carousel';
    
    import 'vue3-carousel/dist/carousel.css';
    
    export default defineComponent({
    name: 'Autoplay',
    components: {
    Carousel,
    Slide,
    Pagination,
    },
});
</script>