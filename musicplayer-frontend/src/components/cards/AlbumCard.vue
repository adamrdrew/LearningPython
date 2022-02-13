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
    <div class="card" style="width: 18rem;">
        <img class="card-img-top" v-bind:src="album.ArtSmall"/>
        <div class="card-body">
            <h5 class="card-title">{{album.Title}}</h5>
            <p class="card-text">{{album.Artist.Title}}</p>
        </div>
  </div>
</template>

<style scoped>
</style>
