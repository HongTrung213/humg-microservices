<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layoutsinstructor></layoutsinstructor>

    <!-- Page Wrapper -->
    <div class="page-content">
      <div class="container">
        <div class="row">
          <instructorsidebar></instructorsidebar>

          <!-- Instructor Dashboard -->
          <div class="col-xl-9 col-lg-8 col-md-12">
            <div class="tak-instruct-group">
              <div class="row">
                <div class="col-md-12">
                  <div class="settings-widget">
                    <div class="settings-inner-blk p-0">
                      <div class="sell-course-head comman-space">
                        <h3>Payout Method</h3>
                        <p>Order Dashboard is a quick overview of all current orders.</p>
                      </div>
                    </div>
                  </div>
                  <div class="settings-widget">
                    <div class="settings-inner-blk p-0">
                      <div class="comman-space pb-0">
                        <div
                          class="sell-course-head withdraw-history-head border-bottom-0"
                        >
                          <h3>Withdraw History</h3>
                        </div>
                        <div class="instruct-search-blk mb-0">
                          <div class="show-filter all-select-blk">
                            <form action="#">
                              <div class="row gx-2 align-items-center">
                                <div class="col-md-6 col-lg-3 col-item">
                                  <div class="form-group select-form mb-0">
                                    <vue-select :options="days" placeholder="30 days" />
                                  </div>
                                </div>
                                <div class="col-md-6 col-lg-3 col-item">
                                  <div class="form-group select-form mb-0">
                                    <vue-select :options="Oct" placeholder="Oct 2023" />
                                  </div>
                                </div>
                                <div class="col-md-6 col-lg-3 col-item">
                                  <div class="form-group select-form mb-0">
                                    <vue-select
                                      :options="Transaction"
                                      placeholder="Transaction Type"
                                    />
                                  </div>
                                </div>
                                <div class="col-md-6 col-lg-3 col-item">
                                  <div class="download-widra">
                                    <a href="javascript:;"
                                      ><i class="feather-download"></i
                                    ></a>
                                  </div>
                                </div>
                              </div>
                            </form>
                          </div>
                        </div>
                      </div>
                      <div class="comman-space pb-0">
                        <div
                          class="settings-referral-blk course-instruct-blk table-responsive"
                        >
                          <!-- Instructor Users-->
                          <table class="table table-nowrap mb-0">
                            <thead>
                              <tr>
                                <th>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </th>
                                <th>ID</th>
                                <th>DATE</th>
                                <th>STATUS</th>
                                <th>AMOUNT</th>
                                <th>METHOD</th>
                                <th>&nbsp;</th>
                              </tr>
                            </thead>
                            <tbody>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <router-link to="view-invoice">#1061</router-link>
                                </td>
                                <td>10-05-23</td>
                                <td><span class="badge info-low">Paid</span></td>
                                <td>$1800</td>
                                <td>Mastercard</td>
                                <td>
                                  <a href="javascript:;"
                                    ><i class="feather-more-vertical"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <router-link to="view-invoice">#1051</router-link>
                                </td>
                                <td>10-05-23</td>
                                <td><span class="badge info-low">Paid</span></td>
                                <td>$1200</td>
                                <td>Mastercard</td>
                                <td>
                                  <a href="javascript:;"
                                    ><i class="feather-more-vertical"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <router-link to="view-invoice">#2061</router-link>
                                </td>
                                <td>10-05-23</td>
                                <td><span class="badge info-medium">Pending</span></td>
                                <td>$1100</td>
                                <td>Visa</td>
                                <td>
                                  <a href="javascript:;"
                                    ><i class="feather-more-vertical"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <router-link to="view-invoice">#1021</router-link>
                                </td>
                                <td>10-05-23</td>
                                <td><span class="badge info-high">Cancel</span></td>
                                <td>$1200</td>
                                <td>Visa</td>
                                <td>
                                  <a href="javascript:;"
                                    ><i class="feather-more-vertical"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <router-link to="view-invoice">#1051</router-link>
                                </td>
                                <td>10-05-23</td>
                                <td><span class="badge info-low">Paid</span></td>
                                <td>$1500</td>
                                <td>Mastercard</td>
                                <td>
                                  <a href="javascript:;"
                                    ><i class="feather-more-vertical"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <router-link to="view-invoice">#1061</router-link>
                                </td>
                                <td>10-05-23</td>
                                <td><span class="badge info-low">Paid</span></td>
                                <td>$2200</td>
                                <td>Visa</td>
                                <td>
                                  <a href="javascript:;"
                                    ><i class="feather-more-vertical"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <router-link to="view-invoice">#2061</router-link>
                                </td>
                                <td>10-05-23</td>
                                <td><span class="badge info-low">Paid</span></td>
                                <td>$3200</td>
                                <td>Mastercard</td>
                                <td>
                                  <a href="javascript:;"
                                    ><i class="feather-more-vertical"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <router-link to="view-invoice">#1161</router-link>
                                </td>
                                <td>10-05-23</td>
                                <td><span class="badge info-low">Paid</span></td>
                                <td>$1400</td>
                                <td>Visa</td>
                                <td>
                                  <a href="javascript:;"
                                    ><i class="feather-more-vertical"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <router-link to="view-invoice">#3061</router-link>
                                </td>
                                <td>10-05-23</td>
                                <td><span class="badge info-low">Paid</span></td>
                                <td>$1300</td>
                                <td>Mastercard</td>
                                <td>
                                  <a href="javascript:;"
                                    ><i class="feather-more-vertical"></i
                                  ></a>
                                </td>
                              </tr>
                              <tr>
                                <td>
                                  <div class="form-check instruct-check-list">
                                    <input
                                      class="form-check-input"
                                      type="checkbox"
                                      name="option1"
                                    />
                                  </div>
                                </td>
                                <td>
                                  <router-link to="view-invoice">#1061</router-link>
                                </td>
                                <td>10-05-23</td>
                                <td><span class="badge info-high">Cancel</span></td>
                                <td>$1200</td>
                                <td>Mastercard</td>
                                <td>
                                  <a href="javascript:;"
                                    ><i class="feather-more-vertical"></i
                                  ></a>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                          <!-- /Instructor List-->
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <!-- /Instructor Dashboard -->
        </div>
      </div>
    </div>
    <!-- /Page Wrapper -->

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
      days: ["30 days", "20 days", "10 days"],
      Oct: ["Oct 2023", "Nov 2023", "Jan 2023"],
      Transaction: ["Transaction Type", "Cash", "Card", "Online"],
    };
  },
};
</script>
