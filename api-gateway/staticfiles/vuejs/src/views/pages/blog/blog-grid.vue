<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layoutslogin></layoutslogin>

    <bloggrid></bloggrid>

    <!-- Blog Grid -->
    <section class="course-content">
      <div class="container">
        <div class="row">
          <div class="col-lg-9 col-md-12">
            <div class="row">
              <div
                class="col-md-6 col-sm-12"
                v-for="blogPost in blogPosts"
                :key="blogPost.id"
              >
                <!-- Blog Post -->
                <div class="blog grid-blog">
                  <div class="blog-image">
                    <router-link to="blog-details">
                      <img
                        class="img-fluid"
                        :src="require(`@/assets/img/blog/${blogPost.image}`)"
                        alt="Post Image"
                      />
                    </router-link>
                  </div>
                  <div class="blog-grid-box">
                    <div class="blog-info clearfix">
                      <div class="post-left">
                        <ul>
                          <li>
                            <img
                              class="img-fluid"
                              src="@/assets/img/icon/icon-22.svg"
                              alt=""
                            />
                            {{ blogPost.date }}
                          </li>
                          <li>
                            <img
                              class="img-fluid"
                              src="@/assets/img/icon/icon-23.svg"
                              alt=""
                            />
                            {{ blogPost.category }}
                          </li>
                        </ul>
                      </div>
                    </div>
                    <h3 class="blog-title">
                      <router-link to="blog-details">{{ blogPost.title }}</router-link>
                    </h3>
                    <div class="blog-content blog-read">
                      <p>{{ blogPost.content }}</p>
                      <router-link to="blog-details" class="read-more btn btn-primary">
                        Read More
                      </router-link>
                    </div>
                  </div>
                </div>
                <!-- /Blog Post -->
              </div>
            </div>

            <pagination></pagination>
          </div>

          <blogsidebar></blogsidebar>
        </div>
      </div>
    </section>
    <!-- /Blog Grid -->

    <layouts1></layouts1>
  </div>
  <!-- /Main Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      blogPosts: [
        {
          id: 1,
          title: "Learn Webs Applications Development from Experts",
          image: "blog-08.jpg",
          date: "Jun 14, 2023",
          category: "Programming, Web Design",
          content:
            "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit. Sed egestas, ante et vulputate volutpat, eros pede [...]",
        },
        {
          id: 2,
          title: "Expand Your Career Opportunities With Python",
          image: "blog-09.jpg",
          date: "May 24, 2023",
          category: "Programming, Courses",
          content:
            "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit. Sed egestas, ante et vulputate volutpat, eros pede [...]",
        },
        {
          id: 3,
          title: "Complete PHP Programming Career Guideline",
          image: "blog-10.jpg",
          date: "Jun 14, 2023",
          category: "Programming, Web Design",
          content:
            "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit. Sed egestas, ante et vulputate volutpat, eros pede [...]",
        },
        {
          id: 4,
          title: "Programming Content Guideline For Beginners",
          image: "blog-11.jpg",
          date: "Jun 18, 2023",
          category: "Programming, Courses",
          content:
            "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit. Sed egestas, ante et vulputate volutpat, eros pede [...]",
        },
        {
          id: 5,
          title: "The Complete JavaScript Course for Beginners",
          image: "blog-12.jpg",
          date: "Jun 26, 2023",
          category: "Programming, Web Design",
          content:
            "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit. Sed egestas, ante et vulputate volutpat, eros pede [...]",
        },
        {
          id: 6,
          title: "Learn Mobile Applications Development from Experts",
          image: "blog-13.jpg",
          date: "Jun 18, 2023",
          category: "Programming, Courses",
          content:
            "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit. Sed egestas, ante et vulputate volutpat, eros pede [...]",
        },
      ],
    };
  },
};
</script>
