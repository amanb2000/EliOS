<template>
   <div>
        <apexchart type="radar" :options="chartOptions" :series="series"></apexchart>
   </div>
</template>

<script>
import Vue from 'vue';
import VueApexCharts from 'vue-apexcharts';
Vue.use(VueApexCharts)

Vue.component('apexchart', VueApexCharts)

export default {
    data: function() {
      return {
        series: [{
            name: 'Today',
            data: [80, 50, 30],
        }, {
            name: 'Average',
            data: [50, 30, 40],
        }
        ],
        
        chartOptions: {
          chart: {
              dropShadow: {
                  enabled: true,
                  blur: 1,
                  left: 1,
                  top: 1
              }
          },
          title: {
              text: 'EEG Scan Data'
          },
          stroke: {
              width: 1
          },
          fill: {
              opacity: 0.4
          },
          markers: {
              size: 0
          },
          labels: ['Alpha', 'Beta', 'Gamma']
        }
      }
    },
};
</script>