<template>
      <bar-chart-component :chartData="normalDataList" :options="options" :width="600" :height="300"></bar-chart-component>
</template>

<script>
import * as _ from 'lodash'
import BarChartComponent from '@/components/BarChartComponent'

export default {
  name: 'CrossValidationChartViewer',
  data () {
    return {
      options: {
        responsive: false
      },
      rangeValuesFlag: false
    }
  },
  components: {
    barChartComponent: BarChartComponent
  },
  props: {
    data: {
      type: Object,
      required: true
    }
  },
  computed: {
    normalDataList () {
      let dataset = this.data
      let labelList = []
      let valuesList = []
      _.forOwn(dataset, function (value, key) {
        labelList.push(key)
        valuesList.push(value)
      })

      let datasetObject = {
        labels: labelList,
        datasets: [
          {
            data: valuesList
          }
        ]
      }
      return datasetObject
    },
    rangedDataList () {
      return {
        labels: ['hi', 'bye', 'hello', 'rise'],
        datasets: [
          {
            data: [23, 34, 38, 45]
          // data: [{x:23, y:23}, {x:45, y:45}]
          }
        ]
      }
    }
  }
}
</script>

<style>
</style>
