import React, { useState } from "react";
import { Link } from "react-router-dom";
import Footer from "../../footer";
import {
  User1,
  User2,
  User3,
  User4,
} from "../../imagepath";
import { InstructorHeader } from "../header";
import InstructorSidebar from "../sidebar";
import Select from "react-select";
import FeatherIcon from "feather-icons-react";


export default function InstructorReviews() {
  const [setReview] = useState(null);
  const [setRating] = useState(null);
  const [setSort] = useState(null);
  const options1 = [
    { label: "All", value: "All" },
    { label: "review 1", value: "1" },
    { label: "review 2", value: "2" },
    { label: "review 3", value: "3" },
  ];
  const options2 = [
    { label: "Rating", value: "rating" },
    { label: "5", value: "5" },
    { label: "4", value: "4" },
    { label: "3", value: "3" },
  ];
  const options3 = [
    { label: "Sort", value: "sort" },
    { label: "Sort 1", value: "1" },
    { label: "Sort 2", value: "2" },
    { label: "Sort 3", value: "3" },
  ];
  const style = {
    control: (baseStyles, state) => ({
      ...baseStyles,
      backgroundColor: "white",
      width: "100%",
      height: "40px",
      color: "black",
      minHeight: "40px",
      border: "1px solid #e9ecef",
      paddingLeft: "5px",
      // This line disable the blue border
      boxShadow: state.isFocused ? 0 : 0,
      borderRadius: state.isSelected ? "0" : "10px",
      fontSize: "14px",
      "&:hover": {
        cursor: "pointer",
      },
      outline: "none",
    }),
    menu: (base) => ({ ...base, marginTop: "0px" }),
    menuList: (base) => ({ ...base, padding: "0" }),
    option: (provided, state) => ({
      ...provided,
      backgroundColor: state.isSelected ? "#FFDEDA" : "white",
      color: "black",
      fontSize: "14px",
      "&:hover": {
        backgroundColor: "#FFDEDA",
        // #dddddd
      },
    }),
    indicatorSeparator: (base) => ({
      ...base,
      display: "none",
    }),
    dropdownIndicator: (base, state) => ({
      ...base,
      color: "black",
      transform: state.selectProps.menuIsOpen ? "rotate(-180deg)" : "rotate(0)",
      transition: "250ms",
    }),
  };
  return (
    <div className="main-wrapper">
      <InstructorHeader activeMenu={"Reviews"} />
      {/* Page Wrapper */}
      <div className="page-content">
        <div className="container">
          <div className="row">
            {/* Sidebar */}
            <InstructorSidebar activeMenu={"Reviews"} />
            {/* Sidebar */}

            {/* Instruction Dashboard */}
            <div className="col-xl-9 col-lg-8 col-md-12">
              <div className="row">
                <div className="col-md-12">
                  <div className="settings-widget">
                    <div className="settings-inner-blk p-0">
                      <div className="sell-course-head comman-space">
                        <h3>Reviews</h3>
                        <p>
                          You have full control to manage your own account
                          setting.
                        </p>
                      </div>
                      <div className="comman-space pb-0">
                        <div className="instruct-search-blk mb-0">
                          <div className="show-filter all-select-blk">
                            <form action="#">
                              <div className="row gx-2 align-items-center">
                                <div className="col-md-6 col-lg-3 col-item">
                                  <div className="form-group select-form mb-1">
                                    <Select
                                      className=" select"
                                      name="sellist1"
                                      options={options1}
                                      defaultValue={options1[0]}
                                      placeholder="All"
                                      onChange={setReview}
                                      styles={style}
                                    ></Select>
                                  </div>
                                </div>
                                <div className="col-md-6 col-lg-3 col-item">
                                  <div className="form-group select-form mb-1">
                                    <Select
                                      className=" select"
                                      name="sellist1"
                                      options={options2}
                                      defaultValue={options2[0]}
                                      placeholder="Rating"
                                      onChange={setRating}
                                      styles={style}
                                    ></Select>
                                  </div>
                                </div>
                                <div className="col-md-6 col-lg-3 col-item">
                                  <div className="form-group select-form mb-1">
                                    <Select
                                      className=" select"
                                      name="sellist1"
                                      options={options3}
                                      defaultValue={options3[0]}
                                      placeholder="Sort"
                                      onChange={setSort}
                                      styles={style}
                                    ></Select>
                                  </div>
                                </div>
                              </div>
                            </form>
                          </div>
                        </div>
                      </div>
                      <div className="comman-space bdr-bottom-line">
                        <div className="instruct-review-blk ">
                          <div className="review-item">
                            <div className="instructor-wrap border-0 m-0">
                              <div className="about-instructor">
                                <div className="abt-instructor-img">
                                  <Link to="/instructor-profile">
                                    <img
                                      src={User1}
                                      alt="img"
                                      className="img-fluid"
                                    />
                                  </Link>
                                </div>
                                <div className="instructor-detail">
                                  <h5>
                                    <Link to="/instructor-profile">
                                      Nicole Brown
                                    </Link>
                                  </h5>
                                  <p>UX/UI Designer</p>
                                </div>
                              </div>
                              <div className="rating">
                                <i className="fas fa-star filled"></i>
                                <i className="fas fa-star filled"></i>
                                <i className="fas fa-star filled"></i>
                                <i className="fas fa-star filled"></i>
                                <i className="fas fa-star"></i>
                              </div>
                            </div>
                            <p className="rev-info">
                              “ This is the second Photoshop course I have
                              completed with Cristian. Worth every penny and
                              recommend it highly. To get the most out of this
                              course, its best to to take the Beginner to
                              Advanced course first. The sound and video quality
                              is of a good standard. Thank you Cristian. “
                            </p>
                            <Link to="#;" className="btn btn-reply">
                              <FeatherIcon icon="corner-up-left"/>
                              Respond
                            </Link>
                          </div>
                        </div>
                      </div>
                      <div className="comman-space bdr-bottom-line">
                        <div className="instruct-review-blk ">
                          <div className="review-item">
                            <div className="instructor-wrap border-0 m-0">
                              <div className="about-instructor">
                                <div className="abt-instructor-img">
                                  <Link to="/instructor-profile">
                                    <img
                                      src={User2}
                                      alt="img"
                                      className="img-fluid"
                                    />
                                  </Link>
                                </div>
                                <div className="instructor-detail">
                                  <h5>
                                    <Link to="/instructor-profile">
                                      Jesse Stevens
                                    </Link>
                                  </h5>
                                  <p>UX/UI Designer</p>
                                </div>
                              </div>
                              <div className="rating">
                                <i className="fas fa-star filled"></i>
                                <i className="fas fa-star filled"></i>
                                <i className="fas fa-star filled"></i>
                                <i className="fas fa-star filled"></i>
                                <i className="fas fa-star"></i>
                              </div>
                            </div>
                            <p className="rev-info">
                              “ This is the second Photoshop course I have
                              completed with Cristian. Worth every penny and
                              recommend it highly. To get the most out of this
                              course, its best to to take the Beginner to
                              Advanced course first. The sound and video quality
                              is of a good standard. Thank you Cristian. “
                            </p>
                            <Link to="#;" className="btn btn-reply">
                              <FeatherIcon icon="corner-up-left"/>Respond
                            </Link>
                          </div>
                        </div>
                      </div>
                      <div className="comman-space bdr-bottom-line">
                        <div className="instruct-review-blk ">
                          <div className="review-item">
                            <div className="instructor-wrap border-0 m-0">
                              <div className="about-instructor">
                                <div className="abt-instructor-img">
                                  <Link to="/instructor-profile">
                                    <img
                                      src={User3}
                                      alt="img"
                                      className="img-fluid"
                                    />
                                  </Link>
                                </div>
                                <div className="instructor-detail">
                                  <h5>
                                    <Link to="/instructor-profile">
                                      John Smith
                                    </Link>
                                  </h5>
                                  <p>UX/UI Designer</p>
                                </div>
                              </div>
                              <div className="rating">
                                <i className="fas fa-star filled"></i>
                                <i className="fas fa-star filled"></i>
                                <i className="fas fa-star filled"></i>
                                <i className="fas fa-star filled"></i>
                                <i className="fas fa-star"></i>
                              </div>
                            </div>
                            <p className="rev-info">
                              “ This is the second Photoshop course I have
                              completed with Cristian. Worth every penny and
                              recommend it highly. To get the most out of this
                              course, its best to to take the Beginner to
                              Advanced course first. The sound and video quality
                              is of a good standard. Thank you Cristian. “
                            </p>
                            <Link to="#;" className="btn btn-reply">
                              <FeatherIcon icon="corner-up-left"/>Respond
                            </Link>
                          </div>
                        </div>
                      </div>
                      <div className="comman-space">
                        <div className="instruct-review-blk ">
                          <div className="review-item">
                            <div className="instructor-wrap border-0 m-0">
                              <div className="about-instructor">
                                <div className="abt-instructor-img">
                                  <Link to="/instructor-profile">
                                    <img
                                      src={User4}
                                      alt="img"
                                      className="img-fluid"
                                    />
                                  </Link>
                                </div>
                                <div className="instructor-detail">
                                  <h5>
                                    <Link to="/instructor-profile">
                                      Stella Johnson
                                    </Link>
                                  </h5>
                                  <p>UX/UI Designer</p>
                                </div>
                              </div>
                              <div className="rating">
                                <i className="fas fa-star filled"></i>
                                <i className="fas fa-star filled"></i>
                                <i className="fas fa-star filled"></i>
                                <i className="fas fa-star filled"></i>
                                <i className="fas fa-star"></i>
                              </div>
                            </div>
                            <p className="rev-info">
                              “ This is the second Photoshop course I have
                              completed with Cristian. Worth every penny and
                              recommend it highly. To get the most out of this
                              course, its best to to take the Beginner to
                              Advanced course first. The sound and video quality
                              is of a good standard. Thank you Cristian. “
                            </p>
                            <Link to="#;" className="btn btn-reply">
                              <FeatherIcon icon="corner-up-left"/>Respond
                            </Link>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            {/* Instructor Dashboard */}
          </div>
        </div>
      </div>
      {/* Page Wrapper */}
      <Footer />
    </div>
  );
}
