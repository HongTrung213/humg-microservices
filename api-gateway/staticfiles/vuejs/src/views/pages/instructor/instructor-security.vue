<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layoutsinstructor></layoutsinstructor>

    <!--Dashbord Student -->
    <div class="page-content">
      <div class="container">
        <div class="row">
          <instructorsidebar></instructorsidebar>

          <!-- Student Security -->
          <div class="col-xl-9 col-md-8">
            <div class="settings-widget profile-details">
              <div class="settings-menu p-0">
                <div class="profile-heading">
                  <h3>Security</h3>
                  <p>Edit your account settings and change your password here.</p>
                </div>
                <div class="checkout-form personal-address border-line">
                  <div class="personal-info-head">
                    <h4>Email Address</h4>
                    <p>Your current email address is <span>maxwell@example.com</span></p>
                  </div>
                  <form action="#">
                    <div class="new-address">
                      <div class="row">
                        <div class="col-lg-6">
                          <div class="form-group">
                            <label class="form-control-label">New email address</label>
                            <input
                              type="text"
                              class="form-control"
                              placeholder="Enter your New email address"
                            />
                          </div>
                        </div>
                        <div class="profile-share d-flex">
                          <button type="button" class="btn btn-success">Update</button>
                        </div>
                      </div>
                    </div>
                  </form>
                </div>
                <div class="checkout-form personal-address">
                  <div class="personal-info-head">
                    <h4>Change Password</h4>
                    <p>
                      We will email you a confirmation when changing your password, so
                      please expect that email after submitting.
                    </p>
                  </div>
                  <div class="row">
                    <div class="col-lg-6">
                      <form action="#">
                        <div class="form-group">
                          <label class="form-control-label">Current password</label>
                          <input type="password" class="form-control" />
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
                            <span @click="toggleShow" class="toggle-password-sec">
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
                              <span
                                v-else-if="validationError === 3"
                                style="color: orange"
                                >😲 Average. Must contain at least 1 letter or
                                number</span
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
                        <div class="form-group">
                          <label class="form-control-label">Confirm New Password</label>
                          <input type="password" class="form-control" />
                        </div>
                        <div class="update-profile save-password">
                          <button type="button" class="btn btn-primary">
                            Save Password
                          </button>
                        </div>
                      </form>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- Student Security -->
        </div>
      </div>
    </div>
    <!-- /Dashbord Student -->

    <layouts1></layouts1>
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
