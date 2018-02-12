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
    },
    saveDataAndMlConfig () {
      this.saveMlConfig()
      this.saveDataConfig()
    },
    getDataAndMlConfig () {
      this.getMlConfig()
      this.getDataConfig()
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
