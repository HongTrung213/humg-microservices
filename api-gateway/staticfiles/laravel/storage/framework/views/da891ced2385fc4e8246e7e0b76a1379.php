 <!-- pagination -->
 <div class="row">
     <div class="col-md-12">
         <?php if(!Route::is(['instructor-list', 'instructor-student-grid'])): ?>
             <ul class="pagination lms-page">
         <?php endif; ?>
         <?php if(Route::is(['instructor-list'])): ?>
             <ul class="pagination lms-page lms-pagination">
         <?php endif; ?>
         <?php if(Route::is(['instructor-list', 'instructor-student-grid'])): ?>
             <ul class="pagination lms-page mt-0">
         <?php endif; ?>
         <li class="page-item prev">
             <a class="page-link" href="#" tabindex="-1"><i class="fas fa-angle-left"></i></a>
         </li>
         <li class="page-item first-page active">
             <a class="page-link" href="#">1</a>
         </li>
         <li class="page-item">
             <a class="page-link" href="#">2</a>
         </li>
         <li class="page-item">
             <a class="page-link" href="#">3</a>
         </li>
         <li class="page-item">
             <a class="page-link" href="#">4</a>
         </li>
         <li class="page-item">
             <a class="page-link" href="#">5</a>
         </li>
         <li class="page-item next">
             <a class="page-link" href="#"><i class="fas fa-angle-right"></i></a>
         </li>
         </ul>
     </div>
 </div>
 <!-- /pagination -->
<?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/components/pagination.blade.php ENDPATH**/ ?>