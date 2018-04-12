<template>
<div>
    <h4>Enter a name for your class</h4>
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
      if (!this.mlClassName) { this.$notify({title: 'Error', message: 'Name must be entered'}); return }
      if (this.mlClassName.length < 3) { this.$notify({title: 'Error', message: 'Name must be a bit longer'}); return }
      const className = this.appendMLextension(this.mlClassName)
      let createdFlag = this.$store.getters.isMlClassConfigNameExists(className)
      if (createdFlag) { this.$notify({title: 'Error', message: 'Enter another name'}); return }
      const initialCode = `
# Pretend that the imoprt statement is already executed: import sklearn

class ${className}(AbstractMlClass):
    def __init__(self, name, settings_json=''):
        '''Default constructor: the conditions must be the same to accomodate for default and
        optional settings of the algorithm'''
        if settings_json:
            super().__init__(name, sklearn.NameOfTheAlgorithmConstructor(**settings_json))
        else:
            super().__init__(name, sklearn.NameOfTheAlgorithmConstructor())
`
      let mlClassObj = {class_name: className, code: initialCode}
      this.$store.commit('addMlClassConfigObj', mlClassObj)
      this.$router.push('ml-class-editor/' + className)
    },
    appendMLextension (className) {
      let extension = className.slice(-2)
      if (extension !== 'ML') { return className + 'ML' } else { return className }
    }
  }
}
</script>

<style>
</style>
