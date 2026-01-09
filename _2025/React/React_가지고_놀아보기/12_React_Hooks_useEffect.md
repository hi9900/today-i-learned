# React Hooks

## useEffect

- useEffect에서는 총 3개의 LifeCycle API를 구현할 수 있음

  componentDidMount, componentDidUpdate, componentWillUnmount

> Counter 프로젝트

```js
// 경로 : src/App.js

import React, { useState, useEffect } from "react";
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
  const [ number, setNumber ] = useState(0);

  useEffect(() => {
    console.log("useEffect -> componentDidMount");

    return () => {
      console.log("useEffect -> componentWillUnmount");
    }
  }, []);

  useEffect(() => {
    console.log(`componentDidUpdate (number) -> ${number}`);
  }, [number]);

  useEffect(() => {
    console.log("useEffect -> componentDidUpdate");
  });

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

- useEffect는 하나의 컴포넌트에서 여러 개 사용 가능

> 첫 번째 useEffect

  - 해당 Hooks에서는 첫 번째 인자로 함수를 받았고, 두 번째 인자로 빈 배열을 받음

  - 첫 번째 인자값인 함수는 특정 시기에 실행될 함수

  - 두 번째 인자값인 빈 배열은 컴포넌트가 처음 렌더링 될 때만 실행하라는 의미

  - 따라서 이 useEffect는 componentDidMount와 동일한 기능을 가짐

  - 해당 Hooks에서 두 번째 인자값으로 빈 배열을 받을 때, return 구문의 함수는 componentWillUnmount와 동일한 기능을 가짐

> 두 번째 useEffect

  - 두 번째 인자값으로 비어있지 않은 배열을 받음

  - 배열 안에는 state, props등과 같은 값이 들어올 수 있음

  - 만약 배열 안에 어떤 변수가 들어있다면, 해당 useEffect는 그 변수의 값이 변경될 때 함수를 실행시킴

    따라서 number 값을 변경했을 때, 콘솔창에 기록이 남음

> 세 번째 useEffect

  - 두 번째 인자값이 없다는 것은 컴포넌트가 업데이트될 때 실행하라는 의미

  - 따라서 컴포넌트가 리렌더링될 때 언제든 함수가 실행됨
