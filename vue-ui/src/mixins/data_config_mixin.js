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
      } else if (this.dataConfigName && this.mlConfigName) {
        console.log('I have been called')
        let configObj = this.$store.getters.getDataConfigObjByName(this.dataConfigName)
        this.dataConfigObject = configObj
      } else {
        console.log("Something's wrong in data mixin's getDataConfig", modelName)
      }
    }
  }
}
