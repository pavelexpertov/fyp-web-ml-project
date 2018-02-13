<template>
    <div>
        <h2>Prediction Panel</h2>
        <vue-form-generator :schema="predictionSchemaDoc.features_values_schema" :model="predictionSchemaDoc.features_values" :options="formOptions"> </vue-form-generator>
    </div>
</template>

<script>
export default {
  name: 'MlPredictionQueryPanel',
  data () {
    return {
      formOptions: {
        validateAfterLoad: false,
        validateAfterChanged: false
      }
    }
  },
  props: {
    predictionSchemaDoc: {
      type: Object,
      required: true
    }
  }
}
</script>

<style>

</style>
