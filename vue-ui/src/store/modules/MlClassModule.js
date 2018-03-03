import * as _ from 'lodash'

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
      let index = _.findIndex(list, {class_name: passedDict.class_name})
      if (index !== -1) {
        list[index].code = passedDict.code
      } else {
        console.log("Something's wrong in saveMlClassCode")
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
      return namesList
    }
  }
}

export default mlClassConfigModule
