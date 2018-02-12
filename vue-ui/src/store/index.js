import Vue from 'vue'
import Vuex from 'vuex'
import * as _ from 'lodash'

Vue.use(Vuex)

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
      if (index !== -1) { return state.data_configs_obj_list[index].data_config_obj } else { console.log("Something's wrong in the getDataConfigObjByName") }
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

let mlConfigModule = {
  state: {
    ml_config_obj_list: []
  },
  mutations: {
    addMlConfigObj (state, passedDict) {
      state.ml_config_obj_list.push({name: passedDict.name, ml_config_obj: passedDict.config})
    },
    saveMlConfigObjByName (state, passedDict) {
      let index = _.findIndex(state.ml_configs_obj_list, {name: passedDict.name})
      if (index !== -1) { state.ml_configs_obj_list[index].data_config_obj = passedDict.config } else { console.log("Something's wrong when config was trying to be saved") }
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
      if (index !== -1) { return state.ml_config_obj_list[index] } else { console.log("Something's wrong happened in getMlConfigObjByName") }
    }
  }
}

export default new Vuex.Store({
  modules: {
    ml: mlConfigModule,
    data: dataConfigModule
  }
})
