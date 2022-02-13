<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />

    <div class="wrapper">

      <nav>
        <RouterLink to="/songs">Songs</RouterLink>
        <RouterLink to="/artists">Artists</RouterLink>
        <RouterLink to="/albums">Albums</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style>

</style>
