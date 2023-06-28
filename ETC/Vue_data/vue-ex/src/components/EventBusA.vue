<template>
  <div>
    <div class="box" @click="clickO()">O</div>
    <div class="box" @click="clickX()">X</div>
  </div>
</template>

<script>
export default {
  methods: {
    clickO() {
      this.$EventBus.$emit("fetchData", "O");
    },
    clickX() {
      this.$EventBus.$emit("fetchData", "X");
    },
  },
};
</script>

<style>
</style>