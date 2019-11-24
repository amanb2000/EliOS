<template>
    <div class = "sign-up">
        <!-- Middle Interactive Section -->
        <!-- <div class='e-form-previous' @click='jumpPrev'>Meow
        </div> -->
        <div class='e-form-container'>
            <router-link class='e-form-flow-bttn' id='return-bttn' to="/login">Cancel</router-link>
            <question prompt="First Name" type="text" v-model="fname"></question>
            <question prompt="Last Name" type="text" v-model="lname"></question>

            <question prompt="Postal Code (Weather Info)" type="text" v-model="postal"></question>
            <div class='e-form'>
                <div class='e-form-question'>What Bear is best?</div>
                <div class='e-form-response'>
                    <div class='e-form-input-text'>
                    <select class='e-form-text' v-model="diagnosis_sec">
                        <option>Bipolar I</option>
                        <option>Bipolar II</option>
                        <option>Major Depression</option>
                        <option>Moderate Depression</option>
                        <option>Dysthemia</option>
                        <option>Seasonal Affective Disorder</option>
                        <option>Order</option>
                    </select>
                    </div>
                </div>
            </div>
            <question v-show="diagnosis_sec == 'Order'" prompt="What is the other diagnosis?" type="text" v-bind:value="(diagnosis_sec != 'Order') ? diagnosis_sec : value" v-model="diagnosis"></question>
            <div class='e-form'>
                <div class='e-form-question'> Gender </div>
                <div class='e-form-response radio-stack'>
                    <label class='e-form-label'>Male<input type='radio' name='gender' value='male' class='e-form-radio' v-model="gender"><i class='material-icons'></i></label>
                    <label class='e-form-label'>Female<input type='radio' name='gender' value='female' class='e-form-radio' v-model="gender"><i class='material-icons'></i></label>
                    <label class='e-form-label'>Other<input type='radio' name='gender' value='other' class='e-form-radio' v-model="gender"><i class='material-icons'></i></label>
                </div>
            </div>
            <div class='e-form'>
                <div class='e-form-question'>Date of Birth</div>
                <div class='e-form-response'>
                    Day: <select><option></option></select><br>
                    Month: <select><option></option></select><br>
                    Year: <input type='text' class='e-form-num'>
                </div>
            </div>
            <question prompt="Date of Birth" type="date" v-model="exerciseIntensity" min=0 max=12></question>
            <question prompt="Email" type="text" v-model="email"></question>

            <div class='e-form'>
                <div class='e-form-response complete-cont'>
                    <button class='e-form-bttn complete' @click="signup">Complete Sign Up</button>
                </div>
            </div>
            <div class='e-form-flow-bttn' @click="pushNext">Next</div>
        </div>
        <!-- <button @click="signup">Sign Up</button> -->
        <!-- <span>Or <router-link to="/login">back to login.</router-link></span> -->
    </div>
</template>

<script>
import firebase from 'firebase';
import question from '@/components/Question.vue';

export default {
    name: 'signUp',
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
        signup: function() {
            let pather = this;
            firebase.auth().createUserWithEmailAndPassword(this.email, this.password).then(
                function(user){
                    
                    console.log(user);
                    firebase.firestore().collection('users').doc(user.user.uid).set({
                        fname: pather.fname,
                        lname: pather.lname,
                        email: pather.email,
                        postal: pather.postal,
                        diagnoses: pather.diagnoses,
                        gender: pather.gender,
                        dob: pather.dob
                        
                    }).then(function() {
                        console.log('User successfully created!');
                        alert('Account was created!');
                        // pather.$router.
                    }).catch(function(error) {
                        alert('Failed to create user when interfacing with database: ' + error.message);
                    })
                },
                function(err){
                    alert('Error in creating user: ' + err.message);
                }
            )
        },
        pushNext: function() {
            var container = this.$el.querySelector(".e-form-container");
            container.scrollTop = container.scrollTop + container.clientHeight;
        }
    },
    components: {
        'question': question
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
        background-color: #cad4f8;
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
    @import "../assets/css/elios_entry.css";
</style>