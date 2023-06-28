<template>
  <div>
    <h1>Props/Emit</h1>
    <p>(부모-자식 간 EventBus 사용)</p>

    <div class="container">
      <div class="A">
        <AComponent @click="click" />
      </div>
      <div class="B">
        <BComponent :result="result" />
      </div>
    </div>
  </div>
</template>

<script>
import AComponent from "@/components/AComponent";
import BComponent from "@/components/BComponent";

export default {
  components: {
    AComponent,
    BComponent,
  },
  data() {
    return {
      result: "",
    };
  },
  methods: {
    click(value) {
      this.result = value;
    },
  },
};
</script>

<style>
</style>