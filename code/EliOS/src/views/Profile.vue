<template>
    <div class = "profile">
        <!-- Middle Interactive Section -->
        <!-- <div class='e-form-previous' @click='jumpPrev'>Meow
        </div> -->
        <div class="e-update-form">
            First Name:<input type="text" class="e-form-text">
            Last Name:<input type="text" class="e-form-text">
            Postal Code:<input type="text"  class="e-form-text">
            Gender:<div>
                        <label>Male<input type='radio' name='gender' value='male' v-model="gender"><i class='material-icons'></i></label>
                        <label>Female<input type='radio' name='gender' value='female' v-model="gender"><i class='material-icons'></i></label>
                        <label>Other<input type='radio' name='gender' value='other' v-model="gender"><i class='material-icons'></i></label>
                    </div>
            Diagnosis:<select class='e-form-dropdown' v-model="diagnosis_sec">
                        <option>Bipolar I</option>
                        <option>Bipolar II</option>
                        <option>Major Depression</option>
                        <option>Moderate Depression</option>
                        <option>Dysthemia</option>
                        <option>Seasonal Affective Disorder</option>
                        <option>Other</option>
                    </select>
            
            Date of Birth:<input type="date" class="e-form-date">

            <div class='e-form'>
                <div class='e-form-response complete-cont'>
                    <button class='e-form-bttn complete' @click="profile">Update Profile</button>
                </div>
            </div>
        </div>
        <!-- <button @click="signup">Sign Up</button> -->
        <!-- <span>Or <router-link to="/login">back to login.</router-link></span> -->
    </div>
</template>
<script>
// import firebase from 'firebase';

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
        pushNext: function() {
            var container = this.$el.querySelector(".e-form-container");
            container.scrollTop = container.scrollTop + container.clientHeight;
        }
    }
}
</script>

<style scoped>
    .sign-up {
        display: flex;
        flex-direction: column;
        width: 100%;
        height: 100%;
        justify-content: center;
        align-items: center;
        background-color: #dbe0f5;
    }
    input {
        margin: 10px 0;
        width: 20%;
        padding: 15px;
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
        display: block;
        height: auto;
        width: auto;
        font-size: 1.2rem;
        text-decoration: none;
        color: black;
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
    .e-update-form {
        display: block;
        height: 100%;
        width: 100%;
        margin: auto;
    }
    @import "../assets/css/elios_entry.css";
</style>