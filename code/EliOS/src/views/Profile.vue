<template>
    <div class = "profile">
        <!-- Middle Interactive Section -->
        <!-- <div class='e-form-previous' @click='jumpPrev'>Meow
        </div> -->
        <router-link class='e-form-flow-bttn' id='return-bttn' to="/home">Done</router-link>
        <div class="e-update-form">
            <input type="text" class="e-form-text" placeholder='First Name' v-model="userObject.data.fname">
            <input type="text" class="e-form-text" placeholder='Last Name' v-model="userObject.data.lname">
            Postal Code:<input type="text"  class="e-form-text">
            Gender:<div>
                        <label>Male<input type='radio' name='gender' value='male' v-model="userObject.data.gender"><i class='material-icons'></i></label>
                        <label>Female<input type='radio' name='gender' value='female' v-model="userObject.data.gender"><i class='material-icons'></i></label>
                        <label>Other<input type='radio' name='gender' value='other' v-model="userObject.data.gender"><i class='material-icons'></i></label>
                    </div>
            Diagnosis:<select class='e-form-dropdown' v-model="userObject.data.gender">
                        <option>Bipolar I</option>
                        <option>Bipolar II</option>
                        <option>Major Depression</option>
                        <option>Moderate Depression</option>
                        <option>Dysthemia</option>
                        <option>Seasonal Affective Disorder</option>
                        <option>Other</option>
                    </select>
            
            <input type="date" class="e-form-date" v-model="userObject.data.dob">

            
        </div>
        <div class='e-save-bttn'>
                <div class='e-form-response complete-cont'>
                    <button class='e-form-bttn complete' @click="profile">Update Profile</button>
                </div>
            </div>
        <!-- <button @click="signup">Sign Up</button> -->
        <!-- <span>Or <router-link to="/login">back to login.</router-link></span> -->
    </div>
</template>
<script>
import firebase from 'firebase';
import { mapState } from 'vuex';

export default {
    name: 'profile',
    data() {
        return {
            fname: '',
            lname: '',

            postal: '',
            diagnosis: '',
            diagnosis_sec: '',
            gender: '',
            dob: '',

            email: '',
            password: ''
        }
    },
    methods: {
        saveObject: function() {
            firebase();
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
    }
}
</script>

<style scoped>
    .profile {
        display: flex;
        flex-direction: column;
        width: 100%;
        height: 100%;
        justify-content: center;
        align-items: center;
        background-color: #dbe0f5;
    }
    .radio-stack {
        display: flex;
        flex-direction: column;
        flex-grow: 1;
        justify-content: center;
        align-items: flex-end;
        width: 70%;
        font-size: 2rem;
    }
    .e-form-label {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 0.5rem;
    }
    #return-bttn {
        position: absolute;
        top: 1rem;
        left: 1rem;
        display: flex;
        height: 2.2rem;
        width: auto;
        padding: 0.3rem 0.5rem;
        justify-content: flex-start;
        align-self: flex-start;
        font-size: 1.2rem;
        text-decoration: none;
        color: black;
        background-color: rgba(161,185,255,1);
    }
    .complete {
        width: 80%;
        display: flex;
        justify-content: center;
        text-align: center;
    }
    .complete-cont {
        display:flex;
        justify-content: center;
        align-items: center;
    }
    .e-save-bttn {
        display: flex;
        flex: 1 1 10%;
    }
    .e-update-form {
        display: flex;
        height: 100%;
        width: 100%;
        margin: auto;
        flex: 2 1 90%;
    }
    @import "../assets/css/elios_entry.css";
</style>