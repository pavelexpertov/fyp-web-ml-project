<template>
    <div>
    <h2>{{dataConfigName}}</h2>
    <el-row>
        <el-col :span="8">
            <p>Note: each time you change properties in a dataset settings, you need to press refresh button.</p>
            <data-set-configurations-panel
            :datasetConfigObj="dataConfigObject"
            :showButton="true"
            @click="executeQuery"
            >
            </data-set-configurations-panel>
            <div>
                <el-checkbox v-model="isCombinedDatasetChartActive">Use 2 dataset combined chart</el-checkbox>
                <template v-if="isCombinedDatasetChartActive">
                    <el-form ref="form" label-width="120px">
                        <el-form-item label="DataSet 1">
                            <el-select v-model="selectedField1">
                                <el-option
                                v-for="feature in featureList1"
                                :key="feature"
                                :label="feature"
                                :value="feature"
                                >
                                </el-option>
                            </el-select>
                        </el-form-item>
                        <el-form-item label="DataSet 2">
                            <el-select v-model="selectedField2">
                                <el-option
                                v-for="feature in featureList2"
                                :key="feature"
                                :label="feature"
                                :value="feature"
                                >
                                </el-option>
                            </el-select>
                        </el-form-item>
                    </el-form>
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
  },
  computed: {
    featureList1 () {
      let selectedField = this.selectedField2
      if (this.dataConfigObject.features_list.indexOf(selectedField) === -1) {  this.selectedField2 = '' }
      return this.dataConfigObject.features_list.filter(feature => feature !== selectedField)
    },
    featureList2 () {
      let selectedField = this.selectedField1
      if (this.dataConfigObject.features_list.indexOf(selectedField) === -1) {  this.selectedField1 = '' }
      return this.dataConfigObject.features_list.filter(feature => feature !== selectedField)
    }
  }
}
</script>

<style>
</style>
