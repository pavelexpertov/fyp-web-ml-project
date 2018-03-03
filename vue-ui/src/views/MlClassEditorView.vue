<template>
    <div>
    <h1>{{className}}</h1>
    <ml-class-editor :codeText="codeText" @saveCodeText="value => handleSaveCodeText(value)"></ml-class-editor>
</div>
</template>

<script>
import MlClassEditor from '@/components/MlClassEditor'
export default {
  name: 'MlClassEditorView',
  data () {
    return {
      codeText: '',
      className: ''
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
    }
  },
  created () {
    this.getClassConfigObject()
  },
  watch: {
    '$route' (to, from) {
      this.saveClassConfigObject()
      this.getClassConfigObject()
    }
  }
}
</script>

<style>
</style>
