<template>
  <div class="box">
    Answer<br />
    {{ this.result }}
  </div>
</template>

<script>
export default {
  data() {
    return {
      result: "",
    };
  },
  created() {
    this.$EventBus.$on("fetchData", (res) => {
      this.result = res;
    });
  },
};
</script>

<style>
</style>