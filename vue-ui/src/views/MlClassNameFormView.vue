<template>
<div>
    <h4>Enter a name for you class</h4>
    <el-input v-model="mlClassName"></el-input>
    <el-button @click="handleCreateClick">Create</el-button>
</div>
</template>

<script>
export default {
  name: 'MlClassNameFormView',
  data () {
    return {
      mlClassName: ''
    }
  },
  created () {

  },
  methods: {
    handleCreateClick () {
      const className = this.mlClassName
      const initialCode = `
import sklearn

class ${className}(AbstractMlClass):
    def __init__(self, name, settings_json=''):
        '''Default constructor: the conditions must be the same to accomodate for default and
        optional settings of the algorithm'''
        if settings_json:
            super().__init__(name, DecisionTreeRegressor(**settings_json))
        else:
            super().__init__(name, DecisionTreeRegressor())
`
      console.log(initialCode)
    }
  }
}
</script>

<style>
</style>
