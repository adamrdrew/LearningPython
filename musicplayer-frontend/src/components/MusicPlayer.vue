<script>
import {Howl, Howler} from 'howler';

export default {
  data() {
    return {
      SongLoaded: false,
      Song: {
          Title: "",
          MusicStream: "",
      },
      SongPlayer: {},
      intervalHandle: {},
      SongLength: 0,
      SongPlaybackPosition: 0
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
        this.SongLength = 100;
        this.SongPlaybackPosition = 0;
        this.SongPlayer.play();
        this.SongPlayer.on('end', () => {
          this.SkipForward()
        });
        this.SongLoaded = true;
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
      },
      Tick() {
        if ( this.SongLoaded ) {
          this.SongLength = this.SongPlayer.duration();
          this.SongPlaybackPosition = this.SongPlayer.seek();
        }

      }
  },
  created() {
    this.intervalHandle = setInterval(this.Tick, 1000);
  },
  beforeDestroy() {
    clearInterval(this.intervalHandle);
  },
  computed: {
      SongURL() {
          return "http://127.0.0.1:5000/api/song/" + this.SongID;
      },
      NowPlayingSong() {
        return this.$store.getters.NowPlayingSong
      },
      ProgressBarStyle() {
        const pct = (this.SongPlaybackPosition / this.SongLength) * 100;
        return {width: pct + "%"}
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
<div class="container-fluid fixed-top shadow-sm" style="background-color:white">
  <div v-if="SongLoaded" class="container-fluid">
    <div class="row">
      <div class="col-md-4 d-flex align-items-center">
        <div class="btn-group">
          <button class="btn btn-secondary"  v-on:click="SkipBackward">Back</button>
          <button class="btn btn-secondary" v-on:click="PlaySong">Play</button>
          <button class="btn btn-secondary" >Pause</button>
          <button class="btn btn-secondary" v-on:click="StopSong">Stop</button>
          <button class="btn btn-secondary" v-on:click="SkipForward">Next</button>
        </div>
      </div>
      <div class="col-md-4">
        <div class="d-flex align-items-center">
          <div class="flex-shrink-0">
            <img v-bind:src="Song.Album.ArtSmall" class="img-fluid" style="width:5em;"/>
          </div>
          <div class="flex-grow-1 ms-3">
            <h6>{{Song.Title}}</h6>
            <small class="card-text">{{Song.Artist.Title}}</small>
            <div class="progress">
              <div class="progress-bar" v-bind:style="ProgressBarStyle"></div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-4">

      </div>
    </div>
  </div>
  <div v-else class="container-fluid center text-center">
    <img src="../assets/UnknownAlbumSmall.jpg" class="img-fluid" style="width:5em;"/>
    <button class="btn btn-primary" disabled>Back</button>
    <button class="btn btn-primary" disabled>Play</button>
    <button class="btn btn-primary" disabled>Pause</button>
    <button class="btn btn-primary" disabled>Stop</button>
    <button class="btn btn-primary" disabled>Next</button>
  </div>
</div>
</template>

<style scoped>
</style>
