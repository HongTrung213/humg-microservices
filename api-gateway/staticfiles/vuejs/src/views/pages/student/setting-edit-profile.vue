<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layouts></layouts>

    <!--Dashbord Student -->
    <div class="page-content">
      <div class="container">
        <div class="row">
          <studentsidebar></studentsidebar>

          <!-- Profile Details -->
          <div class="col-xl-9 col-md-8">
            <div class="settings-widget profile-details">
              <div class="settings-menu p-0">
                <div class="profile-heading">
                  <h3>Profile Details</h3>
                  <p>You have full control to manage your own account setting.</p>
                </div>
                <div class="course-group mb-0 d-flex">
                  <div class="course-group-img d-flex align-items-center">
                    <router-link to="student-profile"
                      ><img src="@/assets/img/user/user11.jpg" alt="" class="img-fluid"
                    /></router-link>
                    <div class="course-name">
                      <h4><router-link to="student-profile">Your avatar</router-link></h4>
                      <p>PNG or JPG no bigger than 800px wide and tall.</p>
                    </div>
                  </div>
                  <div
                    class="profile-share d-flex align-items-center justify-content-center"
                  >
                    <a href="javascript:;" class="btn btn-success">Update</a>
                    <a href="javascript:;" class="btn btn-danger">Delete</a>
                  </div>
                </div>
                <div class="checkout-form personal-address add-course-info">
                  <div class="personal-info-head">
                    <h4>Personal Details</h4>
                    <p>Edit your personal information and address.</p>
                  </div>
                  <form action="#">
                    <div class="row">
                      <div class="col-lg-6">
                        <div class="form-group">
                          <label class="form-control-label">First Name</label>
                          <input
                            type="text"
                            class="form-control"
                            placeholder="Enter your first Name"
                          />
                        </div>
                      </div>
                      <div class="col-lg-6">
                        <div class="form-group">
                          <label class="form-control-label">Last Name</label>
                          <input
                            type="text"
                            class="form-control"
                            placeholder="Enter your last Name"
                          />
                        </div>
                      </div>
                      <div class="col-lg-6">
                        <div class="form-group">
                          <label class="form-control-label">Phone</label>
                          <input
                            type="text"
                            class="form-control"
                            placeholder="Enter your Phone"
                          />
                        </div>
                      </div>
                      <div class="col-lg-6">
                        <div class="form-group">
                          <label class="form-control-label">Email</label>
                          <input
                            type="text"
                            class="form-control"
                            placeholder="Enter your Email"
                          />
                        </div>
                      </div>
                      <div class="col-lg-6">
                        <div class="form-group">
                          <label class="form-control-label">Birthday</label>
                          <input
                            type="text"
                            class="form-control"
                            placeholder="Birth of Date"
                          />
                        </div>
                      </div>
                      <div class="col-lg-6">
                        <div class="form-group">
                          <label class="form-label">Country</label>
                          <vue-select
                            :options="country"
                            placeholder="Select country"
                            name="sellist1"
                          />
                        </div>
                      </div>
                      <div class="col-lg-6">
                        <div class="form-group">
                          <label class="form-control-label">Address Line 1</label>
                          <input type="text" class="form-control" placeholder="Address" />
                        </div>
                      </div>
                      <div class="col-lg-6">
                        <div class="form-group">
                          <label class="form-control-label"
                            >Address Line 2 (Optional)</label
                          >
                          <input type="text" class="form-control" placeholder="Address" />
                        </div>
                      </div>
                      <div class="col-lg-6">
                        <div class="form-group">
                          <label class="form-control-label">City</label>
                          <input
                            type="text"
                            class="form-control"
                            placeholder="Enter your City"
                          />
                        </div>
                      </div>
                      <div class="col-lg-6">
                        <div class="form-group">
                          <label class="form-control-label">ZipCode</label>
                          <input
                            type="text"
                            class="form-control"
                            placeholder="Enter your Zipcode"
                          />
                        </div>
                      </div>
                      <div class="update-profile">
                        <button type="button" class="btn btn-primary">
                          Update Profile
                        </button>
                      </div>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
          <!-- Profile Details -->
        </div>
      </div>
    </div>
    <!-- /Dashbord Student -->

    <layouts1></layouts1>
  </div>
  <!-- /Main Wrapper -->
</template>
<script>
import Vue from "vue";
export default {
  components: {},
  data() {
    return {
      country: ["Select country", "India", "America", "London"],
    };
  },
};
</script>
