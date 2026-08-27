<div>
   
    <select wire:model="selectedOption" id="select2" class="form-select select">
        <!--[if BLOCK]><![endif]--><?php $__currentLoopData = $options; $__env->addLoop($__currentLoopData); foreach($__currentLoopData as $option): $__env->incrementLoopIndices(); $loop = $__env->getLastLoop(); ?>
            <option value="<?php echo e($option); ?>"><?php echo e($option); ?></option>
        <?php endforeach; $__env->popLoop(); $loop = $__env->getLastLoop(); ?> <!--[if ENDBLOCK]><![endif]-->
    </select>
</div>

<?php $__env->startPush('scripts'); ?>
    <script>
        $(document).ready(function() {
            $('#select2').select2();
        });
    </script>
<?php $__env->stopPush(); ?>

<?php /**PATH C:\xampp\htdocs\DreamsLms-laravel\projectname\resources\views/livewire/select2-component-filter.blade.php ENDPATH**/ ?>