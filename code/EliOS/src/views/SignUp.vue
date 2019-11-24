<template>
    <div class = "sign-up">
        <!-- Middle Interactive Section -->
        <div class='e-form-previous' @click='jumpPrev'>Meow
        </div>
        <div v-on:scroll="placePrevious" class='e-form-container'>
            <question prompt="First Name" type="text" v-model="fname"></question>
            <question prompt="Last Name" type="text" v-model="lname"></question>

            <question prompt="How much sleep did you get?" type="slider" min=0 max=24 v-model="sleep"></question>
            <question prompt="How many calories (roughly) did you consume today?" type="slider" v-model="calories" min=0 max=1700></question>
            <question prompt="How many hours did you spend exercising?" type="slider" v-model="exerciseDuration" min=0 max=12></question>
            <question prompt="How intense was this exercise?" type="slider" v-model="exerciseIntensity" min=0 max=12></question>
            <question prompt="Upload the EEG from a guided meditation now if possible" type="upload"></question>
            <div class='e-form'>
                <div class='e-form-input-bttn' @click="signup">Sign Up</div>
            </div>
        </div>
        <!-- <router-link class='e-form-flow-bttn'>Back to Login</router-link>
        <input type="text" placeholder="First Name" v-model="fname"><br />
        <input type="text" placeholder="Last Name" v-model="lname"><br />

        <input type="text" placeholder="Postal Code" v-model="postal"><br />
        <input type="text" placeholder="Diagnosis" v-model="diagnoses[0]"><br />
        <input type="text" placeholder="Gender" v-model="gender"><br />
        <input type="text" placeholder="Date of Birth" v-model="dob"><br />
        

        <input type="text" placeholder="Email" v-model="email"><br>
        <input type="password" placeholder="Password" v-model="password"><br>
        <button @click="signup">Sign Up</button>
        <span>Or <router-link to="/login">back to login.</router-link></span> -->
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
            diagnoses: [''],
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
        jumpPrev: function() {
            var container = this.$el.querySelector(".e-form-container");
            container.scrollTop = container.scrollTop - container.clientHeight;
        }
    },
    components: {
        'question': question
    }
}
</script>

<style scoped>
    .signup {
        /* margin-top: 40px; */
        background-color: #cad4f8;
    }
    input {
        margin: 10px 0;
        width: 20%;
        padding: 15px;
    }
    button {
        margin-top: 10px;
        width: 10%;
        cursor: pointer;
    }
    span {
        display: block;
        margin-top: 20px;
        font-size: 11px;
    }
</style>