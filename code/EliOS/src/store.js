import Vue from 'vue'
import Vuex from 'vuex'
// import { removeAllListeners } from 'cluster';

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        userObject: {}
    },
    getters: {
        countLinks: function(state){
            return state.links.length;
        }
    },
    mutations: {
        POPULATE_USER: function(state, data) {
            console.log('Stored user data')
            state.userObject = data;
        },
    },
    actions: { // This is where you put async operations
        
    }
});