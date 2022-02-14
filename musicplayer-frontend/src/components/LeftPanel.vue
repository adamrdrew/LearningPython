

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
  <div>
        <RouterLink to="/songs">Songs</RouterLink><br>
        <RouterLink to="/artists">Artists</RouterLink><br>
        <RouterLink to="/albums">Albums</RouterLink>
  </div>
</template>

<style scoped>
</style>
