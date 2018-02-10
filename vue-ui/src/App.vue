<template>
  <div id="app">
      <el-container direction="vertical">
          <header-bar-component></header-bar-component>
          <el-container>
              <side-bar-component></side-bar-component>
              <el-main>
                <router-view/>
              </el-main>
          </el-container>
      </el-container>
  </div>
</template>

<script>
import HeaderBarComponent from './components/HeaderBarComponent'
import SideBarComponent from './components/SideBarComponent'
export default {
  name: 'App',
  components: {
    headerBarComponent: HeaderBarComponent,
    SideBarComponent: SideBarComponent
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
