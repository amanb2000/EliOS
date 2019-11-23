import Vue from 'vue'
import Vuex from 'vuex'
// import { removeAllListeners } from 'cluster';

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        title: 'My Custom VUEX Title',
        links: [
            'http://google.com',
            'deepthink.io',
            'caretrack.io'
        ]
    },
    getters: {
        countLinks: function(state){
            return state.links.length;
        }
    },
    mutations: {
        ADD_LINK: function(state, link) {
            state.links.push(link);
        },
        REMOVE_LINK: function(state, link) {
            state.links.splice(link, 1);
        },
        REMOVE_ALL: function(state) {
            state.links = [];
        }
    },
    actions: { // This is where you put async operations
        removeLink: function(context, link) {
            context.commit("REMOVE_LINK", link);
        },
        removeAll({commit}) {
            return new Promise((resolve) => {
                setTimeout(() => {
                    commit('REMOVE_ALL')
                    resolve()
                }, 1500);
            });
        }
    }
});