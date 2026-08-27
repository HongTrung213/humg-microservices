<template>
  <ul class="nav header-navbar-rht" v-if="isHometwoRoute">
    <li class="nav-item">
      <router-link class="login-head button" to="login">Login</router-link>
    </li>
    <li class="nav-item">
      <router-link class="signin-head" to="register">Sign up</router-link>
    </li>
  </ul>
  <ul class="nav header-navbar-rht align-items-center" v-else-if="isHomethreeRoute">
    <li class="nav-item">
      <router-link class="nav-link login-three-head button" to="login"
        ><span>Login</span></router-link
      >
    </li>
    <li class="nav-item">
      <router-link class="nav-link signin-three-head" to="register">Register</router-link>
    </li>
  </ul>
  <ul class="nav header-navbar-rht header-navbar-five" v-else-if="isHomefourRoute">
    <li class="nav-item">
      <router-link class="login-five" to="login">Login</router-link>
    </li>
    <li class="nav-item">
      <router-link class="signup-five" to="register">Signup</router-link>
    </li>
  </ul>
  <ul class="nav header-navbar-rht" v-else>
    <li class="nav-item">
      <router-link class="nav-link header-sign" to="login">Signin</router-link>
    </li>
    <li class="nav-item">
      <router-link class="nav-link header-login" to="register">Signup</router-link>
    </li>
  </ul>
</template>
<script>
export default {
  computed: {
    isHometwoRoute() {
      return this.$route.path === "/index-two";
    },
    isHomethreeRoute() {
      return this.$route.path === "/index-three";
    },
    isHomefourRoute() {
      return this.$route.path === "/index-four";
    },
  },
};
</script>
