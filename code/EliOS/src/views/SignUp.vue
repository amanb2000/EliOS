<template>
    <div class = "sign-up">
        <p>Welcome! Create your new new account:</p>
        <input type="text" placeholder="First Name" v-model="fname"><br />
        <input type="text" placeholder="Last Name" v-model="lname"><br />
        <input type="text" placeholder="Email" v-model="email"><br>
        <input type="password" placeholder="Password" v-model="password"><br>
        <button @click="signup">Sign Up</button>
        <span>Or <router-link to="/login">back to login.</router-link></span>
    </div>
</template>

<script>
import firebase from 'firebase';

export default {
    name: 'signUp',
    data() {
        return {
            fname: '',
            lname: '',
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
                        email: pather.email
                        // add Gender, DOB, etc.
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
        }
    },
}
</script>

<style scoped>
    .signup {
        margin-top: 40px;
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