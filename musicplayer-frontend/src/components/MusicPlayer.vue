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
  },
  methods: {
      PlaySong() {
        this.StopSong();
        this.SongPlayer = new Howl({
          src: [this.Song.MusicStream],
          //format: ["flac"]
        });
        this.SongPlayer.play();
      },
      async GetSong() {
        const res = await fetch("http://127.0.0.1:5000/api/song/" + this.NowPlayingSong.Id);
        const d = await res.json();
        this.Song = d;
      },
      StopSong() {
        if ( !this.SongPlayer.playing ) return
        this.SongPlayer.stop();
      },
      SkipForward() {
        this.$store.commit("SkipForward");
      },
      SkipBackward() {
        this.$store.commit("SkipBackward");
      }
  },
  computed: {
      SongURL() {
          return "http://127.0.0.1:5000/api/song/" + this.SongID;
      },
      NowPlayingSong() {
        return this.$store.getters.NowPlayingSong
      }
  },
  watch: {
      NowPlayingSong() {
          this.GetSong().then(() => {
              this.PlaySong();
          })
      }
  }
}
</script>

<template>
<div>

  <button v-on:click="SkipBackward">Back</button>
  <button v-on:click="PlaySong">Play</button>
  <button>Pause</button>
  <button v-on:click="StopSong">Stop</button>
  <button v-on:click="SkipForward">Next</button>
</div>
</template>

<style scoped>
</style>
