<template>
  <!-- Sidebar -->
  <div class="col-xl-3 col-lg-4 col-md-12 theiaStickySidebar">
    <div class="stickysidebar">
      <div class="settings-widget dash-profile">
        <div class="settings-menu p-0">
          <div class="profile-bg">
            <h5>Beginner</h5>
            <img src="@/assets/img/instructor-profile-bg.jpg" alt="" />
            <div class="profile-img">
              <router-link to="instructor-profile"
                ><img src="@/assets/img/user/user15.jpg" alt=""
              /></router-link>
            </div>
          </div>
          <div class="profile-group">
            <div class="profile-name text-center">
              <h4><router-link to="instructor-profile">Jenny Wilson</router-link></h4>
              <p>Instructor</p>
            </div>
            <div class="go-dashboard text-center">
              <router-link to="add-course" class="btn btn-primary"
                >Create New Course</router-link
              >
            </div>
          </div>
        </div>
      </div>
      <div class="settings-widget account-settings">
        <div class="settings-menu">
          <h3>DASHBOARD</h3>
          <ul>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'instructor-dashboard' ? 'active' : 'notactive'"
                to="instructor-dashboard"
                class="nav-link"
              >
                <i class="feather-home"></i> My Dashboard
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'instructor-course' ? 'active' : 'notactive'"
                to="instructor-course"
                class="nav-link"
              >
                <i class="feather-book"></i> My Courses
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'instructor-reviews' ? 'active' : 'notactive'"
                to="instructor-reviews"
                class="nav-link"
              >
                <i class="feather-star"></i> Reviews
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'instructor-earnings' ? 'active' : 'notactive'"
                to="instructor-earnings"
                class="nav-link"
              >
                <i class="feather-pie-chart"></i> Earnings
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'instructor-orders' ? 'active' : 'notactive'"
                to="instructor-orders"
                class="nav-link"
              >
                <i class="feather-shopping-bag"></i> Orders
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="
                  currentPath == 'instructor-student-grid' ||
                  currentPath == 'instructor-student-list'
                    ? 'active'
                    : 'notactive'
                "
                to="instructor-student-grid"
                class="nav-link"
              >
                <i class="feather-users"></i> Students
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'instructor-payouts' ? 'active' : 'notactive'"
                to="instructor-payouts"
                class="nav-link"
              >
                <i class="feather-dollar-sign"></i> Payouts
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'instructor-tickets' ? 'active' : 'notactive'"
                to="instructor-tickets"
                class="nav-link"
              >
                <i class="feather-server"></i> Support Tickets
              </router-link>
            </li>
          </ul>
          <div class="instructor-title">
            <h3>ACCOUNT SETTINGS</h3>
          </div>
          <ul>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'instructor-edit-profile' ? 'active' : 'notactive'"
                to="instructor-edit-profile"
                class="nav-link"
              >
                <i class="feather-settings"></i> Edit Profile
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'instructor-security' ? 'active' : 'notactive'"
                to="instructor-security"
                class="nav-link"
              >
                <i class="feather-user"></i> Security
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="
                  currentPath == 'instructor-social-profiles' ? 'active' : 'notactive'
                "
                to="instructor-social-profiles"
                class="nav-link"
              >
                <i class="feather-refresh-cw"></i> Social Profiles
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'instructor-notification' ? 'active' : 'notactive'"
                to="instructor-notification"
                class="nav-link"
              >
                <i class="feather-bell"></i> Notifications
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="
                  currentPath == 'instructor-profile-privacy' ? 'active' : 'notactive'
                "
                to="instructor-profile-privacy"
                class="nav-link"
              >
                <i class="feather-lock"></i> Profile Privacy
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="
                  currentPath == 'instructor-delete-profile' ? 'active' : 'notactive'
                "
                to="instructor-delete-profile"
                class="nav-link"
              >
                <i class="feather-trash-2"></i> Delete Profile
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="
                  currentPath == 'instructor-linked-account' ? 'active' : 'notactive'
                "
                to="instructor-linked-account"
                class="nav-link"
              >
                <i class="feather-user"></i> Linked Accounts
              </router-link>
            </li>
            <li class="nav-item">
              <router-link
                :class="currentPath == 'index' ? 'active' : 'notactive'"
                to="/"
                class="nav-link"
              >
                <i class="feather-power"></i> Sign Out
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <!-- /Sidebar -->
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
