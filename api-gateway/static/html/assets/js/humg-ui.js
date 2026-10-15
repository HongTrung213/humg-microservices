/* =====================================================
   HUMG UI — Custom JavaScript
   File tạo tự động để fix 404.
   Thêm code custom UI vào đây khi cần.
   ===================================================== */

(function() {
    'use strict';

    // Auto dismiss alerts sau 4 giây
    document.addEventListener('DOMContentLoaded', function() {
        // Toggle sidebar nếu có
        var toggles = document.querySelectorAll('[data-toggle="sidebar"]');
        toggles.forEach(function(el) {
            el.addEventListener('click', function() {
                document.body.classList.toggle('sidebar-open');
            });
        });
    });

    console.log('[HUMG UI] Loaded');
})();