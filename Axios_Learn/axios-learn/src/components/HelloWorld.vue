<template>
  <div class="hello">
    <p>Weather: {{ info.data.weather[0].main }}</p>
    <p>Other weather: {{ info.data.weather[0].description }}</p>
    <p>Temperature: {{ info.data.main.temp }}</p>
    <p>Clouds: {{ info.data.clouds.all }}</p>
    <p>Sunset - Sunrise: {{ info.data.sys.sunset - info.data.sys.sunrise }}</p>

  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: "HelloWorld",
  data: function() {
    return {
      info: null
    }
  },
  mounted () {
    axios
      .get('http://api.openweathermap.org/data/2.5/weather?q='+'Toronto'+'&?units=metric&APPID='+'39718834535fb8fff8e625fd17ca5556')
      .then(response => (this.info = response))
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
