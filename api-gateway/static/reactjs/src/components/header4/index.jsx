import React, { useState } from "react";
import { Link } from "react-router-dom";
import { logoFivePng, logoFiveSvg } from "../imagepath";

export const Header4 = () => {
  // change header background on scroll
  const [navbar, setNavbar] = useState(false);

  const changeHeaderBackground = () => {
    if (window.scrollY >= 90) {
      setNavbar(true);
    } else {
      setNavbar(false);
    }
  };

  // Mobile Menu toggle
  const [mobileSubMenu, setMobileSubMenu] = useState(false);
  const [mobileSubMenu2, setMobileSubMenu2] = useState(false);
  const [mobileSubMenu22, setMobileSubMenu22] = useState(false);
  const [mobileSubMenu3, setMobileSubMenu3] = useState(false);
  const [mobileSubMenu32, setMobileSubMenu32] = useState(false);
  const [mobileSubMenu4, setMobileSubMenu4] = useState(false);
  const [mobileSubMenu42, setMobileSubMenu42] = useState(false);
  const [mobileSubMenu43, setMobileSubMenu43] = useState(false);
  const [mobileSubMenu5, setMobileSubMenu5] = useState(false);

  const openMobileMenu = () => {
    document.body.classList.add("menu-opened");
  };
  const hideMobileMenu = () => {
    document.body.classList.remove("menu-opened");
  };

  const openMobileSubMenu = (e) => {
    e.preventDefault();
    setMobileSubMenu(!mobileSubMenu);
  };
  const openMobileSubMenu2 = (e) => {
    e.preventDefault();
    setMobileSubMenu2(!mobileSubMenu2);
  };
  const openMobileSubMenu22 = (e) => {
    e.preventDefault();
    setMobileSubMenu22(!mobileSubMenu22);
  };
  const openMobileSubMenu3 = (e) => {
    e.preventDefault();
    setMobileSubMenu3(!mobileSubMenu3);
  };
  const openMobileSubMenu32 = (e) => {
    e.preventDefault();
    setMobileSubMenu32(!mobileSubMenu32);
  };
  const openMobileSubMenu4 = (e) => {
    e.preventDefault();
    setMobileSubMenu4(!mobileSubMenu4);
  };
  const openMobileSubMenu42 = (e) => {
    e.preventDefault();
    setMobileSubMenu42(!mobileSubMenu42);
  };
  const openMobileSubMenu43 = (e) => {
    e.preventDefault();
    setMobileSubMenu43(!mobileSubMenu43);
  };
  const openMobileSubMenu5 = (e) => {
    e.preventDefault();
    setMobileSubMenu5(!mobileSubMenu5);
  };

  window.addEventListener("scroll", changeHeaderBackground);
  return (
    <>
      <header className="header-five">
        <div className="header-fixed">
          <nav
            className={
              navbar
                ? "navbar navbar-expand-lg header-nav scroll-sticky add-header-bg"
                : "navbar navbar-expand-lg header-nav scroll-sticky"
            }
          >
            <div className="container">
              <div className="navbar-header">
                <Link id="mobile_btn" to="#;" onClick={openMobileMenu}>
                  <span className="bar-icon">
                    <span></span>
                    <span></span>
                    <span></span>
                  </span>
                </Link>
                <Link to="/" className="navbar-brand logo">
                  <img src={logoFivePng} className="img-fluid" alt="Logo" />
                </Link>
              </div>
              <div className="main-menu-wrapper">
                <div className="menu-header">
                  <Link to="/" className="menu-logo">
                    <img src={logoFiveSvg} className="img-fluid" alt="Logo" />
                  </Link>
                  <Link
                    id="menu_close"
                    className="menu-close"
                    to="#;"
                    onClick={hideMobileMenu}
                  >
                    <i className="fas fa-times"></i>
                  </Link>
                </div>
                <ul className="main-nav">
                  <li className="has-submenu active">
                    <Link to="/">
                      Home{" "}
                      <i
                        className="fas fa-chevron-down"
                        onClick={openMobileSubMenu}
                      ></i>
                    </Link>
                    <ul
                      className={
                        mobileSubMenu ? "submenu submenuShow" : "submenu"
                      }
                    >
                      <li>
                        <Link to="/">Home</Link>
                      </li>
                      <li>
                        <Link to="/home2">Home Two</Link>
                      </li>
                      <li>
                        <Link to="/home3">Home Three</Link>
                      </li>
                      <li className="active">
                        <Link to="/home4">Home Four</Link>
                      </li>
                    </ul>
                  </li>
                  <li className="has-submenu">
                    <Link to="">
                      Instructor{" "}
                      <i
                        className="fas fa-chevron-down"
                        onClick={openMobileSubMenu2}
                      ></i>
                    </Link>
                    <ul
                      className={
                        mobileSubMenu2 ? "submenu submenuShow" : "submenu"
                      }
                    >
                      <li>
                        <Link to="/instructor-dashboard">Dashboard</Link>
                      </li>
                      <li className="has-submenu">
                        <Link to="/instructor-list">
                          Instructor
                          <i
                            className="fas fa-chevron-right listMob"
                            onClick={openMobileSubMenu22}
                          ></i>
                        </Link>
                        <ul
                          className={
                            mobileSubMenu22 ? "submenu submenuShow" : "submenu"
                          }
                        >
                          <li>
                            <Link to="/instructor-list">List</Link>
                          </li>
                          <li>
                            <Link to="/instructor-grid">Grid</Link>
                          </li>
                        </ul>
                      </li>
                      <li>
                        <Link to="/instructor-course">My Course</Link>
                      </li>
                      <li>
                        <Link to="/instructor-reviews">Reviews</Link>
                      </li>
                      <li>
                        <Link to="/instructor-earnings">Earnings</Link>
                      </li>
                      <li>
                        <Link to="/instructor-orders">Orders</Link>
                      </li>
                      <li>
                        <Link to="/instructor-payouts">Payouts</Link>
                      </li>
                      <li>
                        <Link to="/instructor-tickets">Support Ticket</Link>
                      </li>
                      <li>
                        <Link to="/instructor-edit-profile">
                          Instructor Profile
                        </Link>
                      </li>
                      <li>
                        <Link to="/instructor-security">Security</Link>
                      </li>
                      <li>
                        <Link to="/instructor-social-profile">
                          Social Profiles
                        </Link>
                      </li>
                      <li>
                        <Link to="/instructor-notifications">
                          Notifications
                        </Link>
                      </li>
                      <li>
                        <Link to="/instructor-profile-privacy">
                          Profile Privacy
                        </Link>
                      </li>
                      <li>
                        <Link to="/instructor-delete-profile">
                          Delete Profile
                        </Link>
                      </li>
                      <li>
                        <Link to="/instructor-linked-account">
                          Linked Accounts
                        </Link>
                      </li>
                    </ul>
                  </li>
                  <li className="has-submenu">
                    <Link to="/students-list">
                      Student{" "}
                      <i
                        className="fas fa-chevron-down"
                        onClick={openMobileSubMenu3}
                      ></i>
                    </Link>
                    <ul
                      className={
                        mobileSubMenu3
                          ? "submenu first-submenu submenuShow"
                          : "submenu first-submenu"
                      }
                    >
                      <li className="has-submenu ">
                        <Link to="/students-list">
                          Student
                          <i
                            className="fas fa-chevron-right listMob"
                            onClick={openMobileSubMenu32}
                          ></i>
                        </Link>
                        <ul
                          className={
                            mobileSubMenu32 ? "submenu submenuShow" : "submenu"
                          }
                        >
                          <li>
                            <Link to="/students-list">List</Link>
                          </li>
                          <li>
                            <Link to="/students-grid">Grid</Link>
                          </li>
                        </ul>
                      </li>
                      <li>
                        <Link to="/setting-edit-profile">Student Profile</Link>
                      </li>
                      <li>
                        <Link to="/setting-student-security">Security</Link>
                      </li>
                      <li>
                        <Link to="/setting-student-social-profile">
                          Social profile
                        </Link>
                      </li>
                      <li>
                        <Link to="/setting-student-notification">
                          Notification
                        </Link>
                      </li>
                      <li>
                        <Link to="/setting-student-privacy">
                          Profile Privacy
                        </Link>
                      </li>
                      <li>
                        <Link to="/setting-student-accounts">
                          Link Accounts
                        </Link>
                      </li>
                      <li>
                        <Link to="/setting-student-referral">Referal</Link>
                      </li>
                      <li>
                        <Link to="/setting-student-subscription">
                          Subscription
                        </Link>
                      </li>
                      <li>
                        <Link to="/setting-student-billing">Billing</Link>
                      </li>
                      <li>
                        <Link to="/setting-student-payment">Payment</Link>
                      </li>
                      <li>
                        <Link to="/setting-student-invoice">Invoice</Link>
                      </li>
                      <li>
                        <Link to="/setting-support-tickets">
                          Support Tickets
                        </Link>
                      </li>
                    </ul>
                  </li>
                  <li className="has-submenu">
                    <Link to="">
                      Pages{" "}
                      <i
                        className="fas fa-chevron-down"
                        onClick={openMobileSubMenu4}
                      ></i>
                    </Link>
                    <ul
                      className={
                        mobileSubMenu4 ? "submenu submenuShow" : "submenu"
                      }
                    >
                      <li>
                        <Link to="/page-notification">Notification</Link>
                      </li>
                      <li>
                        <Link to="/pricing-plan">Pricing Plan</Link>
                      </li>
                      <li>
                        <Link to="/wishlist">Wishlist</Link>
                      </li>
                      <li className="has-submenu">
                        <Link to="/course-list">
                          Course
                          <i
                            className="fas fa-chevron-right listMob"
                            onClick={openMobileSubMenu42}
                          ></i>
                        </Link>
                        <ul
                          className={
                            mobileSubMenu42 ? "submenu submenuShow" : "submenu"
                          }
                        >
                          <li>
                            <Link to="/add-course">Add Course</Link>
                          </li>
                          <li>
                            <Link to="/course-list">Course List</Link>
                          </li>
                          <li>
                            <Link to="/course-grid">Course Grid</Link>
                          </li>
                          <li>
                            <Link to="/course-details">Course Details</Link>
                          </li>
                        </ul>
                      </li>
                      <li className="has-submenu">
                        <Link to="/come-soon">
                          Error
                          <i
                            className="fas fa-chevron-right listMob"
                            onClick={openMobileSubMenu43}
                          ></i>
                        </Link>
                        <ul
                          className={
                            mobileSubMenu43 ? "submenu submenuShow" : "submenu"
                          }
                        >
                          <li>
                            <Link to="/come-soon">Coming soon</Link>
                          </li>
                          <li>
                            <Link to="/error-404">404</Link>
                          </li>
                          <li>
                            <Link to="/error-500">500</Link>
                          </li>
                          <li>
                            <Link to="under-construction">
                              Under Construction
                            </Link>
                          </li>
                        </ul>
                      </li>
                      <li>
                        <Link to="/faq">FAQ</Link>
                      </li>
                      <li>
                        <Link to="/support">Support</Link>
                      </li>
                      <li>
                        <Link to="/job-category">Category</Link>
                      </li>
                      <li>
                        <Link to="/cart">Cart</Link>
                      </li>
                      <li>
                        <Link to="/checkout">Checkout</Link>
                      </li>
                      <li>
                        <Link to="/login">Login</Link>
                      </li>
                      <li>
                        <Link to="/register">Register</Link>
                      </li>
                      <li>
                        <Link to="/forgot-password">Forgot Password</Link>
                      </li>
                    </ul>
                  </li>
                  <li className="has-submenu">
                    <Link to="">
                      Blog{" "}
                      <i
                        className="fas fa-chevron-down"
                        onClick={openMobileSubMenu5}
                      ></i>
                    </Link>
                    <ul
                      className={
                        mobileSubMenu5 ? "submenu submenuShow" : "submenu"
                      }
                    >
                      <li>
                        <Link to="/blog-list">Blog List</Link>
                      </li>
                      <li>
                        <Link to="/blog-grid">Blog Grid</Link>
                      </li>
                      <li>
                        <Link to="/blog-masonry">Blog Masonry</Link>
                      </li>
                      <li>
                        <Link to="/blog-modern">Blog Modern</Link>
                      </li>
                      <li>
                        <Link to="/blog-details">Blog Details</Link>
                      </li>
                    </ul>
                  </li>
                </ul>
              </div>
              <ul className="nav header-navbar-rht header-navbar-five">
                <li className="nav-item">
                  <Link className="login-five" to="/login">
                    Login
                  </Link>
                </li>
                <li className="nav-item">
                  <Link className="signup-five" to="/register">
                    Signup
                  </Link>
                </li>
              </ul>
            </div>
          </nav>
        </div>
      </header>
    </>
  );
};
