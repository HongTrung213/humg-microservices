<?php

namespace App\Livewire;

use Livewire\Component;

class Select2ComponentFilter extends Component
{
    public function render()
    {
        return view('livewire.select2-component-filter',
        [
            'options' => ['Newly published', 'Angular', 'Nodejs','React']
        ]);
    }
}
