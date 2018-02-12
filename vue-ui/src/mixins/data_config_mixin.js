export default {
  data () {
    return {
      dataConfigObject: '',
      dataConfigName: ''
    }
  },
  methods: {
    saveDataConfig () {
      let dict = { name: this.dataConfigName, config: this.dataConfigObject }
      this.$store.commit('saveDataConfigObjByName', dict)
    },
    getDataConfig () {
    // console.log("I am called when the router is pushed")
      let modelName = this.$route.params.data_config_name
      if (modelName) {
        this.dataConfigName = modelName
        let configObj = this.$store.getters.getDataConfigObjByName(modelName)
        this.dataConfigObject = configObj
      } else if (this.mlConfigName) {
        let configObj = this.$store.getters.getDataConfigObjByName(this.dataConfigName)
        if (configObj) { this.dataConfigObject = configObj } else { this.dataConfigObject = '' }
      } else {
        console.log("Something's wrong in data mixin's getDataConfig, unless, an empty data config object is being set. Modelname", modelName)
      }
    }
  }
}
