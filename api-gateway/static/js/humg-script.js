// ===========================================================
// TRUNG TÂM NGOẠI NGỮ - TIN HỌC HUMG — script.js
// ===========================================================

document.addEventListener('DOMContentLoaded', function () {

  // ---------- Mobile nav toggle ----------
  const navToggle = document.getElementById('navToggle');
  const mobileNav = document.getElementById('mobileNav');
  const mainNavLinks = document.querySelectorAll('.main-nav a');

  if (navToggle && mobileNav) {
    // Clone main nav links into mobile nav
    mainNavLinks.forEach(function (link) {
      const clone = link.cloneNode(true);
      mobileNav.appendChild(clone);
    });

    navToggle.addEventListener('click', function () {
      const isOpen = mobileNav.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    // Close mobile nav after clicking a link
    mobileNav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        mobileNav.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // ---------- Advisory form submit ----------
  const form = document.getElementById('advisoryForm');
  const successBox = document.getElementById('formSuccess');

  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      // Basic validation feedback (native required attrs already cover this)
      if (!form.checkValidity()) {
        return;
      }

      // ---- Integration point ----
      // Thay URL dưới đây bằng Google Apps Script Web App URL hoặc API endpoint
      // của bạn để form gửi dữ liệu vào Google Sheet / email / hệ thống quản lý.
      //
      // Ví dụ:
      // fetch('https://script.google.com/macros/s/XXXXX/exec', {
      //   method: 'POST',
      //   body: new FormData(form)
      // }).then(() => { ... });

      const data = Object.fromEntries(new FormData(form).entries());
      console.log('Dữ liệu đăng ký tư vấn:', data);

      successBox.classList.add('show');
      form.reset();

      setTimeout(function () {
        successBox.classList.remove('show');
      }, 6000);
    });
  }

  // ---------- Active link highlight on scroll ----------
  const sections = document.querySelectorAll('section[id]');
  const navAnchors = document.querySelectorAll('.main-nav a[href^="#"]');

  function onScrollHighlight() {
    let currentId = '';
    sections.forEach(function (sec) {
      const rect = sec.getBoundingClientRect();
      if (rect.top <= 120 && rect.bottom >= 120) {
        currentId = sec.id;
      }
    });
    navAnchors.forEach(function (a) {
      a.classList.toggle('active', a.getAttribute('href') === '#' + currentId);
    });
  }

  window.addEventListener('scroll', onScrollHighlight, { passive: true });
});
