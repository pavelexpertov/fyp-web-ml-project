<template>
    <el-aside width="200px">
        <el-menu>
            <el-menu-item-group title="Dataset Settings" index="1">
                <el-menu-item index="1-1">
                    Item 1
                </el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="ML Algorithm Playground" index="2">
                <el-menu-item index="2-1">
                    Item 2
                </el-menu-item>
            </el-menu-item-group>
        </el-menu>
    </el-aside>
</template>

<script>
export default {
  name: 'SideBarComponent',
  data () {
    return {
      nothing: 'sdf'
    }
  }
}
</script>

<style>
</style>
