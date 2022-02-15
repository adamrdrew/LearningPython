<script>
export default {
  data() {
    return {
        TitleMaxLen: 33,
    }
  },
  props: {
      artist: {
          title: String,
          id: String,
          albums: []
      }
  },
  methods: {
      ShowArtistAlbums(){
        this.$store.dispatch('GetAndQueueAlbumSongs', this.album.id);
      }
  },
  computed: {
      ShortTitle() {
          const len = this.artist.title.length;
          if ( len <= this.TitleMaxLen ) return this.artist.title;
          const sub = this.artist.title.slice(0, this.TitleMaxLen - 3);
          const subElipsed = sub + "...";
          return subElipsed;
      }
  }
}
</script>

<template>
    <div class="card shadow-lg" style="width: 10em;"  v-on:click="ShowArtistAlbums()">
        <img class="card-img-top" v-bind:src="artist.albums[0].art_small" style="width: 10em; height: 10em"/>
        <div class="card-body">
            <h6 class="card-title">{{ShortTitle}}</h6>
        </div>
  </div>
</template>

<style scoped>
</style>
