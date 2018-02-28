import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import DataFeatureAnalysisView from '@/views/DataFeatureAnalysisView'
import DataConfigNameFormView from '@/views/DataConfigNameFormView'
import MlPlaygroundNameFormView from '@/views/MlPlaygroundNameFormView'
import MlPlaygroundView from '@/views/MlPlaygroundView'
import MlClassEditorView from '@/views/MlClassEditorView'

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
      path: '/ml-playground-panel',
      name: 'NewMlConfigPanel',
      component: MlPlaygroundNameFormView
    },
    {
      path: '/ml-playground-panel/:model_name',
      name: 'MlConfigPanel',
      component: MlPlaygroundView
    },
    {
      path: '/mlclasseditor',
      name: 'MlClassEditor',
      component: MlClassEditorView
    }
  ]
})
