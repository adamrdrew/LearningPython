<script>
//import AlbumCard from '@/components/cards/AlbumCard.vue'
import AlbumCard from './cards/AlbumCard.vue';
import {Howl, Howler} from 'howler';

export default {
  components: { AlbumCard },
  data() {
    return {
      message: "Hey from Adam",
      albums: [],
      SongPlayer: {},
      Song: ""
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
      },
      async GetSong() {
        const res = await fetch("http://127.0.0.1:5000/api/song/1")
        const d = await res.json();
        this.Song = d;
      },
      PlaySong() {
        console.log("didi")
        this.SongPlayer = new Howl({
          src: [this.Song],
          format: ["flac"]
        });
        this.SongPlayer.play();
        console.log(this.SongPlayer)
      }
  }
}
</script>

<template>
<div class="container-fluid">
    <button v-on:click="GetAlbums">Get</button>
    <button v-on:click="GetSong">Get Song</button>
    <button v-on:click="PlaySong">Play Song</button>
    <p>{{Song.Title}}</p>
    <div class="d-flex flex-row flex-wrap gap-3" >
        <album-card v-for="album in albums" v-bind:album="album" v-bind:key="album.ID"/>
    </div>
</div>
</template>

<style scoped>
</style>
