<template>
  <div class="bd-main home">
    <!-- Top Tray -->
    <div class='e-bar e-top-bar'>
        <div v-resize-text="{ratio:1, maxFontSize:'70px', delay:100}" id='welcome-text'>Welcome, {{ userObject.data.fname }}</div>
    </div>
    <!-- Middle Scroll Section -->
    <div class='e-scroll-container'>
        <div class='e-scroller' v-on:scroll="scroll_track">
            <div class='e-scroll-pane'>
              <!-- {{ lastDays }} -->
              <line-chart :chart-data="sleepcollection"></line-chart>
            </div>
            <div class='e-scroll-pane'>
                <img src='https://images.unsplash.com/photo-1529778873920-4da4926a72c2?ixlib=rb-1.2.1&w=1000&q=80'>
            </div>
        </div>
        <div class='e-scroll-status'>
            <i v-bind:class="[status_select == 0 ? 'material-icons' : 'material-icons-outlined']" class='e-scroll-icon' @click='scrollDir'>brightness_1</i>
            <i v-bind:class="[status_select == 1 ? 'material-icons' : 'material-icons-outlined']" class='e-scroll-icon' @click='scrollDir'>brightness_1</i>
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
import firebase from 'firebase';
import { Bar } from 'vue-chartjs'
import LineChart from '@/components/LineChart.vue';
import ResizeText from 'vue-resize-text';

export default {
  extends: Bar,
  name: "home", 
  data: function() {
    return {
      status_select: 0,
      lastDays: [],
      sleepcollection: null
    }
  },
  methods: {
    fillData: function() {
      let pather = this;
      let sleepArry = [];
      let labels = []
      for(let i = 0; i < pather.lastDays.length; i++){
        sleepArry.push(pather.lastDays[i].sleep);
        labels.push(i);
      }
      console.log(sleepArry);
      this.sleepcollection = {
        labels: labels,
        datasets: [
          {
            label: 'Sleep',
            backgroundColor: '#eedddd',
            data: sleepArry
          }
        ]
      }
    },
    getRandomInt: function () {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5
    },
    scroll_track: function (e) {
      this.status_select = Math.round(e.target.scrollLeft/e.target.clientWidth);
    },
    getGraphData: function() {
      this.lastDays = [];
      let pather = this;
      let today = this.currentEpoch();
      firebase.firestore().collection('users').doc(pather.userObject.user.user.uid).collection('days').where("epoch", "<=", today).get().then((snapshot) => {
        console.log(snapshot.docs[0].data());

        for(let i = 0; i < snapshot.docs.length; i++){
          console.log(snapshot.docs[i].data());
          pather.lastDays.push(snapshot.docs[i].data());
        }
        this.fillData(); // test random data
        console.log('That was a snapshot of all this users data!')
      });
    },
    currentEpoch: function() {
        var dateObj = new Date();
        var month = dateObj.getMonth()+1; //months from 1-12
        var day = dateObj.getDate();
        var year = dateObj.getFullYear();

        var epoch = this.getEpoch(year, month, day);
        return(epoch);
    },
    getEpoch: function(year, month, day) {
        var datObj = new Date(year, month-1, day, 0, 0, 0, 0);
        var epoch = datObj.getTime();
        epoch /= 1000;
        return(epoch)
    },
    scrollDir: function (e) {
      console.log(e);
    }
  },
  computed: {
    ...mapState([
        'userObject'
    ])
  },
  components: {
    LineChart
  },
  directives: {
    ResizeText
  },
  mounted: function() {
    let superScope = this;
    this.$nextTick(function() {
      superScope.getGraphData();
    })
  }

};
</script>
