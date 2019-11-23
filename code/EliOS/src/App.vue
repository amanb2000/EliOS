<template>
  <div id="app">
    <!-- <div id="nav"> -->
      <!-- This is how you link to other routes:  -->
      <!-- <router-link to="/">Home</router-link> | -->
      <!-- <router-link to="/about">About</router-link> -->
    <!-- </div> -->
    <!-- <img alt="EliOS Logo" src="./assets/logo.png" /> -->
    <!-- TODO: Add sexy top bar here... -->
    <router-view />
  </div>
</template>

<style>
html, body, #app {
  width: 100%;
  height: 100%;
}
#app {
  font-family: "Roboto", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: flex;
  flex-direction: column;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

@import "https://fonts.googleapis.com/icon?family=Material+Icons|Material+Icons+Outlined";
@import "https://fonts.googleapis.com/css?family=Roboto&display=swap";
@import "./assets/css/elios.css";
</style>
