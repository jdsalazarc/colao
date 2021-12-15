<template>
  <div class="hello">
    <h1 class="text-center">EL COLAO</h1>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

h1{
  font-size:100px;
  font-weight: 900;
  color:#FF6363;
  -webkit-text-stroke:3px #4399D9

}
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
