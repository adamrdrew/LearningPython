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
