<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\CustomAuthController;
/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/
Route::get('index', [CustomAuthController::class, 'dashboard']); 
Route::get('login', [CustomAuthController::class, 'index'])->name('login');
Route::post('custom-login', [CustomAuthController::class, 'customLogin'])->name('login.custom'); 
Route::get('register', [CustomAuthController::class, 'registration'])->name('register-user');
Route::post('custom-registration', [CustomAuthController::class, 'customRegistration'])->name('register.custom'); 
Route::get('signout', [CustomAuthController::class, 'signOut'])->name('signout');


    Route::get('/', function () {
    return view('index');
    })->name('index');
    Route::get('/index-two', function () {
    return view('index-two');
    })->name('index-two');
    Route::get('/index-three', function () {
    return view('index-three');
    })->name('index-three');
    Route::get('/index-four', function () {
    return view('index-four');
    })->name('index-four');
    Route::get('/add-course', function () {
    return view('add-course');
    })->name('add-course');
    Route::get('/blog-details', function () {
    return view('blog-details');
    })->name('blog-details');
    Route::get('/blog-grid', function () {
    return view('blog-grid');
    })->name('blog-grid');
    Route::get('/blog-list', function () {
    return view('blog-list');
    })->name('blog-list');
    Route::get('/blog-masonry', function () {
    return view('blog-masonry');
    })->name('blog-masonry');
    Route::get('/blog-modern', function () {
    return view('blog-modern');
    })->name('blog-modern');
    Route::get('/cart', function () {
    return view('cart');
    })->name('cart');
    Route::get('/checkout', function () {
    return view('checkout');
    })->name('checkout');
    Route::get('/come-soon', function () {
    return view('come-soon');
    })->name('come-soon');
    Route::get('/course-details', function () {
    return view('course-details');
    })->name('course-details');
    Route::get('/course-details1', function () {
    return view('course-details1');
    })->name('course-details1');
    Route::get('/course-details2', function () {
    return view('course-details2');
    })->name('course-details2');
    Route::get('/course-grid', function () {
    return view('course-grid');
    })->name('course-grid');
    Route::get('/course-lesson', function () {
    return view('course-lesson');
    })->name('course-lesson');
    Route::get('/course-list', function () {
    return view('course-list');
    })->name('course-list');
    Route::get('/course-message', function () {
    return view('course-message');
    })->name('course-message');
    Route::get('/course-student', function () {
    return view('course-student');
    })->name('course-student');
    Route::get('/course-wishlist', function () {
    return view('course-wishlist');
    })->name('course-wishlist');
    Route::get('/dashboard-instructor', function () {
    return view('dashboard-instructor');
    })->name('dashboard-instructor');
    Route::get('/deposit-instructor-dashboard', function () {
    return view('deposit-instructor-dashboard');
    })->name('deposit-instructor-dashboard');
    Route::get('/deposit-instructor', function () {
    return view('deposit-instructor');
    })->name('deposit-instructor');
    Route::get('/deposit-instructor', function () {
    return view('deposit-instructor');
    })->name('deposit-instructor');
    Route::get('/deposit-student-dashboard', function () {
    return view('deposit-student-dashboard');
    })->name('deposit-student-dashboard');
    Route::get('/deposit-student', function () {
    return view('deposit-student');
    })->name('deposit-student');
    Route::get('/error-404', function () {
    return view('error-404');
    })->name('error-404');
    Route::get('/error-500', function () {
    return view('error-500');
    })->name('error-500');
    Route::get('/faq', function () {
    return view('faq');
    })->name('faq');
    Route::get('/forgot-password', function () {
    return view('forgot-password');
    })->name('forgot-password');
    Route::get('/help-center', function () {
    return view('help-center');
    })->name('help-center');
    Route::get('/index', function () {
    return view('index');
    })->name('index');
    Route::get('/instructor-chat', function () {
    return view('instructor-chat');
    })->name('instructor-chat');
    Route::get('/instructor-course', function () {
    return view('instructor-course');
    })->name('instructor-course');
    Route::get('/instructor-dashboard', function () {
    return view('instructor-dashboard');
    })->name('instructor-dashboard');
    Route::get('/instructor-delete-profile', function () {
    return view('instructor-delete-profile');
    })->name('instructor-delete-profile');
    Route::get('/instructor-earnings', function () {
    return view('instructor-earnings');
    })->name('instructor-earnings');
    Route::get('/instructor-edit-profile', function () {
    return view('instructor-edit-profile');
    })->name('instructor-edit-profile');
    Route::get('/instructor-edit', function () {
    return view('instructor-edit');
    })->name('instructor-edit');
    Route::get('/instructor-grid-2', function () {
    return view('instructor-grid-2');
    })->name('instructor-grid-2');
    Route::get('/instructor-grid', function () {
    return view('instructor-grid');
    })->name('instructor-grid');
    Route::get('/instructor-linked-account', function () {
    return view('instructor-linked-account');
    })->name('instructor-linked-account');
    Route::get('/instructor-list', function () {
    return view('instructor-list');
    })->name('instructor-list');
    Route::get('/instructor-new-tickets', function () {
    return view('instructor-new-tickets');
    })->name('instructor-new-tickets');
    Route::get('/instructor-notification', function () {
    return view('instructor-notification');
    })->name('instructor-notification');
    Route::get('/instructor-orders', function () {
    return view('instructor-orders');
    })->name('instructor-orders');
    Route::get('/instructor-payouts', function () {
    return view('instructor-payouts');
    })->name('instructor-payouts');
    Route::get('/instructor-profile-privacy', function () {
    return view('instructor-profile-privacy');
    })->name('instructor-profile-privacy');
    Route::get('/instructor-profile', function () {
    return view('instructor-profile');
    })->name('instructor-profile');
    Route::get('/instructor-reviews', function () {
    return view('instructor-reviews');
    })->name('instructor-reviews');
    Route::get('/instructor-security', function () {
    return view('instructor-security');
    })->name('instructor-security');
    Route::get('/instructor-social-profiles', function () {
    return view('instructor-social-profiles');
    })->name('instructor-social-profiles');
    Route::get('/instructor-student-grid', function () {
    return view('instructor-student-grid');
    })->name('instructor-student-grid');
    Route::get('/instructor-student-list', function () {
    return view('instructor-student-list');
    })->name('instructor-student-list');
    Route::get('/instructor-tickets', function () {
    return view('instructor-tickets');
    })->name('instructor-tickets');
    Route::get('/job-category', function () {
    return view('job-category');
    })->name('job-category');
    Route::get('/login', function () {
    return view('login');
    })->name('login');
    Route::get('/new-password', function () {
    return view('new-password');
    })->name('new-password');
    Route::get('/notifications', function () {
    return view('notifications');
    })->name('notifications');
    Route::get('/pricing-plan-2', function () {
    return view('pricing-plan-2');
    })->name('pricing-plan-2');
    Route::get('/pricing-plan', function () {
    return view('pricing-plan');
    })->name('pricing-plan');
    Route::get('/privacy-policy', function () {
    return view('privacy-policy');
    })->name('privacy-policy');
    Route::get('/purchase-history', function () {
    return view('purchase-history');
    })->name('purchase-history');
    Route::get('/register-step-five', function () {
    return view('register-step-five');
    })->name('register-step-five');
    Route::get('/register-step-four', function () {
    return view('register-step-four');
    })->name('register-step-four');
    Route::get('/register-step-one', function () {
    return view('register-step-one');
    })->name('register-step-one');
    Route::get('/register-step-three', function () {
    return view('register-step-three');
    })->name('register-step-three');
    Route::get('/register-step-two', function () {
    return view('register-step-two');
    })->name('register-step-two');
    Route::get('/register', function () {
    return view('register');
    })->name('register');
    Route::get('/setting-edit-profile', function () {
    return view('setting-edit-profile');
    })->name('setting-edit-profile');
    Route::get('/setting-student-accounts', function () {
    return view('setting-student-accounts');
    })->name('setting-student-accounts');
    Route::get('/setting-student-billing', function () {
    return view('setting-student-billing');
    })->name('setting-student-billing');
    Route::get('/setting-student-delete-profile', function () {
    return view('setting-student-delete-profile');
    })->name('setting-student-delete-profile');
    Route::get('/setting-student-invoice', function () {
    return view('setting-student-invoice');
    })->name('setting-student-invoice');
    Route::get('/setting-student-notification', function () {
    return view('setting-student-notification');
    })->name('setting-student-notification');
    Route::get('/setting-student-payment', function () {
    return view('setting-student-payment');
    })->name('setting-student-payment');
    Route::get('/setting-student-privacy', function () {
    return view('setting-student-privacy');
    })->name('setting-student-privacy');
    Route::get('/setting-student-referral', function () {
    return view('setting-student-referral');
    })->name('setting-student-referral');
    Route::get('/setting-student-security', function () {
    return view('setting-student-security');
    })->name('setting-student-security');
    Route::get('/setting-student-social-profile', function () {
    return view('setting-student-social-profile');
    })->name('setting-student-social-profile');
    Route::get('/setting-student-subscription', function () {
    return view('setting-student-subscription');
    })->name('setting-student-subscription');
    Route::get('/setting-support-new-tickets', function () {
    return view('setting-support-new-tickets');
    })->name('setting-support-new-tickets');
    Route::get('/setting-support-view-tickets', function () {
    return view('setting-support-view-tickets');
    })->name('setting-support-view-tickets');
    Route::get('/student-profile', function () {
    return view('student-profile');
    })->name('student-profile');
    Route::get('/students-grid', function () {
    return view('students-grid');
    })->name('students-grid');
    Route::get('/students-grid2', function () {
    return view('students-grid2');
    })->name('students-grid2');
    Route::get('/students-list', function () {
    return view('students-list');
    })->name('students-list');
    Route::get('/support', function () {
    return view('support');
    })->name('support');
    Route::get('/term-condition', function () {
    return view('term-condition');
    })->name('term-condition');
    Route::get('/transactions-instructor', function () {
    return view('transactions-instructor');
    })->name('transactions-instructor');
    Route::get('/transactions-student', function () {
    return view('transactions-student');
    })->name('transactions-student');
    Route::get('/under-construction', function () {
    return view('under-construction');
    })->name('under-construction');
    Route::get('/verification-code', function () {
    return view('verification-code');
    })->name('verification-code');
    Route::get('/verification-code', function () {
    return view('verification-code');
    })->name('verification-code');
    Route::get('/view-invoice', function () {
    return view('view-invoice');
    })->name('view-invoice');
    Route::get('/wishlist', function () {
    return view('wishlist');
    })->name('wishlist');
    Route::get('/withdrawal-instructor', function () {
    return view('withdrawal-instructor');
    })->name('withdrawal-instructor');
    Route::get('/setting-support-tickets', function () {
    return view('setting-support-tickets');
    })->name('setting-support-tickets');