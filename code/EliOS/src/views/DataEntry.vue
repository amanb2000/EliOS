<template>
  <div class="data-entry">
    <!-- Top Tray -->
    <router-link class='e-bar' to="/home">
        <div v-resize-text="{ratio:1.3, delay:100}" id='welcome-text'>Return to Home</div>
    </router-link>
    <div v-on:scroll="placePrevious" class='e-form-container'>
        <question prompt="How was your mood today overall?" type="likhert" v-model="mood" @change="submitDay"></question>
        <question prompt="How much did your moood vary over today?" type="slider" min=1 max=17 v-model="moodVar" @change="submitDay"></question>
        <question prompt="How much sleep did you get?" type="slider" min=0 max=24 v-model="sleep" @change="submitDay"></question>
        <question prompt="How many calories (roughly) did you consume today?" type="slider" v-model="calories" min=0 max=1700 @change="submitDay"></question>
        <question prompt="How many hours did you spend exercising?" type="slider" v-model="exerciseDuration" min=0 max=12 @change="submitDay"></question>
        <question prompt="How intense was this exercise?" type="slider" v-model="exerciseIntensity" min=0 max=12 @change="submitDay"></question>
        
        <div class = "e-form">
            <div class = "e-form-question">Upload your Meditation  :</div>
            <div class = "e-form-response">
                <input type="file" @change="previewCSV" >
                <p>Progress: {{uploadValue.toFixed()+"%"}}
                <progress id="progress" :value="uploadValue" max="100" ></progress>  </p>
                <button @click="onUpload">Upload</button>
            </div>
        </div>
    </div>
    <div v-show="(selectedPrompt != 6)" v-bind:class="[([mood, moodVar, sleep, calories, exerciseDuration, exerciseIntensity][selectedPrompt] == null) ? 'e-form-flow-skip' : 'e-form-flow-next']" class='e-form-flow-bttn' @click="pushNext"></div>
    <router-link v-show="(selectedPrompt == 6)" v-bind:class="[([mood, moodVar, sleep, calories, exerciseDuration, exerciseIntensity][selectedPrompt] == null) ? 'e-form-flow-skip' : 'e-form-flow-next']" class='e-form-flow-bttn' to="/home"></router-link>
  </div>
</template>

<script>
import { mapState } from 'vuex';
import firebase from 'firebase';
import question from '@/components/Question.vue';
import axios from 'axios';
import ResizeText from 'vue-resize-text';

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
            },

            uploadValue: 0,
            eegCSV: null,
            metaData: null,
        }
    },
    methods: {
        previewCSV: function(event) {
            console.log('h');
            this.uploadValue = 0;
            this.eegCSV = null;
            this.metaData = event.target.files[0];
        },

        onUpload: function(){
            this.eegCSV=null;
            let pather = this;
            const storageRef=firebase.storage().ref(`${this.metaData.name}`).put(this.metaData);

            storageRef.on(`state_changed`,snapshot=>{
                pather.uploadValue = (snapshot.bytesTransferred/snapshot.totalBytes)*100;
            }, error=>{console.log(error.message)},
            ()=>{pather.uploadValue=100;
                storageRef.snapshot.ref.getDownloadURL().then((url)=>{
                    // this.picture =url;
                    // Populate logic to save location of this file!
                    console.log('URL: ' + url);
                    firebase.firestore().collection('users').doc(pather.userObject.user.user.uid).collection('days').doc(pather.currentEpoch()+'').update({
                        'EEG_URL': url,
                    }).then(function() {
                        console.log('Successfully uploaded CSV and saved URL in Database!')
                    }).catch(function(error) {
                        console.log('Could not save URL of EEG CSV after uploading it to the storage system: ' + error.message);
                    });

                });
            }
            );
        },

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
                        weather: pather.weather,
                        epoch: pather.currentEpoch()
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
                        weather: pather.weather,
                        epoch: pather.currentEpoch()
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
                    weather: pather.weather,
                    epoch: pather.currentEpoch()
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
            let daysPast = 2;
            return(epoch-(86400*daysPast));
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
    },
    computed: {
        ...mapState([
            'userObject'
        ])
    },
    components: {
        'question': question
    },
    directives: {
        ResizeText
    }
};
</script>

<style scoped>
@import "../assets/css/elios_entry.css";
</style>