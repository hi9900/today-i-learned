# Local Storage

## Window.localStorage

- 브라우저의 내장 객체 중 하나

- Key-Value 형태로 데이터를 저장할 수 있는 저장소

- localStorage에 저장된 데이터는 브라우저를 종료해도 계속해서 유지됨

  - 다른 탭에서도 동일한 데이터를 공유할 수 있는 반면, 다른 도메인에서는 접근할 수 없음

  - 단, 보안과 관련된 중요한 정보를 저장하기에는 적합하지 않음

### .setItem(key, value)

  - key, value 형태로 데이터 저장

  - 데이터 저장 시 문자열 형태로 저장됨에 주의

### .getItem(key)

  - key 값으로 저장된 데이터 불러오기

  - 데이터 저장 시 문자열 형태로 저장하였으므로, 불러올 때도 문자열로 불러옴

### JSON.stringify

  - JSON(JavaScript Object Notation) 객체의 메서드

  - 자바스크립트 객체를 JSON 형식의 문자열로 변환하여 반환

### JSON.parse

  - JSON 형식의 문자열을 자바스크립트 객체로 변환하여 반환

> Vuex에 적용하기

```vue
// App.vue

<template>
  <div id="app">
    <h1>{{ message }}</h1>
    <input type="text" @keyup.enter="changeMessage" v-model="inputData">
  </div>
</template>

<script>

export default {
  ...
  created() {
    this.$store.dispatch('loadMessage')
  },
}
```

```js
// src/store/index.js

export default new Vuex.Store({
  ...
  state: {
    message: 'message in state',
  },
  mutations: {
    LOAD_MESSAGE(state) {
      const parsedMessage = JSON.parse(localStorage.getItem('message'))
      state.message = parsedMessage ? parsedMessage : ''
    },
  },
  actions: {
    changeMessage(context, message){
      context.commit('CHANGE_MESSAGE', message)
      context.dispatch('messageSaveToLocalStorage')
    },
    messageSaveToLocalStorage(context) {
      const message = JSON.stringify(context.state.message)
      localStorage.setItem('message', message)
    },
    loadMessage(context) {
      context.commit('LOAD_MESSAGE')
    },
  }
})
```