# 스토어와 슬라이스

## 스토어(store)

- Zustand에서 애플리케이션의 전역 상태를 저장하고 관리하는 역할을 하는 객체나 공간

## 슬라이스(slice)

- 스토어 내의 상태를 특정 기능이나 도메인 별로 나눈 작은 단위
- 사용자 정보 관리, 주문 내역 관리 등과 같이 각각의 독립적인 기능에 대한 상태 관리 로직을 슬라이스로 분리할 수 있다.

# Zustand의 슬라이스 패턴

- [공식문서 - slices-pattern](https://docs.pmnd.rs/zustand/guides/slices-pattern)
- [공식문서 - typescript-slices-pattern](https://docs.pmnd.rs/zustand/guides/typescript#slices-pattern)

- 하나의 store를 두고 상태마다 Slice를 만들어 병합하는 식
- 애플리케이션의 상태 관리를 더 모듈화하고 구조화하기 위한 방법
- 상태를 여러 개의 독립적인 부분으로 나누어 관리할 수 있게 해 주고, 각각의 기능 별로 상태 관리 코드를 분리하고 싶을 때 유용하다.

## 1. 적용

- 일반적인 접근 방식은 단순히 여러 개의 create 호출을 통해 각각의 스토어를 만들고, 이들 각각을 기능 별로 관리하는 것이다.
- 보다 구조적으로 슬라이스 패턴을 적용하고 싶다면, 상태 관리 로직을 함수나 객체로 분리하고, 분리된 함수/객체를 조합해서 최종적인 스토어를 만들 수 있다.

## 2. 예시

1. 두 개의 작은 store 생성

```ts
// fishSlice.ts
export const createFishSlice = (set) => ({
  fishes: 0,
  addFish: () => set((state) => ({ fishes: state.fishes + 1 })),
});

// bearSlice.ts
export const createBearSlice = (set) => ({
  bears: 0,
  addBear: () => set((state) => ({ bears: state.bears + 1 })),
  eatFish: () => set((state) => ({ fishes: state.fishes - 1 })),
});
```

2. 하나의 store로 병합

- 직접적으로 슬라이스 결합 메커니즘을 제공하는 것은 아니고, 개발자가 이런 구조를 직접 설계해야 한다
- 슬라이스의 상태와 업데이터 함수들을 수동으로 결합하는 경우, 아래와 같이 선언할 수 있다.
- 다만 수동으로 결합하는 방식은 간단한 경우에는 잘 작동하지만, 스토어가 커지고 복잡해질수록 당연히 관리가 어렵다.

```ts
// boundStore.ts
import { create } from "zustand";
import { createBearSlice } from "./bearSlice";
import { createFishSlice } from "./fishSlice";

export const useBoundStore = create((...a) => ({
  ...createBearSlice(...a),
  ...createFishSlice(...a),
}));
```

3. Component에서 사용

```tsx
"use client";

import useBoundStore from "@/stores/boundStore";

export default function SlicePattern() {
  const bears = useBoundStore((state) => state.bears);
  const fishes = useBoundStore((state) => state.fishes);
  const addBear = useBoundStore((state) => state.addBear);
  return (
    <div>
      <h2>Number of bears: {bears}</h2>
      <h2>Number of fishes: {fishes}</h2>
      <button type="button" onClick={() => addBear()}>
        Add a bear
      </button>
    </div>
  );
}
```

4. 여러 개의 store update

- 하나의 function으로 여러 store을 업데이트 할 수 있다.

```ts
// bearFishSlice.ts
export const createBearFishSlice = (set, get) => ({
  addBearAndFish: () => {
    get().addBear();
    get().addFish();
  },
});
```

5. 타입 지정 및 수정

> **StateCreator**: Zustand에서 사용되는 제네릭 타입
>
> Zustand 스토어의 상태를 생성하는 함수의 타입을 정의할 때 사용된다.

```ts
StateCreator<BearSlice & FishSlice, [], [], BearSlice>;
```

- `BearSlice & FishSlice`

  - BearSlice 타입과 FishSlice 타입이 합쳐진 새로운 타입을 의미
  - `&` 연산자는 TypeScript의 교차 타입(intersection type)을 나타낸다. 즉, BearSlice와 FishSlice 두 타입이 가지는 속성들을 모두 합친 형태의 타입을 첫 번째 인자로 사용한다.
  - 이는 스토어가 BearSlice와 FishSlice 두 영역의 상태를 모두 관리할 수 있음을 의미한다.

- `[]`

  - 두 번째와 세 번째 인자는 Zustand 미들웨어를 위한 공간
  - 여기서 빈 배열 []은 추가적인 미들웨어가 사용되지 않음을 나타냄

- `BearSlice`

  - 네 번째 인자는 이 StateCreator를 통해 생성되는 스토어의 상태의 "슬라이스"를 지정한다.
  - 여기서는 BearSlice만을 지정하고 있는데, 이는 해당 상태 생성자가 주로 BearSlice 관련 상태를 다루는 데 초점을 맞추고 있음을 나타낸다.
  - 그러나 첫 번째 인자에서 BearSlice & FishSlice를 사용함으로써, 실제 스토어의 상태는 FishSlice의 상태도 포함하고 있음을 알 수 있다.

---

## 수정된 전체 코드

<details>
<summary>코드 보기</summary>

```ts
// boundStore.ts
import { StateCreator, create } from "zustand";
import { devtools } from "zustand/middleware";

const enum BoundActions {
  ADD_BEAR = "bear/AddBear",
  EAT_FISH = "fish/EatFish",
  ADD_FISH = "fish/AddFish",
}

interface BearSlice {
  bears: number;
  addBear: () => void;
  eatFish: () => void;
}

interface FishSlice {
  fishes: number;
  addFish: () => void;
}

interface SharedSlice {
  addBoth: () => void;
  getBoth: () => void;
}

const createBearSlice: StateCreator<
  BearSlice & FishSlice,
  [["zustand/devtools", never]],
  [],
  BearSlice
> = (set) => ({
  bears: 0,
  addBear: () =>
    set((state) => ({ bears: state.bears + 1 }), false, BoundActions.ADD_BEAR),
  eatFish: () =>
    set(
      (state) => ({ fishes: state.fishes - 1 }),
      false,
      BoundActions.EAT_FISH
    ),
});

const createFishSlice: StateCreator<
  BearSlice & FishSlice,
  [["zustand/devtools", never]],
  [],
  FishSlice
> = (set) => ({
  fishes: 0,
  addFish: () =>
    set(
      (state) => ({ fishes: state.fishes + 1 }),
      false,
      BoundActions.ADD_FISH
    ),
});

const createSharedSlice: StateCreator<
  BearSlice & FishSlice,
  [["zustand/devtools", never]],
  [],
  SharedSlice
> = (set, get) => ({
  addBoth: () => {
    get().addBear();
    get().addFish();
  },
  getBoth: () => get().bears + get().fishes,
});

type BoundSlice = BearSlice & FishSlice & SharedSlice;

const useBoundStore = create<BoundSlice>()(
  devtools(
    (...a) => ({
      ...createBearSlice(...a),
      ...createFishSlice(...a),
      ...createSharedSlice(...a),
    }),
    { name: "BoundStore", enabled: !!(process.env.NODE_ENV !== "production") }
  )
);

export default useBoundStore;
```

</details>
