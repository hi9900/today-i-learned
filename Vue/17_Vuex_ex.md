# Vuex 실습

```js
// store/index.js

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
```

## state

- 중앙에서 관리하는 모든 상태 정보

- `$store.state`로 접근 가능

- store의 state에 massage 데이터 정의

```js
// store/index.js

...
export default new Vuex.Store({
  state: {
    message: 'message in store'
  },
```

- component에서 state 사용

```vue
// App.vue

<template>
  <div id="app">
    <h1>{{ $store.state.message }}</h1>
  </div>
</template>
```

- `$store.state`로 바로 접근하는 것 보다 `computed`에 정의 후 접근하는 것을 권장

```vue
// App.vue

<template>
  <div id="app">
    <h1>{{ message }}</h1>
  </div>
</template>

<script>
  export default {
    name: 'App',
    computed: {
      massage() {
        return this.$store.state.message
      }
    }
  }
</script>
```

## actions

- state를 변경할 수 있는 mutation 호출

- component에서 `dispatch()`에 의해 호출됨

  - `dispatch(A, B)`

    A: 호출하고자 하는 actions 함수

    B: 넘겨주는 데이터(payload)

- actions에 정의된 changeMessage 함수에 데이터 전달하기

```vue
// App.vue

<template>
  <div id="app">
    ...
    <input type="text"
    @keyup.enter="changeMessage"
    v-model="inputData"
    >
  </div>
</template>

<script>
  export default {
    ...
    data() {
      return {
        inputData: null,
      }
    },
    methods: {
      changeMessage() {
        const newMessage = this.inputData
        this.$store.dispatch('changeMessage', newMessage)
        this.inputData = null
      }
    }
  }
</script>
```

- actions의 첫번째 인자는 `context`

  - context는 store의 전반적인 속성을 모두 가지고 있으므로 context.state와 context.getters를 통해 mutations를 호출하는 것이 모두 가능

  - dispatch()를 사용해 다른 actions도 호출할 수 있음

  - 단, actions에서 state를 직접 조작하는 것은 삼가야 함

- actions의 두번째 인자는 `payload`

  - 넘겨준 데이터를 받아서 사용

```js
// store/index.js

export default new Vuex.Store({
  ...
  actions: {
    changeMessage(context, message) {
      console.log(context)
      console.log(message)
    }
  }
})
```

## mutations

- actions에서 `commit()`을 통해 mutation 호출하기

- mutations는 state를 변경하는 유일한 방법

- component 또는 actions에서 `commit()`에 의해 호출됨

  - commit(A, B)

    A: 호출하고자 하는 mutations 함서

    B: payload

- mutations 함수의 첫번째 인자는 state, 두번째 인자는 payload

```js
// store/index.js

export default new Vuex.Store({
  ...
  mutations: {
    CHANGE_MESSAGE(state, message) {
      state.message = message
    }
  },
  actions: {
    changeMessage(context, message) {
      context.commit('CHANGE_MESSAGE', message)
    }
  },
})
```

## getters

- getters는 state를 활용한 새로운 변수

- getters 함수의 첫번째 인자는 state, 두번째 인자는 getters

```js
// store/index.js

export default new Vuex.Store({
  ...
  getters: {
    messageLength(state) {
      return state.message.length
    },
    // getters의 다른 함수를 사용한 함수
    doubleLength(state, getters) {
      return getters.messageLength * 2
    }
  },
})
```

- getters 출력하기

- state와 마찬가지로 computed에 정의해서 사용하는 것을 권장

```vue
// App.vue

<script>
  export default {
    ...
    computed: {
      messageLength() {
        return this.$store.getters.messageLength
      },
      doubleLength() {
        return this.$store.getters.doubleLength
      },
    }
  }
</script>
```

## mutations으로만 state를 변경

- mutations으로만 state를 변경할 수 있음

- 저장소의 각 컨셉(state, getters, mutations, actions)은 각자의 역할이 존재하도록 설계되어 있음

- actions의 로직이 특별한 작업 없이 단순히 mutations만을 호출하는 경우도 있으나,

  Vuex 도입의 적절성을 판단해 볼 필요가 있음

## Vuex의 사용

- Vuex는 공유된 상태 관리를 처리하는 데 유용하지만, 개념에 대한 이해와 시작하는 비용이 큼

- 애플리케이션이 단순하다면 Vuex가 없는 것이 더 효율적일 수 있음

- 그러나, 중대형 규모의 SPA를 구축하는 경우 Vuex는 자연스럽게 선택할 수 있는 단계가 오게 됨

- 결과적으로 역할에 적절한 상황에서 활용했을 때, Vuex 라이브러리 효용을 극대화할 수 있음

- 즉, 필요한 순간이 왔을 때 사용하는 것을 권장