export default {
  data () {
    return {
      mlConfigObject: '',
      mlConfigName: '',
      dataConfigName: ''
    }
  },
  methods: {
    saveMlConfig () {
      let dict = { name: this.mlConfigName, config: this.mlConfigObject }
      this.$store.commit('saveMlConfigObjByName', dict)
      dict = { ml_name: this.mlConfigName, data_name: this.dataConfigName }
      this.$store.commit('saveDataConfigNameByName', dict)
    },
    getMlConfig () {
    // console.log("I am called when the router is pushed")
      let modelName = this.$route.params.model_name
      if (modelName) {
        this.mlConfigName = modelName
        let configObj = this.$store.getters.getMlConfigObjByName(modelName)
        this.mlConfigObject = configObj
        this.dataConfigName = this.$store.getters.getDataConfigNameByMlName(this.mlConfigName)
      } else {
        console.log("Something's wrong", modelName)
      }
    }
  }
}
