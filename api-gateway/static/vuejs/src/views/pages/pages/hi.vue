<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <div class="row">
      <loginbanner></loginbanner>

      <div class="col-md-6 login-wrap-bg">
        <!-- Login -->
        <div class="login-wrapper">
          <div class="loginbox">
            <div class="img-logo">
              <img src="@/assets/img/logo.svg" class="img-fluid" alt="Logo" />
              <div class="back-home">
                <a href="javascript:void(0);">Back to Home</a>
              </div>
            </div>
            <h1>Setup New Password</h1>
            <form action="#">
              <div class="form-group">
                <label class="form-control-label">Password</label>
                <div class="pass-group" ref="passwordGroup">
                  <input
                    ref="passwordInput"
                    type="password"
                    class="form-control pass-input"
                    placeholder="Enter your password"
                    :class="{ 'password-error': validationError }"
                    v-model="password"
                    @input="handlePasswordChange"
                  />
                  <span
                    class="toggle-password feather-eye"
                    @click="togglePassword"
                    :class="{
                      'feather-eye': showPassword,
                      'feather-eye-off': !showPassword,
                    }"
                  ></span>
                  <span class="pass-checked" :class="{ active: isPasswordSecure }">
                    <i class="feather-check"></i>
                  </span>
                </div>
                <div
                  id="passwordStrength"
                  style="display: flex"
                  :class="[
                    'password-strength',
                    strength === 'poor' ? 'poor-active' : '',
                    strength === 'weak' ? 'avg-active' : '',
                    strength === 'strong' ? 'strong-active' : '',
                    strength === 'heavy' ? 'heavy-active' : '',
                  ]"
                >
                  <span
                    id="poor"
                    class="active"
                    :class="{ active: strength === 'poor' }"
                  ></span>
                  <span
                    id="weak"
                    class="active"
                    :class="{ active: strength === 'weak' }"
                  ></span>
                  <span
                    id="strong"
                    class="active"
                    :class="{ active: strength === 'strong' }"
                  ></span>
                  <span
                    id="heavy"
                    class="active"
                    :class="{ active: strength === 'heavy' }"
                  ></span>
                </div>
                <div id="passwordInfo">
                  <span v-if="validationError === 1"></span>
                  <span v-else-if="validationError === 2" style="color: red"
                    >😠 Weak. Must contain at least 8 characters</span
                  >
                  <span v-else-if="validationError === 3" style="color: orange"
                    >😲 Average. Must contain at least 1 letter or number</span
                  >
                  <span v-else-if="validationError === 4" style="color: blue"
                    >🙂 Almost. Must contain a special symbol</span
                  >
                  <span v-else-if="validationError === 5" style="color: green"
                    >😊 Awesome! You have a secure password.</span
                  >
                </div>
              </div>
              <div class="form-group">
                <label class="form-control-label">Confirm Password</label>
                <div class="pass-group" ref="passwordGroup1">
                  <input
                    ref="passwordInput1"
                    type="password"
                    class="form-control pass-input"
                    placeholder="Enter your password"
                    :class="{ 'password-error1': validationError1 }"
                    v-model="password1"
                    @input="handlePasswordChange1"
                  />
                  <span
                    class="toggle-password feather-eye"
                    @click="togglePassword1"
                    :class="{
                      'feather-eye': showPassword1,
                      'feather-eye-off': !showPassword1,
                    }"
                  ></span>
                  <span class="pass-checked" :class="{ active: isPasswordSecure1 }">
                    <i class="feather-check"></i>
                  </span>
                </div>
                <div
                  id="passwordStrength"
                  style="display: flex"
                  :class="[
                    'password-strength',
                    strength1 === 'poor' ? 'poor-active' : '',
                    strength1 === 'weak' ? 'avg-active' : '',
                    strength1 === 'strong' ? 'strong-active' : '',
                    strength1 === 'heavy' ? 'heavy-active' : '',
                  ]"
                >
                  <span
                    id="poor"
                    class="active"
                    :class="{ active: strength1 === 'poor' }"
                  ></span>
                  <span
                    id="weak"
                    class="active"
                    :class="{ active: strength1 === 'weak' }"
                  ></span>
                  <span
                    id="strong"
                    class="active"
                    :class="{ active: strength1 === 'strong' }"
                  ></span>
                  <span
                    id="heavy"
                    class="active"
                    :class="{ active: strength1 === 'heavy' }"
                  ></span>
                </div>
                <div id="passwordInfo">
                  <span v-if="validationError1 === 1"></span>
                  <span v-else-if="validationError1 === 2" style="color: red"
                    >😠 Weak. Must contain at least 8 characters</span
                  >
                  <span v-else-if="validationError1 === 3" style="color: orange"
                    >😲 Average. Must contain at least 1 letter or number</span
                  >
                  <span v-else-if="validationError1 === 4" style="color: blue"
                    >🙂 Almost. Must contain a special symbol</span
                  >
                  <span v-else-if="validationError1 === 5" style="color: green"
                    >😊 Awesome! You have a secure password.</span
                  >
                </div>
              </div>
              <div class="form-check remember-me">
                <label class="form-check-label mb-0">
                  <input class="form-check-input" type="checkbox" name="remember" /> I
                  agree to the <a href="javascript:void(0);">Terms of Service</a> and
                  <a href="javascript:void(0);">Privacy Policy.</a>
                </label>
              </div>
              <div class="d-grid">
                <button class="btn btn-primary btn-start" type="submit">
                  Reset Password
                </button>
              </div>
              <div class="reset-account">
                <p class="mb-0">
                  Already have an account? <router-link to="login">Sign in</router-link>
                </p>
              </div>
            </form>
          </div>
        </div>
        <!-- /Login -->
      </div>
    </div>
  </div>
  <!-- /Main Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      showPassword: true,
      password: "",
      validationError: 0,
      isPasswordValid: false,
      strength: "",
      showPassword1: true,
      password1: "",
      validationError1: 0,
      isPasswordValid1: false,
      strength1: "",
    };
  },
  computed: {
    isPasswordSecure() {
      return this.strength === "heavy" && this.validationError === 5;
    },
    isPasswordSecure1() {
      return this.strength1 === "heavy" && this.validationError1 === 5;
    },
  },
  methods: {
    togglePassword() {
      this.showPassword = !this.showPassword;
      const passwordInput = this.$refs.passwordInput;
      passwordInput.type = this.showPassword ? "text" : "password";
    },
    togglePassword1() {
      this.showPassword1 = !this.showPassword1;
      const passwordInput1 = this.$refs.passwordInput1;
      passwordInput1.type = this.showPassword1 ? "text" : "password";
    },
    handlePasswordChange() {
      const newPassword = this.password;
      this.validatePassword(newPassword);
    },
    handlePasswordChange1() {
      const newPassword1 = this.password1;
      this.validatePassword1(newPassword1);
    },
    validatePassword(value) {
      this.validationError = 0;
      if (!value) {
        this.validationError = 0;
      } else if (value.length < 8) {
        this.validationError = 2;
      } else if (!/[a-zA-Z]/.test(value) && !/[0-9]/.test(value)) {
        this.validationError = 3;
      } else if (!/[!@#$%^&*()]/.test(value)) {
        this.validationError = 4;
      } else {
        this.validationError = 5;
      }
      this.strength = this.strengthColor(this.validationError);
    },
    validatePassword1(value) {
      this.validationError1 = 0;
      if (!value) {
        this.validationError1 = 0;
      } else if (value.length < 8) {
        this.validationError1 = 2;
      } else if (!/[a-zA-Z]/.test(value) && !/[0-9]/.test(value)) {
        this.validationError1 = 3;
      } else if (!/[!@#$%^&*()]/.test(value)) {
        this.validationError1 = 4;
      } else {
        this.validationError1 = 5;
      }
      this.strength1 = this.strengthColor1(this.validationError1);
    },
    strengthColor(count) {
      if (count < 1) return "";
      if (count < 2) return "poor";
      if (count < 3) return "weak";
      if (count < 4) return "strong";
      return "heavy";
    },
    strengthColor1(count) {
      if (count < 1) return "";
      if (count < 2) return "poor";
      if (count < 3) return "weak";
      if (count < 4) return "strong";
      return "heavy";
    },
    // hasNumber(value) {
    //   return /[0-9]/.test(value);
    // },
    // hasMixed(value) {
    //   return /[a-z]/.test(value) && /[A-Z]/.test(value);
    // },
    // hasSpecial(value) {
    //   return /[!#@$%^&*)(+=._-]/.test(value);
    // },
    // strengthIndicator(value) {
    //   let strengths = 0;

    //   if (value.length >= 8) strengths = 1;
    //   if (this.hasNumber(value) && value.length >= 8) strengths = 2;
    //   if (this.hasSpecial(value) && value.length >= 8 && this.hasNumber(value))
    //     strengths = 3;
    //   if (
    //     this.hasMixed(value) &&
    //     this.hasSpecial(value) &&
    //     value.length >= 8 &&
    //     this.hasNumber(value)
    //   )
    //     strengths = 3;
    //   return strengths;
    // },
  },
  mounted() {
    // Call the validatePassword method here
    this.validatePassword(this.password);
    this.validatePassword1(this.password1);
  },
};
</script>
