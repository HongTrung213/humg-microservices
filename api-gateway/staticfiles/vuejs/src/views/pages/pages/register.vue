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
                <router-link to="/">Back to Home</router-link>
              </div>
            </div>
            <h1>Sign up</h1>
            <Form
              class="register"
              @submit="onSubmit"
              :validation-schema="schema"
              v-slot="{ errors }"
            >
              <div class="form-group">
                <label class="form-control-label">Full Name</label>
                <input
                  type="text"
                  class="form-control"
                  placeholder="Enter your Full Name"
                />
              </div>
              <div class="form-group">
                <label class="form-control-label">Email</label>
                <Field
                  name="email"
                  type="text"
                  class="form-control mt-2"
                  :class="{ 'is-invalid': errors.email }"
                />
                <div class="invalid-feedback">{{ errors.email }}</div>
                <div class="emailshow text-danger" id="email"></div>
              </div>
              <div class="form-group">
                <label class="form-control-label">Password</label>
                <div class="pass-group" id="passwordInput">
                  <input
                    name="password"
                    :type="showPassword ? 'text' : 'password'"
                    class="form-control pass-input mt-2"
                    :class="{ 'password-error': validationError }"
                    v-model="password"
                    @input="handlePasswordChange"
                  />
                  <span @click="toggleShow" class="toggle-password">
                    <i
                      :class="{
                        'fas fa-eye': showPassword,
                        'fas fa-eye-slash': !showPassword,
                      }"
                    ></i>
                  </span>
                  <div class="invalid-feedback">{{ errors.password }}</div>
                  <div class="emailshow text-danger" id="password"></div>

                  <!-- Conditionally render password strength only if there is a password -->
                  <div
                    v-if="password"
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

                  <!-- Conditionally render password information only if there is a password -->
                  <div v-if="password" id="passwordInfo">
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
              </div>
              <div class="form-check remember-me">
                <label class="form-check-label mb-0">
                  <input class="form-check-input" type="checkbox" name="remember" /> I
                  agree to the
                  <router-link to="term-condition">Terms of Service</router-link> and
                  <router-link to="privacy-policy">Privacy Policy.</router-link>
                </label>
              </div>
              <div class="d-grid">
                <button class="btn btn-primary btn-start" type="submit">
                  Create Account
                </button>
              </div>
            </Form>
          </div>
          <div class="google-bg text-center">
            <span><a href="javascript:void(0);">Or sign in with</a></span>
            <div class="sign-google">
              <ul>
                <li>
                  <a href="javascript:void(0);"
                    ><img
                      src="@/assets/img/net-icon-01.png"
                      class="img-fluid"
                      alt="Logo"
                    />
                    Sign In using Google</a
                  >
                </li>
                <li>
                  <a href="javascript:void(0);"
                    ><img
                      src="@/assets/img/net-icon-02.png"
                      class="img-fluid"
                      alt="Logo"
                    />Sign In using Facebook</a
                  >
                </li>
              </ul>
            </div>
            <p class="mb-0">
              Already have an account? <router-link to="login">Sign in</router-link>
            </p>
          </div>
        </div>
        <!-- /Login -->
      </div>
    </div>
  </div>
  <!-- /Main Wrapper -->
</template>
<script>
import { Form, Field } from "vee-validate";
import { router } from "@/router";
import VueRouter from "vue-router";
import * as Yup from "yup";
export default {
  data() {
    return {
      password: "",
      showPassword: false,
      validationError: 0,
      strength: "",
      errors: {
        password: "",
      },
    };
  },
  components: {
    Form,
    Field,
  },
  computed: {
    buttonLabel() {
      return this.showPassword ? "Hide" : "Show";
    },
  },
  setup() {
    const schema = Yup.object().shape({
      email: Yup.string().required("Email is required").email("Email is invalid"),
      password: Yup.string()
        .min(6, "Password must be at least 6 characters")
        .required("Password is required"),
    });
    const onSubmit = (values) => {
      if (values.password === values.password) {
        let Rawdata = localStorage.getItem("storedData");
        let Pdata = [];
        Pdata = JSON.parse(Rawdata);
        const Eresult = Pdata.find(({ email }) => email == values.email);
        if (Eresult) {
          document.getElementById("email").innerHTML = "This email are already exist";
        } else {
          Pdata.push(values);
          const jsonData = JSON.stringify(Pdata);
          router.push("/login");
          localStorage.setItem("storedData", jsonData);
        }
      } else {
        document.getElementById("password").innerHTML = "Password not matching";
      }
    };
    return {
      schema,
      onSubmit,
    };
  },
  methods: {
    handlePasswordChange() {
      let passwordValue = this.password;
      let passwordLength = passwordValue.length;
      let poorPassword = /[a-z]/.test(passwordValue);
      let weakPassword = /(?=.*?[0-9])/.test(passwordValue);
      let strongPassword = /(?=.*?[#?!@$%^&*-])/.test(passwordValue);
      let whitespace = /^\s*$/.test(passwordValue);

      if (passwordValue !== "") {
        if (whitespace) {
          this.errors.password = "whitespaces are not allowed";
        } else {
          this.errors.password = "";
          this.poorPasswordStrength(
            passwordLength,
            poorPassword,
            weakPassword,
            strongPassword
          );
          this.weakPasswordStrength(
            passwordLength,
            poorPassword,
            weakPassword,
            strongPassword
          );
          this.strongPasswordStrength(
            passwordLength,
            poorPassword,
            weakPassword,
            strongPassword
          );
          this.heavyPasswordStrength(
            passwordLength,
            poorPassword,
            weakPassword,
            strongPassword
          );
        }
      } else {
        this.errors.password = "";
        this.validationError = 0;
        this.strength = "";
      }
    },

    toggleShow() {
      this.showPassword = !this.showPassword;
    },

    poorPasswordStrength(passwordLength, poorPassword, weakPassword, strongPassword) {
      if (passwordLength < 8) {
        this.validationError = 2;
        this.strength = "poor";
      }
    },

    weakPasswordStrength(passwordLength, poorPassword, weakPassword, strongPassword) {
      if (passwordLength >= 8 && (poorPassword || weakPassword || strongPassword)) {
        this.validationError = 3;
        this.strength = "weak";
      }
    },

    strongPasswordStrength(passwordLength, poorPassword, weakPassword, strongPassword) {
      if (passwordLength >= 8 && poorPassword && (weakPassword || strongPassword)) {
        this.validationError = 4;
        this.strength = "strong";
      }
    },

    heavyPasswordStrength(passwordLength, poorPassword, weakPassword, strongPassword) {
      if (passwordLength >= 8 && poorPassword && weakPassword && strongPassword) {
        this.validationError = 5;
        this.strength = "heavy";
      }
    },
  },
};
</script>
