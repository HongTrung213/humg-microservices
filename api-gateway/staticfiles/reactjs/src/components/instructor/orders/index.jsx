import React from "react";
import { MoreVertical } from "react-feather";
import { Link } from "react-router-dom";

import FooterOrders from "../../footerOrders";
import { InstructorHeader } from "../header";
import InstructorSidebar from "../sidebar";

export default function InstructorOrders() {
  return (
    <div className="main-wrapper">
      <InstructorHeader activeMenu={"Orders"} />
      {/* Page Wrapper */}
      <div className="page-content">
        <div className="container">
          <div className="row">
            {/* Sidebar */}
            <InstructorSidebar activeMenu={"Orders"} />
            {/* Sidebar */}

            {/* Instructor Dashboard */}
            <div className="col-xl-9 col-lg-8 col-md-12">
              <div className="row">
                <div className="col-md-12">
                  <div className="settings-widget">
                    <div className="settings-inner-blk p-0">
                      <div className="sell-course-head comman-space">
                        <h3>Orders</h3>
                        <p>
                          Order Dashboard is a quick overview of all current
                          orders.
                        </p>
                      </div>
                      <div className="comman-space pb-0">
                        <div className="settings-tickets-blk course-instruct-blk table-responsive">
                          {/* Referred Users */}
                          <table className="table table-nowrap mb-0">
                            <thead>
                              <tr>
                                <th>COURSES</th>
                                <th>SALES</th>
                                <th>INVOICE</th>
                                <th>DATE</th>
                                <th>METHOD</th>
                                <th></th>
                              </tr>
                            </thead>
                            <tbody>
                              <tr>
                                <td className="instruct-orders-info">
                                  <p>
                                    <Link to="/course-details">
                                      Information About UI/UX Design Degree
                                    </Link>
                                  </p>
                                </td>
                                <td>34</td>
                                <td>#10021</td>
                                <td>10-05-20</td>
                                <td>Mastercard</td>
                                <td>
                                  <Link to="#;">
                                    <MoreVertical
                                      size={16}
                                      className="hoverRed"
                                    />
                                  </Link>
                                </td>
                              </tr>
                              <tr>
                                <td className="instruct-orders-info">
                                  <p>
                                    <Link to="/course-details">
                                      Wordpress for Beginners - Master Wordpress
                                      Quickly
                                    </Link>
                                  </p>
                                </td>
                                <td>30</td>
                                <td>#12421</td>
                                <td>10-05-20</td>
                                <td>Visa</td>
                                <td>
                                  <Link to="#;">
                                    <MoreVertical
                                      size={16}
                                      className="hoverRed"
                                    />
                                  </Link>
                                </td>
                              </tr>
                              <tr>
                                <td className="instruct-orders-info">
                                  <p>
                                    <Link to="/course-details">
                                      Sketch from A to Z (2022): Become an app
                                      designer
                                    </Link>
                                  </p>
                                </td>
                                <td>24</td>
                                <td>#11021</td>
                                <td>10-05-20</td>
                                <td>Mastercard</td>
                                <td>
                                  <Link to="#;">
                                    <MoreVertical
                                      size={16}
                                      className="hoverRed"
                                    />
                                  </Link>
                                </td>
                              </tr>
                              <tr>
                                <td className="instruct-orders-info">
                                  <p>
                                    <Link to="/course-details">
                                      Learn Angular Fundamentals From beginning
                                      to advance lavel
                                    </Link>
                                  </p>
                                </td>
                                <td>34</td>
                                <td>#10021</td>
                                <td>10-05-20</td>
                                <td>Mastercard</td>
                                <td>
                                  <Link to="#;">
                                    <MoreVertical
                                      size={16}
                                      className="hoverRed"
                                    />
                                  </Link>
                                </td>
                              </tr>
                              <tr>
                                <td className="instruct-orders-info">
                                  <p>
                                    <Link to="/course-details">
                                      Build Responsive Real World Websites with
                                      HTML5 and CSS3
                                    </Link>
                                  </p>
                                </td>
                                <td>34</td>
                                <td>#10021</td>
                                <td>10-05-20</td>
                                <td>Mastercard</td>
                                <td>
                                  <Link to="#;">
                                    <MoreVertical
                                      size={16}
                                      className="hoverRed"
                                    />
                                  </Link>
                                </td>
                              </tr>
                              <tr>
                                <td className="instruct-orders-info">
                                  <p>
                                    <Link to="/course-details">
                                      C# Developers Double Your Coding Speed
                                      with Visual Studio
                                    </Link>
                                  </p>
                                </td>
                                <td>34</td>
                                <td>#10021</td>
                                <td>10-05-20</td>
                                <td>Mastercard</td>
                                <td>
                                  <Link to="#;">
                                    <MoreVertical
                                      size={16}
                                      className="hoverRed"
                                    />
                                  </Link>
                                </td>
                              </tr>
                              <tr>
                                <td className="instruct-orders-info">
                                  <p>
                                    <Link to="/course-details">
                                      Learn JavaScript and Express to become a
                                      professional JavaScript
                                    </Link>
                                  </p>
                                </td>
                                <td>34</td>
                                <td>#10021</td>
                                <td>10-05-20</td>
                                <td>Mastercard</td>
                                <td>
                                  <Link to="#;">
                                    <MoreVertical
                                      size={16}
                                      className="hoverRed"
                                    />
                                  </Link>
                                </td>
                              </tr>
                              <tr>
                                <td className="instruct-orders-info">
                                  <p>
                                    <Link to="/course-details">
                                      Learn and Understand AngularJS to become a
                                      professional developer
                                    </Link>
                                  </p>
                                </td>
                                <td>34</td>
                                <td>#10021</td>
                                <td>10-05-20</td>
                                <td>Mastercard</td>
                                <td>
                                  <Link to="#;">
                                    <MoreVertical
                                      size={16}
                                      className="hoverRed"
                                    />
                                  </Link>
                                </td>
                              </tr>
                              <tr>
                                <td className="instruct-orders-info">
                                  <p>
                                    <Link to="/course-details">
                                      Responsive Web Design Essentials HTML5
                                      CSS3 and Bootstrap
                                    </Link>
                                  </p>
                                </td>
                                <td>34</td>
                                <td>#10021</td>
                                <td>10-05-20</td>
                                <td>Mastercard</td>
                                <td>
                                  <Link to="#;">
                                    <MoreVertical
                                      size={16}
                                      className="hoverRed"
                                    />
                                  </Link>
                                </td>
                              </tr>
                              <tr>
                                <td className="instruct-orders-info">
                                  <p>
                                    <Link to="/course-details">
                                      The Complete App Design Course - UX, UI
                                      and Design Thinking
                                    </Link>
                                  </p>
                                </td>
                                <td>34</td>
                                <td>#10021</td>
                                <td>10-05-20</td>
                                <td>Mastercard</td>
                                <td>
                                  <Link to="#;">
                                    <MoreVertical
                                      size={16}
                                      className="hoverRed"
                                    />
                                  </Link>
                                </td>
                              </tr>
                            </tbody>
                          </table>
                          {/* Referred Users */}
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
      <FooterOrders />
    </div>
  );
}
