

<script>
import { RouterLink, RouterView } from 'vue-router';
export default {
  components: {RouterLink},
  data() {
    return {
    }
  },
  methods: {
  }
}
</script>

<template>
  <div class="container-fluid tight">
      <ul class="list-group tight">
        <li class="list-group-item"><RouterLink to="/songs">Songs</RouterLink></li>
        <li class="list-group-item"><RouterLink to="/artists">Artists</RouterLink></li>
        <li class="list-group-item"><RouterLink to="/albums">Albums</RouterLink></li>
      </ul>
  </div>
</template>

<style scoped>
.tight {
  margin: 0em;
  padding: 0em;
}
</style>
