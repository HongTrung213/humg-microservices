import React from "react";
import { InstructorHeader } from "../../instructor/header";
import Footer from "../../footer";
import { Link } from "react-router-dom";
import {
  Course10,
  Course11,
  Course12,
  Course13,
  Course14,
  Course15,
  Icon1,
  Icon2,
  Icon25,
  Icon26,
  Icon27,
  InstructorBgBanner,
  ProfileAvatar,
} from "../../imagepath";

export default function DashboardInstructor() {
  return (
    <div className="main-wrapper">
      <InstructorHeader />

      <div
        className="page-banner instructor-bg-blk"
        style={{ backgroundImage: "url(" + InstructorBgBanner + ")" }}
      >
        <div className="container">
          <div className="row align-items-center">
            <div className="col-lg-6 col-md-12">
              <div className="instructor-profile d-flex align-items-center">
                <div className="instructor-profile-pic">
                  <Link to="/instructor-profile">
                    <img src={ProfileAvatar} alt="" className="img-fluid" />
                  </Link>
                </div>
                <div className="instructor-profile-content">
                  <h4>
                    <Link to="/instructor-profile">
                      Jenny Wilson <span>Beginner</span>
                    </Link>
                  </h4>
                  <p>Instructor</p>
                </div>
              </div>
            </div>
            <div className="col-lg-6 col-md-12">
              <div className="instructor-profile-menu">
                <ul className="nav">
                  <li>
                    <div className="d-flex align-items-center">
                      <div className="instructor-profile-menu-img">
                        <img src={Icon25} alt="" />
                      </div>
                      <div className="instructor-profile-menu-content">
                        <h4>32</h4>
                        <p>Courses</p>
                      </div>
                    </div>
                  </li>
                  <li>
                    <div className="d-flex align-items-center">
                      <div className="instructor-profile-menu-img">
                        <img src={Icon26} alt="" />
                      </div>
                      <div className="instructor-profile-menu-content">
                        <h4>11,604</h4>
                        <p>Total Students</p>
                      </div>
                    </div>
                  </li>
                  <li>
                    <div className="d-flex align-items-center">
                      <div className="instructor-profile-menu-img">
                        <img src={Icon27} alt="" />
                      </div>
                      <div className="instructor-profile-menu-content">
                        <h4>12,230</h4>
                        <p>Reviews</p>
                      </div>
                    </div>
                  </li>
                </ul>
              </div>
            </div>
          </div>
          <div className="row">
            <div className="col-md-12">
              <div className="instructor-profile-text">
                <p>
                  I am an Innovation designer focussing on UX/UI based in
                  Berlin. As a creative resident at Figma explored the city of
                  the future and how new technologies like AI, voice control,
                  and augmented reality will change our interfaces.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <section className="page-content course-sec">
        <div className="container">
          <div className="row">
            <div className="col-lg-12">
              <div className="card instructor-card">
                <div className="card-header">
                  <h4>My Courses</h4>
                  <Link
                    to="/add-course"
                    className="btn btn-dark btn-dark-1"
                  >
                    Create New Course
                  </Link>
                </div>
                <div className="card-body">
                  <div className="instructor-grid">
                    <div className="product-img">
                      <Link to="course-details">
                        <img src={Course10} className="img-fluid" alt="" />
                      </Link>
                    </div>
                    <div className="instructor-product-content">
                      <div className="head-course-title">
                        <h3 className="title">
                          <Link to="course-details">
                            Information About UI/UX Design Degree
                          </Link>
                        </h3>
                      </div>
                      <div className="course-info d-flex align-items-center border-bottom-0 pb-0">
                        <div className="rating-img d-flex align-items-center">
                          <img src={Icon1} alt="" />
                          <p>12+ Lesson</p>
                        </div>
                        <div className="course-view d-flex align-items-center">
                          <img src={Icon2} alt="" />
                          <p>9hr 30min</p>
                        </div>
                      </div>
                      <div className="rating mb-0">
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star"></i>
                        <span className="d-inline-block average-rating">
                          <span>4.0</span> (15)
                        </span>
                      </div>
                    </div>
                  </div>
                  <div className="instructor-grid">
                    <div className="product-img">
                      <Link to="course-details">
                        <img src={Course11} className="img-fluid" alt="" />
                      </Link>
                    </div>
                    <div className="instructor-product-content">
                      <div className="head-course-title">
                        <h3 className="title">
                          <Link to="course-details">
                            Wordpress for Beginners - Master Wordpress Quickly
                          </Link>
                        </h3>
                      </div>
                      <div className="course-info d-flex align-items-center border-bottom-0 pb-0">
                        <div className="rating-img d-flex align-items-center">
                          <img src={Icon1} alt="" />
                          <p>10+ Lesson</p>
                        </div>
                        <div className="course-view d-flex align-items-center">
                          <img src={Icon2} alt="" />
                          <p>7hr 20min</p>
                        </div>
                      </div>
                      <div className="rating mb-0">
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star"></i>
                        <span className="d-inline-block average-rating">
                          <span>4.2</span> (20)
                        </span>
                      </div>
                    </div>
                  </div>
                  <div className="instructor-grid">
                    <div className="product-img">
                      <Link to="course-details">
                        <img src={Course12} className="img-fluid" alt="" />
                      </Link>
                    </div>
                    <div className="instructor-product-content">
                      <div className="head-course-title">
                        <h3 className="title">
                          <Link to="course-details">
                            Sketch from A to Z (2022): Become an app designer
                          </Link>
                        </h3>
                      </div>
                      <div className="course-info d-flex align-items-center border-bottom-0 pb-0">
                        <div className="rating-img d-flex align-items-center">
                          <img src={Icon1} alt="" />
                          <p>05+ Lesson</p>
                        </div>
                        <div className="course-view d-flex align-items-center">
                          <img src={Icon2} alt="" />
                          <p>8hr 00min</p>
                        </div>
                      </div>
                      <div className="rating mb-0">
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star"></i>
                        <span className="d-inline-block average-rating">
                          <span>4.0</span> (10)
                        </span>
                      </div>
                    </div>
                  </div>
                  <div className="instructor-grid">
                    <div className="product-img">
                      <Link to="course-details">
                        <img src={Course13} className="img-fluid" alt="" />
                      </Link>
                    </div>
                    <div className="instructor-product-content">
                      <div className="head-course-title">
                        <h3 className="title">
                          <Link to="course-details">
                            Learn Angular Fundamentals From beginning to advance
                            lavel
                          </Link>
                        </h3>
                      </div>
                      <div className="course-info d-flex align-items-center border-bottom-0 pb-0">
                        <div className="rating-img d-flex align-items-center">
                          <img src={Icon1} alt="" />
                          <p>30+ Lesson</p>
                        </div>
                        <div className="course-view d-flex align-items-center">
                          <img src={Icon2} alt="" />
                          <p>10hr 30min</p>
                        </div>
                      </div>
                      <div className="rating mb-0">
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star"></i>
                        <span className="d-inline-block average-rating">
                          <span>4.3</span> (25)
                        </span>
                      </div>
                    </div>
                  </div>
                  <div className="instructor-grid">
                    <div className="product-img">
                      <Link to="course-details">
                        <img src={Course14} className="img-fluid" alt="" />
                      </Link>
                    </div>
                    <div className="instructor-product-content">
                      <div className="head-course-title">
                        <h3 className="title">
                          <Link to="course-details">
                            Build Responsive Real World Websites with HTML5 and
                            CSS3
                          </Link>
                        </h3>
                      </div>
                      <div className="course-info d-flex align-items-center border-bottom-0 pb-0">
                        <div className="rating-img d-flex align-items-center">
                          <img src={Icon1} alt="" />
                          <p>20+ Lesson</p>
                        </div>
                        <div className="course-view d-flex align-items-center">
                          <img src={Icon2} alt="" />
                          <p>7hr 00min</p>
                        </div>
                      </div>
                      <div className="rating mb-0">
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star"></i>
                        <span className="d-inline-block average-rating">
                          <span>4.0</span> (15)
                        </span>
                      </div>
                    </div>
                  </div>
                  <div className="instructor-grid mb-0">
                    <div className="product-img">
                      <Link to="course-details">
                        <img src={Course15} className="img-fluid" alt="" />
                      </Link>
                    </div>
                    <div className="instructor-product-content">
                      <div className="head-course-title">
                        <h3 className="title">
                          <Link to="course-details">
                            C# Developers Double Your Coding Speed with Visual
                            Studio
                          </Link>
                        </h3>
                      </div>
                      <div className="course-info d-flex align-items-center border-bottom-0 pb-0">
                        <div className="rating-img d-flex align-items-center">
                          <img src={Icon1} alt="" />
                          <p>50+ Lesson</p>
                        </div>
                        <div className="course-view d-flex align-items-center">
                          <img src={Icon2} alt="" />
                          <p>10hr 30min</p>
                        </div>
                      </div>
                      <div className="rating mb-0">
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star filled"></i>
                        <i className="fas fa-star"></i>
                        <span className="d-inline-block average-rating">
                          <span>4.5</span> (30)
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <Footer />
    </div>
  );
}
