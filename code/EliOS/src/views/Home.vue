<template>
  <div class="bd-main home">
    <!-- Top Tray -->
    <div class='e-bar e-top-bar'>
        <div id='welcome-text'>Welcome, {{ userObject.data.fname }}</div>
    </div>
    <!-- Middle Scroll Section -->
    <div class='e-scroll-container'>
        <div class='e-scroller' v-on:scroll="scroll_track">
            <div class='e-scroll-pane'>
                <img src='https://timedotcom.files.wordpress.com/2019/03/kitten-report.jpg?w=600&quality=85'>
            </div>
            <div class='e-scroll-pane'>
                <img src='https://images.unsplash.com/photo-1529778873920-4da4926a72c2?ixlib=rb-1.2.1&w=1000&q=80'>
            </div>
        </div>
        <div class='e-scroll-status'>
            <i v-bind:class="[status_select == 0 ? 'material-icons' : 'material-icons-outlined']" class='e-scroll-icon'>brightness_1</i>
            <i v-bind:class="[status_select == 1 ? 'material-icons' : 'material-icons-outlined']" class='e-scroll-icon'>brightness_1</i>
            <!-- <i class='material-icons-outlined e-scroll-icon'>brightness_1</i>
            <i class='material-icons-outlined e-scroll-icon'>brightness_1</i> -->
        </div>
    </div>
    <!-- Bottom Tray -->
    <div class='e-tray e-bar'>
        <div class='e-tray-bttn'>
            <i class='material-icons-outlined e-tray-icon'>person</i>
            <div class='e-tray-caption'>Profile</div>
        </div>
        <router-link class='e-tray-bttn' to="/data-entry">
            <i class='material-icons-outlined e-tray-icon'>add_box</i>
            <div class='e-tray-caption'>Track</div>
        </router-link>
        <div class='e-tray-bttn'>
            <i class='material-icons-outlined e-tray-icon'>people_alt</i>
            <div class='e-tray-caption'>Contacts</div>
        </div>
    </div>
  </div>
</template>

<script>
// import { mapState, mapGetters, mapMutations, mapActions } from 'vuex';
// import firebase from 'firebase';
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";

import { mapState } from 'vuex';

export default {
  name: "home", 
  data: function() {
    return {
      status_select: 0
    }
  },
  methods: {
    scroll_track: function (e) {
      this.status_select = Math.round(e.target.scrollLeft/e.target.clientWidth);
    }
  },
  computed: {
    ...mapState([
        'userObject'
    ])
  }
};
</script>
