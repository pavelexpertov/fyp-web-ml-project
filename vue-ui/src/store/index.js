import Vue from 'vue'
import Vuex from 'vuex'
import mlConfigModule from '@/store/modules/MlModule'
import dataConfigModule from '@/store/modules/DataModule'
import mlClassConfigModule from '@/store/modules/MlClassModule'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    ml: mlConfigModule,
    data: dataConfigModule,
    mlClass: mlClassConfigModule
  }
})
