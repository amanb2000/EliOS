<script>
import { Line, mixins } from 'vue-chartjs';
const { reactiveProp } = mixins

export default {
    extends: Line,
    mixins: [reactiveProp],
    props: ['chartdata', 'options'],
    mounted() {
        this.renderChart(this.chartdata, this.options, {responsive: true});
    }
}

</script>

<style scoped>
* {
    max-width: 90vw;
}

</style>