<template>
  <div class="navbar-header">
    <a id="mobile_btn" href="javascript:void(0);" @click="toggleSidebar">
      <span class="bar-icon">
        <span></span>
        <span></span>
        <span></span>
      </span>
    </a>
    <router-link to="/" class="navbar-brand logo">
      <img src="@/assets/img/logo.svg" class="img-fluid" alt="Logo" />
    </router-link>
  </div>
  <div class="menu-header">
    <router-link to="/" class="menu-logo">
      <img src="@/assets/img/logo.svg" class="img-fluid" alt="Logo" />
    </router-link>
    <a
      id="menu_close"
      class="menu-close"
      href="javascript:void(0);"
      v-show="isSidebarOpen"
      @click="closeSidebar"
    >
      <i class="fas fa-times"></i>
    </a>
  </div>
</template>
<script>
export default {
  data() {
    return {
      isSidebarOpen: false,
    };
  },
  methods: {
    toggleSidebar() {
      this.isSidebarOpen = !this.isSidebarOpen;
      if (this.isSidebarOpen) {
        document.documentElement.classList.add("menu-opened");
      } else {
        document.documentElement.classList.remove("menu-opened");
      }
    },
    closeSidebar() {
      this.isSidebarOpen = false;
      document.documentElement.classList.remove("menu-opened");
    },
  },
};
</script>
