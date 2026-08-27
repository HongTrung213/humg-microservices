<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layouts></layouts>

    <!-- New Course -->
    <section class="page-content course-sec">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-md-12">
            <div class="add-course-header">
              <h2>Add New Course</h2>
              <div class="add-course-btns">
                <ul class="nav">
                  <li>
                    <router-link to="dashboard-instructor" class="btn btn-black"
                      >Back to Course</router-link
                    >
                  </li>
                  <li>
                    <a href="javascript:void(0);" class="btn btn-success-dark">Save</a>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-12">
            <div class="card">
              <!-- Course Wizard -->
              <div class="widget-set">
                <div class="widget-setcount">
                  <ul id="progressbar" v-show="currentStep === 1">
                    <li class="progress-active">
                      <p><span></span> Basic Information</p>
                    </li>
                    <li>
                      <p><span></span> Courses Media</p>
                    </li>
                    <li>
                      <p><span></span> Curriculum</p>
                    </li>
                    <li>
                      <p><span></span> Settings</p>
                    </li>
                  </ul>
                  <ul id="progressbar" v-show="currentStep === 2">
                    <li>
                      <p><span></span> Basic Information</p>
                    </li>
                    <li class="progress-active">
                      <p><span></span> Courses Media</p>
                    </li>
                    <li>
                      <p><span></span> Curriculum</p>
                    </li>
                    <li>
                      <p><span></span> Settings</p>
                    </li>
                  </ul>
                  <ul id="progressbar" v-show="currentStep === 3">
                    <li>
                      <p><span></span> Basic Information</p>
                    </li>
                    <li>
                      <p><span></span> Courses Media</p>
                    </li>
                    <li class="progress-active">
                      <p><span></span> Curriculum</p>
                    </li>
                    <li>
                      <p><span></span> Settings</p>
                    </li>
                  </ul>
                  <ul id="progressbar" v-show="currentStep === 4">
                    <li>
                      <p><span></span> Basic Information</p>
                    </li>
                    <li>
                      <p><span></span> Courses Media</p>
                    </li>
                    <li>
                      <p><span></span> Curriculum</p>
                    </li>
                    <li class="progress-active">
                      <p><span></span> Settings</p>
                    </li>
                  </ul>
                </div>
                <div class="widget-content multistep-form">
                  <fieldset id="first" v-if="currentStep === 1">
                    <div class="add-course-info">
                      <div class="add-course-inner-header">
                        <h4>Basic Information</h4>
                      </div>
                      <div class="add-course-form">
                        <form action="#">
                          <div class="form-group">
                            <label class="add-course-label">Course Title</label>
                            <input
                              type="text"
                              class="form-control"
                              placeholder="Course Title"
                            />
                          </div>
                          <div class="form-group">
                            <label class="add-course-label">Courses Category</label>
                            <vue-select :options="Category" placeholder="Category 01" />
                          </div>
                          <div class="form-group">
                            <label class="add-course-label">Courses Level</label>
                            <vue-select :options="Level" placeholder="Level 01" />
                          </div>
                          <div class="form-group mb-0">
                            <label class="add-course-label">Course Description</label>
                            <SummernoteEditor
                              v-model="myValue"
                              @update:modelValue="summernoteChange($event)"
                              @summernoteImageLinkInsert="summernoteImageLinkInsert"
                            />
                          </div>
                        </form>
                      </div>
                      <div class="widget-btn">
                        <a class="btn btn-black">Back</a>
                        <a
                          class="btn btn-info-light next_btn"
                          @click="nextStep"
                          :disabled="currentStep === totalSteps"
                          >Continue</a
                        >
                      </div>
                    </div>
                  </fieldset>
                  <fieldset class="field-card" v-if="currentStep === 2">
                    <div class="add-course-info">
                      <div class="add-course-inner-header">
                        <h4>Courses Media</h4>
                      </div>
                      <div class="add-course-form">
                        <form action="#">
                          <div class="form-group">
                            <label class="add-course-label">Course cover image</label>
                            <div class="relative-form">
                              <span>No File Selected</span>
                              <label class="relative-file-upload">
                                Upload File <input type="file" />
                              </label>
                            </div>
                          </div>
                          <div class="form-group">
                            <div class="add-image-box">
                              <a href="javascript:void(0);">
                                <i class="far fa-image"></i>
                              </a>
                            </div>
                          </div>
                          <div class="form-group">
                            <input
                              type="text"
                              class="form-control"
                              placeholder="Video URL"
                            />
                          </div>
                          <div class="form-group">
                            <div class="add-image-box add-video-box">
                              <a href="javascript:void(0);">
                                <i class="fas fa-circle-play"></i>
                              </a>
                            </div>
                          </div>
                        </form>
                      </div>
                      <div class="widget-btn">
                        <a
                          class="btn btn-black prev_btn"
                          @click="previousStep"
                          :disabled="currentStep === 1"
                          >Previous</a
                        >
                        <a
                          class="btn btn-info-light next_btn"
                          @click="nextStep"
                          :disabled="currentStep === totalSteps"
                          >Continue</a
                        >
                      </div>
                    </div>
                  </fieldset>
                  <fieldset class="field-card" v-if="currentStep === 3">
                    <div class="add-course-info">
                      <div class="add-course-inner-header">
                        <h4>Curriculum</h4>
                      </div>
                      <div class="add-course-section">
                        <a href="javascript:void(0);" class="btn">Add Section</a>
                      </div>
                      <div class="add-course-form">
                        <div class="curriculum-grid">
                          <div class="curriculum-head">
                            <p>Section 1: Introduction</p>
                            <a href="javascript:void(0);" class="btn">Add Lecture</a>
                          </div>
                          <div class="curriculum-info">
                            <div id="accordion">
                              <div class="faq-grid">
                                <div class="faq-header">
                                  <a
                                    class="collapsed faq-collapse"
                                    data-bs-toggle="collapse"
                                    href="#collapseOne"
                                  >
                                    <i class="fas fa-align-justify"></i> Introduction
                                  </a>
                                  <div class="faq-right">
                                    <a href="javascript:void(0);">
                                      <i class="far fa-pen-to-square me-1"></i>
                                    </a>
                                    <a href="javascript:void(0);" class="me-0">
                                      <i class="far fa-trash-can"></i>
                                    </a>
                                  </div>
                                </div>
                                <div
                                  id="collapseOne"
                                  class="collapse"
                                  data-bs-parent="#accordion"
                                >
                                  <div class="faq-body">
                                    <div class="add-article-btns">
                                      <a href="javascript:void(0);" class="btn"
                                        >Add Article</a
                                      >
                                      <a href="javascript:void(0);" class="btn me-0"
                                        >Add Description</a
                                      >
                                    </div>
                                  </div>
                                </div>
                              </div>
                              <div class="faq-grid">
                                <div class="faq-header">
                                  <a
                                    class="collapsed faq-collapse"
                                    data-bs-toggle="collapse"
                                    href="#collapseTwo"
                                  >
                                    <i class="fas fa-align-justify"></i> Installing
                                    Development Software
                                  </a>
                                  <div class="faq-right">
                                    <a href="javascript:void(0);">
                                      <i class="far fa-pen-to-square me-1"></i>
                                    </a>
                                    <a href="javascript:void(0);" class="me-0">
                                      <i class="far fa-trash-can"></i>
                                    </a>
                                  </div>
                                </div>
                                <div
                                  id="collapseTwo"
                                  class="collapse"
                                  data-bs-parent="#accordion"
                                >
                                  <div class="faq-body">
                                    <div class="add-article-btns">
                                      <a href="javascript:void(0);" class="btn"
                                        >Add Article</a
                                      >
                                      <a href="javascript:void(0);" class="btn me-0"
                                        >Add Description</a
                                      >
                                    </div>
                                  </div>
                                </div>
                              </div>
                              <div class="faq-grid mb-0">
                                <div class="faq-header">
                                  <a
                                    class="collapsed faq-collapse"
                                    data-bs-toggle="collapse"
                                    href="#collapseThree"
                                  >
                                    <i class="fas fa-align-justify"></i> Hello World
                                    Project from GitHub
                                  </a>
                                  <div class="faq-right">
                                    <a href="javascript:void(0);">
                                      <i class="far fa-pen-to-square me-1"></i>
                                    </a>
                                    <a href="javascript:void(0);" class="me-0">
                                      <i class="far fa-trash-can"></i>
                                    </a>
                                  </div>
                                </div>
                                <div
                                  id="collapseThree"
                                  class="collapse"
                                  data-bs-parent="#accordion"
                                >
                                  <div class="faq-body">
                                    <div class="add-article-btns">
                                      <a href="javascript:void(0);" class="btn"
                                        >Add Article</a
                                      >
                                      <a href="javascript:void(0);" class="btn me-0"
                                        >Add Description</a
                                      >
                                    </div>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div class="curriculum-grid mb-0">
                          <div class="curriculum-head">
                            <p>Section 1: JavaScript Beginnings</p>
                            <a href="javascript:void(0);" class="btn">Add Lecture</a>
                          </div>
                          <div class="curriculum-info">
                            <div id="accordion-one">
                              <div class="faq-grid">
                                <div class="faq-header">
                                  <a
                                    class="collapsed faq-collapse"
                                    data-bs-toggle="collapse"
                                    href="#collapseFour"
                                  >
                                    <i class="fas fa-align-justify"></i> Introduction
                                  </a>
                                  <div class="faq-right">
                                    <a href="javascript:void(0);">
                                      <i class="far fa-pen-to-square me-1"></i>
                                    </a>
                                    <a href="javascript:void(0);" class="me-0">
                                      <i class="far fa-trash-can"></i>
                                    </a>
                                  </div>
                                </div>
                                <div
                                  id="collapseFour"
                                  class="collapse"
                                  data-bs-parent="#accordion-one"
                                >
                                  <div class="faq-body">
                                    <div class="add-article-btns">
                                      <a href="javascript:void(0);" class="btn"
                                        >Add Article</a
                                      >
                                      <a href="javascript:void(0);" class="btn me-0"
                                        >Add Description</a
                                      >
                                    </div>
                                  </div>
                                </div>
                              </div>
                              <div class="faq-grid">
                                <div class="faq-header">
                                  <a
                                    class="collapsed faq-collapse"
                                    data-bs-toggle="collapse"
                                    href="#collapseFive"
                                  >
                                    <i class="fas fa-align-justify"></i> Installing
                                    Development Software
                                  </a>
                                  <div class="faq-right">
                                    <a href="javascript:void(0);">
                                      <i class="far fa-pen-to-square me-1"></i>
                                    </a>
                                    <a href="javascript:void(0);" class="me-0">
                                      <i class="far fa-trash-can"></i>
                                    </a>
                                  </div>
                                </div>
                                <div
                                  id="collapseFive"
                                  class="collapse"
                                  data-bs-parent="#accordion-one"
                                >
                                  <div class="faq-body">
                                    <div class="add-article-btns">
                                      <a href="javascript:void(0);" class="btn"
                                        >Add Article</a
                                      >
                                      <a href="javascript:void(0);" class="btn me-0"
                                        >Add Description</a
                                      >
                                    </div>
                                  </div>
                                </div>
                              </div>
                              <div class="faq-grid">
                                <div class="faq-header">
                                  <a
                                    class="collapsed faq-collapse"
                                    data-bs-toggle="collapse"
                                    href="#collapseSix"
                                  >
                                    <i class="fas fa-align-justify"></i> Hello World
                                    Project from GitHub
                                  </a>
                                  <div class="faq-right">
                                    <a href="javascript:void(0);">
                                      <i class="far fa-pen-to-square me-1"></i>
                                    </a>
                                    <a href="javascript:void(0);" class="me-0">
                                      <i class="far fa-trash-can"></i>
                                    </a>
                                  </div>
                                </div>
                                <div
                                  id="collapseSix"
                                  class="collapse"
                                  data-bs-parent="#accordion-one"
                                >
                                  <div class="faq-body">
                                    <div class="add-article-btns">
                                      <a href="javascript:void(0);" class="btn"
                                        >Add Article</a
                                      >
                                      <a href="javascript:void(0);" class="btn me-0"
                                        >Add Description</a
                                      >
                                    </div>
                                  </div>
                                </div>
                              </div>
                              <div class="faq-grid mb-0">
                                <div class="faq-header">
                                  <a
                                    class="collapsed faq-collapse"
                                    data-bs-toggle="collapse"
                                    href="#collapseSeven"
                                  >
                                    <i class="fas fa-align-justify"></i> Our Sample
                                    Website
                                  </a>
                                  <div class="faq-right">
                                    <a href="javascript:void(0);">
                                      <i class="far fa-pen-to-square me-1"></i>
                                    </a>
                                    <a href="javascript:void(0);" class="me-0">
                                      <i class="far fa-trash-can"></i>
                                    </a>
                                  </div>
                                </div>
                                <div
                                  id="collapseSeven"
                                  class="collapse"
                                  data-bs-parent="#accordion-one"
                                >
                                  <div class="faq-body">
                                    <div class="add-article-btns">
                                      <a href="javascript:void(0);" class="btn"
                                        >Add Article</a
                                      >
                                      <a href="javascript:void(0);" class="btn me-0"
                                        >Add Description</a
                                      >
                                    </div>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                      <div class="widget-btn">
                        <a
                          class="btn btn-black prev_btn"
                          @click="previousStep"
                          :disabled="currentStep === 2"
                          >Previous</a
                        >
                        <a
                          class="btn btn-info-light next_btn"
                          @click="nextStep"
                          :disabled="currentStep === totalSteps"
                          >Continue</a
                        >
                      </div>
                    </div>
                  </fieldset>
                  <fieldset class="field-card" v-if="currentStep === 4">
                    <div class="add-course-info">
                      <div class="add-course-inner-header">
                        <h4>Requirements</h4>
                      </div>
                      <div class="add-course-form">
                        <form action="#">
                          <div class="form-group form-group-tagsinput">
                            <vue3-tags-input :tags="tags" />
                          </div>
                          <div class="form-group mb-0">
                            <label class="add-course-label">Price</label>
                            <input type="text" class="form-control" placeholder="10.00" />
                          </div>
                        </form>
                      </div>
                      <div class="widget-btn">
                        <a
                          class="btn btn-black prev_btn"
                          @click="previousStep"
                          :disabled="currentStep === 3"
                          >Previous</a
                        >
                        <a
                          class="btn btn-info-light next_btn"
                          @click="nextStep"
                          :disabled="currentStep === totalSteps"
                          >Continue</a
                        >
                      </div>
                    </div>
                  </fieldset>
                  <fieldset class="field-card" v-if="currentStep === 5">
                    <div class="add-course-info">
                      <div class="add-course-msg">
                        <i class="fas fa-circle-check"></i>
                        <h4>The Course Added Succesfully</h4>
                        <p>Admin will be Approve soon.</p>
                      </div>
                    </div>
                  </fieldset>
                </div>
              </div>
              <!-- /Course Wizard -->
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- /New Course -->

    <layouts1></layouts1>
  </div>
  <!-- /Main Wrapper -->
</template>
<script>
import Vue3TagsInput from "vue3-tags-input";
import SummernoteEditor from "vue3-summernote-editor";
export default {
  components: {
    Vue3TagsInput,
    SummernoteEditor,
  },
  data() {
    return {
      tags: ["jquery", "bootstrap"],
      Category: ["Category 01", "Category 02", "Category 03", "Category 04"],
      Level: ["Level 01", "Level 02", "Level 03", "Level 04"],
      myValue: "",
      currentStep: 1,
      totalSteps: 5,
    };
  },
  methods: {
    nextStep() {
      if (this.currentStep < this.totalSteps) {
        this.currentStep++;
      }
    },
    previousStep() {
      if (this.currentStep > 1) {
        this.currentStep--;
      }
    },
    summernoteChange(newValue) {
      // console.log("summernoteChange", newValue);
    },
    summernoteImageLinkInsert(...args) {
      // console.log("summernoteImageLinkInsert()", args);
    },
  },
};
</script>
