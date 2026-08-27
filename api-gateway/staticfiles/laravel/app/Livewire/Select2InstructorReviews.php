<?php

namespace App\Livewire;

use Livewire\Component;

class Select2InstructorReviews extends Component
{
    public $selectedOption1;
    public $selectedOption2;
    public $selectedOption3;
    public $options1;
    public $options2;
    public $options3;

    public function mount()
    {
        $this->options1 = ['All', 'review 1', 'review 2','review 3'];
        $this->options2 = ['Rating', '5', '4','3'];
        $this->options3 = ['Sort', 'Sort 1', 'Sort 2','Sort 3'];
    }
    public function render()
    {
        return view('livewire.select2-instructor-reviews');
    }
}
