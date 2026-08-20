<template>
  <div class="error-page">
    <!-- Main Wrapper -->
    <div class="main-wrapper">
      <div class="error-box">
        <div class="error-logo">
          <router-link to="/">
            <img src="@/assets/img/logo.svg" class="img-fluid" alt="Logo" />
          </router-link>
        </div>
        <h4>WE ARE COMING SOON!!</h4>
        <h6 class="font-weight-normal">Stay tuned for something amazing</h6>
        <div class="countdown-container">
          <div class="countdown-el days-c">
            <p class="big-text" ref="daysRef">0</p>
            <span>Days</span>
          </div>
          <div class="countdown-el hours-c">
            <p class="big-text" ref="hoursRef">0</p>
            <span>hrs</span>
          </div>
          <div class="countdown-el mins-c">
            <p class="big-text" ref="minsRef">0</p>
            <span>mins</span>
          </div>
        </div>
        <div class="error-box-img">
          <img src="@/assets/img/come-soon.png" alt="" class="img-fluid" />
        </div>
        <div class="come-soon-box">
          <h5 class="h4 font-weight-normal">
            Subscribe to our mailing list to get latest updates
          </h5>
          <div class="subscribe-soon">
            <form>
              <div class="input-group mb-3">
                <input type="text" class="form-control" placeholder="Email" />
                <button class="btn btn-danger" type="button">Subscribe</button>
              </div>
            </form>
          </div>
          <div class="social-icon-soon">
            <ul>
              <li>
                <a href="javascript:;"><i class="fa-brands fa-facebook face-book"></i></a>
              </li>
              <li>
                <a href="javascript:;"><i class="fa-brands fa-twitter twit-ter"></i></a>
              </li>
              <li>
                <a href="javascript:;"
                  ><i class="fa-brands fa-instagram insta-gram"></i
                ></a>
              </li>
              <li>
                <a href="javascript:;"><i class="fa-brands fa-linkedin linked-in"></i></a>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <!-- /Main Wrapper -->
  </div>
</template>
<script>
import { ref, onMounted } from "vue";

export default {
  setup() {
    const daysRef = ref(null);
    const hoursRef = ref(null);
    const minsRef = ref(null);

    onMounted(() => {
      setInterval(() => {
        updateCountdown({ daysRef, hoursRef, minsRef });
      }, 1000);
    });

    return {
      daysRef,
      hoursRef,
      minsRef,
    };
  },
};

function updateCountdown({ daysRef, hoursRef, minsRef }) {
  const targetDate = new Date("2023-07-01T00:00:00Z");
  const currentDate = new Date();
  const timeDifference = targetDate - currentDate;

  // Calculate the remaining days, hours, and minutes
  const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));
  const hours = Math.floor((timeDifference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((timeDifference % (1000 * 60 * 60)) / (1000 * 60));

  // Update the HTML elements with the remaining time
  if (daysRef.value) {
    daysRef.value.textContent = days;
  }
  if (hoursRef.value) {
    hoursRef.value.textContent = hours;
  }
  if (minsRef.value) {
    minsRef.value.textContent = minutes;
  }
}
</script>
