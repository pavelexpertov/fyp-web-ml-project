import {Bar, mixins} from 'vue-chartjs'
const {reactiveProp} = mixins

export default {
  name: 'BarChartComponent',
  extends: Bar,
  data () {
    return { }
  },
  props: {
    options: {
      type: Object,
      required: true
    }
  },
  mixins: [reactiveProp],
  mounted () {
    this.renderChart(this.chartData, this.options)
  }
}
