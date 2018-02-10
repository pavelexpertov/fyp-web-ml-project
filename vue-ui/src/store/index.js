import Vue from 'vue'
import Vuex from 'vuex'
import * as _ from 'lodash'

Vue.use(Vuex)

let dataConfigModule = {
  state: {
    data_configs_obj_list: []
  },
  mutations: {
    addDataConfigObj (state, configName, dataConfigObj) {
      state.data_configs_obj_list.push({name: configName, data_config_obj: dataConfigObj})
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
    addMlConfigObj (state, newMlConfigName, newMlConfigObj) {
      state.ml_config_obj_list.push({name: newMlConfigName, ml_config_obj: newMlConfigObj})
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
    mlConfigModule,
    dataConfigModule
  }
})
