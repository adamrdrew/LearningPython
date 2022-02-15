<script>
export default {
  data() {
    return {
      Songs: []
    }
  },
  methods: {
      async GetSongs() {
        const res = await fetch("http://127.0.0.1:5000/api/song/all")
        const d = await res.json();
        this.Songs = d;
      },
      PlaySong(id) {
        this.$store.dispatch("GetAndQueueSong", id)
      }
  },
  computed: {

  },
  mounted() {
    this.GetSongs();
  }
}
</script>

<template>
  <div class="container-fluid">
    <table class="table table-default table-striped table-bordered">
        <thead>
          <tr>
            <th></th>
            <th>Song</th>
            <th>Artist</th>
            <th>Album</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="song in Songs" v-bind:key="song.ID">
            <td>
              <button class="btn btn-secondary" v-on:click="PlaySong(song.id)">
                <i class="fa-solid fa-play"/>
              </button>
            </td>
            <td>{{song.title}}</td>
            <td>{{song.artist.title}}</td>
            <td>{{song.album.title}}</td>
          </tr>
        </tbody>
    </table>
  </div>
</template>

<style scoped>
</style>
