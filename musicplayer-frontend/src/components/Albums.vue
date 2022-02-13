<script>
//import AlbumCard from '@/components/cards/AlbumCard.vue'
import AlbumCard from './cards/AlbumCard.vue';

export default {
  components: { AlbumCard },
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
      async GetAlbums() {
        const res = await fetch("http://127.0.0.1:5000/api/album/all")
        const d = await res.json();
        this.albums = d;
      }
  }
}
</script>

<template>
<div class="container-fluid">
    <button v-on:click="GetAlbums">Get</button>
    <div class="d-flex flex-row flex-wrap gap-3" >
        <album-card v-for="album in albums" v-bind:album="album" v-bind:key="album.ID"/>
    </div>
</div>
</template>

<style scoped>
</style>
