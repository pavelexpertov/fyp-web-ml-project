<template>
    <div>
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
