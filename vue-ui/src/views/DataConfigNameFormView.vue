<template>
    <div>
        <h4>Enter a name for a dataset configuration</h4>
        <el-input v-model="newDataConfigName" placeholder="Enter a new name for Dataset configuration"></el-input>
        <el-button @click="saveName">Save</el-button>
    </div>
</template>

<script>
export default {
  name: 'DataConfigNameFormView',
  data () {
    return {
      newDataConfigName: ''
    }
  },
  methods: {
    saveName () {
      // Add a default dataset configuration
      if (this.newDataConfigName.length === 0) { this.$notify({title: 'Error', message: 'Enter name!'}); return }
      let createdFlag = this.$store.getters.isDataConfigNameExists(this.newDataConfigName)
      if (createdFlag) { this.$notify({title: 'Error', message: 'The name already exists. Enter a new one.'}); return }
      let defaultConfig = { store_number: 1, start_date: '2010-05-05', end_date: '2011-05-05' }
      let dict = {name: this.newDataConfigName, config: defaultConfig}
      this.$store.commit('addDataConfigObj', dict)
      // Setting the config object within instance
      this.dataConfigObject = defaultConfig
      // Move to an appended route
      this.$router.push('dataset-config-panel/' + dict.name)
    }
  }
}
</script>

<style>
</style>
