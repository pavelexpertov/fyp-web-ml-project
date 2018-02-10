<template>
    <el-select v-model="selectedAlgorithm">
        <el-option
        v-for="algorithm_obj in mlAlgorithmList"
        :key="algorithm_obj.name"
        :label="algorithm_obj.name"
        :value="algorithm_obj"
        @change="handleSelectedItem"
        >
        </el-option>
    </el-select>
</template>

<script>
// import _ from 'lodash'
// import * as _ from 'lodash'

export default {
  name: 'MlAlgorithmsDropDownList',
  props: {
    selectedAlgorithm: {
      type: Object,
      default: function () {
        return {}
      }
    }
  },
  data () {
    return {
      mlAlgorithmList: []
    }
  },
  methods: {
    handleSelectedItem: function () {
      this.$emit('selectedItem', this.selectedAlgorithm)
      /* let index = _.findIndex(this.mlAlgorithmList, {name: this.selectedAlgorithm})
            if(index !== -1){
                this.$emit("selectedItem", this.mlAlgorithmList[index])
            }
            else{
                console.log("Unfortunately, the mlalgorithm of", this.selectedAlgorithm, "couldn't be found")
            } */
      /* for(var i = 0; i < this.mlAlgorithmList.length; ++i){
            } */
    }
  },
  created: function () {
    this.$http.get('mlalgorithms')
      .then(mlAlgorithmListResponse => {
        this.mlAlgorithmList = mlAlgorithmListResponse.body
      })
  }
}
</script>

<style>
</style>
