<template>
    <div>
        <el-row>
        </el-row>
        <el-row>
            <ml-configurations-panel
            :mlConfigurationsObj="mlConfigObject"
            >
            </ml-configurations-panel>
        </el-row>
        <el-row>
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
    handleSelectedDatasetName () {
      this.dataConfigObject = this.$store.getters.getDataConfigObjByName(this.dataConfigName)
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
    // check for the existing ml Config
    let modelName = this.$route.params.model_name
    if (modelName) {
      let config = this.$store.getters.getMlConfigObjByName(modelName)
      let datasetName = this.$store.getters.getDataConfigNameByMlName(modelName)
      this.mlConfigObject = config
      this.mlConfigName = modelName
      this.dataConfigName = datasetName
      this.getDataConfig()
    } else {
      console.log("Something's wrong in mlplaygrnd", modelName)
    }
  },
  beforeDestroy () {
    console.log('implement me')
  },
  mixins: [mlMixin, dataMixin]
}
</script>

<style>
</style>
