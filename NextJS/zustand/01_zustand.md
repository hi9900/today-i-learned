# Zustand란?

- 독일어로 "상태"라는 뜻

- Redux Devtools를 사용한 Debugging이 가능

> Zustand 설치

```bash
$ npm i zustand
or
$ yarn add zustand
```

# Zustand 동작 원리 이해하기

- zustand는 발행/구독 모델 기반으로 이루어져 있으며, 내부적으로 스토어 상태를 클로저로 관리한다.

  ```tsx
  // vanilla.ts
  const createStoreImpl = (createState) => {
    let state;
    const listeners = new Set();

    const setState = (partial, replace) => {
      // ... (생략)
    };

    const getState = () => state;

    const subscribe = (listener) => {
      // ... (생략)
    };

    const api = { setState, getState, subscribe };
    state = createState(setState, getState, api);

    return api;
  };

  export const createStore = (createState) =>
    createState ? createStoreImpl(createState) : createStoreImpl;
  ```

## setState

- 상태를 변경하는 setState함수
- 인자가 _function_ 타입일 경우 현재 상태를 인자로 넘겨 nextState를 정의한다.
- nextState와 state가 다르다면, `Object.assign`을 이용해 상태를 갱신한다.

```tsx
const setState = (partial, replace) => {
  const nextState = typeof partial === "function" ? partial(state) : partial;

  if (!Object.is(nextState, state)) {
    const previousState = state;
    state =
      replace ?? typeof nextState !== "object"
        ? nextState
        : Object.assign({}, state, nextState);

    listeners.forEach((listener) => listener(state, previousState));
  }
};
```

## subscribe

- 상태를 구독하는 subscribe 함수
- 구독을 해제하는 함수 또한 리턴하고 있다.

```tsx
const subscribe = (listener) => {
  listeners.add(listener);

  return () => listeners.delete(listener);
};
```

---

# Zustand 사용 예시

- 카운터 예시

1. store 생성

```tsx
// store.ts

import { create } from "zustand";

export interface CountState {
  count: number;
  increaseCount: () => void;
  decreaseCount: () => void;
}

export const useCounter = create<CountState>((set) => ({
  count: 0,
  increaseCount: () => set((state) => ({ count: state.count + 1 })),
  decreaseCount: () => set((state) => ({ count: state.count - 1 })),
}));
```

2. 컴포넌트에서 사용

```tsx
"use client";

import { useCounter } from "@/store/store";

export default function Counter() {
  const { count, increaseCount, decreaseCount } = useCounter();
  return (
    <>
      <div>{count}</div>
      <button type="button" onClick={increaseCount}>
        + 1
      </button>
      <button type="button" onClick={decreaseCount}>
        - 1
      </button>
    </>
  );
}
```

- 고수 사용법

  react의 비교로직과 달리 state로 가져온 사용법은 `===` 연산자를 쓰기 때문에 조금 더 효율적인 랜더링이 가능하다.

  ```tsx
  import { shallow } from "zustand/shallow";

  // 일반 사용법
  const { increment } = useCounter();

  // 고수 사용법 1
  const increment = useCounter((state) => state.increment);

  // 고수 사용법 2 shallow
  const { increment, decrement } = useCounter(
    (state) => ({
      increment: state.increment,
      decrement: state.decrement,
    }),
    shallow
  );
  ```

3. 카운트 초기화

- 초깃값을 지정

```tsx
import create from "zustand";

export interface CountState {
  count: number;
  increaseCount: () => void;
  decreaseCount: () => void;
  resetCount: () => void;
}

const initialState = {
  count: 0,
};

export const useCounter = create<CountState>((set) => ({
  count: 0,
  increaseCount: () => set((state) => ({ count: state.count + 1 })),
  decreaseCount: () => set((state) => ({ count: state.count - 1 })),
  resetCount: () => set(initialState),
}));
```
