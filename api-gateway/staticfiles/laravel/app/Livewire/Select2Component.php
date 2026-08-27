<?php

namespace App\Livewire;

use Livewire\Component;

class Select2Component extends Component
{
 
    public function render()
    {
    
        return view('livewire.select2-component',
        [
            'options' => ['Category', 'Angular', 'Node Js','React','Python']
        ]);
    }
}
