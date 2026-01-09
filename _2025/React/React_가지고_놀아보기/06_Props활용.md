## Props 활용 방법 (Counter 프로젝트)

- Props: 부모 컴포넌트에게서 받는 데이터

### Number

- App.js 에서 선언한 state를 Number라는 컴포넌트를 만들어 전달 후 Number 컴포넌트에서 이 값을 화면에 출력

  - props를 인자값으로 받아와 속성명으로 출력

  ```js
  // src/components/Number.js

  import React from 'react';
  import { styled } from 'styled-components';

  const Count = styled.div`
    padding: 5px 0;
    width: 200px;
    text-align: center;
    border: 1px solid black;
    font-size: 2rem;
  `

  const Number = props => {
    return (
      <Count>
        {props.number}
      </Count>
    );
  };

  export default Number
  ```

  - Destructing Assignment 문법 활용

  ```js
  ...
  const Number = ({ number }) => {
  return (
    <Count>
      {number}
    </Count>
  );
  };
  ...
  ```

  - App 컴포넌트에서 state 값 전달

  ```js
  // src/App.js

  ...
  return (
    <Wrapper>
      ...
      <Number number={number} />
    </Wrapper>
    )
  ```

### CountButton

  - CountButton 컴포넌트를 만들어 number 값을 바꾸는 함수를 전달받아 컴포넌트 클릭 시 함수가 실행되도록 만듦

  - onClick, text 속성이 들어있는 Props를 받아옴

  ```js
  // src/components/CountButton.js

  import React from 'react'
  import { styled } from 'styled-components'

  const Button = styled.button`
    font-size: 20px;
    font-weight: 700;
    width: 50px;
    padding: 10px 0;
    border: 1px solid black;
    background: white;

    & + & {
      margin-left: 10px;
    }
  `

  const CountButton = ({ onClick, text }) => {
    return (
      <Button onClick={onClick}>
        {text}
      </Button>
      )
  }

  export default CountButton
  ```

  - App 컴포넌트에서 CountButton 컴포넌트 불러오기

  ```js
  // src/App.js

  ...
  return (
    <Wrapper>
      <ButtonWrapper>
        <CountButton onClick={countUp} text="+" />
        <CountButton onClick={countDown} text="-" />
      </ButtonWrapper>
      ...
    </Wrapper>
    )  
  ```