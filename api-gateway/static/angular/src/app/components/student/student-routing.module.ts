import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { StudentComponent } from './student.component';

const routes: Routes = [
  { path: '', component: StudentComponent, 
  children: [

    {
      path: 'setting-edit-profile',
      loadChildren: () =>
        import('./setting-edit-profile/setting-edit-profile.module').then(
          (m) => m.SettingEditProfileModule
        ),
    },
    {
      path: 'setting-student-accounts',
      loadChildren: () =>
        import('./setting-student-accounts/setting-student-accounts.module').then(
          (m) => m.SettingStudentAccountsModule
        ),
    },
    {
      path: 'setting-student-billing',
      loadChildren: () =>
        import('./setting-student-billing/setting-student-billing.module').then(
          (m) => m.SettingStudentBillingModule
        ),
    },
    {
      path: 'setting-student-invoice',
      loadChildren: () =>
        import('./setting-student-invoice/setting-student-invoice.module').then(
          (m) => m.SettingStudentInvoiceModule
        ),
    },
    {
      path: 'setting-student-notification',
      loadChildren: () =>
        import(
          './setting-student-notification/setting-student-notification.module'
        ).then((m) => m.SettingStudentNotificationModule),
    },
    {
      path: 'setting-student-payment',
      loadChildren: () =>
        import('./setting-student-payment/setting-student-payment.module').then(
          (m) => m.SettingStudentPaymentModule
        ),
    },
    {
      path: 'setting-student-privacy',
      loadChildren: () =>
        import('./setting-student-privacy/setting-student-privacy.module').then(
          (m) => m.SettingStudentPrivacyModule
        ),
    },
    {
      path: 'setting-student-referral',
      loadChildren: () =>
        import('./setting-student-referral/setting-student-referral.module').then(
          (m) => m.SettingStudentReferralModule
        ),
    },
    {
      path: 'setting-student-security',
      loadChildren: () =>
        import('./setting-student-security/setting-student-security.module').then(
          (m) => m.SettingStudentSecurityModule
        ),
    },
    {
      path: 'setting-student-social-profile',
      loadChildren: () =>
        import(
          './setting-student-social-profile/setting-student-social-profile.module'
        ).then((m) => m.SettingStudentSocialProfileModule),
    },
    {
      path: 'student-view',
      loadChildren: () =>
        import('./student-view/student-view.module').then(
          (m) => m.StudentViewModule
        ),
    },
    {
      path: 'setting-student-subscription',
      loadChildren: () =>
        import(
          './setting-student-subscription/setting-student-subscription.module'
        ).then((m) => m.SettingStudentSubscriptionModule),
    },
    {
      path: 'setting-support-tickets',
      loadChildren: () =>
        import('./setting-support-tickets/setting-support-tickets.module').then(
          (m) => m.SettingSupportTicketsModule
        ),
    },
    {
      path: 'student-profile',
      loadChildren: () =>
        import('./student-profile/student-profile.module').then(
          (m) => m.StudentProfileModule
        ),
    },
    {
      path: 'setting-student-delete-profile',
      loadChildren: () =>
        import(
          './setting-student-delete-profile/setting-student-delete-profile.module'
        ).then((m) => m.SettingStudentDeleteProfileModule),
    },
    {
      path: 'view-invoice',
      loadChildren: () =>
        import(
          './view-invoice/view-invoice.module'
        ).then((m) => m.ViewInvoiceModule),
    },
  ] 
},
  { path: 'deposit-student', loadChildren: () => import('./deposit-student/deposit-student.module').then(m => m.DepositStudentModule) },
  { path: 'course-student', loadChildren: () => import('./course-student/course-student.module').then(m => m.CourseStudentModule) },
  { path: 'transactions-student', loadChildren: () => import('./transactions-student/transactions-student.module').then(m => m.TransactionsStudentModule) },
  { path: 'setting-support-new-tickets', loadChildren: () => import('./setting-support-new-tickets/setting-support-new-tickets.module').then(m => m.SettingSupportNewTicketsModule) },
  { path: 'setting-support-view-tickets', loadChildren: () => import('./setting-support-view-tickets/setting-support-view-tickets.module').then(m => m.SettingSupportViewTicketsModule) },
  {
    path: 'deposit-student-dashboard',
    loadChildren: () =>
      import(
        './deposit-student-dashboard/deposit-student-dashboard.module'
      ).then((m) => m.DepositStudentDashboardModule),
  }
];
 
@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class StudentRoutingModule {}
