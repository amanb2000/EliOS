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
              <h2 class='e-plot-title'>Sleep</h2>
              <div class='e-chumapopa'>
                <linechart :series="sleepInfo"></linechart>
              </div>
              <br />
              <div class = "lower-content">
                <h3>Your Report: </h3>
                <p>
                  Remember to track your <b>mood</b> and <b>brain scan</b> for today!
                </p>
                <p>
                  Don't forget to check our our newest visualizations for your progress 😄
                </p>
              </div>
            </div>
            <div class='e-scroll-pane'>
              <!-- {{ lastDays }} -->
              <h2 class='e-plot-title'>Mood</h2>
              <div class='e-chumapopa'>
                <linechart :series="sleepInfo"></linechart>
              </div>
              <br />
              <div class = "lower-content">
                <h3>Your Report: </h3>
                <p>
                  Remember to track your <b>mood</b> and <b>brain scan</b> for today!
                </p>
                <p>
                  Don't forget to check our our newest visualizations for your progress 😄
                </p>
              </div>
            </div>
            <div class='e-scroll-pane'>
              <!-- {{ lastDays }} -->
              <h2 class='e-plot-title'>Brain Activity</h2>
              <div class='e-chumapopa'>
                <radarchart :series="sleepInfo"></radarchart> -->
              </div>
              
              <br />
              <div class = "lower-content">
                <h3>Your Report: </h3>
                <p>
                  Remember to track your <b>mood</b> and <b>brain scan</b> for today!
                </p>
                <p>
                  Don't forget to check our our newest visualizations for your progress 😄
                </p>
              </div>
            </div>
        </div>
        <div class='e-scroll-status'>
            <i v-bind:class="[status_select == 0 ? 'material-icons' : 'material-icons-outlined']" class='e-scroll-icon' @click='scrollDir'>brightness_1</i>
            <i v-bind:class="[status_select == 1 ? 'material-icons' : 'material-icons-outlined']" class='e-scroll-icon' @click='scrollDir'>brightness_1</i>
            <i v-bind:class="[status_select == 2 ? 'material-icons' : 'material-icons-outlined']" class='e-scroll-icon' @click='scrollDir'>brightness_1</i>
            <!-- <i class='material-icons-outlined e-scroll-icon'>brightness_1</i>
            <i class='material-icons-outlined e-scroll-icon'>brightness_1</i> -->
        </div>
    </div>
    <!-- Bottom Tray -->
    <div class='e-tray e-bar'>
        <router-link class='e-tray-bttn' to='/profile'>
            <i class='material-icons-outlined e-tray-icon'>person</i>
            <div class='e-tray-caption'>Profile</div>
        </router-link>
        <router-link class='e-tray-bttn' to="/data-entry">
            <i class='material-icons-outlined e-tray-icon'>add_box</i>
            <div class='e-tray-caption'>Track</div>
        </router-link>
        <router-link class='e-tray-bttn' to='/contacts'>
            <i class='material-icons-outlined e-tray-icon'>people_alt</i>
            <div class='e-tray-caption'>Contacts</div>
        </router-link>
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
import RadarChart from '@/components/RadarChart.vue';
import ResizeText from 'vue-resize-text';
// import grapher from '@/grapher';

export default {
  extends: Bar,
  name: "home", 
  data: function() {
    return {
      status_select: 0,
      lastDays: [],
      sleepcollection: null,
      
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

      this.sleepInfo = {
        name: "hours",
        data: sleepArry
      }

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
    "linechart": LineChart,
    "radarchart": RadarChart
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
<style>
#line-chart {
  margin: 0 auto;
}
.lower-content {
  display: flex;
  flex: 1;
  flex-direction: column;
  padding-left: 1.1rem;
  padding-right: 1.1rem;
}
.e-chumapopa {
  width: 100%;
  display: flex;
  flex: 0 1 auto;
  justify-content: center;
  align-items: center;
  /* margin-top: 1.1rem; */
}
</style>
