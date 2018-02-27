
<template>
    <div>
        <line-chart-component :chartData="combinedDataObjectWithTwoDatasets" :options="options">
        </line-chart-component>
    </div>
</template>

<script>
import LineChartComponent from '@/components/LineChartComponent'

export default {
  name: 'CombinedDataChartViewer',
  data () {
    return {
      options: {
        responsive: true,
        scales: {
          xAxes: [{
            type: 'time'
          }]
        }
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
    },
    selectedField1: {
      type: String,
      required: true
    },
    selectedField2: {
      type: String,
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
    },
    combinedDataObjectWithTwoDatasets () {
      let formattedDataObjectList = this.formattedDataObjectList
      let selectedFieldList = [this.selectedField1, this.selectedField2]
      let selectedDatasetObjectList = []
      let colourRgbaList = ['rgba(150, 0, 0, 0.1)', 'rgba(0, 150, 0, 0.1)']
      selectedFieldList.forEach(function (fieldName) {
        formattedDataObjectList.forEach(function (dataObject) {
          let datasetObject = dataObject.datasets[0]
          if (datasetObject.label === fieldName) {
            datasetObject.backgroundColor = colourRgbaList.pop()
            selectedDatasetObjectList.push(datasetObject)
          }
        })
      })
      let dataObject = {
        datasets: selectedDatasetObjectList
      }
      return dataObject
    }
  },
  components: {
    lineChartComponent: LineChartComponent
  }
}
</script>

<style>
</style>
