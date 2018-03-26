<template>
  <div>
    <h2>Cross validation panel</h2>
    <el-row>
      <el-col :span="8">
        <el-form ref="form" label-width="120px">
          <el-form-item label="Number Of Runs">
            <el-input-number v-model="numberOfRuns"></el-input-number>
          </el-form-item>
          <el-form-item label="Split Percentage">
            <el-input-number v-model="percOfSplit"></el-input-number>
          </el-form-item>
        <el-button type="primary" @click="handleClick">
            Cross-Validate
        </el-button>
        </el-form>
      </el-col>
      <el-col :span="16">
        <cross-validation-chart-viewer
        v-if="result"
        :data="result.score"
        >
        </cross-validation-chart-viewer>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import CrossValidationChartViewer from '@/components/CrossValidationChartViewer'
export default {
  name: 'MlCrossValidationPanel',
  props: {
    dataConfigObject: {
      type: Object,
      required: true
    },
    mlConfigObject: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      numberOfRuns: 10,
      percOfSplit: 0.70,
      result: ''
    }
  },
  methods: {
    handleClick () {
      let mlConfigObject = this.mlConfigObject
      let path = 'mlalgorithms/' + mlConfigObject.name + '/score'
      let query = {
        settings_json: mlConfigObject.settings_values,
        dataset_query_json: this.dataConfigObject,
        number_or_runs: this.numberOfRuns,
        perc_of_split: this.percOfSplit
      }
      this.$http.post(path, query)
        .then(response => {
          this.result = response.body
        })
        .catch(err => console.log('OHHHHH SOMETHING GOT WRONG:\n', err))
    }
  },
  components: {
    crossValidationChartViewer: CrossValidationChartViewer
  }
}
</script>

<style>
</style>
