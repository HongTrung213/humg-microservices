<div>
    <select wire:model="selectedOption" id="select2" class="form-select select">
        @foreach ($options as $option)
            <option value="{{ $option }}">{{ $option }}</option>
        @endforeach
    </select>
</div>



