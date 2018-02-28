<template>
    <div>
    <h1>asdfsafds</h1>
    <ml-class-editor :codeText="codeText"></ml-class-editor>
</div>
</template>

<script>
import MlClassEditor from '@/components/MlClassEditor'
export default {
  name: 'MlClassEditorView',
  data () {
    return {
      codeText: 'sdfasfasfsadf'
    }
  },
  components: {
    mlClassEditor: MlClassEditor
  }
}
</script>

<style>
</style>
