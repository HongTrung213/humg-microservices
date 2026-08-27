// import React from "react";
// import { Route, Routes } from "react-router-dom";
// import BlogDetails from "./components/blog/blogDetails";
// import BlogGrid from "./components/blog/blogGrid";
// import BlogList from "./components/blog/bloglist";
// import BlogMasonry from "./components/blog/blogMasonry";
// import BlogModern from "./components/blog/blogModern";
// import Cart from "./components/pages/cart";
// import JobCategory from "./components/pages/category";
// import Checkout from "./components/pages/checkout";
// import AddCourse from "./components/pages/course/addCourse";
// import CourseDetails from "./components/pages/course/courseDetails";
// import CourseDetails1 from "./components/pages/course/courseDetails1";
// import CourseDetails2 from "./components/pages/course/courseDetails2";
// import CourseGrid from "./components/pages/course/courseGrid";
// import CourseLesson from "./components/pages/course/courseLesson";
// import CourseList from "./components/pages/course/courseList";
// import ComingSoon from "./components/pages/error/comingSoon";
// import Error404 from "./components/pages/error/error404";
// import Error500 from "./components/pages/error/error500";
// import UnderConstruction from "./components/pages/error/underConstruction";
// import Faq from "./components/pages/faq";
// import ForgotPassword from "./components/pages/forgotPassword";
// import Login from "./components/pages/login";
// import Notification from "./components/pages/notification";
// import PrivacyPolicy from "./components/pages/policy";
// import PricingPlan from "./components/pages/pricingPlan";
// import PricingPlan2 from "./components/pages/pricingPlan/pricingPlan2";
// import Register from "./components/pages/register";
// import RegisterOne from "./components/pages/register/register1";
// import RegisterTwo from "./components/pages/register/register2";
// import RegisterThree from "./components/pages/register/register3";
// import RegisterFour from "./components/pages/register/register4";
// import RegisterFive from "./components/pages/register/register5";
// import Support from "./components/pages/support";
// import TermsCondition from "./components/pages/termsCondition";
// import Wishlist from "./components/pages/wishlist";

// //harish
// import {Home} from "./components/home";
// import { Home2 } from "./components/home2";
// import { Home3 } from "./components/home3";
// import { Home4 } from "./components/home4";
// import { Dashboard } from "./components/instructor/dashboard";
// import { InstructorList } from "./components/instructor/list";
// import InstructorGrid from "./components/instructor/grid";
// import InstructorCourse from "./components/instructor/course";
// import InstructorReviews from "./components/instructor/reviews";
// import InstructorEarnings from "./components/instructor/earnings";
// import InstructorOrders from "./components/instructor/orders";
// import InstructorPayouts from "./components/instructor/payouts";
// import InstructorEditProfile from "./components/instructor/editProfile";
// import InstructorSecurity from "./components/instructor/security";
// import InstructorSocialProfile from "./components/instructor/socialProfiles";
// import InstructorNotification from "./components/instructor/notification";
// import InstructorTickets from "./components/instructor/tickets";
// import InstructorChat from "./components/instructor/chat";
// import InstructorDeleteProfile from "./components/instructor/deleteProfile";
// import InstructorEdit from "./components/instructor/edit";
// import InstructorGrid2 from "./components/instructor/grid2";
// import InstructorLinkedAccount from "./components/instructor/linkedAccount";
// import InstructorNewTickets from "./components/instructor/newTickets";
// import InstructorProfile from "./components/instructor/profile";
// import InstructorProfilePrivacy from "./components/instructor/profilePrivacy";
// import InstructorStudentGrid from "./components/instructor/studentGrid";
// import InstructorStudentList from "./components/instructor/studentList";
// import StudentEditProfile from "./components/student/editProfile";
// import StudentAccounts from "./components/student/accounts";
// import StudentBilling from "./components/student/billing";
// import StudentDeleteProfile from "./components/student/deleteProfile";
// import StudentInvoice from "./components/student/invoice";
// import StudentNotification from "./components/student/notification";
// import StudentPayment from "./components/student/payment";
// import StudentPrivacy from "./components/student/privacy";
// import StudentReferral from "./components/student/referral";
// import StudentSecurity from "./components/student/security";
// import StudentSocialProfile from "./components/student/socialProfile";
// import StudentSubscription from "./components/student/subscription";
// import StudentNewTickets from "./components/student/newTickets";
// import StudentTickets from "./components/student/tickets";
// import StudentViewTickets from "./components/student/viewTickets";
// import StudentProfile from "./components/student/profile";
// import StudentsGrid from "./components/student/grid";
// import StudentsGrid2 from "./components/student/grid2";
// import StudentsList from "./components/student/list";
// import InstructorDepositDashboard from "./components/instructor/deposit";
// import StudentDepositDashboard from "./components/student/depositDashboard";
// import DashboardInstructor from "./components/instructor/dashboardInstructor";
// import WithdrawalInstructor from "./components/instructor/withdrawalInstructor";
// import DepositInstructor from "./components/instructor/depositInstructor";
// import TransactionInstructor from "./components/instructor/transactionInstructor";
// import DepositStudent from "./components/student/depositStudent";
// import TransactionStudent from "./components/student/transactionStudent";

// import CourseMessage from "./components/student/courseMessage";
// import CourseWishlist from "./components/student/courseWishlist";
// import CourseStudent from "./components/student/courseStudent";
// import PurchaseHistory from "./components/student/purchaseHistory";
// import ViewInvoice from "./components/student/invoice/viewInvoice";
// import NewPassword from "./components/pages/newPassword";
// export const App = () => {
//   return (
//     <Routes>
//       <Route path="/" element={<Home />} />
//       <Route path="/home2" element={<Home2 />} />
//       <Route path="/home3" element={<Home3 />} />
//       <Route path="/home4" element={<Home4 />} />
//       <Route path="/instructor-dashboard" element={<Dashboard />} />
//       <Route path="/instructor-list" element={<InstructorList />} />
//       <Route path="/instructor-grid" element={<InstructorGrid />} />
//       <Route path="" element={<InstructorCourse />} />

//       {/* Blog */}
//       <Route path="/blog-list" element={<BlogList />} />
//       <Route path="/blog-grid" element={<BlogGrid />} />
//       <Route path="/blog-masonry" element={<BlogMasonry />} />
//       <Route path="/blog-modern" element={<BlogModern />} />
//       <Route path="/blog-details" element={<BlogDetails />} />
       
//        {/* Pages */}
//        <Route path="/page-notification" element={<Notification />} />
//        <Route path="/pricing-plan" element={<PricingPlan />} />
//        <Route path="/pricing-plan2" element={<PricingPlan2 />} />
//        <Route path="/wishlist" element={<Wishlist />} />
//        <Route path="/add-course" element={<AddCourse />} />
//        <Route path="/course-list" element={<CourseList />} />
//        {/* <Route path="/course-message" element={<CourseMessage />} /> */}
//        <Route path="/course-grid" element={<CourseGrid />} />
//        <Route path="/course-details" element={<CourseDetails />} />
//        <Route path="/course-details1" element={<CourseDetails1 />} />
//        <Route path="/course-details2" element={<CourseDetails2 />} />
//        <Route path="/come-soon" element={<ComingSoon/>} />
//        <Route path="/error-404" element={<Error404/>} />
//        <Route path="/error-500" element={<Error500/>} />
//        <Route path="/under-construction" element={<UnderConstruction/>} />
//        <Route path="/faq" element={<Faq/>} />
//        <Route path="/support" element={<Support/>} />
//        <Route path="/job-category" element={<JobCategory/>} />
//        <Route path="/cart" element={<Cart/>} />
//        <Route path="/checkout" element={<Checkout/>} />
//        <Route path="/login" element={<Login/>} />
//        <Route path="/new-password" element={<NewPassword/>} />
//        <Route path="/register" element={<Register/>} />
//        <Route path="/register1" element={<RegisterOne/>} />
//        <Route path="/register2" element={<RegisterTwo/>} />
//        <Route path="/register3" element={<RegisterThree/>} />
//        <Route path="/register4" element={<RegisterFour/>} />
//        <Route path="/register5" element={<RegisterFive/>} />
//        <Route path="/forgot-password" element={<ForgotPassword/>} />
//        <Route path="/term-condition" element={<TermsCondition/>} />
//        <Route path="/privacy-policy" element={<PrivacyPolicy/>} />

// {/* Instructor Routes */}
// <Route path="/instructor-dashboard" element={<Dashboard />} />
//       <Route path="/instructor-list" element={<InstructorList />} />
//       <Route path="/instructor-grid" element={<InstructorGrid />} />
//       <Route path="/instructor-course" element={<InstructorCourse />} />
//       <Route path="/instructor-reviews" element={<InstructorReviews />} />
//       <Route path="/instructor-earnings" element={<InstructorEarnings />} />
//       <Route path="/instructor-orders" element={<InstructorOrders />} />
//       <Route path="/instructor-payouts" element={<InstructorPayouts />} />
//       <Route path="/instructor-tickets" element={<InstructorTickets />} />
//       <Route path="/instructor-profile" element={<InstructorProfile />} />
//       <Route
//         path="/instructor-edit-profile"
//         element={<InstructorEditProfile />}
//       />
//       <Route path="/instructor-security" element={<InstructorSecurity />} />
//       <Route
//         path="/instructor-social-profile"
//         element={<InstructorSocialProfile />}
//       />
//       <Route
//         path="/instructor-notifications"
//         element={<InstructorNotification />}
//       />
//       <Route path="/instructor-chat" element={<InstructorChat />} />
//       <Route
//         path="/instructor-delete-profile"
//         element={<InstructorDeleteProfile />}
//       />
//       <Route path="/instructor-edit" element={<InstructorEdit />} />
//       <Route path="/instructor-grid-2" element={<InstructorGrid2 />} />
//       <Route
//         path="/instructor-linked-account"
//         element={<InstructorLinkedAccount />}
//       />
//       <Route
//         path="/instructor-new-tickets"
//         element={<InstructorNewTickets />}
//       />
//       <Route
//         path="/instructor-profile-privacy"
//         element={<InstructorProfilePrivacy />}
//       />
//       <Route
//         path="/instructor-student-grid"
//         element={<InstructorStudentGrid />}
//       />
//       <Route
//         path="/instructor-student-list"
//         element={<InstructorStudentList />}
//       />
//       <Route
//         path="/deposit-instructor-dashboard"
//         element={<InstructorDepositDashboard />}
//       />
//       <Route path="/dashboard-instructor" element={<DashboardInstructor />} />
//       <Route path="/withdrawal-instructor" element={<WithdrawalInstructor />} />
//       <Route path="/deposit-instructor" element={<DepositInstructor />} />
//       <Route
//         path="/transactions-instructor"
//         element={<TransactionInstructor />}
//       />

//       {/*Student Routes  */}
//       <Route path="/setting-edit-profile" element={<StudentEditProfile />} />
//       <Route path="/setting-student-accounts" element={<StudentAccounts />} />
//       <Route path="/setting-student-billing" element={<StudentBilling />} />
//       <Route
//         path="/setting-student-delete-profile"
//         element={<StudentDeleteProfile />}
//       />
//       <Route path="/setting-student-invoice" element={<StudentInvoice />} />
//       <Route path="/view-invoice" element={<ViewInvoice />} />
//       <Route
//         path="/setting-student-notification"
//         element={<StudentNotification />}
//       />
//       <Route path="/setting-student-payment" element={<StudentPayment />} />
//       <Route path="/setting-student-privacy" element={<StudentPrivacy />} />
//       <Route path="/setting-student-referral" element={<StudentReferral />} />
//       <Route path="/setting-student-security" element={<StudentSecurity />} />
//       <Route
//         path="/setting-student-social-profile"
//         element={<StudentSocialProfile />}
//       />
//       <Route
//         path="/setting-student-subscription"
//         element={<StudentSubscription />}
//       />
//       <Route
//         path="/setting-support-new-tickets"
//         element={<StudentNewTickets />}
//       />
//       <Route path="/setting-support-tickets" element={<StudentTickets />} />
//       <Route
//         path="/setting-support-view-tickets"
//         element={<StudentViewTickets />}
//       />
//       <Route
//         path="/deposit-student-dashboard"
//         element={<StudentDepositDashboard />}
//       />
//       <Route path="/students-profile" element={<StudentProfile />} />
//       <Route path="/students-grid" element={<StudentsGrid />} />
//       <Route path="/students-grid2" element={<StudentsGrid2 />} />
//       <Route path="/students-list" element={<StudentsList />} />
//       <Route path="/course-student" element={<CourseStudent />} />
//       <Route path="/course-wishlist" element={<CourseWishlist />} />
//       <Route path="/course-message" element={<CourseMessage />} />
//       <Route path="/purchase-history" element={<PurchaseHistory />} />
//       <Route path="/deposit-student" element={<DepositStudent />} />
//       <Route path="/transactions-student" element={<TransactionStudent />} />
//     </Routes>
//   );
// };
