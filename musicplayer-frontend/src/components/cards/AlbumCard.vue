<script>
export default {
  data() {
    return {
      albums: [],
      TitleMaxLen: 33
    }
  },
  props: {
      album: {
          art_small: String,
          title: String,
          id: String,
          artist: {
              title: String,
              id: String
          }
      }
  },
  methods: {
      PlayAlbum(){
        this.$store.dispatch('GetAndQueueAlbumSongs', this.album.id);
      }
  },
  computed: {
      ShortTitle() {
          const len = this.album.title.length;
          if ( len <= this.TitleMaxLen ) return this.album.title;
          const sub = this.album.title.slice(0, this.TitleMaxLen - 3);
          const subElipsed = sub + "...";
          return subElipsed;
      }
  }
}
</script>

<template>
    <div class="card shadow-lg" style="width: 10em;"  v-on:click="PlayAlbum()">
        <img class="card-img-top" v-bind:src="album.art_small" style="width: 10em; height: 10em"/>
        <div class="card-body">
            <h6 class="card-title">{{ShortTitle}}</h6>
            <small class="card-text">{{album.artist.title}}</small>
        </div>
  </div>
</template>

<style scoped>
</style>
