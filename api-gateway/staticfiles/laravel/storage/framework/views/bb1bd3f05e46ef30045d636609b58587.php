<div>
<div class="row gx-2 align-items-center">
    <div class="col-md-6 col-lg-3 col-item">
        <div class="form-group select-form mb-1">
            <select wire:model="selectedOption1" class="select2 form-select select">
                <!--[if BLOCK]><![endif]--><?php $__currentLoopData = $options1; $__env->addLoop($__currentLoopData); foreach($__currentLoopData as $option): $__env->incrementLoopIndices(); $loop = $__env->getLastLoop(); ?>
                    <option value="<?php echo e($option); ?>"><?php echo e($option); ?></option>
                <?php endforeach; $__env->popLoop(); $loop = $__env->getLastLoop(); ?> <!--[if ENDBLOCK]><![endif]-->
            </select>
        </div>
    </div>
    <div class="col-md-6 col-lg-3 col-item">
        <div class="form-group select-form mb-1">
            <select wire:model="selectedOption2" class="select2 form-select select">
                <!--[if BLOCK]><![endif]--><?php $__currentLoopData = $options2; $__env->addLoop($__currentLoopData); foreach($__currentLoopData as $option): $__env->incrementLoopIndices(); $loop = $__env->getLastLoop(); ?>
                    <option value="<?php echo e($option); ?>"><?php echo e($option); ?></option>
                <?php endforeach; $__env->popLoop(); $loop = $__env->getLastLoop(); ?> <!--[if ENDBLOCK]><![endif]-->
            </select>
        </div>
    </div>
    <div class="col-md-6 col-lg-3 col-item">
        <div class="form-group select-form mb-1">
            <select wire:model="selectedOption3" class="select2 form-select select">
                <!--[if BLOCK]><![endif]--><?php $__currentLoopData = $options3; $__env->addLoop($__currentLoopData); foreach($__currentLoopData as $option): $__env->incrementLoopIndices(); $loop = $__env->getLastLoop(); ?>
                    <option value="<?php echo e($option); ?>"><?php echo e($option); ?></option>
                <?php endforeach; $__env->popLoop(); $loop = $__env->getLastLoop(); ?> <!--[if ENDBLOCK]><![endif]-->
            </select>
        </div>
    </div>
</div>
</div>

<?php $__env->startPush('scripts'); ?>
    <script>
        $(document).ready(function() {
            $('#select2').select2();
        });
    </script>
<?php $__env->stopPush(); ?>
<?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/livewire/select2-instructor-reviews.blade.php ENDPATH**/ ?>