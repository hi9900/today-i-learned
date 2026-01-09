# Vuex 시작하기

## 프로젝트 with vuex

```bash
$ vue create vuex-app
$ cd vuex-app
$ vue add vuex
```

- src / store / index.js 가 생성됨

> vuex의 핵심 컨셉 4가지

### 1. state

  - vue 인스턴스의 data에 해당

  - 중앙에서 관리하는 모든 상태 정보

  - 개별 component는 state에서 데이터를 가져와서 사용

    - 개별 component가 관리하던 data를 중앙 저장소(Vuex Store의 state)에서 관리하게 됨

  - state의 데이터가 변화하면 해당 데이터를 사용(공유)하는 component도 자동으로 다시 렌더링

  - `$store.state`로 state 데이터에 접근

### 2. mutations

  - 실제로 state를 변경하는 유일한 방법

  - vue 인스턴스의 methods에 해당하지만 Mutations에서 호출되는 핸들러(handler) 함수는 반드시 동기적이어야 함

    - 비동기 로직으로 mutations를 사용해서 state를 변경하는 경우, state의 변화의 시기를 특정할 수 없기 때문

  - 첫 번째 인자로 `state`를 받으며, component 혹은 Actions에서 `commit()` 메서드로 호출됨

  > mutation, action에서 호출되는 함수를 handler 함수라고 함

### 3. actions

  - mutations과 비슷하지만 비동기 작업을 포함할 수 있다는 차이가 있음

  - state를 직접 변경하지 않고 `commit()` 메서드로 mutations를 호출해서 state를 변경함

  - context 객체를 인자로 받으며, 이 객체를 통해 store.js의 모든 요소와 메서드에 접근할 수 있음

    즉, state를 직접 변경할 수는 있지만 하지 않아야 함

  - component에서 `dispatch()` 메서드에 의해 호출됨

### 4. getters

  - vue 인스턴스의 computed에 해당

  - state를 활용하여 계산된 값을 얻고자 할 때 사용

    state의 원본 데이터를 건들지 않고 계산된 값을 얻을 수 있음

  - computed와 마찬가지로 getters의 결과는 캐시(cache)되며, 종속된 값이 변경된 경우에만 재계산됨

  - getters에서 계산된 값은 state에 영향을 미치지 않음

  - 첫번째 인자로 `state`, 두번째 인자로 `getter`을 받음

## Vuex에서 데이터 관리

- Vuex를 사용한다고 해서 모든 데이터를 state에 넣어야 하는 것은 아님

- Vuex에서도 여전히 pass props, emit event를 사용하여 상태를 관리할 수 있음

- 개발 환경에 따라 적절하게 사용하는 것이 필요함

