<template>
  <!-- Main Wrapper -->
  <div class="main-wrapper">
    <layoutslogin></layoutslogin>
    <bloglist></bloglist>
    <!-- Course -->
    <section class="course-content">
      <div class="container">
        <div class="row">
          <div class="col-lg-9 col-md-12">
            <!-- Blog Post -->
            <div class="blog" v-for="post in blogPosts" :key="post.id">
              <div class="blog-image">
                <router-link to="blog-details">
                  <img
                    class="img-fluid"
                    :src="require(`@/assets/img/blog/${post.image}`)"
                    alt="Post Image"
                /></router-link>
              </div>
              <div class="blog-info clearfix">
                <div class="post-left">
                  <ul>
                    <li>
                      <div class="post-author">
                        <router-link to="instructor-profile"
                          ><img
                            :src="require(`@/assets/img/user/${post.authorImage}`)"
                            alt="Post Author"
                          />
                          <span>{{ post.author }}</span></router-link
                        >
                      </div>
                    </li>
                    <li>
                      <img
                        class="img-fluid"
                        src="@/assets/img/icon/icon-22.svg"
                        alt=""
                      />{{ post.date }}
                    </li>
                    <li>
                      <img
                        class="img-fluid"
                        src="@/assets/img/icon/icon-23.svg"
                        alt=""
                      />{{ post.category }}
                    </li>
                  </ul>
                </div>
              </div>
              <h3 class="blog-title">
                <router-link to="blog-details">{{ post.title }}</router-link>
              </h3>
              <div class="blog-content blog-read">
                <p>{{ post.content }}</p>
                <router-link to="blog-details" class="read-more btn btn-primary"
                  >Read More</router-link
                >
              </div>
            </div>
            <!-- /Blog Post -->

            <pagination></pagination>
          </div>

          <blogsidebar></blogsidebar>
        </div>
      </div>
    </section>
    <!-- /Course -->

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
          image: "blog-05.jpg",
          authorImage: "user.jpg",
          author: "Ruby Perrin",
          date: "April 20, 2023",
          category: "Programming, Web Design",
          title: "Learn Web Applications Development from Experts",
          content:
            "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit...",
        },
        {
          id: 2,
          image: "blog-06.jpg",
          authorImage: "user1.jpg",
          author: "Jenis R.",
          date: "May 20, 2023",
          category: "Programming, Courses",
          title: "Expand Your Career Opportunities With Python",
          content:
            "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit...",
        },
        {
          id: 3,
          image: "blog-07.jpg",
          authorImage: "user3.jpg",
          author: "Rolands R.",
          date: "Jun 20, 2023",
          category: "Programming, Web Design",
          title: "Complete PHP Programming Career Guideline",
          content:
            "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Phasellus hendrerit...",
        },
      ],
    };
  },
};
</script>
