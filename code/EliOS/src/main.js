import Vue from "vue";
import firebase from "firebase";
import App from "./App.vue";
import router from "./router";

Vue.config.productionTip = false;

// Your web app's Firebase configuration
var firebaseConfig = {
  apiKey: "AIzaSyDshEQ0z17UhetiA5F70BAVLeUPOIjNRjw",
  authDomain: "resolute-future-242915.firebaseapp.com",
  databaseURL: "https://resolute-future-242915.firebaseio.com",
  projectId: "resolute-future-242915",
  storageBucket: "resolute-future-242915.appspot.com",
  messagingSenderId: "721016135808",
  appId: "1:721016135808:web:c73aebaa5c7b4f5ced4665"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
