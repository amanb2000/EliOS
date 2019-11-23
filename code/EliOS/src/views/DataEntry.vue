<template>
  <div class="data-entry">
    <!-- Top Tray -->
    <router-link class='e-bar' to="/home">
        <div id='welcome-text'>Return to Home</div>
    </router-link>
    <!-- Middle Interactive Section -->
    <div class='e-form-previous' @click='jumpPrev'>Meow
    </div>
    <div v-on:scroll="placePrevious" class='e-form-container'>
        <question prompt="How was your mood today overall?" type="likhert" v-model="mood"></question>
        <question prompt="How much did your moood vary over today?" type="slider" min=1 max=17 v-model="moodVar"></question>
        <question prompt="How much sleep did you get?" type="slider" min=0 max=24 v-model="sleep"></question>
        <question prompt="How many calories (roughly) did you consume today?" type="slider" v-model="calories" min=0 max=1700></question>
        <question prompt="How many hours did you spend exercising?" type="slider" min=0 max=12></question>
        <question prompt="How intense was this exercise?" type="slider" min=0 max=12></question>
        <question prompt="Upload the EEG from a guided meditation now if possible" type="upload"></question>
    </div>
    <div class='e-form-flow-bttn' @click="pushNext">Skip</div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import firebase from 'firebase';
import question from '@/components/Question.vue';

export default {
    name: "dataEntry", // We should get the day's data when you're here
    data: function() {
        return {
            mood: null,
            moodVar: null,
            sleep: null,
            sleepChunks: null,
            calories: null,
            postal: null,
            exerciseDuration: null,
            exerciseIntensity: null,
            selectedPrompt: 0
        }
    },
    methods: {
        submitDay: function() {
            let pather = this;
            firebase.firestore().collection('users').doc(this.userObject.user.user.uid).collection('days').doc(this.currentEpoch()+'').set({
                mood: pather.mood,
                moodVar: pather.moodVar,
                sleep: pather.sleep,
                sleepChunks: pather.sleepChunks,
                calories: pather.calories,
                postal: pather.postal,
                exerciseDuration: pather.exerciseDuration,
                exerciseIntensity: pather.exerciseIntensity
            })
            .then(function() {
                console.log('User successfully created!');
                alert('Day Successfully Saved!');
            }).catch(function(error) {
                alert('Failed to create user when interfacing with database: ' + error.message);
            })
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
        placePrevious: function(e) {
            this.selectedPrompt = Math.round(e.target.scrollTop/e.target.clientHeight);
            
        },
        jumpPrev: function() {
            var container = this.$el.querySelector(".e-form-container");
            container.scrollTop = container.scrollTop - container.clientHeight;
        },
        pushNext: function() {
            var container = this.$el.querySelector(".e-form-container");
            container.scrollTop = container.scrollTop + container.clientHeight;
        }
    },
    computed: {
        ...mapState([
            'userObject'
        ])
    },
    components: {
        'question': question
    }
};
</script>

<style>
@import "../assets/css/elios_entry.css";
</style>