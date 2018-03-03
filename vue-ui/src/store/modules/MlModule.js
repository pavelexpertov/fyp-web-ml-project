import * as _ from 'lodash'

let mlConfigModule = {
  state: {
    ml_config_obj_list: []
  },
  mutations: {
    addMlConfigObj (state, passedDict) {
      state.ml_config_obj_list.push({name: passedDict.name, ml_config_obj: passedDict.config, dataset_config_name: passedDict.dataset_config_name})
    },
    saveMlConfigObjByName (state, passedDict) {
      let configList = state.ml_config_obj_list
      let index = _.findIndex(configList, {name: passedDict.name})
      if (index !== -1) { configList[index].ml_config_obj = passedDict.config } else { console.log("Something's wrong when config was trying to be saved") }
    },
    saveDataConfigNameByName (state, passedDict) {
      let configList = state.ml_config_obj_list
      let index = _.findIndex(configList, {name: passedDict.ml_name})
      if (index !== -1) {
        configList[index].dataset_config_name = passedDict.data_name
      } else {
        console.log("something's wron when datasetname was trying to be saved in savedataconfignamebyname funct")
      }
    }
  },
  getters: {
    getMlConfigNameList: (state) => {
      let namesList = []
      _.forEach(state.ml_config_obj_list, function (value) {
        namesList.push(value.name)
      })
      return namesList
    },
    getMlConfigObjByName: (state) => (mlConfigName) => {
      let index = _.findIndex(state.ml_config_obj_list, {name: mlConfigName})
      if (index !== -1) { return state.ml_config_obj_list[index].ml_config_obj } else { console.log("Something's wrong happened in getMlConfigObjByName") }
    },
    getDataConfigNameByMlName: (state) => (datasetConfigName) => {
      let index = _.findIndex(state.ml_config_obj_list, {name: datasetConfigName})
      if (index !== -1) { return state.ml_config_obj_list[index].dataset_config_name } else { console.log("Something's wrong happened in getDataConfigObjByName in ml mixin") }
    }
  }
}

export default mlConfigModule
