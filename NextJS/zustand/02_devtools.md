> zustand 카운트 예시에서 계속

## devtools

- devtools로 감싸면, 개발자 모드의 Redux 탭으로 디버깅 가능

```tsx
import { SetState, create } from "zustand";
import { devtools } from "zustand/middleware";

export interface CountState {
  count: number;
  increaseCount: () => void;
  decreaseCount: () => void;
  resetCount: () => void;
}

const initialState = {
  count: 0,
};

const counterStore = (set: SetState<CountState>) => ({
  count: 0,
  increaseCount: () => set((state) => ({ count: state.count + 1 })),
  decreaseCount: () => set((state) => ({ count: state.count - 1 })),
  resetCount: () => set(initialState),
});

const useCounter = create(devtools(counterStore));

export default useCounter;
```

## 프로덕션 빌드 시 삭제

- 디버깅 모드는 보안 등의 문제로 프로덕션 빌드 시에 삭제해야한다.

1. create 재정의

   > 타입스크립트와 zustand

   - `SetState` 사용 시 **The declaration was marked as deprecated here.** 에러
   - `StateCreator`의 첫 번째 제네릭 타입은 스토어의 상태(`CounterState`)를 나타내고, 두 번째 제네릭 타입은 미들웨어 배열을 나타냅니다. `[['zustand/devtools', never]]`는 `devtools` 미들웨어를 사용함을 나타내며, 특별한 타입 설정이 필요하지 않을 때 `never`를 사용합니다.
   - 이러한 방식으로 코드를 작성하면, `SetState`가 deprecated 되었음에도 불구하고, 타입 안전성을 유지하며 Zustand를 사용할 수 있습니다.

   ```tsx
   import { create, StateCreator } from "zustand";
   import { devtools } from "zustand/middleware";

   export interface CountState {
     count: number;
     increaseCount: () => void;
     decreaseCount: () => void;
   }

   const counterStore: StateCreator<
     CountState,
     [["zustand/devtools", never]]
   > = (set) => ({
     count: 0,
     increaseCount: () => set((state) => ({ count: state.count + 1 })),
     decreaseCount: () => set((state) => ({ count: state.count - 1 })),
   });

   // 프로덕션 환경에서는 DevTools를 비활성화합니다.
   const useCounter =
     process.env.NODE_ENV === "production"
       ? create<CountState>(counterStore)
       : create(devtools(counterStore, { name: "CounterStore" }));

   // or
   const useCounter = create(
     devtools(counterStore, {
       name: "CounterStore",
       enabled: !!(process.env.NODE_ENV !== "production"),
     })
   );

   export default useCounter;
   ```

2. 디버깅 툴 이름 지정

   ```tsx
   import { create, StateCreator } from "zustand";
   import { devtools } from "zustand/middleware";

   const enum counterActions {
     INCREASE = "counter/increase",
     DECREASE = "counter/decrease",
   }

   export interface CountState {
     count: number;
     increaseCount: () => void;
     decreaseCount: () => void;
   }

   const counterStore: StateCreator<
     CountState,
     [["zustand/devtools", never]]
   > = (set) => ({
     count: 0,
     increaseCount: () =>
       set(
         (state) => ({ count: state.count + 1 }),
         false,
         counterActions.INCREASE
       ),
     decreaseCount: () =>
       set(
         (state) => ({ count: state.count - 1 }),
         false,
         counterActions.DECREASE
       ),
   });

   const useCounter = create(
     devtools(counterStore, {
       name: "CounterStore",
       enabled: !!(process.env.NODE_ENV !== "production"),
     })
   );

   export default useCounter;
   ```
