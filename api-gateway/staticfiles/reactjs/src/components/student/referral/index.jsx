import React, { useState } from "react";
import StudentHeader from "../../student/header";
import Footer from "../../footer";
import StudentSideBar from "../sidebar";
import {
  BankImage,
  ReferImage1,
  ReferImage10,
  ReferImage2,
  ReferImage3,
  ReferImage4,
  ReferImage5,
  ReferImage6,
  ReferImage7,
  ReferImage8,
  ReferImage9,
} from "../../imagepath";
import { Link } from "react-router-dom";
import { Clipboard } from "react-feather";
import Select from "react-select";

export default function StudentReferral() {
  const [setMonthValue] = useState(null);
  const [setYearValue] = useState(null);
  const months = [
    { label: "Month", value: "Month" },
    { label: "Daily", value: "Daily" },
    { label: "Week", value: "Week" },
  ];
  const year = [
    { label: "Oct 2020", value: "Oct 2020" },
    { label: "Jan 2020", value: "Jan 2020" },
    { label: "Feb 2020", value: "Feb 2020" },
    { label: "Mar 2020", value: "Mar 2020" },
  ];
  const style = {
    control: (baseStyles, state) => ({
      ...baseStyles,
      backgroundColor: "white",
      color: "black",
      width: "100%",
      height: "40px",
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
      color: "black",
      backgroundColor: state.isSelected ? "#FFDEDA" : "white",
      fontSize: "14px",
      "&:hover": {
        backgroundColor: "#FFDEDA",
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
      <StudentHeader activeMenu={"Referral"} />
      {/* Student Database */}
      <div className="page-content">
        <div className="container">
          <div className="row">
            {/* sidebar */}
            <StudentSideBar activeMenu={"Referral"} />
            {/* sidebar */}

            {/* Profile Details */}
            <div className="col-xl-9 col-md-8">
              <div className="settings-top-widget">
                <div className="row">
                  <div className="col-xl-3 col-lg-6">
                    <div className="card stat-info net-earn">
                      <div className="card-body">
                        <span>Net Earnings</span>
                        <h3>$ 63,240</h3>
                        <p>Earning this month</p>
                      </div>
                    </div>
                  </div>
                  <div className="col-xl-3 col-lg-6">
                    <div className="card stat-info bal">
                      <div className="card-body">
                        <span>Balance</span>
                        <h3>$ 8,530</h3>
                        <p>Earning this month</p>
                      </div>
                    </div>
                  </div>
                  <div className="col-xl-3 col-lg-6">
                    <div className="card stat-info avg">
                      <div className="card-body">
                        <span>Avg Deal Size</span>
                        <h3>$ 2,600</h3>
                        <p>Earning this month</p>
                      </div>
                    </div>
                  </div>
                  <div className="col-xl-3 col-lg-6">
                    <div className="card stat-info refer">
                      <div className="card-body">
                        <span>Referral Signups</span>
                        <h3>$ 783</h3>
                        <p>Earning this month</p>
                      </div>
                    </div>
                  </div>
                </div>
                <div className="row">
                  <div className="col-xl-6 d-flex">
                    <div className="card link-box flex-fill">
                      <div className="card-body">
                        <h3>Your Referral Link</h3>
                        <p>
                          Plan your blog post by choosing a topic, creating an
                          outline conduct research, and checking facts
                        </p>
                        <div className="form-group">
                          <input
                            type="text"
                            className="form-control"
                            defaultValue="https://dreamslmscourse.com/reffer/?refid=345re667877k9"
                          />
                        </div>
                        <Link to="#;">Copy link</Link>
                      </div>
                    </div>
                  </div>
                  <div className="col-xl-6 d-flex">
                    <div className="card withdraw-box flex-fill">
                      <div className="card-body">
                        <div className="widra-your-money d-flex align-items-end justify-content-between">
                          <div>
                            <h4>Withdraw Your Money to a Bank Account</h4>
                            <p>
                              Withdraw money securily to your bank account.
                              Commision is $25 per transaction under $50,000
                            </p>
                            <div className="hvr-sweep-to-right">
                              <Link to="#;">Withdraw Money</Link>
                            </div>
                          </div>
                          <div>
                            <img src={BankImage} alt="Withdraw money" />
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div className="settings-widget">
                <div className="settings-inner-blk p-0">
                  <div className="comman-space pb-0">
                    <div className="filter-grp user-referred table-select-blk d-flex align-items-center justify-content-between">
                      <h3>Referred Users</h3>
                      <div className="filter-blk d-flex">
                        <div className="form-group select-form mb-0">
                          <Select
                            className=" select"
                            id="datefilter"
                            name="datefilterby"
                            options={months}
                            defaultValue={months[0]}
                            placeholder="Month"
                            onChange={setMonthValue}
                            styles={style}
                          ></Select>
                        </div>
                        <div className="form-group select-form mb-0">
                          <Select
                            className=" select"
                            id="filterpicker"
                            name="filterpickerby"
                            options={year}
                            defaultValue={year[0]}
                            placeholder="Oct 2020"
                            onChange={setYearValue}
                            styles={style}
                          ></Select>
                        </div>
                      </div>
                    </div>
                    <div className="settings-referral-blk table-responsive">
                      {/* Referred Users */}
                      <table className="table table-nowrap mb-0">
                        <thead>
                          <tr>
                            <th>Referrals</th>
                            <th>Referred ID</th>
                            <th>URL</th>
                            <th>&nbsp;</th>
                            <th className="text-center">Visits</th>
                            <th className="text-end">Total earned</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <td>
                              <Link
                                to="/students-profile"
                                className="refer-avatar-blk d-flex align-items-center"
                              >
                                <img
                                  src={ReferImage1}
                                  className="rounded-circle me-2"
                                  alt="Referred User Info"
                                />
                                <p>Guy Hawkins</p>
                              </Link>
                            </td>
                            <td>09341</td>
                            <td>
                              <span className="text-wrap">
                                https://dreamslmscourse.com/reffer/?refid=345re667877k9
                              </span>
                            </td>
                            <td>
                              <Link to="#;" className="btn-style">
                                <Clipboard />
                              </Link>
                            </td>
                            <td className="text-center">10</td>
                            <td className="text-end">$45.00</td>
                          </tr>
                          <tr>
                            <td>
                              <Link
                                to="/students-profile"
                                className="refer-avatar-blk d-flex align-items-center"
                              >
                                <img
                                  src={ReferImage2}
                                  className="rounded-circle me-2"
                                  alt="Referred User Info"
                                />
                                <p>Dianna Smiley</p>
                              </Link>
                            </td>
                            <td>09342</td>
                            <td>
                              <span className="text-wrap">
                                https://dreamslmscourse.com/reffer/?refid=345re667877k9
                              </span>
                            </td>
                            <td>
                              <Link to="#;" className="btn-style">
                                <Clipboard />
                              </Link>
                            </td>
                            <td className="text-center">15</td>
                            <td className="text-end">$75.00</td>
                          </tr>
                          <tr>
                            <td>
                              <Link
                                to="/students-profile"
                                className="refer-avatar-blk d-flex align-items-center"
                              >
                                <img
                                  src={ReferImage3}
                                  className="rounded-circle me-2"
                                  alt="Referred User Info"
                                />
                                <p>Guy Hawkins</p>
                              </Link>
                            </td>
                            <td>09343</td>
                            <td>
                              <span className="text-wrap">
                                https://dreamslmscourse.com/reffer/?refid=345re667877k9
                              </span>
                            </td>
                            <td>
                              <Link to="#;" className="btn-style">
                                <Clipboard />
                              </Link>
                            </td>
                            <td className="text-center">20</td>
                            <td className="text-end">$100.00</td>
                          </tr>
                          <tr>
                            <td>
                              <Link
                                to="/students-profile"
                                className="refer-avatar-blk d-flex align-items-center"
                              >
                                <img
                                  src={ReferImage4}
                                  className="rounded-circle me-2"
                                  alt="Referred User Info"
                                />
                                <p>Jacob Jones</p>
                              </Link>
                            </td>
                            <td>09344</td>
                            <td>
                              <span className="text-wrap">
                                https://dreamslmscourse.com/reffer/?refid=345re667877k9
                              </span>
                            </td>
                            <td>
                              <Link to="#;" className="btn-style">
                                <Clipboard />
                              </Link>
                            </td>
                            <td className="text-center">1</td>
                            <td className="text-end">$44.00</td>
                          </tr>
                          <tr>
                            <td>
                              <Link
                                to="/students-profile"
                                className="refer-avatar-blk d-flex align-items-center"
                              >
                                <img
                                  src={ReferImage5}
                                  className="rounded-circle me-2"
                                  alt="Referred User Info"
                                />
                                <p>Kristin Watson</p>
                              </Link>
                            </td>
                            <td>09345</td>
                            <td>
                              <span className="text-wrap">
                                https://dreamslmscourse.com/reffer/?refid=345re667877k9
                              </span>
                            </td>
                            <td>
                              <Link to="#;" className="btn-style">
                                <Clipboard />
                              </Link>
                            </td>
                            <td className="text-center">5</td>
                            <td className="text-end">$25.00</td>
                          </tr>
                          <tr>
                            <td>
                              <Link
                                to="/students-profile"
                                className="refer-avatar-blk d-flex align-items-center"
                              >
                                <img
                                  src={ReferImage6}
                                  className="rounded-circle me-2"
                                  alt="Referred User Info"
                                />
                                <p>Rivao Luke</p>
                              </Link>
                            </td>
                            <td>09346</td>
                            <td>
                              <span className="text-wrap">
                                https://dreamslmscourse.com/reffer/?refid=345re667877k9
                              </span>
                            </td>
                            <td>
                              <Link to="#;" className="btn-style">
                                <Clipboard />
                              </Link>
                            </td>
                            <td className="text-center">500</td>
                            <td className="text-end">$160.00</td>
                          </tr>
                          <tr>
                            <td>
                              <Link
                                to="/students-profile"
                                className="refer-avatar-blk d-flex align-items-center"
                              >
                                <img
                                  src={ReferImage7}
                                  className="rounded-circle me-2"
                                  alt="Referred User Info"
                                />
                                <p>Nia Sikhone</p>
                              </Link>
                            </td>
                            <td>09347</td>
                            <td>
                              <span className="text-wrap">
                                https://dreamslmscourse.com/reffer/?refid=345re667877k9
                              </span>
                            </td>
                            <td>
                              <Link to="#;" className="btn-style">
                                <Clipboard />
                              </Link>
                            </td>
                            <td className="text-center">187</td>
                            <td className="text-end">$150.00</td>
                          </tr>
                          <tr>
                            <td>
                              <Link
                                to="/students-profile"
                                className="refer-avatar-blk d-flex align-items-center"
                              >
                                <img
                                  src={ReferImage8}
                                  className="rounded-circle me-2"
                                  alt="Referred User Info"
                                />
                                <p>Xiaon Merry</p>
                              </Link>
                            </td>
                            <td>09348</td>
                            <td>
                              <span className="text-wrap">
                                https://dreamslmscourse.com/reffer/?refid=345re667877k9
                              </span>
                            </td>
                            <td>
                              <Link to="#;" className="btn-style">
                                <Clipboard />
                              </Link>
                            </td>
                            <td className="text-center">10</td>
                            <td className="text-end">$45.00</td>
                          </tr>
                          <tr>
                            <td>
                              <Link
                                to="/students-profile"
                                className="refer-avatar-blk d-flex align-items-center"
                              >
                                <img
                                  src={ReferImage9}
                                  className="rounded-circle me-2"
                                  alt="Referred User Info"
                                />
                                <p>Guy Hawkins</p>
                              </Link>
                            </td>
                            <td>09349</td>
                            <td>
                              <span className="text-wrap">
                                https://dreamslmscourse.com/reffer/?refid=345re667877k9
                              </span>
                            </td>
                            <td>
                              <Link to="#;" className="btn-style">
                                <Clipboard />
                              </Link>
                            </td>
                            <td className="text-center">15</td>
                            <td className="text-end">$10.00</td>
                          </tr>
                          <tr>
                            <td>
                              <Link
                                to="/students-profile"
                                className="refer-avatar-blk d-flex align-items-center"
                              >
                                <img
                                  src={ReferImage10}
                                  className="rounded-circle me-2"
                                  alt="Referred User Info"
                                />
                                <p>Dianna Smiley</p>
                              </Link>
                            </td>
                            <td>09350</td>
                            <td>
                              <span className="text-wrap">
                                https://dreamslmscourse.com/reffer/?refid=345re667877k9
                              </span>
                            </td>
                            <td>
                              <Link to="#;" className="btn-style">
                                <Clipboard />
                              </Link>
                            </td>
                            <td className="text-center">98</td>
                            <td className="text-end">$10.00</td>
                          </tr>
                        </tbody>
                      </table>
                      {/* Referred Users */}
                    </div>
                  </div>
                </div>
              </div>
            </div>
            {/* Profile Details */}
          </div>
        </div>
      </div>
      {/* Student Database */}
      <Footer />
    </div>
  );
}
