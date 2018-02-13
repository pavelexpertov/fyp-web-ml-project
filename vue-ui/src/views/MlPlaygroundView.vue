<template>
    <div>
        <h2>{{mlConfigName}}</h2>
        <el-row>
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
import mlMixin from '@/mixins/ml_config_mixin'
import dataMixin from '@/mixins/data_config_mixin'

export default {
  name: 'MlPlaygroundView',
  components: {
    mlConfigurationsPanel: MlConfigurationsPanel,
    dataSetConfigurationsPanel: DataSetConfigurationsPanel
  },
  methods: {
    handleBuildButtonClick () {
      let dataQueryJson = this.dataConfigObject
      let mlClassName = this.mlConfigObject.name
      let settingsJson = this.mlConfigObject.settings_values
      let jsonRequest = {
        ml_class_name: mlClassName,
        settings_json: settingsJson,
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
              console.log(response.body)
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
