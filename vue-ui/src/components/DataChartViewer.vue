<template>
    <div>
        <div v-for="dataObject in formattedDataObjectList" v-bind:key="dataObject.datasets[0].label">
            <line-chart-component :chartData="dataObject" :options="options" :key="dataObject.datasets[0].label + 2">
            </line-chart-component>
        </div>
    </div>
</template>

<script>
// import * as _ from 'lodash'
import * as moment from 'moment'
import LineChartComponent from '@/components/LineChartComponent'

export default {
  name: 'DataChartViewer',
  data () {
    return {
      options: {
        responsive: true
      }
    }
  },
  props: {
    dataSetList: {
      type: Array,
      required: true
    },
    queryList: {
      type: Array,
      required: true
    }
  },
  computed: {
    formattedDataObjectList () {
      const weeklyDateFieldKeyword = 'Date'
      let dataSetList = this.dataSetList
      let dataObjectList = []
      this.queryList.forEach(function (fieldName) {
        let formattedDatasetDataPropertyList = []
        dataSetList.forEach(function (dataElement) {
          let datasetObj = {
            //t: moment(dataElement[weeklyDateFieldKeyword]),
            t: dataElement[weeklyDateFieldKeyword],
            y: dataElement[fieldName]
          }
          formattedDatasetDataPropertyList.push(datasetObj)
        })
        let dataObject = {
          datasets: [
            {
              label: fieldName,
              data: formattedDatasetDataPropertyList
            }
          ]
        }
        dataObjectList.push(dataObject)
      })
      return dataObjectList
    }
  },
  components: {
    lineChartComponent: LineChartComponent
  }
}
</script>

<style>
</style>
