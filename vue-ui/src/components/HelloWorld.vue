<template>
  <!-- <div class="hello"> -->
  <div>
    <h1>Welcome</h1>
    <p>This web application is used for playing with machine learning algorithms. The sub tabs on the left are:</p>
    <ul>
      <li>Dataset Settings - It allows you to configure a settings based on dataset's features and see what the data looks like based on them.</li>
      <li>ML Algorithm Playground - It allows you to create a model based on selected machine learning algorithm, its tweaked settings and selected Data Set settings.</li>
      <li>User ML Classes - It allows you to add your own algorithm implementation of the machine learning class by either utilising sci-kit library or your own implementation.</li>
    </ul>
  </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App',
      response_show: '',
      response_add: '',
    }
},
methods: {
    add: function(){
        this.$http.get('add')
        .then(result => {
            this.response_add = result.body
        })
    },
    show: function(){
        this.$http.get('show')
        .then(result => {
            this.response_show = result.body
        })
    }
}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
/* ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
} */
a {
  color: #42b983;
}
div li, p{
  text-align: left;
}
</style>
