# React Redux

## Counter에 Redux 적용하기

### 라이브러리 설치

- `redux`, `react-redux`: 리액트에서 Redux를 사용할 수 있게 해주는 라이브러리

- `redux-actions`, `immer`: Redux를 더 쉽게 사용해주는 라이브러리

  - `redux-actions`: 액션 생성자와 리듀서 함수를 더 쉽게 만들어주는 라이브러리

  - `immer`: 스토어의 불변성 관리를 위해 사용하는 라이브러리

    State와 마찬가지로 Redux에서 불변성을 지키지 않는다면 컴포넌트 리렌더링을 보장받지 못하고, 최적화를 할 수 없기 때문에 꼭 불변성을 보장해야 함

```bash
$ yarn add redux react-redux redux-actions immer
```

### Reducer

- Redux 공식 홈페이지에서 사용한 패턴은 액션 관련 부분과 리듀서 관련 부분을 분리하는 것이지만

  이 방식을 따라가지 않고 하나의 파일에 모두 작성하는 Ducks 패턴

> ### Ducks 패턴을 사용할 때 지켜야 하는 룰

1. MUST export default a function called reducer()

  - 리듀서 함수는 반드시 default export 해야 함

2. MUST export its action creators as functions

  - 액션 생성자는 반드시 함수로 export 해야 함

3. MUST have action types in the form npm-module-or-app/reducer/ACTION_TYPE

- 액션 타입의 형식은 반드시 `npm-module-or-app/reducer/ACTION_TYPE`과 같은 형태를 따라야 함

4. MAY export its action types as UPPER_SNAKE_CASE, if an external reducer needs to listen for them, or if it is a published reusable library

- 액션 타입들을 UPPER_SNAKE_CASE로 export 할 수도 있음

- 3번째 규칙은 리듀서 함수의 개수가 많을 때 액션 객체를 구별하기 위한 용도이므로 리듀서 함수가 단 한 개인 Counter 프로젝트에서는 편의에 맞게 액션 타입만 명시함

하지만, Redux 코드를 작성할 때는 룰에 맞춰 작성하는 습관 들이기

```js
// src/store/reducer.js

const INCREASE = "INCREASE"
const DECREASE = "DECREASE"

export const increase = number => ({
  type: INCREASE,
  payload: number
})

export const decrease = number => ({
  type: DECREASE,
  payload: number
})

const initialState = {
  number: 0
}

const reducer = (state = initialState, action) => {
  switch (action.type) {
    case "INCREASE":
      return { number: action.payload }
    case "DECREASE":
      return { number: action.payload }
    default:
      return state
  }
}

export default reducer
```

- reducer.js에서 Ducks 패턴을 사용해 액션 생성자와 리듀서 함수를 작성했다면

  index.js에서는 이런 리듀서 함수들을 모아 스토어를 만들고 반환하는 역할

- 여기서 Redux Middleware를 적용할 수도 있음

  비동기 처리, 로그 작성 등과 같은 작업을 미들웨어로 처리하지만, 지금은 필요하지 않음

```js
// src/store/index.js

import reducer from './reducer'

export default reducer
```

### 스토어 연결

- Redux 디버깅 또는 테스팅을 위한 확장 프로그램 설치

  [Chrome Redux DevTools](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd)

```js
// src/index.js

import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import reportWebVitals from './reportWebVitals';

import { Provider } from 'react-redux'
import { createStore } from 'redux'
import reducer from './store'

const root = ReactDOM.createRoot(document.getElementById('root'));

// 스토어 생성 (리듀서 함수 연결 및 Redux Devtools Extension 연결)
const store = createStore(reducer, window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__());

root.render(
  <Provider store={store}>
    <App />
  </Provider>
)

reportWebVitals();
```

### App 컴포넌트

> connect 함수

  - 상태 값을 받아오거나 변경하기 위해 해당 컴포넌트에 스토어를 연결하기 위해 사용하는 것

  - react-redux 라이브러리에 있는 함수로, 복잡한 store 구독 과정을 알아서 처리해주는 함수

  ```js
  export default connect(mapStateToProps, mapDispatchToProps)(App)
  ```

> connect 함수의 인자값

1. mapStateToProps

  스토어의 상태 값을 Props로 매핑하는 함수

  state를 인자값으로 받아와 props로 넘겨줄 값을 json 형태로 반환

  ```js
  const mapStateToProps = state => ({
    number: state.number
  })
  ```

2. mapDispatchToProps

  액션 생성자를 Props로 매핑하는 함수

  dispatch 함수를 인자값으로 받아와 props로 넘겨줄 값을 json 형태로 반환

  ```js
  const mapDispatchToProps = dispatch => ({
    increase: number => dispatch(increase(number)),
    decrease: number => dispatch(decrease(number)),
  })

  // 더 간단하게 표현한 방식
  // props로 counterAction을 받아 counterActions.increase와 같은 형식으로 함수 사용 가능
  // bindActionCreators는 redux 라이브러리에서 제공
  const mapDispatchToProps = dispatch => ({
    counterActions: bindActionCreators(counterActions, dispatch)
  })
  ```

```js
// src/App.js

import React from "react"
import CountButton from "./components/CountButton"
import Number from "./components/Number"
import styled from "styled-components"
import { connect } from "react-redux"
import { decrease, increase } from "./store/reducer"


const Wrapper = styled.div`
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100px;
  margin-top: 100px;
`;

const ButtonWrapper = styled.div`
  width: 100%;
  display: flex;
  justify-content: space-between;
  margin-bottom: 50px;
`;

// Redux
const App = ({ number, increase, decrease }) => {
  return (
    <Wrapper>
      <ButtonWrapper>
        <CountButton onClick={() => increase(number + 1)} text="+" />
        <CountButton onClick={() => decrease(number - 1)} text="-" />
      </ButtonWrapper>
      <Number number={number} />
    </Wrapper>
  )
}

const mapStateToProps = state => ({
  number: state.number
})

const mapDispatchToProps = dispatch => ({
  increase: number => dispatch(increase(number)),
  decrease: number => dispatch(decrease(number))
})

export default connect(mapStateToProps, mapDispatchToProps)(App)
```

- redux 라이브러리에서 제공하는 bindActionCreator 함수를 사용하면 쉽게 여러 액션 생성자 함수를 dispatch에 연결할 수 있음

---

## redux-actions

- redux 코드 줄이기

- 리듀서 함수 내에서 불변성은 필수 요소이고, 불변성을 지키는 만큼 모드도 매우 복잡해짐

- 이를 위한 라이브러리가 `Immer`

  `Immutable`이라는 라이브러리도 존재하지만, get, set 함수 등올 통해 상태 값을 변경해야 한다는 불편함이 존재하기 때문에 Immer 사용

```js
// src/store/reducer.js

import { createAction, handleActions } from "redux-actions"
import { produce } from "immer"

const INCREASE = "INCREASE"
const DECREASE = "DECREASE"

export const increase = createAction(INCREASE, number => number)
export const decrease = createAction(DECREASE, number => number)

const initialState = {
  number: 0
}

export default handleActions({
  [INCREASE]: (state, action) =>
    produce(state, draft => {
      draft.number = action.payload
    }),
  [DECREASE]: (state, action) =>
    produce(state, draft => {
      draft.number = action.payload
    })
}, initialState)
```

### 1. createAction

  - 간편하게 액션 생성자를 만들어주는 함수

  - 인자값으로 2가지를 넘기는 데, 하나는 액션 타입이고 다른 하나는 payloadCreator

  - 액션 타입은 위에서 정의했던 액션 타입 상수를 넣었고,

    payloadCreator는 함수의 형태로 넘겨줌

    어떤 데이터를 받는다는 것을 명시하기 위함. payloadCreator는 생략 가능

### 2. handleActions

  - Redux의 핵심 부분인 리듀서 부분을 더 간편하게 만들어주는 함수

  - 인자값으로 2가지를 넘기는 데, 하나는 리듀서이고 다른 하나는 initialState 값

  - 작동 방식은 스위치문으로 작성된 리듀서와 동일함

### Immer 라이브러리

  - Immer 라이브러리를 사용하면 마치 불변성을 신경쓰지 않는 것처럼 코드를 짜도 상관 없음

    알아서 불변성을 관리해줌

  - 현재 상태를 임시적인 Draft에 적용하고, 사용자는 이 Draft를 수정함

  - 수정작업이 모두 완료되면 Draft를 통해 새로운 상태를 만들어 반환

  - 스토어 내에서 불변성을 관리하는 과정에서 실수할 수 있기 때문에 이와 같은 라이브러리를 사용하는 것이 좋음