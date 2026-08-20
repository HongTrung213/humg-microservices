<template>
  <!-- sidebar -->
  <div class="col-xl-3 col-md-4 theiaStickySidebar">
    <div class="stickysidebar">
      <div class="settings-widget dash-profile mb-3">
        <div class="settings-menu p-0">
          <div class="profile-bg">
            <h5>Beginner</h5>
            <img src="@/assets/img/profile-bg.jpg" alt="" />
            <div class="profile-img">
              <router-link to="student-profile"
                ><img src="@/assets/img/user/user11.jpg" alt=""
              /></router-link>
            </div>
          </div>
          <div class="profile-group">
            <div class="profile-name text-center">
              <h4><router-link to="student-profile">Rolands R</router-link></h4>
              <p>Student</p>
            </div>
            <div class="go-dashboard text-center">
              <router-link to="deposit-student-dashboard" class="btn btn-primary"
                >Go to Dashboard</router-link
              >
            </div>
          </div>
        </div>
      </div>
      <div class="settings-widget account-settings">
        <div class="settings-menu">
          <h3>ACCOUNT SETTINGS</h3>
          <ul>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'setting-edit-profile' ? 'active' : 'notactive'"
                to="setting-edit-profile"
                class="nav-link"
              >
                <i class="feather-settings"></i> Edit Profile
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="
                  currentPath == 'setting-student-security' ? 'active' : 'notactive'
                "
                to="setting-student-security"
                class="nav-link"
              >
                <i class="feather-user"></i> Security
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="
                  currentPath == 'setting-student-social-profile' ? 'active' : 'notactive'
                "
                to="setting-student-social-profile"
                class="nav-link"
              >
                <i class="feather-refresh-cw"></i> Social Profiles
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="
                  currentPath == 'setting-student-notification' ? 'active' : 'notactive'
                "
                to="setting-student-notification"
                class="nav-link"
              >
                <i class="feather-bell"></i> Notifications
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'setting-student-privacy' ? 'active' : 'notactive'"
                to="setting-student-privacy"
                class="nav-link"
              >
                <i class="feather-lock"></i> Profile Privacy
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="
                  currentPath == 'setting-student-delete-profile' ? 'active' : 'notactive'
                "
                to="setting-student-delete-profile"
                class="nav-link"
              >
                <i class="feather-trash-2"></i> Delete Profile
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="
                  currentPath == 'setting-student-accounts' ? 'active' : 'notactive'
                "
                to="setting-student-accounts"
                class="nav-link"
              >
                <i class="feather-user"></i> Linked Accounts
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="
                  currentPath == 'setting-student-referral' ? 'active' : 'notactive'
                "
                to="setting-student-referral"
                class="nav-link"
              >
                <i class="feather-user-plus"></i> Referrals
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'login' ? 'active' : 'notactive'"
                to="login"
                class="nav-link"
              >
                <i class="feather-power"></i> Sign Out
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'setting-support-tickets' ? 'active' : 'notactive'"
                to="setting-support-tickets"
                class="nav-link"
              >
                <i class="feather-clipboard"></i> Support Tickets
              </router-link>
            </li>
          </ul>
          <h3 class="student-title">SUBSCRIPTION</h3>
          <ul>
            <li class="nav-item">
              <router-link
                :class="
                  currentPath == 'setting-student-subscription' ? 'active' : 'notactive'
                "
                to="setting-student-subscription"
                class="nav-link"
              >
                <i class="feather-calendar"></i> My Subscriptions
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'setting-student-billing' ? 'active' : 'notactive'"
                to="setting-student-billing"
                class="nav-link"
              >
                <i class="feather-credit-card"></i> Billing Info
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'setting-student-payment' ? 'active' : 'notactive'"
                to="setting-student-payment"
                class="nav-link"
              >
                <i class="feather-credit-card"></i> Payment
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'setting-student-invoice' ? 'active' : 'notactive'"
                to="setting-student-invoice"
                class="nav-link"
              >
                <i class="feather-clipboard"></i> Invoice
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <!-- /sidebar -->
</template>
<script>
export default {
  computed: {
    currentPath() {
      return this.$route.name;
    },
  },
};
</script>
