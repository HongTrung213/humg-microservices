<?php if(Route::is(['setting-student-invoice'])): ?>
    <div class="modal custom-modal fade" id="addpaymentMethod" tabindex="-1" aria-labelledby="addpaymentMethod"
        aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Add New Payment Method</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="addpaymethod-form">
                        <form action="#">
                            <div class="row">
                                <div class="col-lg-12">
                                    <div class="wallet-method">
                                        <label class="radio-inline custom_radio me-4">
                                            <input type="radio" name="optradio" checked="">
                                            <span class="checkmark"></span> Credit or Debit card
                                        </label>
                                        <label class="radio-inline custom_radio">
                                            <input type="radio" name="optradio">
                                            <span class="checkmark"></span> PayPal
                                        </label>
                                    </div>
                                    <div class="form-group">
                                        <label class="form-control-label">Card Number</label>
                                        <input type="text" class="form-control" placeholder="XXXX XXXX XXXX XXXX">
                                    </div>
                                </div>
                                <div class="col-lg-4">
                                    <div class="form-group">
                                        <label class="form-label">Month</label>
                                        <select class="form-select" name="sellist1">
                                            <option>Month</option>
                                            <option>Brazil</option>
                                            <option>French</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="col-lg-4">
                                    <div class="form-group">
                                        <label class="form-label">Year</label>
                                        <select class="form-select" name="sellist1">
                                            <option>Year</option>
                                            <option>India</option>
                                            <option>America</option>
                                            <option>London</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="col-lg-4">
                                    <div class="form-group">
                                        <label class="form-control-label">CVV Code </label>
                                        <input type="text" class="form-control" placeholder="XXXX">
                                    </div>
                                </div>
                                <div class="col-lg-12">
                                    <div class="form-group mb-0">
                                        <label class="form-control-label">Name on Card</label>
                                        <input type="text" class="form-control" placeholder="Address">
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
                <div class="modal-footer me-auto">
                    <button type="button" class="btn btn-primary btn-theme" data-bs-dismiss="modal">Save
                        changes</button>
                    <button type="button" class="btn btn-primary btn-cancel" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
<?php endif; ?>
<?php if(Route::is(['setting-student-payment'])): ?>
    <!-- Modal -->
    <div class="modal custom-modal fade" id="addpaymentMethod" tabindex="-1" aria-labelledby="addpaymentMethod"
        aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Add New Payment Method</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="addpaymethod-form add-course-info">
                        <form action="#">
                            <div class="row">
                                <div class="col-lg-12">
                                    <div class="wallet-method">
                                        <label class="radio-inline custom_radio me-4">
                                            <input type="radio" name="optradio" checked="">
                                            <span class="checkmark"></span> Credit or Debit card
                                        </label>
                                        <label class="radio-inline custom_radio">
                                            <input type="radio" name="optradio">
                                            <span class="checkmark"></span> PayPal
                                        </label>
                                    </div>
                                    <div class="form-group">
                                        <label class="form-control-label">Card Number</label>
                                        <input type="text" class="form-control" placeholder="XXXX XXXX XXXX XXXX">
                                    </div>
                                </div>
                                <div class="col-lg-4">
                                    <div class="form-group">
                                        <label class="form-label">Month</label>
                                        <select class="form-select" name="sellist1">
                                            <option>Month</option>
                                            <option>Brazil</option>
                                            <option>French</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="col-lg-4">
                                    <div class="form-group">
                                        <label class="form-label">Year</label>
                                        <select class="form-select" name="sellist1">
                                            <option>Year</option>
                                            <option>India</option>
                                            <option>America</option>
                                            <option>London</option>
                                        </select>
                                    </div>
                                </div>
                                <div class="col-lg-4">
                                    <div class="form-group">
                                        <label class="form-control-label">CVV Code </label>
                                        <input type="text" class="form-control" placeholder="XXXX">
                                    </div>
                                </div>
                                <div class="col-lg-12">
                                    <div class="form-group mb-0">
                                        <label class="form-control-label">Name on Card</label>
                                        <input type="text" class="form-control" placeholder="Address">
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
                <div class="modal-footer me-auto">
                    <button class="btn btn-primary btn-theme" data-bs-dismiss="modal">Save changes</button>
                    <button class="btn btn-primary btn-cancel" data-bs-dismiss="modal">Close</button>
                </div>
            </div>
        </div>
    </div>
    <!-- Modal -->
<?php endif; ?>
<?php if(Route::is(['withdrawal-instructor', 'deposit-student'])): ?>
    <!-- Deposit Modal -->
    <div class="modal custom-modal fade" id="depositMethod" tabindex="-1" aria-labelledby="addpaymentMethod"
        aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="addpaymentMethod">Deposit Method</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <div class="addpaymethod-form add-course-info">
                        <form action="#">
                            <div class="row">
                                <div class="col-lg-12">

                                    <!-- Deposit Method -->
                                    <div class="radio-with-img">
                                        <p class="radio-deposit-item">
                                            <input type="radio" name="deposittypes" id="deposit-type-one"
                                                value="true" class="ng-valid ng-dirty ng-touched ng-empty"
                                                aria-invalid="false">
                                            <label for="deposit-type-one">
                                                <img src="<?php echo e(URL::asset('/assets/img/deposit-01.jpg')); ?>"
                                                    alt="" class="img-fluid">
                                                Bank
                                            </label>
                                        </p>
                                        <p class="radio-deposit-item">
                                            <input type="radio" name="deposittypes" id="deposit-type-two"
                                                value="false" class="ng-valid ng-dirty ng-touched ng-empty"
                                                aria-invalid="false" checked>
                                            <label for="deposit-type-two">
                                                <img src="<?php echo e(URL::asset('/assets/img/deposit-02.jpg')); ?>"
                                                    alt="" class="img-fluid">
                                                Paypal
                                            </label>
                                        </p>
                                        <p class="radio-deposit-item">
                                            <input type="radio" name="deposittypes" id="deposit-type-three"
                                                value="false" class="ng-valid ng-dirty ng-touched ng-empty"
                                                aria-invalid="false">
                                            <label for="deposit-type-three">
                                                <img src="<?php echo e(URL::asset('/assets/img/deposit-03.jpg')); ?>"
                                                    alt="" class="img-fluid">
                                                Stripe
                                            </label>
                                        </p>
                                        <p class="radio-deposit-item me-0">
                                            <input type="radio" name="deposittypes" id="deposit-type-four"
                                                value="false" class="ng-valid ng-dirty ng-touched ng-empty"
                                                aria-invalid="false">
                                            <label for="deposit-type-four">
                                                <img src="<?php echo e(URL::asset('/assets/img/deposit-04.jpg')); ?>"
                                                    alt="" class="img-fluid">
                                                Flutterwave - USD
                                            </label>
                                        </p>
                                    </div>
                                    <!-- /Deposit Method -->

                                </div>
                                <div class="col-lg-12">
                                    <div class="form-group mb-0">
                                        <label class="form-control-label">Enter Amount:</label>
                                        <input type="text" class="form-control" placeholder="Amount">
                                    </div>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
                <div class="modal-footer me-auto">
                    <button type="button" class="btn btn-primary btn-theme" data-bs-dismiss="modal">Submit</button>
                    <button type="button" class="btn btn-primary btn-cancel" data-bs-dismiss="modal">Cancel</button>
                </div>
            </div>
        </div>
    </div>
    <!-- Deposit Modal -->
<?php endif; ?>
<?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/components/modalpopup.blade.php ENDPATH**/ ?>