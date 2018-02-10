<template>
    <el-row>
        <el-col :span="8">
            <template v-if="!mlConfigObject">
                <el-input v-model="newDataConfigName" placeholder="Enter a new name for Dataset configuration"></el-input>
                <el-button @click="saveName">Save</el-button>
            </template>
            <data-set-configurations-panel
            v-else
            :datasetConfigObj="dataConfigObject"
            :showButton="true"
            >
            </data-set-configurations-panel>
        </el-col>
        <el-col :span="18">
        </el-col>
    </el-row>
</template>

<script>
import DataSetConfigurationsPanel from '@components/DataSetConfigurationsPanel'

export default {
    name: 'DataFeatureAnalysisView',
    data () {
        return {
            dataConfigObject: ''
        }
    },
    methods: {
        saveName () {
            //Add a default dataset configuration
            console.log("Implement me in the savename of the datafeatureanalysis!!!")
        }
    },
    components: {
        dataSetConfigurationsPanel: DataSetConfigurationsPanel
    }
}
</script>

<style>
</style>
