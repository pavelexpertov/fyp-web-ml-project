<template>
    <div>
        <el-form ref="form" :model="datasetConfigObj">
            <el-form-item label="StoreId">
                <el-select v-model="datasetConfigObj.store_number">
                    <el-option
                    v-for="store_number in storeIdList"
                    :key="store_number"
                    :label="store_number"
                    :value="store_number"
                    >
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="Date From:">
                <el-date-picker
                v-model="datasetConfigObj.start_date"
                type="date"
                :clearable="false"
                format="dd/MM/yyyy"
                value-format="yyyy-MM-dd">
                </el-date-picker>
            </el-form-item>
            <el-form-item label="Date To:">
                <el-date-picker
                v-model="datasetConfigObj.end_date"
                type="date"
                format="dd/MM/yyyy"
                :clearable="false"
                value-format="yyyy-MM-dd">
                </el-date-picker>
            </el-form-item>
            <el-button type="primary" v-if="showButton" @click="handleClick">
                Refresh
            </el-button>
        </el-form>
        <el-transfer
          v-model="datasetConfigObj.features_list"
          :titles="['Available', 'Selected']"
          :data="featureNamesList"
          class="transfer-class"
        >
        </el-transfer>
    </div>
</template>

<script>
export default {
  name: 'DataSetConfigurationsPanel',
  data () {
    return {}
  },
  props: {
    datasetConfigObj: {
      type: Object,
      required: true
    },
    showButton: {
      type: Boolean,
      required: true
    }
  },
  computed: {
    storeIdList: function () {
      let storeList = []
      for (var id = 1; id <= 45; ++id) { storeList.push(id) }
      return storeList
    },
    featureNamesList: function () {
      let featuresList = ['Weekly_Sales', 'Temperature', 'Fuel_Price',
        'MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4',
        'MarkDown5', 'CPI', 'Unemployment']
      let length = featuresList.length
      for (var i = 0; i < length; ++i) {
        let obj = {
          key: featuresList[i],
          label: featuresList[i],
          disabled: false
        }
        featuresList[i] = obj
      }
      return featuresList
    }
  },
  methods: {
    handleClick: function () {
      this.$emit('click')
    }
  }
}
</script>

<style scoped>
.transfer-class {
    text-align: left;
}
</style>
