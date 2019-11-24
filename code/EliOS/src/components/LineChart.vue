<template>
   <div>
        <apexchart type="line" :options="chartOptions" :series="series"></apexchart>
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
                name: "Hours",
                data: this.chartdata
            }],
            chartOptions: {
            chart: {
                    height: 350,
                    zoom: {
                        enabled: false
                    }
                },
                dataLabels: {
                    enabled: false
                },
                stroke: {
                    curve: 'straight'
                },
                title: {
                    text: 'Amount of sleep per night',
                    align: 'left'
                },
                grid: {
                    row: {
                        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
                        opacity: 0.5
                    },
                },
                xaxis: {
                    categories: ['20/11', '21/11', '22/11', '23/11', '24/11'],
                }
            }
        }
    },
};
</script>


<style scoped>
* {
    max-width: 90vw;
}

</style>

