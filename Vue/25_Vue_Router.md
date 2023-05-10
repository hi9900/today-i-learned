# Vue Router 실습

## 주소를 이동하는 2가지 방법

## 1. 선언적 방식 네비게이션

- router-link의 `to` 속성으로 주소 전달

- routes에 등록된 주소와 매핑된 컴포넌트로 이동

```vue
// App.vue

<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </nav>
    <router-view/>
  </div>
</template>
```

> ### Named Routes

  - 이름을 가지는 routes

    - Django에서 path 함수의 name 인자의 활용과 같은 방식

  ```js
  // router/index.js

  const routes = [
    {
      path: '/',
      name: 'home',
      component: HomeView
    }
  ]
  ```

- 동적인 값을 사용하기 때문에 v-bind를 사용해야 정상적으로 작동

```vue
// App.vue

<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'home' }">Home</router-link> |
      <router-link :to="{ name: 'about' }">About</router-link>
    </nav>
    <router-view/>
  </div>
</template>
```

## 2. 프로그래밍 방식 네비게이션

- Vue 인스턴스 내부에서 라우터 인스턴스에 `$router`로 접근할 수 있음

- 다른 URL로 이동하려면 `this.$router.push`를 사용

  - history stack에 이동할 URL을 넣는(push) 방식

  - history stack에 기록이 남기 때문에 사용자가 브라우저의 뒤로가기 버튼을 클릭하면 이전 URL로 이동할 수 있음

- 결국 `<router-link :to="...">`를 클릭하는 것과 `$router.push(...)`를 호출하는 것은 같은 동작

- 동작 원리는 선언적 방식과 같음

```vue
// AboutView.vue

<template>
  <div class="about">
    <router-link :to="{ name: 'home' }">Home</router-link> |
    <button @click="toHome">홈으로</button>
  </div>
</template>

<script>
  export default {
    name: 'AboutView',
    methods: {
      toHome() {
        this.$router.push({ name: 'home' })
      }
    }
  }
</script>
```

### Dynamic Route Matching

- 동적 인자 전달

  - URL의 특정 값을 변수처럼 사용할 수 있음

  ex. Django에서의 variable routing

- route를 추가할 때 동적 인자를 명시

```js
// router/index.js

import HelloView from '@/views/HelloView.vue'

const routes = [
  ...
  {
    path: '/hello/:userName',
    name: 'hello',
    component: HelloView
  }
]
```

- `$route.params`로 변수에 접근 가능

- HTML에서 직접 사용하기 보다는 data에 넣어서 사용하는 것을 권장

```vue
// views/HelloView.vue

<template>
  <div>
    <h1>Hello, {{ $route.params.userName }}</h1>
    <h1>Hello, {{ userName }}</h1>
  </div>
</template>

<script>
  export default {
    name: 'HelloView',
    data() {
      return {
        userName: this.$route.params.userName
      }
    }
  }
</script>
```

- params를 이용하여 동적 인자 전달 가능

```vue
// App.vue

<template>
  <div class="about">
    <router-link 
    :to="{ name: 'hello', params: { userName: 'hihi'} }"
    >Hello</router-link> |
  </div>
</template>
```

### Dynamic Route Matching - 프로그래밍 방식 네비게이션

- AboutView에서 데이터를 입력받아 HelloView로 이동하여 입력받은 데이터에게 인사하기

```vue
// AboutView.vue

<template>
  <div class="about">
    ...
    <input type="text"
    @keyup.enter="goToHello"
    v-model="inputData">
  </div>
</template>

<script>
  export default {
    name: 'AboutView',
    data() {
      return {
        inputData: null
      }
    },
    methods: {
      goToHello() {
        this.$router.push({ name: 'hello', params: {userName: this.inputData }})
      }
    }
  }
</script>
```

### route에 컴포넌트를 등록하는 또다른 방법

```js
// router/index.js

const routes = [
  {
    path: '/about',
    name: 'about',
    component: () => import('@/views/AboutView')
  }
]
```

> ### lazy-loading

- 모든 파일을 한 번에 로드하려고 하면 모든걸 다 읽는 시간이 매우 오래 걸림

- 미리 로드를 하지 않고 특정 라우트에 방문할 때, 매핑된 컴포넌트의 코드를 로드하는 방식을 활용할 수 있음

  - 모든 파일을 한 번에 로드하지 않아도 되기 때문에 최초에 로드하는 시간이 빨라짐

  - 당장 사용하지 않을 컴포넌트는 먼저 로드하지 않는 것이 핵심