<template>
  <!-- Filter -->
  <div class="showing-list">
    <div class="row">
      <div class="col-lg-12">
        <div class="show-filter choose-search-blk">
          <form action="#">
            <div class="mycourse-student align-items-center">
              <div class="student-search">
                <div class="search-group">
                  <i class="feather-search"></i>
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Search our courses"
                  />
                </div>
              </div>
              <div class="student-filter">
                <div class="form-group select-form mb-0">
                  <vue-select
                    :options="published"
                    placeholder="Newly published"
                    name="sellist1"
                  />
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  <!-- /Filter -->
</template>
<script>
import Vue from "vue";
export default {
  components: {},
  data() {
    return {
      published: ["Newly published", "Angular", "React", "Node"],
    };
  },
};
</script>
