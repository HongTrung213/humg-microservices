<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layouts2></layouts2>
    <checkoutbreadcrumb></checkoutbreadcrumb>
    <!-- Cart -->
    <section class="course-content checkout-widget">
      <div class="container">
        <div class="row">
          <div class="col-lg-8">
            <!-- Billing Address -->
            <div class="student-widget">
              <div class="student-widget-group add-course-info">
                <div class="cart-head">
                  <h4>Billing Address</h4>
                </div>
                <div class="checkout-form">
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
                      <div class="col-lg-12">
                        <div class="form-group">
                          <label class="form-control-label"
                            >Phone Number (Optional)</label
                          >
                          <input
                            type="text"
                            class="form-control"
                            placeholder="Phone Number"
                          />
                        </div>
                      </div>
                      <div class="col-lg-12">
                        <div class="form-group">
                          <label class="form-control-label">Address Line 1</label>
                          <input type="text" class="form-control" placeholder="Address" />
                        </div>
                      </div>
                      <div class="col-lg-12">
                        <div class="form-group">
                          <label class="form-control-label"
                            >Address Line 2 (Optional)</label
                          >
                          <input type="text" class="form-control" placeholder="Address" />
                        </div>
                      </div>
                      <div class="col-lg-4">
                        <div class="form-group">
                          <label class="form-label">State</label>
                          <vue-select
                            :options="State"
                            placeholder="Select State"
                            name="sellist1"
                          />
                        </div>
                      </div>
                      <div class="col-lg-4">
                        <div class="form-group">
                          <label class="form-label">Country</label>
                          <vue-select
                            :options="country"
                            placeholder="Select country"
                            name="sellist1"
                          />
                        </div>
                      </div>
                      <div class="col-lg-4">
                        <div class="form-group">
                          <label class="form-control-label">Zip/Postal Code</label>
                          <input type="text" class="form-control" />
                        </div>
                      </div>
                      <div class="col-md-12 col-lg-10">
                        <div class="form-group ship-check">
                          <input
                            class="form-check-input"
                            type="checkbox"
                            name="remember"
                          />
                          Shipping address is the same as my billing address
                        </div>
                        <div class="form-group ship-check mb-0">
                          <input
                            class="form-check-input"
                            type="checkbox"
                            name="remember"
                          />
                          Save this information for next time
                        </div>
                      </div>
                    </div>
                  </form>
                </div>
              </div>
            </div>
            <!-- /Billing Address -->

            <!-- /Payment Method -->
            <div class="student-widget pay-method">
              <div class="student-widget-group add-course-info">
                <div class="cart-head">
                  <h4>Payment Method</h4>
                </div>
                <div class="checkout-form">
                  <form action="cart">
                    <div class="row">
                      <div class="col-lg-12">
                        <div class="wallet-method">
                          <label class="radio-inline custom_radio me-4">
                            <input type="radio" name="optradio" checked="" />
                            <span class="checkmark"></span> Credit or Debit card
                          </label>
                          <label class="radio-inline custom_radio">
                            <input type="radio" name="optradio" />
                            <span class="checkmark"></span> PayPal
                          </label>
                        </div>
                        <div class="form-group">
                          <label class="form-control-label">Card Number</label>
                          <input
                            type="text"
                            class="form-control"
                            placeholder="XXXX XXXX XXXX XXXX"
                          />
                        </div>
                      </div>
                      <div class="col-lg-4">
                        <div class="form-group">
                          <label class="form-label">Month</label>
                          <vue-select
                            :options="Month"
                            placeholder="Month"
                            name="sellist1"
                          />
                        </div>
                      </div>
                      <div class="col-lg-4">
                        <div class="form-group">
                          <label class="form-label">Year</label>
                          <vue-select
                            :options="Year"
                            placeholder="Year"
                            name="sellist1"
                          />
                        </div>
                      </div>
                      <div class="col-lg-4">
                        <div class="form-group">
                          <label class="form-control-label">CVV Code </label>
                          <input type="text" class="form-control" placeholder="XXXX" />
                        </div>
                      </div>
                      <div class="col-lg-12">
                        <div class="form-group">
                          <label class="form-control-label">Name on Card</label>
                          <input type="text" class="form-control" placeholder="Address" />
                        </div>
                      </div>
                      <div class="col-md-12 col-lg-10">
                        <div class="form-group ship-check">
                          <input
                            class="form-check-input"
                            type="checkbox"
                            name="remember"
                          />
                          Remember this card
                        </div>
                      </div>
                      <div class="payment-btn">
                        <button class="btn btn-primary" type="submit">
                          Make a Payment
                        </button>
                      </div>
                    </div>
                  </form>
                </div>
              </div>
            </div>
            <!-- /Payment Method -->
          </div>
          <div class="col-lg-4 theiaStickySidebar">
            <div class="stickysidebar">
              <div class="student-widget select-plan-group">
                <div class="student-widget-group">
                  <div class="plan-header">
                    <h4>Selected Plan</h4>
                  </div>
                  <div class="basic-plan">
                    <h3>Basic</h3>
                    <p>For individuals who just need to start with the basic features</p>
                    <p>per user, per month when billed monthly</p>
                    <h2><span>$</span>10</h2>
                  </div>
                  <div class="benifits-feature">
                    <h3>Benefits</h3>
                    <ul>
                      <li><i class="fas fa-circle"></i> Access to slack community</li>
                      <li><i class="fas fa-circle"></i> Access to support team</li>
                      <li><i class="fas fa-circle"></i> Algorithmic bidding</li>
                      <li><i class="fas fa-circle"></i> Keyword and ASIN harvesting</li>
                    </ul>
                  </div>
                  <div class="benifits-feature">
                    <h3>Features</h3>
                    <ul>
                      <li><i class="fas fa-circle"></i> Search term isolation</li>
                      <li><i class="fas fa-circle"></i> Total sales analytics</li>
                      <li><i class="fas fa-circle"></i> Best seller rank</li>
                      <li><i class="fas fa-circle"></i> Placement optimization</li>
                    </ul>
                  </div>
                  <div class="plan-change">
                    <router-link to="pricing-plan" class="btn btn-primary"
                      >Change the Plan</router-link
                    >
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- /Cart -->

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
      State: ["Select State", "Brazil", "French"],
      country: ["Select country", "India", "America", "London"],
      Month: ["Month", "Jun", "Feb", "March"],
      Year: ["Year", "2023", "2023", "2023"],
    };
  },
};
</script>
