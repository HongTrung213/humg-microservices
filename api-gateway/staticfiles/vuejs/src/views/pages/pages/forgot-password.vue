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
            <h1>Forgot Password ?</h1>
            <div class="reset-password">
              <p>Enter your email to reset your password.</p>
            </div>
            <Form @submit="onSubmit" :validation-schema="schema" v-slot="{ errors }">
              <div class="form-group">
                <label class="form-control-label">Email</label>
                <Field
                  name="email"
                  type="text"
                  class="form-control"
                  :class="{ 'is-invalid': errors.email }"
                />
              </div>
              <div class="d-grid">
                <button class="btn btn-start" type="submit">Submit</button>
              </div>
            </Form>
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
import * as Yup from "yup";
import { router } from "@/router";
export default {
  data() {
    return {
      emailError: "",
    };
  },
  components: {
    Form,
    Field,
  },
  methods: {
    submitForm() {
      this.$router.push("/login");
    },
    onSubmit(values) {
      this.emailError = "";

      let data = localStorage.getItem("storedData");
      var Pdata = JSON.parse(data);
      const Eresult = Pdata.find(({ email }) => email === values.email);
      if (Eresult) {
        if (Eresult.email === values.email) {
          this.$router.push("/login"); // Use this.$router instead of router
        }
      } else {
        this.emailError = "Email is not valid";
      }
    },
  },
  setup() {
    const schema = Yup.object().shape({
      email: Yup.string().required("Email is required").email("Email is invalid"),
    });
    return {
      schema,
    };
  },
};
</script>
