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
            <el-select v-model="dataConfigObject" placeholder="Select a dataconfig">
                <el-option
                v-for="data_config in datasetConfigsList"
                :key="data_config.name"
                :label="data_config.name"
                :value="data_config">
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
  computed: {
    datasetConfigsList: function () {
      // Return a list of configs for the dropdown list
      console.log('Implement me in the datasetConfigsList')
      return 'sdfsdfsdf'
    }
  },
  created: function () {
    // check for the existing ml Config
    let modelName = this.$route.params.model_name
    if (modelName) {
      console.log('Implement me!!!!!!!')
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
