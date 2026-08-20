<template>
  <!-- Leading Companies -->
  <section class="section lead-companies">
    <div class="container">
      <div class="section-header aos" data-aos="fade-up">
        <div class="section-sub-head feature-head text-center">
          <span>Trusted By</span>
          <h2>500+ Leading Universities And Companies</h2>
        </div>
      </div>
      <div class="lead-group aos" data-aos="fade-up">
        <Carousel
          :autoplay="2000"
          :loop="true"
          :wrap-around="true"
          :settings="settings"
          :breakpoints="breakpoints"
        >
          <Slide
            v-for="item in landingcompany"
            :key="item.id"
            class="lead-group-slider owl-carousel owl-theme"
          >
            <div class="carousel__item item">
              <div class="lead-img">
                <img
                  class="img-fluid"
                  alt=""
                  :src="require(`@/assets/img/${item.img}`)"
                />
              </div>
            </div>
          </Slide>
        </Carousel>
      </div>
    </div>
  </section>
  <!-- /Leading Companies -->
</template>
<script>
import AOS from "aos";
import "aos/dist/aos.css";
import landingcompany from "@/assets/json/landingcompany.json";
import { Carousel, Slide } from "vue3-carousel";
import "vue3-carousel/dist/carousel.css";
export default {
  name: "Autoplay",
  components: {
    Carousel,
    Slide,
  },
  data() {
    return {
      landingcompany: landingcompany,
    };
  },
  setup() {
    return {
      // carousel settings
      settings: {
        itemsToShow: 1,
        snapAlign: "center",
      },

      breakpoints: {
        // 700px and up
        700: {
          itemsToShow: 2,
          snapAlign: "center",
        },
        // 1024 and up
        1024: {
          itemsToShow: 5,
          snapAlign: "start",
        },
      },
    };
  },

  mounted() {
    this.$nextTick(() => {
      AOS.init();
    });
  },
};
</script>
