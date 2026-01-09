<template>
  <div class="box">
    Answer<br />
    {{ this.result }}
  </div>
</template>

<script>
export default {
  props: {
    result: String,
  },
};
</script>

<style scoped>
</style>