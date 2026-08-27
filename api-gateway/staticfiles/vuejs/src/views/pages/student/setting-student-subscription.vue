<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layouts></layouts>

    <!--Dashbord Student -->
    <div class="page-content">
      <div class="container">
        <div class="row">
          <studentsidebar></studentsidebar>

          <!-- My Subscriptions -->
          <div class="col-xl-9 col-md-8">
            <div class="settings-widget profile-details">
              <div class="settings-menu p-0">
                <div class="profile-heading subscription-group d-flex align-items-center">
                  <div class="subscription-name">
                    <h3>My Subscriptions</h3>
                    <p>Here is list of package/product that you have subscribed.</p>
                  </div>
                  <div class="upgrade-now grad-border hvr-sweep-to-right">
                    <router-link to="pricing-plan" class="btn btn-primary"
                      >Upgrade Now — Go Pro $50.00</router-link
                    >
                  </div>
                </div>
                <div class="monthly-subscribtion comman-space border-line">
                  <div class="monthly-group d-flex align-items-center">
                    <div class="subscribtion-active">
                      <div class="active-btns">
                        <button type="button" class="btn btn-success">Active</button>
                      </div>
                      <h5>Monthly</h5>
                      <p>Subscription ID: #100010002</p>
                    </div>
                    <div class="active-change-plan grad-border hvr-sweep-to-right">
                      <router-link to="pricing-plan" class="btn btn-primary"
                        >Change Plan</router-link
                      >
                    </div>
                  </div>
                  <div class="month-plan-detail">
                    <div class="row">
                      <div class="col-xl-3 col-md-6 d-flex">
                        <div class="bill-widget d-flex align-items-center">
                          <div class="plan-icons">
                            <i class="feather-calendar"></i>
                          </div>
                          <div class="bill-name-group">
                            <h5>Started On</h5>
                            <p>Jan 1, 2023</p>
                          </div>
                        </div>
                      </div>
                      <div class="col-xl-2 col-md-6 d-flex">
                        <div class="bill-widget d-flex align-items-center">
                          <div class="plan-icons">
                            <i class="feather-credit-card"></i>
                          </div>
                          <div class="bill-name-group">
                            <h5>Price</h5>
                            <p>Monthly</p>
                          </div>
                        </div>
                      </div>
                      <div class="col-xl-3 col-md-6 d-flex">
                        <div class="bill-widget d-flex align-items-center">
                          <div class="plan-icons">
                            <i class="feather-book-open"></i>
                          </div>
                          <div class="bill-name-group">
                            <h5>Access</h5>
                            <p>Access All Courses</p>
                          </div>
                        </div>
                      </div>
                      <div class="col-xl-4 col-md-6 d-flex">
                        <div class="bill-widget d-flex align-items-center">
                          <div class="plan-icons">
                            <i class="feather-calendar"></i>
                          </div>
                          <div class="bill-name-group">
                            <h5>Billing Date</h5>
                            <p>Next Billing on Jun 1, 2023</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="monthly-subscribtion comman-space">
                  <div class="monthly-group d-flex align-items-center">
                    <div class="subscribtion-active">
                      <div class="active-btns">
                        <button type="button" class="btn btn-danger">Expired</button>
                      </div>
                      <h5>Free Plan</h5>
                      <p>Subscription ID: #100010002</p>
                    </div>
                    <div class="active-change-plan grad-border">
                      <button type="button" class="btn btn-default">Disabled</button>
                    </div>
                  </div>
                  <div class="month-plan-detail">
                    <div class="row">
                      <div class="col-xl-3 col-md-6 d-flex">
                        <div class="bill-widget d-flex align-items-center">
                          <div class="plan-icons">
                            <i class="feather-calendar"></i>
                          </div>
                          <div class="bill-name-group">
                            <h5>Started On</h5>
                            <p>May 1, 2023</p>
                          </div>
                        </div>
                      </div>
                      <div class="col-xl-2 col-md-6 d-flex">
                        <div class="bill-widget d-flex align-items-center">
                          <div class="plan-icons">
                            <i class="feather-credit-card"></i>
                          </div>
                          <div class="bill-name-group">
                            <h5>Price</h5>
                            <p>Monthly</p>
                          </div>
                        </div>
                      </div>
                      <div class="col-xl-3 col-md-6 d-flex">
                        <div class="bill-widget d-flex align-items-center">
                          <div class="plan-icons">
                            <i class="feather-book-open"></i>
                          </div>
                          <div class="bill-name-group">
                            <h5>Access</h5>
                            <p>Access All Courses</p>
                          </div>
                        </div>
                      </div>
                      <div class="col-xl-4 col-md-6 d-flex">
                        <div class="bill-widget d-flex align-items-center">
                          <div class="plan-icons">
                            <i class="feather-calendar"></i>
                          </div>
                          <div class="bill-name-group">
                            <h5>Billing Date</h5>
                            <p>Next Billing on Jun 1, 2023</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- My Subscriptions -->
        </div>
      </div>
    </div>
    <!-- /Dashbord Student -->

    <layouts1></layouts1>
  </div>
  <!-- /Main Wrapper -->
</template>
