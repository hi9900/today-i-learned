# Vue

## Vue의 기본 구조

- Vue 구조는 매우 직관적

```js
// vue_intro.vue

<template>
  <!-- HTML -->
  <div>
    <p>Hello :)</p>
  </div>
</template>

<script>
  // JavaScript
</script>

<style>
  /* CSS */
  p {
    color: black;
  }
</style>
```

### Vue CDN

- Vue로 작업을 시작하기 위해 CDN을 가져와야 함

- Django == Python Web Framework

  - pip install

- Vue === JS Front-end Framework

  - Bootstrap에서 사용했던 CDN 방식 제공

  - npm 활용

- [Vue2 공식문서](https://v2.vuejs.org/) 참고

  - Getting Started > Installation > Development version CDN 복사

  `<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>`

### Vue로 코드 작성

1. Vue CDN 가져오기

2. Vue instance 생성

  - Vue instance - 1개의 Object

  - 미리 정해진 속성명을 가진 Object

3. `el`, `data` 설정

  - data에 관리할 속성 정의

4. 선언적 렌더링 `{{ }}`

  - Vue data를 화면에 렌더링

5. input tag에 `v-model` 작성

  - input에 값 입력 > Vue data 반영 > DOM 반영

```html
<body>
  <div id="app">
    <p id="name">name : {{ message }}</p>
    <input id="inputName" type="text" v-model="message">
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        message: '',
      }
    })
  </script>
</body>
```