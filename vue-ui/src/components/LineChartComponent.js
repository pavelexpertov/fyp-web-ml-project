import {Line, mixins} from 'vue-chartjs'
const {reactiveProp} = mixins

export default {
  name: 'LineChartComponent',
  extends: Line,
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
