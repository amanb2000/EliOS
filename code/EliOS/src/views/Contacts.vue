<template>
    <div class = "contacts">
        <!-- Top Tray -->
        <div class='e-bar e-top-bar'>
            <router-link class='e-icon-bar' to='/home'><i class='material-icons-outlined'>chevron_left</i></router-link>
            <div v-resize-text="{ratio:1.4, maxFontSize:'70px', delay:100}" id='welcome-text'>Contacts</div>
            <router-link class='e-icon-bar' to='/add-contact'><i class='material-icons-outlined'>add_box</i></router-link>
        </div>
        <!-- Contacts Table -->
        <div class='e-conctacts-table'>
            <div v-bind:key="n" v-for="n in userObject.data.contacts">
                {{ n.name}}
            </div> 
            <div>

            </div>
        </div>
    </div>
</template>
<script>

import { mapState } from 'vuex';
import firebase from 'firebase';

export default {
    name: 'contacts',
    data() {
        return {}
    },
    methods: {
        contact: function (target) {
            console.log(target);
        },
        getContacts: function () {
            let pather = this;
            firebase.firestore().collection('users').doc(this.userObject.user.user.uid).collection('contacts').get().then((snapshot) => {
                console.log(snapshot);
                console.log(this.userObject.user.user.uid);
                if(snapshot.exists){
                    console.log('RECORD FOUND');
                    pather.userObject.data.contacts = snapshot.data();
                }  
                else{
                    alert('No records of user found...');
                }
            }).catch((reason) => {
                alert("Login failed when trying to read from database: " + reason);
                return;
            })
        }
    },
    computed: {
    ...mapState([
        'userObject'
    ])
  },
    mounted: function() {
    let superScope = this;
    this.$nextTick(function() {
      superScope.getContacts();
    })
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
    #welcome-text {
        font-size: 2.2rem;
    }
    .e-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .e-icon-bar {
        font-size: 6rem;
        width: auto;
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        text-decoration: none;
        margin: 0 0.4rem;
    }
    .e-icon-bar i {
        font-size: 2.5rem;
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