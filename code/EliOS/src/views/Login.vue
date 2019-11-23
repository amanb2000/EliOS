<template>
    <div class = "login">
        <div class='signin-center'>
            <h1>Sign In</h1>
            <input type="text" placeholder="Email" class='e-form-text' v-model="email"><br>
            <input type="password" placeholder="Password" class='e-form-text' v-model="password"><br>
            <button @click="login" class='e-form-bttn'>Sign In</button>
            <br />
            <span class="red">{{ err }}</span>
            <p>Don't have an account? You can <router-link to="/sign-up">create one!</router-link></p>
        </div>
    </div>
</template>

<script>
import firebase from 'firebase';
import { mapMutations } from 'vuex';

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
        ...mapMutations([
            'POPULATE_USER'
        ]),
        populateUser: function(data) {
            console.log(data);
            this.POPULATE_USER(data);
            this.$router.push({name: 'home'});
        },
        login: function() {
            this.err = '';
            let pather = this;
            
            firebase.auth().signInWithEmailAndPassword(this.email, this.password).then(
                function(user) {
                    // alert('You have logged in!');
                    console.log(user);
                    firebase.firestore().collection('users').doc(user.user.uid).get().then((snapshot) => {
                        console.log(snapshot);
                        if(snapshot.exists){
                            console.log('RECORD FOUND: User is ');
                            pather.populateUser({data: snapshot.data(), user: user});
                        }  
                        else{
                            alert('No record of user found...')
                        }
                    }).catch((reason) => {
                        alert("Login failed when trying to read from database: " + reason);
                        return;
                    })

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
        display: flex;
        flex-direction: column;
        width: 100%;
        height: 100%;
        justify-content: center;
        align-items: center;
         background-color: #cad4f8;
    }
    .signin-center {
        display: flex;
        flex-direction: column;
        width: 100%;
        justify-content: center;
        align-items: center;
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
    @import "../assets/css/elios_entry.css";
</style>