<script>
export default {
  data() {
    return {
      message: "Hey from Adam"
    }
  },
  props: {
      PropMessage: String
  },
  methods: {
      ChangeIt() {
        this.message = "Did it";
      }
  }
}
</script>

<template>
  <div class="greetings">
    <h1 class="green">Adam: {{ message }} {{ PropMessage }}</h1>
    <button v-on:click="ChangeIt"/>
  </div>
</template>

<style scoped>
</style>
