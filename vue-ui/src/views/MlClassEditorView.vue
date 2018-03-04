<template>
    <div>
    <h1>{{className}}</h1>
    <ml-class-editor :codeText="codeText" @saveCodeText="value => handleSaveCodeText(value)"></ml-class-editor>
    <el-button @click="handleUploadButton">Upload</el-button>
    <p>{{errorText}}</p>
</div>
</template>

<script>
import MlClassEditor from '@/components/MlClassEditor'
export default {
  name: 'MlClassEditorView',
  data () {
    return {
      codeText: '',
      className: '',
      errorText: ''
    }
  },
  components: {
    mlClassEditor: MlClassEditor
  },
  props: ['class_name'],
  methods: {
    getClassConfigObject () {
      let configObject = this.$store.getters.getMlClassConfigObjByName(this.class_name)
      this.className = configObject.class_name
      this.codeText = configObject.code
    },
    saveClassConfigObject () {
      let configObject = {
        code: this.codeText,
        class_name: this.className
      }
      this.$store.commit('saveMlClassCode', configObject)
    },
    handleSaveCodeText (value) {
      this.codeText = value
    },
    handleUploadButton () {
      this.errorText = ''
      let jsonObj = {code: this.codeText}
      this.$http.post('mlclass/' + this.className, jsonObj)
        .then(response => {
          this.$notify({
            title: 'Successful Upload',
            message: `${this.className} class has been uploaded successfully`,
            duration: 4000
          })
        })
        .catch(err => { this.errorText = err.body })
    }
  },
  created () {
    this.getClassConfigObject()
  },
  beforeDestroy () {
    this.saveClassConfigObject()
  },
  watch: {
    '$route' (to, from) {
      this.errorText = ''
      this.saveClassConfigObject()
      this.getClassConfigObject()
    }
  }
}
</script>

<style>
</style>
