<template>
    <div>
    <codemirror class="code-style" v-model="providedCodeText" :options="options" ref="myEditor"></codemirror>
</div>
</template>

<script>
import { codemirror } from 'vue-codemirror-lite'
import 'codemirror/mode/python/python.js'
export default {
  name: 'MlClassEditor',
  data () {
    return {
      options: {
        mode: 'python',
        indentUnit: 4,
        tabSize: 4,
        lineNumbers: true,
        line: true,
        lineSeparator: '\n'
      },
      textCode: 'print("helllo")'
    }
  },
  components: {
    codemirror
  },
  props: {
    codeText: {
      type: String,
      required: true
    }
  },
  mounted () {
    this.editor.setOption('extraKeys', {
      Tab: function (cm) {
        var spaces = Array(cm.getOption('indentUnit') + 1).join(' ')
        cm.replaceSelection(spaces)
      }
    })
  },
  computed: {
    editor () {
      return this.$refs.myEditor.editor
    },
    providedCodeText: {
      get () {
        return this.codeText
      },
      set (updatedValue) {
        this.$emit('saveCodeText', updatedValue)
      }
    }
  }
}
</script>

<style scoped>
.code-style {
        text-align: left;
}
</style>
