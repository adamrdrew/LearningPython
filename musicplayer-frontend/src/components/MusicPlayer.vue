<script>
import {Howl, Howler} from 'howler';

export default {
  data() {
    return {
      Song: {
          Title: "",
          MusicStream: ""
      },
      SongPlayer: {}
    }
  },
  props: {
      SongID: String
  },
  methods: {
      async GetSong() {
        const res = await fetch(this.SongURL)
        const d = await res.json();
        this.Song = d;
      },
      PlaySong() {
        this.SongPlayer = new Howl({
          src: [this.Song.MusicStream],
          //format: ["flac"]
        });
        this.SongPlayer.play();
        console.log(this.SongPlayer)
      }
  },
  computed: {
      SongURL() {
          return "http://127.0.0.1:5000/api/song/" + this.SongID;
      }
  },
  watch: {
      SongID() {
          this.GetSong().then(() => {
              this.PlaySong();
          })
      }
  }
}
</script>

<template>
<h1>Sup</h1>
</template>

<style scoped>
</style>
