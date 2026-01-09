## useState를 통해 컴포넌트에서 바뀌는 값 관리하기

- 컴포넌트에서 보여줘야 하는 내용이 사용자 인터랙션에 따라 바뀌어야 할 때 어떻게 구현할 수 있는 지에 대해 알아보기

- 리액트 16.8 이전 버전에서는 함수형 컴포넌트에서 상태를 관리할 수 없었지만,

  16.8 에서 Hooks라는 기능이 도입되면서 함수형 컴포넌트에서도 상태를 관리할 수 있게 되었다.

- 리액트 Hooks 중 하나인 useState라는 함수를 사용한 Counter 컴포넌트 예제

### 이벤트 설정

- Counter에서 버튼이 클릭되는 이벤트가 발생했을 때, 특정 함수가 호출되도록 설정

- Counter 컴포넌트에 `onIncrease`와 `onDecrease` 함수 구현 후 버튼 연결

> 리액트에서 엘리먼트에 이벤트를 설정해줄 때는 `on이벤트이름={실행하고싶은 함수}` 형태로 설정해야 한다.

  `onClick={onIncrease()}`

  이렇게 하면 렌더링되는 시점에서 함수가 호출되버리기 때문에 이벤트를 설정할 때는 함수 타입의 값을 넣어줘야 한다.

  `onClick={onIncrease}`

### 동적 값 넣기, useState

- 컴포넌트에서 동적인 값을 상태(state)라고 부른다.

  리액트의 `useState` 함수를 사용하여 컴포넌트에서 상태를 관리할 수 있다.

`import React, { useState } from 'react';`

- 리액트 패키지에서 useState 함수를 불러온 후 사용한다.

`const [number, setNumber] = useState(0);`

- useState를 사용할 때는 상태의 기본값을 파라미터로 넣어서 호출해준다.

  이 함수를 호출해주면 배열이 반횐되는데, 첫번째 원소는 현재 상태, 두번째 원소는 Setter 함수이다.

- 배열 비구조화 할당을 통해 각 원소를 추출할 수 있다.

  ```js
  const numberState = useState(0);
  const number = numberState[0];
  const setNumber = numberState[1];
  ```

- Setter 함수는 파라미터로 전달받은 값을 최신 상태로 설정해준다.

### 함수형 업데이트

- 지금은 Setter 함수를 사용할 때, 업데이트 하고 싶은 새로운 값을 파라미터로 넣어주고 있는데,

  그 대신 기존 값을 어떻게 업데이트 할 지에 대한 함수를 등록하는 방식으로도 값을 업데이트 할 수 있다.

```js
const onIncrease = () => {
  setNumber(prevNumber => prevNumber + 1);
}

const onDecrease = () => {
  setNumber(prevNumber => prevNumber - 1);
}
```

- setNumber를 사용할 때 그 다음 상태를 파라미터로 넣어준 것이 아니라, 

  값을 업데이트하는 함수를 파라미터로 넣어주었다.

- 함수형 업데이트는 주로 컴포넌트를 최적화 할 때 사용하게 된다.