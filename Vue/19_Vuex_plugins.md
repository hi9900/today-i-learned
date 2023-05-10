# plugins

- Vuex store에 추가적인 기능을 제공하는 확장 기능

- 일반적으로 state의 변화를 감지해, 어플리케이션의 성능을 최적화하는 목적을 가짐

## vuex-persistedstate

- Vuex store의 상태를 브라우저 local storage에 저장해주는 plugin

- 페이지를 새로고침하거나 브라우저를 종료하였다가 다시 열었을 때, 이전 상태를 유지할 수 있도록 해줌

> ### 설치 후 적용

```bash
$ npm i vuex-persistedstate
```

```js
// index.js

import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
})
```

- 메시지 입력 후, Local Storage: vuex key에 state의 message가 가진 값들이 value로 할당됨

> ### 추가 옵션

- 추가 옵션을 사용하여 필요에 따라 저장 방식을 변경할 수 있음

```js
// index.js

import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

const persistedState = createPersistedState({
  // key를 변경
  key: 'my-app',
  // 저장 위치를 변경
  storage: window.localStorage,
  // 상태 중 일부만 저장
  reducer: state => ({
    message: state.message
  })
})

export default new Vuex.Store({
  plugins: [
    persistedState,
  ],
  state: {
    message: 'message in store',
    age: 20,
  }
})
```