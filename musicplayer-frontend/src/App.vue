<script>
import { RouterLink, RouterView } from 'vue-router';
import MusicPlayer from './components/MusicPlayer.vue';
import LeftPanel from './components/LeftPanel.vue';

export default {
  data() {
    return {
      SongID: ""
    }
  },
  components: {MusicPlayer,LeftPanel},
  methods: {
    LoadSong(SongID) {
      this.SongID = SongID;
    }
  }
}
</script>

<template>
<div>
  <header>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  </header>

  <div class="container-fluid">
    <div class="row">
      <div class="col-md-12">
        <MusicPlayer/>      
      </div>
    </div>
    <div class="row" style="padding-top: 5em;">
      <div class="col-md-1">
        <LeftPanel/>
      </div>
      <div class="col-md-11">
        <RouterView/>
      </div>
    </div>
  </div>


</div>

</template>

<style>

</style>
