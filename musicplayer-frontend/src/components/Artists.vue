<script>
//import AlbumCard from '@/components/cards/AlbumCard.vue'
import ArtistCard from './cards/ArtistCard.vue';

export default {
  components: { ArtistCard },
  data() {
    return {
      artists: [],
    }
  },
  methods: {
      async GetArtists() {
        const res = await fetch("http://127.0.0.1:5000/api/artist/all")
        const d = await res.json();
        this.artists = d;
      }
  },
  mounted() {
    this.GetArtists();
  }
}
</script>

<template>
<div class="container-fluid">
    <div class="d-flex flex-row flex-wrap gap-3" >
        <artist-card v-for="artist in artists" v-bind:artist="artist" v-bind:key="artist.ID"/>
    </div>
</div>
</template>

<style scoped>
</style>
