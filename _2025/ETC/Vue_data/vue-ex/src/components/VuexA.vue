<template>
  <div>
    <div class="box" @click="clickO">O</div>
    <div class="box" @click="clickX">X</div>
  </div>
</template>

<script>
import { mapMutations } from "vuex";
export default {
  computed: {},
  methods: {
    ...mapMutations(["clickOX"]),

    clickO() {
      this.$store.commit("clickOX", "O");
    },
    clickX() {
      this.$store.commit("clickOX", "X");
    },
  },
};
</script>

<style scoped>
</style>