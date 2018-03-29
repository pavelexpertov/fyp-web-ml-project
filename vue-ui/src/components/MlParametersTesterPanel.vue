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
        {{result}}
      </el-col>
    </el-row>
  </div>
</template>

<script>
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
