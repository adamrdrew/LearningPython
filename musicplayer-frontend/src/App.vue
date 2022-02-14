<script>
import { RouterLink, RouterView } from 'vue-router';
import MusicPlayer from './components/MusicPlayer.vue';

export default {
  data() {
    return {
      SongID: ""
    }
  },
  components: {MusicPlayer},
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
    <div class="wrapper">

      <nav>
        <RouterLink to="/songs">Songs</RouterLink>
        <RouterLink to="/artists">Artists</RouterLink>
        <RouterLink to="/albums">Albums</RouterLink>
      </nav>
    </div>
  </header>

  <MusicPlayer/>
  <RouterView @load-song="LoadSong"/>
</div>

</template>

<style>

</style>
