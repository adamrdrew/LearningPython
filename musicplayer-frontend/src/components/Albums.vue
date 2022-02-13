<script>
export default {
  data() {
    return {
      message: "Hey from Adam",
      albums: []
    }
  },
  props: {
      PropMessage: String
  },
  methods: {
      ChangeIt() {
        this.message = "Did it";
      },
      GetAlbums() {
          fetch("http://127.0.0.1:5000/api/album/all").then(res => res.json()).then(d => this.data.albums = d)
      }
  }
}
</script>

<template>
  <div class="greetings">
    <h1 class="green">Adam: {{ message }} {{ PropMessage }}</h1>
    <button v-on:click="GetAlbums" title="Get">Get</button>
  </div>
</template>

<style scoped>
</style>
