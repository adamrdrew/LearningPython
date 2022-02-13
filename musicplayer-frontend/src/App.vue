<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
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
