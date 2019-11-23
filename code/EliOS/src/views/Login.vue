<template>
    <div class = "login">
        <h3>Sign In</h3>
        <input type="text" placeholder="Email" v-model="email"><br>
        <input type="password" placeholder="Password" v-model="password"><br>
        <button @click="login">Connection</button>
        <br />
        <span class="red">{{ err }}</span>
        <p>Don't have an account? You can <router-link to="/sign-up">create one!</router-link></p>
    </div>
</template>

<script>
import firebase from 'firebase';

export default {
    name: 'login',
    data() {
        return {
            email: '',
            password: '',
            err: ''
        };
    },
    methods: {
        login: function() {
            this.err = '';
            let pather = this;
            
            firebase.auth().signInWithEmailAndPassword(this.email, this.password).then(
                function(user) {
                    // alert('You have logged in!');
                    console.log(user);
                    pather.$router.replace('home');
                },
                function(err) {
                    pather.err = ('Error in logging in: ' + err.message);
                }
            )
        }
    }
}
</script>

<style scoped>
    .login {
        margin-top: 40px;
    }
    input {
        margin: 10px 0;
        width: 20%;
        padding: 15px;
    }
    button {
        margin-top: 20px;
        width: 10%;
        cursor: pointer;
    }
    p {
        margin-top: 40px;
        font-size: 13px;
    }
    p a {
        text-decoration: underline;
        cursor: pointer;
    }
    .red {
        color: red;
    }
</style>