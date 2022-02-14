<script>
export default {
  data() {
    return {
        TitleMaxLen: 33,
    }
  },
  props: {
      artist: {
          Title: String,
          Id: String,
          Albums: []
      }
  },
  methods: {
      ShowArtistAlbums(){
        this.$store.dispatch('GetAndQueueAlbumSongs', this.album.ID);
      }
  },
  computed: {
      ShortTitle() {
          const len = this.artist.Title.length;
          if ( len <= this.TitleMaxLen ) return this.artist.Title;
          const sub = this.artist.Title.slice(0, this.TitleMaxLen - 3);
          const subElipsed = sub + "...";
          return subElipsed;
      }
  }
}
</script>

<template>
    <div class="card shadow-lg" style="width: 10em;"  v-on:click="ShowArtistAlbums()">
        <img class="card-img-top" v-bind:src="artist.Albums[0].ArtSmall" style="width: 10em; height: 10em"/>
        <div class="card-body">
            <h6 class="card-title">{{ShortTitle}}</h6>
        </div>
  </div>
</template>

<style scoped>
</style>
