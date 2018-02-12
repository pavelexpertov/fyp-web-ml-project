import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import DataFeatureAnalysisView from '@/views/DataFeatureAnalysisView'
import DataConfigNameFormView from '@/views/DataConfigNameFormView'
import MlPlaygroundNameFormView from '@/views/MlPlaygroundNameFormView'
import MlPlaygroundView from '@/views/MlPlaygroundView'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/dataset-config-panel',
      name: 'NewDataConfigPanel',
      component: DataConfigNameFormView
    },
    {
      path: '/dataset-config-panel/:data_config_name',
      name: 'DataConfigPanel',
      component: DataFeatureAnalysisView
    },
    {
      path: '/ml-config-panel',
      name: 'NewMlConfigPanel',
      component: MlPlaygroundNameFormView
    },
    {
      path: '/ml-config-panel/:model_name',
      name: 'MlConfigPanel',
      component: MlPlaygroundView
    }
  ]
})
