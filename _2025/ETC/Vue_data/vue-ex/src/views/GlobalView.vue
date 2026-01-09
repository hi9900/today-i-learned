<template>
  <div>
    <h1>EventBus</h1>
    <p>(Global EventBus 사용)</p>
    <p>
      Vue 2.0에서 사용하던 방식으로 3.0에서는 지양되며, 기존 프로젝트는 외부
      라이브러리를 통해 마이그레이션할 수 있다.
    </p>

    <div class="container">
      <div class="A">
        <EventBusA />
      </div>
      <div class="B">
        <EventBusB />
      </div>
    </div>
  </div>
</template>

<script>
import EventBusA from "@/components/EventBusA.vue";
import EventBusB from "@/components/EventBusB.vue";

export default {
  components: {
    EventBusA,
    EventBusB,
  },
};
</script>

<style>
</style>