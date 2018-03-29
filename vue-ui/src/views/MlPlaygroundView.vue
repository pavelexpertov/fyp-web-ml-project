<template>
    <div>
        <h2>{{mlConfigName}}</h2>
        <el-row>
          <el-tabs v-model="activeTab">
            <el-tab-pane label="Prediction" name="prediction">
              <ml-prediction-query-panel
              v-if="predictionSchemaDoc"
              :predictionSchemaDoc="predictionSchemaDoc"
              :predictedSales="predictedSales"
              @predictionQueryClick="handlePredictionQueryClick">
              </ml-prediction-query-panel>
              <template v-else>
                <h2>Prediction Panel</h2>
                <p>The model is not built</p>
              </template>
            </el-tab-pane>
            <el-tab-pane label="Cross-validation" name="cross-validation">
              <ml-cross-validation-panel
              :dataConfigObject="dataConfigObject"
              :mlConfigObject="mlConfigObject">
              </ml-cross-validation-panel>
            </el-tab-pane>
            <el-tab-pane label="Features" name="features">
              <ml-parameters-tester-panel
              :datasetConfigObj="dataConfigObject"
              :mlClassName="mlConfigObject.name">
              </ml-parameters-tester-panel>
            </el-tab-pane>
          </el-tabs>
        </el-row>
        <el-row>
            <h3>Selected Algorithm: </h3>
            <ml-configurations-panel
            :mlConfigurationsObj="mlConfigObject"
            @selectedMlAlgorithm="ml_obj => handleSelectedAlgorithm(ml_obj)"
            @handleBuildButtonClick="handleBuildButtonClick"
            >
            </ml-configurations-panel>
        </el-row>
        <el-row>
            <h3>Selected Dataset: {{dataConfigName}}</h3>
            <el-select v-model="dataConfigName" placeholder="Select a dataconfig" @change="handleSelectedDatasetName">
                <el-option
                v-for="name in datasetNamesList"
                :key="name"
                :label="name"
                :value="name">
                </el-option>
            </el-select>
            <data-set-configurations-panel
            v-if="dataConfigObject"
            :datasetConfigObj="dataConfigObject"
            :showButton="false"
            >
            </data-set-configurations-panel>
        </el-row>
    </div>
</template>

<script>
import MlConfigurationsPanel from '@/components/MlConfigurationsPanel'
import DataSetConfigurationsPanel from '@/components/DataSetConfigurationsPanel'
import MlPredictionQueryPanel from '@/components/MlPredictionQueryPanel'
import MlCrossValidationPanel from '@/components/MlCrossValidationPanel'
import MlParametersTesterPanel from '@/components/MlParametersTesterPanel'
import mlMixin from '@/mixins/ml_config_mixin'
import dataMixin from '@/mixins/data_config_mixin'
import dataObjectFormatter from '@/utils/data_obj_formatter'

export default {
  name: 'MlPlaygroundView',
  components: {
    mlConfigurationsPanel: MlConfigurationsPanel,
    dataSetConfigurationsPanel: DataSetConfigurationsPanel,
    mlPredictionQueryPanel: MlPredictionQueryPanel,
    mlCrossValidationPanel: MlCrossValidationPanel,
    mlParametersTesterPanel: MlParametersTesterPanel
  },
  data () {
    return {
      predictionSchemaDoc: '',
      predictedSales: 0,
      activeTab: 'prediction'
    }
  },
  methods: {
    handlePredictionQueryClick () {
      let queryJson = this.predictionSchemaDoc.features_values
      let modelName = this.mlConfigName
      this.$http.post('mlmodels/' + modelName + '/predictions', queryJson)
        .then(response => {
          this.predictedSales = response.body.prediction
        })
        .catch(err => console.log(err))
    },
    handleBuildButtonClick () {
      let dataQueryJson = this.dataConfigObject
      let mlClassName = this.mlConfigObject.name
      let settingsJson = this.mlConfigObject.settings_values
      let jsonRequest = {
        ml_class_name: mlClassName,
        settings_json: this.formattedMlSettingsObj,
        dataset_query_json: dataQueryJson
      }
      let modelName = this.mlConfigName
      this.$http.post('mlmodels/' + modelName, jsonRequest)
        .then(response => {
          this.$notify({
            title: 'Successfully Built',
            message: this.mlConfigName + ' is built.',
            duration: 2500
          })
          this.$http.get('mlmodels/' + modelName + '/predictions')
            .then(response => {
              this.predictionSchemaDoc = response.body
            })
            .catch(err => console.log(err))
        })
        .catch(err => console.log(err))
    },
    handleSelectedDatasetName () {
      this.dataConfigObject = this.$store.getters.getDataConfigObjByName(this.dataConfigName)
    },
    saveDataAndMlConfig () {
      this.saveMlConfig()
      this.saveDataConfig()
    },
    getDataAndMlConfig () {
      this.getMlConfig()
      this.getDataConfig()
    },
    handleSelectedAlgorithm (mlAlgorithmObj) {
      this.mlConfigObject = mlAlgorithmObj
    }
  },
  computed: {
    datasetNamesList: function () {
      // Return a list of configs for the dropdown list
      let namesList = this.$store.getters.getDataConfigNamesList
      return namesList
    },
    formattedMlSettingsObj () {
      return dataObjectFormatter(this.mlConfigObject.settings_values)
    }
  },
  created: function () {
    this.getDataAndMlConfig()
  },
  beforeDestroy () {
    this.saveDataAndMlConfig()
  },
  beforeRouteUpdate (to, from, next) {
    this.saveDataAndMlConfig()
    next()
    this.getDataAndMlConfig()
  },
  mixins: [mlMixin, dataMixin]
}
</script>

<style>
</style>
