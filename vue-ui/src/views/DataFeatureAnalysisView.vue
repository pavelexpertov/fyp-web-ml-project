<template>
    <el-row>
        <el-col :span="8">
            <data-set-configurations-panel
            :datasetConfigObj="dataConfigObject"
            :showButton="true"
            >
            </data-set-configurations-panel>
        </el-col>
        <el-col :span="16">
            <p> Here's supposed to be the chart viewer, but I am not implemented just yet</p>
        </el-col>
    </el-row>
</template>

<script>
import DataSetConfigurationsPanel from '@/components/DataSetConfigurationsPanel'

export default {
  name: 'DataFeatureAnalysisView',
  data () {
    return {
      dataConfigObject: '',
      dataConfigName: ''
    }
  },
  components: {
    dataSetConfigurationsPanel: DataSetConfigurationsPanel
  },
  created () {
    // console.log("I am called when the router is pushed")
    let modelName = this.$route.params.model_name
    console.log(modelName)
    if (modelName) {
      let configObj = this.$store.getters.getDataConfigObjByName(modelName)
      this.dataConfigObject = configObj
      this.dataConfigName = modelName
    } else {
      console.log("Something's wrong", modelName)
    }
  },
  beforeDestroy () {
    let dict = { name: this.dataConfigName, config: this.dataConfigObject }
    this.$store.commit('saveDataConfigObjByName', dict)
  }
}
</script>

<style>
</style>
