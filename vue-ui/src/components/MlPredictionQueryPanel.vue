<template>
    <div>
        <h2>Prediction Panel</h2>
        <h3>Weekly Sales: {{predictedSales}}</h3>
        <vue-form-generator :schema="predictionSchemaDoc.features_values_schema" :model="predictionSchemaDoc.features_values" :options="formOptions"> </vue-form-generator>
        <el-button type="primary" @click="handleClick">
            Predict
        </el-button>
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
    },
    predictedSales: {
      type: Number,
      default: 0
    }
  },
  methods: {
    handleClick () {
      this.$emit('predictionQueryClick')
    }
  }
}
</script>

<style>

</style>
