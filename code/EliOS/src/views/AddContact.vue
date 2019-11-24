<template>
    <div class = "add-contact">
        <div class='e-forms-container'>
            <input type='text' placeholder='Name' class='e-form-text' v-model="new_name">
            <input type='text' placeholder='Email' class='e-form-text' v-model="new_email">
            <input type='text' placeholder='Phone Number' class='e-form-text' v-model="new_phone">
            <div class='e-form-action'> <router-link class='e-form-bttn' to="/contacts">Cancel</router-link><button class='e-form-bttn' @click="addContact">Save Contact</button></div>
        </div>
    </div>
</template>
<script>
import firebase from 'firebase';
import { mapState } from 'vuex';

export default {
    name: 'signUp',
    data() {
        return {
            contacts: null,
            new_name: "",
            new_email: '',
            new_phone: ""
        }
    },
    methods: {
        addContact: function() {
            if (this.userObject.data.contacts == undefined) {
                this.contacts = [];
            } else {
                this.contacts = this.userObject.data.contacts;
            }
            // let fullContacts = this.contacts.push({'name': this.new_name, 'email': this.new_email, 'phone': this.new_phone})
            firebase.firestore().collection('users').doc(this.userObject.user.user.uid).collection('contacts').add({
                        name: this.new_name,
                        email: this.new_email,
                        phone: this.new_phone
                    })
                    .then(function() {
                        console.log('Data saved!');
                    }).catch(function(error) {
                        console.log('Failed to create user when interfacing with database: ' + error.message);
                    });
        }
    },
    computed: {
    ...mapState([
        'userObject'
    ])
  },
}
</script>

<style scoped>
    .add-contact {
        display: flex;
        flex-direction: column;
        width: 100%;
        height: 100%;
        justify-content: center;
        align-items: center;
        background-color: #dbe0f5;
    }
    .e-form-text {
        margin: 0.5rem 0;
    }
    .e-form-action {
        display: flex;
        justify-content: space-between;
    }
    .e-form-bttn {
        text-decoration: none;
        color: black;
    }
    @import "../assets/css/elios_entry.css";
</style>