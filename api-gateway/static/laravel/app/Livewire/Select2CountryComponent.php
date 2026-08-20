<?php

namespace App\Livewire;

use Livewire\Component;

class Select2CountryComponent extends Component
{
    public function render()
    {
        return view('livewire.select2-country-component',
        [
            'options' => ['Select country', 'India', 'America','London']
        ]);
    }
}
