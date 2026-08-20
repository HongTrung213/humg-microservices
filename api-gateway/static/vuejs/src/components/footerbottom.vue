<template>
  <!-- Footer Bottom -->
  <div class="footer-bottom">
    <div class="container">
      <!-- Copyright -->
      <div class="copyright">
        <div class="row">
          <div class="col-md-6">
            <div class="privacy-policy">
              <ul>
                <li><router-link to="term-condition">Terms</router-link></li>
                <li><router-link to="privacy-policy">Privacy</router-link></li>
              </ul>
            </div>
          </div>
          <div class="col-md-6">
            <div class="copyright-text">
              <p class="mb-0">
                &copy; {{ new Date().getFullYear() }} DreamsLMS. All rights reserved.
              </p>
            </div>
          </div>
        </div>
      </div>
      <!-- /Copyright -->
    </div>
  </div>
  <!-- /Footer Bottom -->
</template>
