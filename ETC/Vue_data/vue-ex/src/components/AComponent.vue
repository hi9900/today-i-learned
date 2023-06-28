<template>
  <div>
    <div class="box" @click="clickO">O</div>
    <div class="box" @click="clickX">X</div>
  </div>
</template>

<script>
export default {
  methods: {
    clickO() {
      this.$emit("click", "O");
    },
    clickX() {
      this.$emit("click", "X");
    },
  },
};
</script>

<style scoped>
</style>