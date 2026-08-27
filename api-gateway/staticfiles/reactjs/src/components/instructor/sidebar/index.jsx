import React from "react";
import {
  Bell,
  Book,
  DollarSign,
  Home,
  Lock,
  PieChart,
  Power,
  RefreshCw,
  Server,
  Settings,
  ShoppingBag,
  Star,
  Trash2,
  User,
  Users,
} from "react-feather";
import { Link } from "react-router-dom";
import { InstructorProfileBg, User15 } from "../../imagepath";
import StickyBox from "react-sticky-box";

// eslint-disable-next-line react/prop-types
export default function InstructorSidebar({ activeMenu }) {
  return (
    <div className="col-xl-3 col-lg-4 col-md-12 theiaStickySidebar">
      <StickyBox offsetTop={20} offsetBottom={20}>
      <div className="sideStickyBar">
        <div className="settings-widget dash-profile">
          <div className="settings-menu p-0">
            <div className="profile-bg">
              <h5>Beginner</h5>
              <img src={InstructorProfileBg} alt="" />
              <div className="profile-img">
                <Link to="/instructor-profile">
                  <img src={User15} alt="" />
                </Link>
              </div>
            </div>
            <div className="profile-group">
              <div className="profile-name text-center">
                <h4>
                  <Link to="/instructor-profile">Jenny Wilson</Link>
                </h4>
                <p>Instructor</p>
              </div>
              <div className="go-dashboard text-center">
                <Link to="/add-course" className="btn btn-primary">
                  Create New Course
                </Link>
              </div>
            </div>
          </div>
        </div>
        <div className="settings-widget account-settings feather-icon">
          <div className="settings-menu">
            <h3>DASHBOARD</h3>
            <ul>
              <li className="nav-item">
                <Link
                  to="/instructor-dashboard"
                  className={
                    activeMenu === "Dashboard" ? "nav-item active" : "nav-item"
                  }
                >
                  <Home size={20} /> My Dashboard
                </Link>
              </li>
              <li
                className={
                  activeMenu === "Courses" ? "nav-item active" : "nav-item"
                }
              >
                <Link to="/instructor-course" className="nav-link">
                  <Book size={20} /> My Courses
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  to="/instructor-reviews"
                  className={
                    activeMenu === "Reviews" ? "nav-item active" : "nav-item"
                  }
                >
                  <Star size={20} /> Reviews
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  to="/instructor-earnings"
                  className={
                    activeMenu === "Earnings" ? "nav-item active" : "nav-item"
                  }
                >
                  <PieChart size={20} /> Earnings
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  to="/instructor-orders"
                  className={
                    activeMenu === "Orders" ? "nav-item active" : "nav-item"
                  }
                >
                  <ShoppingBag size={20} /> Orders
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  to="/instructor-student-grid"
                  className={
                    activeMenu === ("StudentGrid" || "StudentList")
                      ? "nav-item active"
                      : "nav-item"
                  }
                >
                  <Users size={20} /> Students
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  to="/instructor-payouts"
                  className={
                    activeMenu === "Payouts" ? "nav-item active" : "nav-item"
                  }
                >
                  <DollarSign size={20} /> Payouts
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  to="/instructor-tickets"
                  className={
                    activeMenu === "Tickets" ? "nav-item active" : "nav-item"
                  }
                >
                  <Server size={20} /> Support Tickets
                </Link>
              </li>
            </ul>
            <div className="instructor-title">
              <h3>ACCOUNT SETTINGS</h3>
            </div>
            <ul>
              <li className="nav-item">
                <Link
                  to="/instructor-edit-profile"
                  className={
                    activeMenu === "EditProfile"
                      ? "nav-item active"
                      : "nav-item"
                  }
                >
                  <Settings size={20} /> Edit Profile
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  to="/instructor-security"
                  className={
                    activeMenu === "Security" ? "nav-item active" : "nav-item"
                  }
                >
                  <User size={20} /> Security
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  to="/instructor-social-profile"
                  className={
                    activeMenu === "SocialProfile"
                      ? "nav-item active"
                      : "nav-item"
                  }
                >
                  <RefreshCw size={20} /> Social Profiles
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  to="/instructor-notifications"
                  className={
                    activeMenu === "Notification"
                      ? "nav-item active"
                      : "nav-item"
                  }
                >
                  <Bell size={20} /> Notifications
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  to="/instructor-profile-privacy"
                  className={
                    activeMenu === "ProfilePrivacy"
                      ? "nav-item active"
                      : "nav-item"
                  }
                >
                  <Lock size={20} /> Profile Privacy
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  to="/instructor-delete-profile"
                  className={
                    activeMenu === "DeleteProfile"
                      ? "nav-item active"
                      : "nav-item"
                  }
                >
                  <Trash2 size={20} /> Delete Profile
                </Link>
              </li>
              <li className="nav-item">
                <Link
                  to="/instructor-linked-account"
                  className={
                    activeMenu === "LinkedAccount"
                      ? "nav-item active"
                      : "nav-item"
                  }
                >
                  <User size={20} /> Linked Accounts
                </Link>
              </li>
              <li className="nav-item">
                <Link to="/" className="nav-link">
                  <Power size={20} /> Sign Out
                </Link>
              </li>
            </ul>
          </div>
        </div>
      </div>
      </StickyBox>
    </div>
  );
}
