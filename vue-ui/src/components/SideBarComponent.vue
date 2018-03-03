<template>
    <el-aside width="200px">
        <el-menu>
            <el-menu-item-group title="Dataset Settings" index="1">
                <router-link v-for="item in dataSetList" :key="item.index" :to="'/dataset-config-panel/'+item.name">
                    <el-menu-item
                    :index="item.index"
                    >
                        {{item.name}}
                    </el-menu-item>
                </router-link>
                <router-link to="/dataset-config-panel">
                    <el-button>
                        Add
                    </el-button>
                </router-link>
            </el-menu-item-group>
            <el-menu-item-group title="ML Algorithm Playground" index="2">
                <router-link v-for="item in mlConfigList" :key="item.index" :to="'/ml-playground-panel/'+item.name">
                    <el-menu-item
                    :index="item.index"
                    >
                        {{item.name}}
                    </el-menu-item>
                </router-link>
                <router-link to="/ml-playground-panel">
                    <el-button>
                        Add
                    </el-button>
                </router-link>
            </el-menu-item-group>
            <el-menu-item-group title="User ML Classes" index="3">
                <router-link v-for="item in mlClassList" :key="item.index" :to="'/ml-class-editor/'+item.name">
                    <el-menu-item
                    :index="item.index"
                    >
                    {{item.name}}
                    </el-menu-item>
                </router-link>
                <router-link to="/ml-class-editor">
                    <el-button>Add</el-button>
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
      let l = this.$store.getters.getDataConfigNamesList
      l = l.slice()
      _.forEach(l, (value, index, collection) => { collection[index] = {name: value, index: '1-' + index} })
      return l
    },
    mlConfigList () {
      let l = this.$store.getters.getMlConfigNameList
      l = l.slice()
      _.forEach(l, (value, index, collection) => { collection[index] = { name: value, index: '2-' + index } })
      return l
    },
    mlClassList () {
      let l = this.$store.getters.getMlClassConfigObjNamesList
      l = l.slice()
      _.forEach(l, (value, index, collection) => { collection[index] = { name: value, index: '3-' + index } })
      return l
    }
  }
}
</script>

<style>
</style>
