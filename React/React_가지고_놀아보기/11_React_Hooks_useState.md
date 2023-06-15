# React Hooks

- 상태관리를 할 수 있는 Hooks인 useState

> Counter 프로젝트

```js
// src/App.js

import React, { useState } from "react";
import CountButton from "./components/CountButton";
import Number from "./components/Number";
import styled from "styled-components";

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

const App = () => {
  const [ number, setNumber ] = useState(0)

  return (
    <Wrapper>
      <ButtonWrapper>
        <CountButton onClick={() => setNumber(number + 1)} text="+" />
        <CountButton onClick={() => setNumber(number - 1)} text="-" />
      </ButtonWrapper>
      <Number number={number} />
    </Wrapper>
  );
}

export default App;
```

`const [ number, setNumber ] = useState(0);`

- userState는 상태 값과 상태 값을 변화시키는 함수를 배열형식으로 반환하는데, 여기서는 Destructing Assignment 문법을 통해 필요한 값을 불러옴

- useState의 인자는 상태 값의 초기값에 해당, 처음 number는 0

`<CountButton onClick={() => setNumber(number + 1)} text="+" />`

- 핸들러 함수 내부에 setNumber 함수를 통해 number의 값을 1씩 증가 또는 감소

- 이와 같은 형식으로 useState를 사용함