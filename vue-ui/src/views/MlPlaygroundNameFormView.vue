<template>
    <div>
        <h4>Enter a name for you ML configuration</h4>
        <el-input v-model="newMlConfigName" placeholder="Enter a new name for ML configuration"></el-input>
        <el-button @click="saveName">Save</el-button>
    </div>
</template>

<script>
export default {
  name: 'MlPlaygroundNameFormView',
  data () {
    return {
      newMlConfigName: ''
    }
  },
  methods: {
    saveName () {
      // Create a new empty ML config object after user enters a name
      if (this.newMlConfigName.length === 0) { this.$notify({title: 'Error', message: 'Enter a name'}); return }
      let createdFlag = this.$store.getters.isMlConfigNameExists(this.newMlConfigName)
      if (createdFlag) { this.$notify({title: 'Error', message: 'Enter another name'}); return }
      let defaultConfig = { settings_form_schema: '', settings_values: '', name: '' }
      let dict = {name: this.newMlConfigName, dataset_config_name: '', config: defaultConfig}
      this.$store.commit('addMlConfigObj', dict)
      // Setting the config object within instance
      // Move to an appended route
      this.$router.push('ml-playground-panel/' + dict.name)
    }
  }
}
</script>

<style>
</style>
