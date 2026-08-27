<?php $page = 'setting-support-new-tickets'; ?>
@extends('layout.mainlayout')
@section('content')
    <!--Dashbord Student -->
    <div class="page-content">
        <div class="container">
            <div class="row">
                <!-- Profile Details -->
                <div class="col-md-12">
                    <div class="filter-grp ticket-grp tiket-suport d-flex align-items-center justify-content-between">
                        <div>
                            <h3>Support Tickets</h3>
                        </div>
                        <div class="ticket-btn-grp">
                            <a href="{{ url('setting-support-tickets') }}">Back to Tickets</a>
                        </div>
                    </div>
                    <div class="settings-widget">
                        <div class="settings-inner-blk add-course-info new-ticket-blk p-0">
                            <div class="comman-space">
                                <h4>Create New Support Ticket</h4>
                                <div>
                                    <div class="form-group">
                                        <label class="form-control-label">Ticket Title</label>
                                        <input type="text" class="form-control">
                                    </div>
                                    <div class="form-group">
                                        <label class="form-label">Category</label>
                                        <select class="form-select select country-select" name="sellist1">
                                            <option>Choose Category</option>
                                            <option>Mailing Issue</option>
                                            <option>Language Issue</option>
                                            <option>Installation Error</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label class="form-label">Priority</label>
                                        <select class="form-select select country-select" name="sellist1">
                                            <option>Choose Priority</option>
                                            <option>Mailing Issue</option>
                                            <option>Language Issue</option>
                                            <option>Installation Error</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label class="add-course-label">Description</label>
                                        <div id="editor"></div>
                                    </div>
                                    <div class="form-group ">
                                        <label class="add-course-label">Attachment</label>
                                        <div class="file-drop">
                                            <form action="#" class="dropzone">
                                                <p>Drag & Drop files </p>
                                            </form>
                                        </div>
                                        <div class="accept-drag-file">
                                            <p>Accept File Type: doc,docx,jpg,jpeg,png,txt,pdf</p>
                                        </div>
                                    </div>
                                    <div class="submit-ticket">
                                        <button type="button" class="btn btn-primary">Submit</button>
                                        <button type="button" class="btn btn-dark">Back</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <!-- Profile Details -->

            </div>
        </div>
    </div>
    <!-- /Dashbord Student -->
@endsection
