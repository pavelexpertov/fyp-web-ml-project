<template>
    <div>
    <h2>{{dataConfigName}}</h2>
    <el-row>
        <el-col :span="8">
            <data-set-configurations-panel
            :datasetConfigObj="dataConfigObject"
            :showButton="true"
            @click="executeQuery"
            >
            </data-set-configurations-panel>
            <div>
                <el-checkbox v-model="isCombinedDatasetChartActive">Use 2 dataset combined chart</el-checkbox>
                <template v-if="isCombinedDatasetChartActive">
                    <el-select v-model="selectedField1">
                        <el-option
                        v-for="feature in dataConfigObject.features_list"
                        :key="feature"
                        :label="feature"
                        :value="feature"
                        >
                        </el-option>
                    </el-select>
                    <el-select v-model="selectedField2">
                        <el-option
                        v-for="feature in dataConfigObject.features_list"
                        :key="feature"
                        :label="feature"
                        :value="feature"
                        >
                        </el-option>
                    </el-select>
                </template>
            </div>
        </el-col>
        <el-col :span="16">
            <data-chart-viewer v-if="datasetList && !isCombinedDatasetChartActive" :dataSetList="datasetList" :queryList="dataConfigObject.features_list"></data-chart-viewer>
            <combined-data-chart-viewer v-else :dataSetList="datasetList" :queryList="dataConfigObject.features_list"
            :selectedField1="selectedField1" :selectedField2="selectedField2">
            </combined-data-chart-viewer>
        </el-col>
    </el-row>
    </div>
</template>

<script>
import CombinedDataChartViewer from '@/components/CombinedDataChartViewer'
import DataChartViewer from '@/components/DataChartViewer'
import DataSetConfigurationsPanel from '@/components/DataSetConfigurationsPanel'
import dataMixin from '@/mixins/data_config_mixin'

export default {
  name: 'DataFeatureAnalysisView',
  data () {
    return {
      dataConfigObject: '',
      dataConfigName: '',
      datasetList: '',
      isCombinedDatasetChartActive: false,
      selectedField1: '',
      selectedField2: ''
    }
  },
  components: {
    dataSetConfigurationsPanel: DataSetConfigurationsPanel,
    dataChartViewer: DataChartViewer,
    combinedDataChartViewer: CombinedDataChartViewer
  },
  methods: {
    executeQuery () {
      // Make a copy of the dataConfigObject
      let dataQuery = Object.assign({}, this.dataConfigObject)
      let editedFeaturesList = dataQuery.features_list.slice()
      editedFeaturesList.push('Date')
      dataQuery.features_list = editedFeaturesList
      this.$http.post('dataset', dataQuery)
        .then(response => {
          let queryResultList = response.body
          // console.log(queryResultList)
          this.datasetList = queryResultList
        })
        .catch(err => console.log(err))
    }
  },
  mixins: [dataMixin],
  created () {
    this.getDataConfig()
  },
  beforeDestroy () {
    this.saveDataConfig()
  },
  beforeRouteUpdate (to, from, next) {
    this.datasetList = ''
    this.saveDataConfig()
    next()
    this.getDataConfig()
  }
}
</script>

<style>
</style>
