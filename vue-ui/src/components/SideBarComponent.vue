<template>
    <el-aside width="200px">
        <el-menu>
            <el-menu-item-group title="Dataset Settings" index="1">
                <el-menu-item
                v-for="item in dataSetList"
                :key="item.name"
                :index="item.index"
                >
                {{item.name}}
                </el-menu-item>
                <el-menu-item index="add-data-button">
                    <el-button>
                        Add
                    </el-button>
                </el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="ML Algorithm Playground" index="2">
                <el-menu-item
                v-for="item in mlConfigList"
                :key="item.name"
                :index="item.index"
                >
                {{item.name}}
                </el-menu-item>
                <el-menu-item index="add-ml-button">
                    <el-button>
                        Add
                    </el-button>
                </el-menu-item>
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
      this.$store.commit('addMlConfigObj', 'new name', {name: 23234})
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
