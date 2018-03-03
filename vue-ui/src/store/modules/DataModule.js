import * as _ from 'lodash'

let dataConfigModule = {
  state: {
    data_configs_obj_list: []
  },
  mutations: {
    addDataConfigObj (state, passedDict) {
      state.data_configs_obj_list.push({name: passedDict.name, data_config_obj: passedDict.config})
    },
    saveDataConfigObjByName (state, passedDict) {
      let index = _.findIndex(state.data_configs_obj_list, {name: passedDict.name})
      if (index !== -1) { state.data_configs_obj_list[index].data_config_obj = passedDict.config } else { console.log("Something's wrong when config was trying to be saved") }
    }
  },
  getters: {
    getDataConfigObjByName: (state) => (configObjName) => {
      let index = _.findIndex(state.data_configs_obj_list, {'name': configObjName})
      if (index !== -1) { return state.data_configs_obj_list[index].data_config_obj } else { return null }
    },
    getDataConfigNamesList: (state) => {
      let namesList = []
      _.forEach(state.data_configs_obj_list, function (value) {
        namesList.push(value.name)
      })
      return namesList
    }
  }
}

export default dataConfigModule
