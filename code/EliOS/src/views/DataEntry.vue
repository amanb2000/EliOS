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
        <question prompt="How was your mood today overall?" type="likhert" v-model="mood" @change="submitDay"></question>
        <question prompt="How much did your moood vary over today?" type="slider" min=1 max=17 v-model="moodVar" @change="submitDay"></question>
        <question prompt="How much sleep did you get?" type="slider" min=0 max=24 v-model="sleep" @change="submitDay"></question>
        <question prompt="How many calories (roughly) did you consume today?" type="slider" v-model="calories" min=0 max=1700 @change="submitDay"></question>
        <question prompt="How many hours did you spend exercising?" type="slider" v-model="exerciseDuration" min=0 max=12 @change="submitDay"></question>
        <question prompt="How intense was this exercise?" type="slider" v-model="exerciseIntensity" min=0 max=12 @change="submitDay"></question>
        <question prompt="Upload the EEG from a guided meditation now if possible" type="upload"></question>
    </div>
    <div class='e-form-flow-bttn' @click="pushNext">Skip</div>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import firebase from 'firebase';
import question from '@/components/Question.vue';
import axios from 'axios';

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
            selectedPrompt: 0,
            weather: {
                main: null,
                description: null,
                temperature: null,
                clouds: null,
                sunTime: null
            }
        }
    },
    methods: {
        submitDay: function() {
            console.log("Attempting to submit...")
            let pather = this;

            if(this.weather.main == null){
                axios
                .get('http://api.openweathermap.org/data/2.5/weather?q='+'Toronto'+'&?units=metric&APPID='+'39718834535fb8fff8e625fd17ca5556')
                .then(function(response) {
                    console.log('Received weather response: ');
                    console.log(response.data.weather[0].main);
                    pather.weather.main = response.data.weather[0].main;
                    pather.weather.description = response.data.weather[0].description;
                    pather.weather.temperature = response.data.main.temp;
                    pather.weather.clouds = response.data.clouds.all;
                    pather.weather.sunTime = response.data.sys.sunset - response.data.sys.sunrise;

                    firebase.firestore().collection('users').doc(pather.userObject.user.user.uid).collection('days').doc(pather.currentEpoch()+'').set({
                        mood: pather.mood,
                        moodVar: pather.moodVar,
                        sleep: pather.sleep,
                        sleepChunks: pather.sleepChunks,
                        calories: pather.calories,
                        postal: pather.postal,
                        exerciseDuration: pather.exerciseDuration,
                        exerciseIntensity: pather.exerciseIntensity,
                        weather: pather.weather
                    })
                    .then(function() {
                        console.log('Day successfully saved!');
                        return;
                    }).catch(function(error) {
                        console.log('Failed to create user when interfacing with database: ' + error.message);
                        return;
                    });
                })
                .catch(function(err) {
                    console.log('Weather API Error: ' + err.message);
                    firebase.firestore().collection('users').doc(pather.userObject.user.user.uid).collection('days').doc(pather.currentEpoch()+'').set({
                        mood: pather.mood,
                        moodVar: pather.moodVar,
                        sleep: pather.sleep,
                        sleepChunks: pather.sleepChunks,
                        calories: pather.calories,
                        postal: pather.postal,
                        exerciseDuration: pather.exerciseDuration,
                        exerciseIntensity: pather.exerciseIntensity,
                        weather: pather.weather
                    })
                    .then(function() {
                        console.log('Day saved without weather!');
                    }).catch(function(error) {
                        console.log('Failed to create user when interfacing with database: ' + error.message);
                    })
                });
            }

            else {
                firebase.firestore().collection('users').doc(this.userObject.user.user.uid).collection('days').doc(this.currentEpoch()+'').set({
                    mood: pather.mood,
                    moodVar: pather.moodVar,
                    sleep: pather.sleep,
                    sleepChunks: pather.sleepChunks,
                    calories: pather.calories,
                    postal: pather.postal,
                    exerciseDuration: pather.exerciseDuration,
                    exerciseIntensity: pather.exerciseIntensity,
                    weather: pather.weather
                })
                .then(function() {
                    console.log('Day successfully saved!');
                }).catch(function(error) {
                    console.log('Failed to create user when interfacing with database: ' + error.message);
                })
            }
            

            
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
        },
        // getDay: function() {
        //     let pather = this;
        //     while(!this){
        //         console.log('Waiting...');
        //     }
        //     // Checking if we have started to populate this object...
        //     firebase.firestore().collection('users').doc(pather.user.user.uid).collection('days').doc(this.currentEpoch() + '').get().then((snapshot) => {
        //         console.log(snapshot);
        //         if(snapshot.exists){
        //             console.log('Today\'s Information has been started!');
        //             this.mood = snapshot.data().mood;
        //             this.moodVar = snapshot.data().moodVar;
        //             this.sleep = snapshot.data().sleep;
        //             this.sleepChunks = snapshot.data().sleepChunks;
        //             this.calories = snapshot.data().calories;
        //             this.postal = snapshot.data().postal;
        //             this.exerciseDuration = snapshot.data().exerciseDuration;
        //             this.exerciseIntensity = snapshot.data().exerciseIntensity;
        //             this.weather = snapshot.data().weather;
        //             this.selectedPrompt = 0;
        //         }  
        //         else{
        //             alert('Today\'s information has not been started!');
        //             axios
        //             .get('http://api.openweathermap.org/data/2.5/weather?q='+'Toronto'+'&?units=metric&APPID='+'39718834535fb8fff8e625fd17ca5556')
        //             .then(function(response) {
        //                 this.weather.main = response.data.weather[0].main;
        //                 this.weather.description = response.data.weather[0].description;
        //                 this.weather.temperature = response.data.main.temp;
        //                 this.weather.clouds = response.data.clouds.all;
        //                 this.weather.sunTime = response.data.sys.sunset - response.dataa.sys.sunrise;
        //             });

        //             // weather: {
        //             //     main: null,
        //             //     description: null,
        //             //     temperature: null,
        //             //     clouds: null,
        //             //     sunTime: null
        //             // }
        //                 // <p>Weather: {{ info.data.weather[0].main }}</p>
        //                 // <p>Other weather: {{ info.data.weather[0].description }}</p>
        //                 // <p>Temperature: {{ info.data.main.temp }}</p>
        //                 // <p>Clouds: {{ info.data.clouds.all }}</p>
        //                 // <p>Sunset - Sunrise: {{ info.data.sys.sunset - info.data.sys.sunrise }}</p>
        //         }
        //     }).catch((reason) => {
        //         alert("Login failed when trying to read from database: " + reason);
        //         return;
        //     })
        //     axios
        //     .get('http://api.openweathermap.org/data/2.5/weather?q='+'Toronto'+'&?units=metric&APPID='+'39718834535fb8fff8e625fd17ca5556')
        //     .then(response => (this.weather = response))
        // }

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