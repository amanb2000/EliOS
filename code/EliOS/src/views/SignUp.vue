<template>
    <div class = "sign-up">
        <p>Welcome! Create your new new account:</p>
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
            email: '',
            password: ''
        }
    },
    methods: {
        signup: function() {
            firebase.auth().createUserWithEmailAndPassword(this.email, this.password).then(
                function(user){
                    alert('Account was created!')
                    console.log(user);
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