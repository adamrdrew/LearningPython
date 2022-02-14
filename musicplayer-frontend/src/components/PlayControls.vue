<script>
export default {
  data() {
    return {
      albums: [],
    }
  },
  props: {
      Disabled: Boolean
  },
  methods: {
      SkipBackward() {
          this.$emit("back")
      },
      SkipForward() {
          this.$emit("forward")
      },
      PlaySong() {
          this.$emit("play");
      },
      StopSong() {
          this.$emit("stop")
      },
      PauseSong() {
          this.$emit("pause")
      }
  }
}
</script>

<template>
    <div class="btn-group">
        <button v-bind:disabled="Disabled" class="btn btn-secondary" v-on:click="SkipBackward"><i class="fa-solid fa-backward"/></button>
        <button v-bind:disabled="Disabled"  class="btn btn-secondary" v-on:click="PlaySong"><i class="fa-solid fa-play"/></button>
        <button v-bind:disabled="Disabled"  class="btn btn-secondary" v-on:click="PauseSong"><i class="fa-solid fa-pause"/></button>
        <button v-bind:disabled="Disabled"  class="btn btn-secondary" v-on:click="StopSong"><i class="fa-solid fa-stop"/></button>
        <button v-bind:disabled="Disabled"  class="btn btn-secondary" v-on:click="SkipForward"><i class="fa-solid fa-forward"/></button>
    </div>
</template>

<style scoped>
</style>
