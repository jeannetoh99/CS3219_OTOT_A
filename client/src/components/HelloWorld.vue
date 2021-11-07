<template>
  <div class="hello">
    <div class="container">
      <h4>Cat gif of the day</h4>
      <img :src="`${cat_url}`" />
    </div>
  </div>
</template>

<script>

import axios from "axios"

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      cat_url: ''
    };
  },
  async mounted() {
    await axios({ method: "GET", "url": "http://localhost/cat" })
      .then(res => {
        this.cat_url = res.data['cat_url'];
      }, error => {
        console.error(error);
      });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
