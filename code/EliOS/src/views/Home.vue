<template>
  <div class="home">
    <!-- <img alt="Vue logo" src="../assets/logo.png" /> -->
    <h1>Welcome to EliOS!</h1>
    <h2>From Vuex:</h2>
    <div>
      {{ custom }}
      <button @click="removeAllLinks">Remove All Links</button>
    </div>
    <h2>Also From Vuex: Links! </h2>
    <ul>
      <li v-for="(link, index) in links" v-bind:key="index">
        {{ link }}
        <button @click="removeLinks(index)">remove</button>
      </li>
    </ul>
    <h2>From a Function in Vuex: </h2>
    <p>The number of links is: {{ countLinks  }} </p>
    <form @submit.prevent="addLink">
      <input type="text" placeholder="Add a Link..." v-model="newLink" />
      <input type="submit" />
      <button @click="addLinkNot()">Naughty Add!</button>
    </form>

  </div>
</template>

<script>
import { mapState, mapGetters, mapMutations, mapActions } from 'vuex';
// @ is an alias to /src
// import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "home", 
  data: function() {
    return {
      newLink: '',
    }
  },
  methods: {
    ...mapMutations([
      'ADD_LINK',
      'REMOVE_ALL'
    ]),
    ...mapActions([
      'removeLink',
      'removeAll'
    ]),

    addLink: function() {
      if(this.newLink.trim() != ''){
        this.ADD_LINK(this.newLink);
      }
      this.newLink = '';
    },
    removeLinks: function(link) {
      this.removeLink(link);
    },
    removeAllLinks: function() {
      this.removeAll().then(() => {
        alert('All links removed!');
      })
    },
    addLinkNot: function() {
      this.links.append(this.newLink);
      this.newLink = '';
      return;
    }
 
  },
  computed: {
    ...mapState({
      custom: 'title', // custom is an alias for title
      links: 'links',

    }),
    ...mapGetters([
      'countLinks'
    ]),
    
    // we can now have other properties here.
  }
};
</script>
