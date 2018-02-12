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
      let modelName = this.$route.params.model_name
      this.dataConfigName = modelName
      console.log(modelName)
      if (modelName) {
        let configObj = this.$store.getters.getDataConfigObjByName(modelName)
        this.dataConfigObject = configObj
      } else {
        console.log("Something's wrong", modelName)
      }
    }
  }
}
