<script>
export default {
  data() {
    return {
      message: "Hey from Adam",
      albums: []
    }
  },
  props: {
      album: {
          ArtSmall: String,
          Title: String,
          ID: String,
          Artist: {
              Title: String,
              ID: String
          }
      }
  },
  methods: {
      ChangeIt() {
        this.message = "Did it";
      },
  }
}
</script>

<template>
  <div class="greetings">
      <img v-bind:src="album.ArtSmall"/>
      <h1>{{album.Title}}</h1>
      <h3>{{album.Artist.Title}}</h3>
  </div>
</template>

<style scoped>
</style>
