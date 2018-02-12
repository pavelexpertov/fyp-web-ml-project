<template>
    <el-aside width="200px">
        <el-menu>
            <el-menu-item-group title="Dataset Settings" index="1">
                <router-link v-for="item in dataSetList" :key="item.index" :to="'dataset-config-panel/'+item.name">
                    <el-menu-item
                    :index="item.index"
                    >
                        {{item.name}}
                    </el-menu-item>
                </router-link>
                <router-link to="dataset-config-panel">
                    <el-button>
                        Add
                    </el-button>
                </router-link>
            </el-menu-item-group>
            <el-menu-item-group title="ML Algorithm Playground" index="2">
                <router-link v-for="item in mlConfigList" :key="item.index" :to="'ml-playground-panel/'+item.name">
                    <el-menu-item
                    :index="item.index"
                    >
                        {{item.name}}
                    </el-menu-item>
                </router-link>
                <router-link to="ml-playground-panel">
                    <el-button>
                        Add
                    </el-button>
                </router-link>
            </el-menu-item-group>
        </el-menu>
    </el-aside>
</template>

<script>
import * as _ from 'lodash'

export default {
  name: 'SideBarComponent',
  data () {
    return {
      nothing: 'sdf'
    }
  },
  computed: {
    dataSetList () {
      // let l = ['one', 'two', 'three']
      // this.$store.state.ml.commit('addMlConfigObj', 'new name', {name: 23234})
      // this.$store.commit('addMlConfigObj', 'new name', {name: 23234})
      let l = this.$store.getters.getDataConfigNamesList
      _.forEach(l, (value, index, collection) => { collection[index] = {name: value, index: '1-' + index} })
      return l
    },
    mlConfigList () {
      // let l = ['two', '242', '3452']
      let l = this.$store.getters.getMlConfigNameList
      _.forEach(l, (value, index, collection) => { collection[index] = { name: value, index: '2-' + index } })
      return l
    }
  }
}
</script>

<style>
</style>
