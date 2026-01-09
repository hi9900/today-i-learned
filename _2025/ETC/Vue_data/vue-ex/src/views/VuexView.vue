<template>
  <div>
    <h1>Vuex</h1>
    <p>
      vuex store을 사용하여 컴포넌트 간 데이터를 바인딩하고 업데이트할 수 있다.
    </p>

    <div class="container">
      <div class="A">
        <VuexA />
      </div>
      <div class="B">
        <VuexB />
      </div>
    </div>
  </div>
</template>

<script>
import VuexA from "@/components/VuexA.vue";
import VuexB from "@/components/VuexB.vue";
export default {
  components: {
    VuexA,
    VuexB,
  },
};
</script>

<style>
</style>