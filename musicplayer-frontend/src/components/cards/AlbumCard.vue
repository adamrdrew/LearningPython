<script>
export default {
  data() {
    return {
      message: "Hey from Adam",
      albums: [],
      TitleMaxLen: 33
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
  },
  computed: {
      ShortTitle() {
          const len = this.album.Title.length;
          if ( len <= this.TitleMaxLen ) return this.album.Title;
          const sub = this.album.Title.slice(0, this.TitleMaxLen - 3);
          const subElipsed = sub + "...";
          return subElipsed;
      }
  }
}
</script>

<template>
    <div class="card" style="width: 10em;">
        <img class="card-img-top" v-bind:src="album.ArtSmall" style="width: 10em; height: 10em"/>
        <div class="card-body">
            <h6 class="card-title">{{ShortTitle}}</h6>
            <small class="card-text">{{album.Artist.Title}}</small>
        </div>
  </div>
</template>

<style scoped>
</style>
