<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layoutsinstructor></layoutsinstructor>

    <!--Dashbord Student -->
    <div class="page-content">
      <div class="container">
        <div class="row">
          <!-- Profile Details -->
          <div class="col-md-12">
            <div
              class="filter-grp ticket-grp tiket-suport d-flex align-items-center justify-content-between"
            >
              <div>
                <h3>Support Tickets</h3>
              </div>
              <div class="ticket-btn-grp">
                <router-link to="instructor-tickets">Back to Tickets</router-link>
              </div>
            </div>
            <div class="settings-widget">
              <div class="settings-inner-blk add-course-info new-ticket-blk p-0">
                <div class="comman-space">
                  <h4>Create New Support Ticket</h4>
                  <div>
                    <div class="form-group">
                      <label class="form-control-label">Ticket Title</label>
                      <input type="text" class="form-control" />
                    </div>
                    <div class="form-group">
                      <label class="form-label">Category</label>
                      <vue-select
                        :options="Category"
                        placeholder="Choose Category"
                        name="sellist1"
                      />
                    </div>
                    <div class="form-group">
                      <label class="form-label">Priority</label>
                      <vue-select
                        :options="Priority"
                        placeholder="Choose Priority"
                        name="sellist1"
                      />
                    </div>
                    <div class="form-group">
                      <label class="add-course-label">Description</label>
                      <SummernoteEditor
                        v-model="myValue"
                        @update:modelValue="summernoteChange($event)"
                        @summernoteImageLinkInsert="summernoteImageLinkInsert"
                      />
                    </div>
                    <div class="form-group">
                      <label class="add-course-label">Attachment</label>
                      <div class="file-drop">
                        <form action="#" class="dropzone">
                          <p>Drag & Drop files</p>
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

    <layouts1></layouts1>
  </div>
  <!-- /Main Wrapper -->
</template>
<script>
import { defineComponent } from "vue";
import SummernoteEditor from "vue3-summernote-editor";
import Vue from "vue";
export default {
  components: {
    SummernoteEditor,
  },
  data() {
    return {
      tags: ["jquery", "bootstrap"],
      Category: [
        "Choose Category",
        "Mailing Issue",
        "Language Issue",
        "Installation Error",
      ],
      Priority: [
        "Choose Priority",
        "Mailing Issue",
        "Language Issue",
        "Installation Error",
      ],
      myValue: "",
    };
  },
  methods: {
    summernoteChange(newValue) {
      // console.log("summernoteChange", newValue);
    },
    summernoteImageLinkInsert(...args) {
      // console.log("summernoteImageLinkInsert()", args);
    },
  },
};
</script>
