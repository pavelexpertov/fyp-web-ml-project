<template>
    <el-select v-model="selectedAlgorithm" @change="handleSelectedItem">

        <el-option
        v-for="algorithm_obj in mlAlgorithmList"
        :key="algorithm_obj.name"
        :label="algorithm_obj.name"
        :value="algorithm_obj.name"
        >
        </el-option>
    </el-select>
</template>

<script>
import * as _ from 'lodash'

export default {
  name: 'MlAlgorithmsDropDownList',
  props: {
    selectedAlgorithmName: {
      type: String,
      required: true,
      data: function () {
        return { selectedAlgorithm: this.selectedAlgorithmName }
      }
    }
  },
  data () {
    return {
      mlAlgorithmList: [],
      selectedAlgorithm: this.selectedAlgorithmName
    }
  },
  methods: {
    handleSelectedItem: function () {
      let mlList = this.mlAlgorithmList
      let index = _.findIndex(mlList, {name: this.selectedAlgorithm})
      if (index !== -1) {
        let mlDoc = mlList[index]
        this.$emit('selectedItem', mlDoc)
      } else { console.log('Something wrong in the mlalgorithmsdropdownlist') }
    }
  },
  created: function () {
    this.$http.get('mlalgorithms')
      .then(mlAlgorithmListResponse => {
        this.mlAlgorithmList = mlAlgorithmListResponse.body
      })
      .catch(err => {
        console.log('I think the server is not up and running')
        console.log(err)
      })
  }
}
</script>

<style>
</style>
