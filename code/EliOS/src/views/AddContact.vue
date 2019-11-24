<template>
    <div class = "add-contact">
        <div class='e-forms-container'>
            <input type='text' placeholder='Name'>
            <input type='text' placeholder='Email'>
            <input type='text' placeholder='Phone Number'>
        </div>
    </div>
</template>
<script>
import firebase from 'firebase';

export default {
    name: 'signUp',
    data() {
        return {
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
                        dob: pather.dob.valueAsNumber / 1000
                        
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
    @import "../assets/css/elios_entry.css";
</style>