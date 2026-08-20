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
              <div class="settings-inner-blk p-0">
                <div class="profile-heading">
                  <h3>Invoices</h3>
                  <p>You can find all of your order Invoices.</p>
                </div>
                <div class="comman-space pb-0">
                  <div class="settings-invoice-blk table-responsive">
                    <!-- Invoice info-->
                    <table class="table table-borderless mb-0">
                      <thead>
                        <tr>
                          <th>order id</th>
                          <th>date</th>
                          <th>amount</th>
                          <th>status</th>
                          <th>&nbsp;</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>
                            <router-link to="view-invoice" class="invoice-no"
                              >#1001</router-link
                            >
                          </td>
                          <td>15-01-2023, 10:45pm</td>
                          <td>$50.00</td>
                          <td><span class="badge status-due">Due</span></td>
                          <td>
                            <a href="javascript:;" class="btn-style"
                              ><i class="feather-download"></i
                            ></a>
                          </td>
                        </tr>
                        <tr>
                          <td>
                            <router-link to="view-invoice" class="invoice-no"
                              >#1002</router-link
                            >
                          </td>
                          <td>15-02-2023, 10:45pm</td>
                          <td>$50.00</td>
                          <td><span class="badge status-completed">Completed</span></td>
                          <td>
                            <a href="javascript:;" class="btn-style"
                              ><i class="feather-download"></i
                            ></a>
                          </td>
                        </tr>
                        <tr>
                          <td>
                            <router-link to="view-invoice" class="invoice-no"
                              >#1003</router-link
                            >
                          </td>
                          <td>15-03-2023, 10:45pm</td>
                          <td>$50.00</td>
                          <td><span class="badge status-completed">Completed</span></td>
                          <td>
                            <a href="javascript:;" class="btn-style"
                              ><i class="feather-download"></i
                            ></a>
                          </td>
                        </tr>
                        <tr>
                          <td>
                            <router-link to="view-invoice" class="invoice-no"
                              >#1004</router-link
                            >
                          </td>
                          <td>15-04-2023, 10:45pm</td>
                          <td>$50.00</td>
                          <td><span class="badge status-completed">Completed</span></td>
                          <td>
                            <a href="javascript:;" class="btn-style"
                              ><i class="feather-download"></i
                            ></a>
                          </td>
                        </tr>
                        <tr>
                          <td>
                            <router-link to="view-invoice" class="invoice-no"
                              >#1005</router-link
                            >
                          </td>
                          <td>15-05-2023, 10:45pm</td>
                          <td>$50.00</td>
                          <td><span class="badge status-completed">Completed</span></td>
                          <td>
                            <a href="javascript:;" class="btn-style"
                              ><i class="feather-download"></i
                            ></a>
                          </td>
                        </tr>
                        <tr>
                          <td>
                            <router-link to="view-invoice" class="invoice-no"
                              >#1006</router-link
                            >
                          </td>
                          <td>15-06-2023, 10:45pm</td>
                          <td>$50.00</td>
                          <td><span class="badge status-completed">Completed</span></td>
                          <td>
                            <a href="javascript:;" class="btn-style"
                              ><i class="feather-download"></i
                            ></a>
                          </td>
                        </tr>
                        <tr>
                          <td>
                            <router-link to="view-invoice" class="invoice-no"
                              >#1007</router-link
                            >
                          </td>
                          <td>15-04-2023, 10:45pm</td>
                          <td>$50.00</td>
                          <td><span class="badge status-completed">Completed</span></td>
                          <td>
                            <a href="javascript:;" class="btn-style"
                              ><i class="feather-download"></i
                            ></a>
                          </td>
                        </tr>
                        <tr>
                          <td>
                            <router-link to="view-invoice" class="invoice-no"
                              >#1008</router-link
                            >
                          </td>
                          <td>15-05-2023, 10:45pm</td>
                          <td>$50.00</td>
                          <td><span class="badge status-completed">Completed</span></td>
                          <td>
                            <a href="javascript:;" class="btn-style"
                              ><i class="feather-download"></i
                            ></a>
                          </td>
                        </tr>
                        <tr>
                          <td>
                            <router-link to="view-invoice" class="invoice-no"
                              >#1009</router-link
                            >
                          </td>
                          <td>15-06-2023, 10:45pm</td>
                          <td>$50.00</td>
                          <td><span class="badge status-completed">Completed</span></td>
                          <td>
                            <a href="javascript:;" class="btn-style"
                              ><i class="feather-download"></i
                            ></a>
                          </td>
                        </tr>
                        <tr>
                          <td>
                            <router-link to="view-invoice" class="invoice-no"
                              >#1010</router-link
                            >
                          </td>
                          <td>15-03-2023, 10:45pm</td>
                          <td>$50.00</td>
                          <td><span class="badge status-completed">Completed</span></td>
                          <td>
                            <a href="javascript:;" class="btn-style"
                              ><i class="feather-download"></i
                            ></a>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                    <!-- /Invoice info-->
                  </div>
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
