<template>
  <div class="box">
    Answer<br />
    {{ this.result }}
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  computed: {
    ...mapState(["result"]),
  },
};
</script>

<style scoped>
</style>