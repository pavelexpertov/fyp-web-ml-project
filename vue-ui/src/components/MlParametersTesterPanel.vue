<template>
  <div>
    <el-row>
      <el-col :span="12">
        <el-form ref="form">
          <el-form-item label="Parmeters Json">
            <el-input
            type="textarea"
            :rows="7"
            placeholder="Enter a json which has keys that represent algorithm's parameters and values that are lists with different configuration values."
            v-model="paramJson">
            </el-input>
          </el-form-item>
        </el-form>
          <el-button @click="handleClick">Run</el-button>
      </el-col>
      <el-col :span="12">
        <template v-if="result">
          <h3>Best Score: {{result.result.best_score}}</h3>
          <el-table
          :data="bestParametersTable" style="width: 100%">
            <el-table-column prop="parameter" label="Parameter">
            </el-table-column>
            <el-table-column prop="value" label="Best Value">
            </el-table-column>
          </el-table>
        </template>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import * as _ from 'lodash'
export default {
  name: 'MlParametersTesterPanel',
  props: {
    datasetConfigObj: {
      type: Object,
      required: true
    },
    mlClassName: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      paramJson: '',
      result: ''
    }
  },
  computed: {
    bestParametersTable () {
      let dataList = []
      let bestParamsObj = this.result.result.best_params
      _.forOwn(bestParamsObj, function (value, key) {
        dataList.push({parameter: key, value: value})
      })
      return dataList
    }
  },
  methods: {
    handleClick () {
      let path = 'mlalgorithms/' + this.mlClassName + '/best-params'
      let paramJson = JSON.parse(this.paramJson)
      let query = {
        parameters_grid: paramJson,
        dataset_query_json: this.datasetConfigObj
      }
      this.$http.post(path, query)
        .then(response => {
          this.result = response.body
        })
        .catch(err => console.log(err))
    }
  }
}
</script>

<style>
</style>
