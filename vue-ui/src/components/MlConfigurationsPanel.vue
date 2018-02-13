<template>
    <div>
        <ml-algorithms-drop-down-list :selectedAlgorithmName="mlConfigurationsObj.name" @selectedItem="ml_al_obj => handleSelectedItem(ml_al_obj)">
        </ml-algorithms-drop-down-list>
        <vue-form-generator :schema="mlConfigurationsObj.settings_form_schema" :model="mlConfigurationsObj.settings_values" :options="formOptions">
        </vue-form-generator>
        <el-button type="primary" @click="handleClickButton">
            {{buttonText}}
        </el-button>
    </div>
</template>

<script>
import MlAlgorithmsDropDownList from '@/components/MlAlgorithmsDropDownList'
export default {
  name: 'MlConfigurationsPanel',
  data () {
    return {
      isMlModelBuilt: false,
      formOptions: {
        validateAfterLoad: false,
        validateAfterChanged: false
      }
    }
  },
  computed: {
    mlConfigName: function () {
      return this.mlConfigurationsObj.name
    },
    buttonText: function () {
      return this.isMlModelBuilt ? 'Rebuild' : 'Build'
    }
  },
  methods: {
    handleSelectedItem: function (mlAlgorithmObj) {
      this.$emit('selectedMlAlgorithm', mlAlgorithmObj)
    },
    handleClickButton () {
      this.$emit('handleBuildButtonClick')
    }
  },
  props: {
    mlConfigurationsObj: {
      type: Object,
      required: true
    }
  },
  components: {
    mlAlgorithmsDropDownList: MlAlgorithmsDropDownList
  }
}
</script>

<style>
</style>
