<template>
  <div class="data-entry">
    <!-- <img alt="Vue logo" src="../assets/logo.png" /> -->
    <h1>Data Entry!</h1>
    <p>This is going to be freaking lit, man!</p>

    <form @submit.prevent="submitDay()">
        <p>
            <label for="mood">Mood: </label>
            <input type="number" id="mood" v-model="mood">
        </p>
        <p>
            <label for="mood_var">Mood Variation: </label>
            <input type="number" id="mood_var" v-model="moodVar">
        </p>

        <p>
            <label for="sleep">Sleep (Hours): </label>
            <input type="number" id="sleepp" v-model="sleep">
        </p>
        <p>
            <label for="sleep_chunks">#Sleep Sessions: </label>
            <input type="number" id="sleep_chunks" v-model="sleepChunks">
        </p>

        <p>
            <label for="calories">Calories: </label>
            <input type="number" id="calories" v-model="calories">
        </p>

        <p>
            <label for="postal">Postal Code: </label>
            <input type="text" id="postal" v-model="postal">
        </p>

        <p>
            <label for="exercise_duration">Exercise Duration: </label>
            <input type="number" id="exercise_duration" v-model="exerciseDuration">
        </p>

        <p>
            <label for="exercise_intensity">Exercise Intensity: </label>
            <input type="number" id="exercise_intensity" v-model="exerciseIntensity">
        </p>

        <p>
            <label for="eeg_csv">EEG CSV: </label>
            <input type="file" id="eeg_csv">
        </p>

        <input type="submit">
    </form>

  </div>
</template>

<script>
// import { mapState, mapGetters, mapMutations, mapActions } from 'vuex';
import { mapState } from 'vuex';
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";
import firebase from 'firebase';

export default {
    name: "dataEntry", 
    data: function() {
        return {
            mood: null,
            moodVar: null,
            sleep: null,
            sleepChunks: null,
            calories: null,
            postal: null,
            exerciseDuration: null,
            exerciseIntensity: null
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
        }
    },
    computed: {
        ...mapState([
            'userObject'
        ])
    }
};
</script>
