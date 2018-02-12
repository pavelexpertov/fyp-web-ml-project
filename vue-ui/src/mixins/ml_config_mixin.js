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
    },
    getMlConfig () {
    // console.log("I am called when the router is pushed")
      let modelName = this.$route.params.model_name
      this.mlConfigName = modelName
      if (modelName) {
        let configObj = this.$store.getters.getMlConfigObjByName(modelName)
        this.mlConfigObject = configObj
      } else {
        console.log("Something's wrong", modelName)
      }
    }
  }
}
