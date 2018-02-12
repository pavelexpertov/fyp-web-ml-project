import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import DataFeatureAnalysisView from '@/views/DataFeatureAnalysisView'
import DataConfigNameFormView from '@/views/DataConfigNameFormView'

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
      path: '/dataset-config-panel/:model_name',
      name: 'DataConfigPanel',
      component: DataFeatureAnalysisView
    }
  ]
})
