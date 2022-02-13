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
    <div class="card" style="width: 10em;">
        <img class="card-img-top" v-bind:src="album.ArtSmall" style="width: 10em; height: 10em"/>
        <div class="card-body">
            <h6 class="card-title">{{album.Title}}</h6>
            <p class="card-text">{{album.Artist.Title}}</p>
        </div>
  </div>
</template>

<style scoped>
</style>
