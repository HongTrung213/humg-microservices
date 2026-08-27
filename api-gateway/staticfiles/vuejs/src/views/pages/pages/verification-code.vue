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
            <h1>Enter Varification Code</h1>
            <div class="reset-password">
              <p>We have just sent a verification code to your registed email id</p>
            </div>
            <form @submit.prevent="submitForm" class="verification-code">
              <div class="row">
                <div class="col-lg-12">
                  <div class="d-flex digit-group">
                    <input
                      type="text"
                      class="form-control"
                      id="digit-1"
                      name="digit-1"
                      data-next="digit-2"
                      value="8"
                    />
                    <input
                      type="text"
                      class="form-control"
                      id="digit-2"
                      name="digit-2"
                      data-next="digit-3"
                      data-previous="digit-1"
                    />
                    <input
                      type="text"
                      class="form-control"
                      id="digit-3"
                      name="digit-3"
                      data-next="digit-4"
                      data-previous="digit-2"
                    />
                    <input
                      type="text"
                      class="form-control"
                      id="digit-4"
                      name="digit-4"
                      data-next="digit-5"
                      data-previous="digit-3"
                    />
                  </div>
                </div>
                <div class="send-code">
                  <router-link to="verification-code">Send the code again</router-link>
                </div>
                <div class="d-grid">
                  <button class="btn btn-primary btn-start" type="submit">Submit</button>
                </div>
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
import Vue from "vue";
export default {
  components: {},
  data() {
    return {
      digits: Array.from({ length: 6 }, () => ({ value: "" })),
    };
  },
  methods: {
    submitForm() {
      this.$router.push("/login");
    },

    onKeyUp(index, event) {
      const keyCode = event.keyCode;
      const digit = this.digits[index];
      const inputRefs = this.$refs.inputRefs;
      const input = inputRefs[index];

      if (keyCode === 8 || keyCode === 37) {
        const prev = inputRefs[index - 1];

        if (prev) {
          prev.select();
        }
      } else if (
        (keyCode >= 48 && keyCode <= 57) ||
        (keyCode >= 65 && keyCode <= 90) ||
        (keyCode >= 96 && keyCode <= 105) ||
        keyCode === 39
      ) {
        const next = inputRefs[index + 1];

        if (next) {
          next.select();
        } else {
          // If there is no next input, you may trigger submit here if needed
        }
      }
    },
    onInput(index) {
      const digit = this.digits[index];
      digit.active = digit.value !== "";
    },
  },
};
</script>
