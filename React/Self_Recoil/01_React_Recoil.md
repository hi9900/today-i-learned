# React Recoil

## React 애플리케이션 생성 후 Recoil 설치

```bash
$ npx create-react-app recoil-ex

$ npm install recoil
$ yarn add recoil
```

## Recoil Root

- recoil  상태를 사용하는 컴포넌트는 부모 트리 어딘가에 나타나는 `RecoilRoot`가 필요하다.
  
  보통 루트 컴포넌트에 `RecoilRoot`를 넣는다.

## Atom

- Atom은 상태(state)의 일부를 나타낸다.
  
  Atom은 어떤 컴포넌트에서나 읽고 쓸 수 있다.
  
  Atom의 값을 읽는 컴포넌트들은 암묵적으로 atom을 구독한다.
  
  Atom에 어떤 변화가 있으면 그 atom을 구독하는 모든 컴포넌트가 재렌더링 된다.

- Atom을 설정할 때는 `atom()`을 사용한다. `key`와 `default` 값을 필수러 선언해 주어야 한다.
  
  - `key`: 내부적으로 atom을 식별하는 데 사용되는 고유한 문자열. 어플리케이션 전체에서 다른 atom과 selector에 대해 고유해야 한다.
  
  - `default`: atom의 초깃값. 다양한 타입을 사용할 수 있으며, 동일한 타입의 값을 나타내는 다른 atom이나 selector도 가능하다.

- 컴포넌트가 atom을 읽고 쓰게 하기 위해서는 `useRecoilState()`를 사용한다.

## Selector

- Selector는 파생된 상태(derived state)의 일부를 나타낸다. 파생된 상태는 상태의 변화다.
  
  파생된 상태를 어떤 방법으로든 주어진 상태를 수정하는 순수 함수에 전달된 상태의 결과물로 생각할 수 있다.

- `get` 함수만 제공되면 Selector는 읽기만 가능한 `RecoilValueReadOnly` 객체를 반환한다.
  
  `set` 함수 또한 제공되며 (optional) Selector는 쓰기 가능한 `RecoilState` 객체를 반환한다.

- `get` 매개변수를 이용하여 atom이나 다른 selector를 참조할 수 있다.

- atom의 값이 같으면 내부적으로 반환 값을 메모이즈 하고 있어 캐싱된 값을 반환하므로, 요청을 줄이고 빠르게 값을 반환할 수 있지만 이로 인해 다른 문제가 발생할 수 있다.

### atom 및 selector 사용과 관련된 주요 hooks

- `useRecoilState()`: atom을 읽고 쓰기 위해 사용. 컴포넌트는 atom을 구독함

- `useRecoilValue()`: atom을 읽기만 할 때 사용. 컴포넌트는 atom을 구독함

- `useSetRecoilState()`: atom을 쓰려고만 할 때 사용

- `useResetRecoilState()`: atom을 default 값으로 초기화 할 때 사용

`useSetRecoilState()`와 `useResetRecoilState()` hook은 state를 구독하지 않는다. 따라서 atom 값이 변경되더라도 해당 컴포넌트는 리렌더링이 발생하지 않는다.

state를 변경하기만 하고 읽지 않는 경우 리렌더링을 방지하기 위해 다음과 같이 사용하는 것이 좋다.

```js
// bad
const [ value, setValue ] = useRecoilState(valueState);
setValue({...value, foo: 'bar'})

// good
const setValue = useSetRecoilState(valueState)
setMenu((prevValue) => ({ ...prevValue, foo: 'bar' }))
```