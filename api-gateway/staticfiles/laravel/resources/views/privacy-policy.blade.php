<?php $page = 'privacy-policy'; ?>
@extends('layout.mainlayout')
@section('content')
    @component('components.breadcrumb')
        @slot('title')
            Home
        @endslot
        @slot('li1')
            Pages
        @endslot
        @slot('li2')
            Privacy Policy
        @endslot
    @endcomponent
    @component('components.pagebanner')
        @slot('title')
            Privacy Policy
        @endslot
    @endcomponent

    <!-- Help Details -->
    <div class="page-content">
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <div class="terms-content">
                        <div class="terms-text">
                            <h3>Effective date: <span>23rd of June, 2023</span></h3>
                            <h4>This is a H1, Perfect's for titles.</h4>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Stress, for the United States
                                element ante. Duis cursus, mi quis viverra ornare, eros pain, sometimes none at all, freedom
                                of the living creature was as the profit and financial security. Jasmine neck adapter and
                                just running it lorem makeup sad smile of the television set.</p>
                            <h5>This is a H2's perfect for the titles.</h5>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Stress, for the United States
                                element ante. Duis cursus, mi quis viverra ornare, eros pain , sometimes none at all,
                                freedom of the living creature was as the profit and financial security. Jasmine neck
                                adapter and just running it lorem makeup hairstyle. Now sad smile of the television set.</p>
                            <h5>This is a H2's perfect for the titles.</h5>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Stress, for the United States
                                element ante. Duis cursus, mi quis viverra ornare, eros pain , sometimes none at all,
                                freedom of the living creature was as the profit and financial security. Jasmine neck
                                adapter and just running it lorem makeup hairstyle. Now sad smile of the television set.</p>
                        </div>
                        <div class="terms-text">
                            <h4>This is a H2's perfect for the titles.</h4>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Stress, for the United States
                                element ante. Duis cursus, mi quis viverra ornare, eros pain , sometimes none at all,
                                freedom of the living creature was as the profit and financial security. Jasmine neck
                                adapter and just running it lorem makeup hairstyle. Now sad smile of the television set.</p>
                            <ul>
                                <li>More than 60+ components</li>
                                <li>Five ready tests</li>
                                <li>Coming soon page </li>
                                <li>Check list with left icon</li>
                                <li>And much more ...</li>
                            </ul>
                        </div>
                        <div class="terms-text">
                            <h4>This is a H2's perfect for the titles.</h4>
                            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Stress, for the United States
                                element ante. Duis cursus, mi quis viverra ornare, eros pain , sometimes none at all,
                                freedom of the living creature was as the profit and financial security. Jasmine neck
                                adapter and just running it lorem makeup hairstyle. Now sad smile of the television set.</p>
                        </div>
                        <div class="terms-text">
                            <h4>Changes about terms</h4>
                            <p>If we change our terms of use we will post those changes on this page. Registered users will
                                be sent an email that outlines changes made to the terms of use.</p>
                            <p>Questions? Please email us at <a href="javascript:void(0);">dreamslms@example.com</a></p>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
    <!-- /Help Details -->
@endsection
