<template>
    <div>
        <h2>{{mlConfigurationsObj.name}}</h2>
        <ml-algorithms-drop-down-list :selectedAlgorithm="selectedMlObj" @selectedItem="ml_al_obj => handleSelectedItem(ml_al_obj)">
        </ml-algorithms-drop-down-list>
        <vue-form-generator :schema="selectedMlObj.json_form_fields_dict" :model="selectedMlObj.settings_values" :options="formOptions">
        </vue-form-generator>
    </div>
</template>

<script>
import MlAlgorithmsDropDownList from '@/components/MlAlgorithmsDropDownList'
export default {
  name: 'MlConfigurationsPanel',
  data () {
    return {
      newName: 'Enter a new name for the configuration',
      selectedMlObj: {},
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
      return this.isMlModelBuilt ? 'Build' : 'Rebuild'
    }
  },
  methods: {
    handleSelectedItem: function (mlAlgorithmObj) {
      console.log('Got the selected ml algorithm!!!!', mlAlgorithmObj)
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
