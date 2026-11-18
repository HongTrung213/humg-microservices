/* =====================================================
   HUMG UI — dùng chung cho trang quản trị và cổng sinh viên
   - Menu mobile cổng sinh viên
   - Chế độ sáng/tối (cổng sinh viên)
   - Bảng tự cuộn ngang trên màn hình nhỏ
   - Tự ẩn thông báo thành công
   ===================================================== */
(function () {
    'use strict';

    var THEME_KEY = 'humg-theme';
    var root = document.documentElement;

    function storageGet(key) {
        try { return window.localStorage.getItem(key); } catch (e) { return null; }
    }

    function storageSet(key, value) {
        try { window.localStorage.setItem(key, value); } catch (e) { /* bỏ qua */ }
    }

    /* ---------- Theme (chỉ cổng sinh viên) ---------- */
    function applyTheme(theme) {
        root.setAttribute('data-theme', theme === 'dark' ? 'dark' : 'light');
        document.querySelectorAll('[data-theme-icon]').forEach(function (icon) {
            icon.classList.toggle('fa-moon', theme !== 'dark');
            icon.classList.toggle('fa-sun', theme === 'dark');
        });
    }

    function initTheme() {
        if (!document.body.classList.contains('humg-student')) { return; }
        applyTheme(storageGet(THEME_KEY) || 'light');
        document.querySelectorAll('[data-theme-toggle]').forEach(function (btn) {
            btn.addEventListener('click', function () {
                var next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
                storageSet(THEME_KEY, next);
                applyTheme(next);
            });
        });
    }

    /* ---------- Menu mobile cổng sinh viên ---------- */
    function initStudentMenu() {
        var toggle = document.querySelector('[data-student-menu-toggle]');
        var menu = document.querySelector('[data-student-menu]');
        if (!toggle || !menu) { return; }

        function setOpen(open) {
            menu.classList.toggle('open', open);
            toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
            toggle.setAttribute('aria-label', open ? 'Đóng menu' : 'Mở menu');
        }

        toggle.addEventListener('click', function (e) {
            e.stopPropagation();
            setOpen(!menu.classList.contains('open'));
        });

        document.addEventListener('click', function (e) {
            if (menu.classList.contains('open') && !menu.contains(e.target)) { setOpen(false); }
        });

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && menu.classList.contains('open')) {
                setOpen(false);
                toggle.focus();
            }
        });

        window.addEventListener('resize', function () {
            if (window.innerWidth >= 992) { setOpen(false); }
        });
    }

    /* ---------- Menu off-canvas trang quản trị: đóng bằng phím Esc ---------- */
    function initAdminMenu() {
        if (!document.body.classList.contains('humg-admin')) { return; }
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && root.classList.contains('menu-opened')) {
                root.classList.remove('menu-opened');
                document.querySelectorAll('.sidebar-overlay').forEach(function (el) { el.classList.remove('opened'); });
            }
        });
    }

    /* ---------- Bảng responsive ---------- */
    function initTables() {
        document.querySelectorAll('.humg-admin table.table, .humg-student table.table').forEach(function (table) {
            var wrapper = table.parentElement;
            if (!wrapper.classList.contains('table-responsive')) {
                var div = document.createElement('div');
                div.className = 'table-responsive';
                wrapper.insertBefore(div, table);
                div.appendChild(table);
                wrapper = div;
            }
            var headRow = table.querySelector('thead tr') || table.querySelector('tr');
            var cols = headRow ? headRow.children.length : 0;
            if (cols) {
                var min = Math.max(cols <= 3 ? 0 : 560, Math.min(1100, cols * 115));
                table.style.setProperty('--table-min', min + 'px');
            }
        });
    }

    /* ---------- Tự ẩn thông báo thành công / thông tin ---------- */
    function initAlerts() {
        document.querySelectorAll('.app-messages .alert-success, .app-messages .alert-info').forEach(function (alert) {
            window.setTimeout(function () {
                if (window.bootstrap && window.bootstrap.Alert) {
                    window.bootstrap.Alert.getOrCreateInstance(alert).close();
                } else {
                    alert.remove();
                }
            }, 6000);
        });
    }

    // Áp dụng theme sớm để tránh nháy màu
    if (document.body && document.body.classList.contains('humg-student')) {
        applyTheme(storageGet(THEME_KEY) || 'light');
    }

    document.addEventListener('DOMContentLoaded', function () {
        initTheme();
        initStudentMenu();
        initAdminMenu();
        initTables();
        initAlerts();
    });
})();
