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

let mlClassConfigModule = {
  state: {
    ml_class_configs_obj_list: []
  },
  mutations: {
    addMlClassConfigObj (state, passedDict) {
      if (!(passedDict.code && passedDict.class_name)) { console.log('passedDict needs to have class_name or/and code') } else { state.ml_class_configs_obj_list.push(passedDict) }
    },
    saveMlClassCode (state, passedDict) {
      if (!(passedDict.code && passedDict.class_name)) { console.log('passedDict needs to have class_name or/and code') }
      let list = state.ml_class_configs_obj_list
      let index = _.findIndex(list, passedDict.class_name)
      if (index !== -1) {
        list[index].code = passedDict.code
      } else {
        console.log("Something's wrong in saveMlClassConfgObj")
      }
    }
  },
  getters: {
    getMlClassConfigObjByName: (state) => (className) => {
      let list = state.ml_class_configs_obj_list
      let index = _.findIndex(list, {'class_name': className})
      if (index !== -1) {
        return list[index]
      } else {
        console.log('Something wrong in getMlClassConfigObjByName')
        return null
      }
    },
    getMlClassConfigObjNamesList: (state) => {
      let list = state.ml_class_configs_obj_list
      let namesList = []
      _.forEach(list, function (value) {
        namesList.push(value.class_name)
      })
    }
  }
}

export default new Vuex.Store({
  modules: {
    ml: mlConfigModule,
    data: dataConfigModule,
    mlClass: mlClassConfigModule
  }
})
