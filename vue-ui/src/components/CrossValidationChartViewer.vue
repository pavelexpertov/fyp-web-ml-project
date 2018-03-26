<template>
  <div>
    <el-form>
      <el-form-item label="Select this needs rewrite">
        <el-checkbox v-model="rangeValuesFlag"></el-checkbox>
      </el-form-item>
      <bar-chart-component :chartData="normalDataList" :options="options"></bar-chart-component>
    </el-form>
  </div>
</template>

<script>
import * as _ from 'lodash'
import BarChartComponent from '@/components/BarChartComponent'

export default {
  name: 'CrossValidationChartViewer',
  data () {
    return {
      options: {
        responsive: true
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
