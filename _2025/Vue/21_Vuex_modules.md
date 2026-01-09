# Modules

- Vuex store을 여러 파일로 나눠서 관리할 수 있게 해주는 기능

- Vuex store과 동일한 구성을 가진 별도의 객체를 정의하여 modules 옵션에 작성한 객체를 추가하여 사용

- 별개의 `.js`파일에 정의하고 import 하는 방식으로도 사용가능

- Store의 가독성을 향상시킬 수 있음

> 별도의 js 파일에 객체 정의

```js
// store/modules/myModule.js

const myModule = {
  state: {
    level: 20,
  },
  mutations: {
    INCREMENT_Level(state) {
      state.level += 1
    }
  },
  actions: {
    incrementLebel(context) {
      context.commit('INCREMENT_Level')
    }
  }
}

export default myModule
```

> 정의한 js파일의 객체를 import
> 
> Store의 modules 옵션에 추가

```js
// store/index.js

import Vue from 'vue'
import Vuex from 'vuex'
import myModule from './module/myModule'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    myModule,
  }
})
```