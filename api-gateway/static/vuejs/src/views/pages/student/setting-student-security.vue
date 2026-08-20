<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layouts></layouts>

    <!--Dashbord Student -->
    <div class="page-content">
      <div class="container">
        <div class="row">
          <studentsidebar></studentsidebar>

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
export default {
  data() {
    return {
      showPassword: true,
      password: "",
      validationError: 0,
      isPasswordValid: false,
      strength: "",
    };
  },
  methods: {
    handlePasswordChange() {
      const newPassword = this.password;
      this.validatePassword(newPassword);
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
    strengthColor(count) {
      if (count < 1) return "";
      if (count < 2) return "poor";
      if (count < 3) return "weak";
      if (count < 4) return "strong";
      return "heavy";
    },
    hasNumber(value) {
      return /[0-9]/.test(value);
    },
    hasMixed(value) {
      return /[a-z]/.test(value) && /[A-Z]/.test(value);
    },
    hasSpecial(value) {
      return /[!#@$%^&*)(+=._-]/.test(value);
    },
    strengthIndicator(value) {
      let strengths = 0;

      if (value.length >= 8) strengths = 1;
      if (this.hasNumber(value) && value.length >= 8) strengths = 2;
      if (this.hasSpecial(value) && value.length >= 8 && this.hasNumber(value))
        strengths = 3;
      if (
        this.hasMixed(value) &&
        this.hasSpecial(value) &&
        value.length >= 8 &&
        this.hasNumber(value)
      )
        strengths = 3;
      return strengths;
    },
  },
  mounted() {
    // Call the validatePassword method here
    this.validatePassword(this.password);
  },
};
</script>
