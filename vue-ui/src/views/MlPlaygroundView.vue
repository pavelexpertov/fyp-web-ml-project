<template>
    <div>
        <el-row>
        </el-row>
        <el-row>
            <template v-if="!mlConfigObject">
                <el-input v-model="newMlConfigName" placeholder="Enter a new name for ML configuration"></el-input>
                <el-button @click="saveName">Save</el-button>
            </template>
            <ml-configurations-panel
            v-else
            :mlConfigurationsObj="mlConfigObject"
            >
            </ml-configurations-panel>
        </el-row>
        <el-row>
            <el-select v-model="dataConfigObject" placeholder="Select a dataconfig">
                <el-option
                v-for="data_config in datasetConfigsList"
                :key="data_config.name"
                :label="data_config.name"
                :value="data_config">
                </el-option>
            </el-select>
            <data-set-configurations-panel
            v-if="dataConfigObject"
            :datasetConfigObj="dataConfigObject"
            :showButton="false"
            >
            </data-set-configurations-panel>
        </el-row>
    </div>
</template>

<script>
import MlConfigurationsPanel from '@components/MlConfigurationsPanel'
import DataSetConfigurationsPanel from '@components/DataSetConfigurationsPanel'

export default {
    name: "MlPlaygroundView",
    data () {
        return {
            mlConfigObject: '',
            dataConfigObject:'',
            newMlConfigName: ''
        }
    },
    components: {
        mlConfigurationsPanel: MlConfigurationsPanel,
        dataSetConfigurationsPanel: DataSetConfigurationsPanel
    },
    computed: {
        datasetConfigsList: function(){
            //Return a list of configs for the dropdown list
            console.log("Implement me in the datasetConfigsList")
        }
    }
    methods: {
        saveName () {
            //Create a new empty ML config object after user enters a name
            console.log("Implement me in the saveName")
        }
    },
    created: function(){
        //check for the existing ml Config
        let model_name = this.$route.params.model_name
        if(model_name){
            console.log("Implement me!!!!!!!")
        }
    }
}
</script>

<style>
</style>
