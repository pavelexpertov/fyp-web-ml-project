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
        </el-col>
        <el-col :span="16">
            <p> Here's supposed to be the chart viewer, but I am not implemented just yet</p>
        </el-col>
    </el-row>
    </div>
</template>

<script>
import DataSetConfigurationsPanel from '@/components/DataSetConfigurationsPanel'
import dataMixin from '@/mixins/data_config_mixin'

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
  methods: {
    executeQuery () {
      console.log('Implement me!!!!!')
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
    this.saveDataConfig()
    next()
    this.getDataConfig()
  }
}
</script>

<style>
</style>
