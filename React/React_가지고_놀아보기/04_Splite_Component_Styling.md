# Split Component & Styling

## Split Component

- 컴포넌트를 나눌 때에는 주로 기능 별로 나눔

> ### 전화번호부 프로젝트의 컴포넌트

1. App

  렌더링 할 컴포넌트로 components 디렉토리에 있는 PhoneList 컴포넌트와 InputBox 컴포넌트를 포함

2. InputBox

  이름과 전화번호를 입력받는 폼이 있는 컴포넌트

3. PhoneList

  여러 개의 PhoneItem 컴포넌트를 띄워줌

4. PhoneItem

  이름, 전화번호, 삭제 버튼을 가진 컴포넌트

> ### 컴포넌트 폴더 안의 파일

1. 자바스크립트 파일: 컴포넌트 코드가 들어있는 파일

2. 스타일 파일: 각각의 컴포넌트에 스타일을 지정해주기 위한 파일

3. index.js: 같은 디렉토리에 있는 컴포넌트를 export하는 파일

---

## Component Styling

### 1. CSS를 활용한 스타일링

  - 중복되는 클래스명이 있다면 둘 중 하나가 덮어쓰여지므로 원하는대로 CSS가 설정되지 않음

  - SMACSS, BEM과 같은 CSS 방법론을 적용하거나, CSS Selector를 활용할 수 있음

  > CSS Selector

  특정 클래스명을 가진 요소 안의 것만 스타일이 적용되도록 제한을 걸어줌

  css 파일을 더 복잡하게 만들 수 있다는 단점

  ```css
  .input_boxes {
    margin: 50px 0;
    display: flex;
    flex-direction: column;
  }

  .input_boxes .input_box {
    padding: 10px 0;
  }
  ```

  > CSS Module

  css 클래스를 불러올 때 `[파일이름]_[클래스이름]_[해시값]`으로 고유한 클래스명을 부여하여 동일한 클래스명이 생기지 않게 만드는 기술

  이를 적용하기 위해서는 css 파일을 `[파일이름].module.css`와 같이 저장해야 함

  ```css
  /* .../InputBox.module.css */

  .input_boxes {
    margin: 50px 0;
    display: flex;
    flex-direction: column;
  }
  ...
  ```

  ```js
  // .../InputBox.js

  import styles from "./InputBox.module.css";

  const InputBox = () => {
    return (
      <div className={styles.input_boxes}>
        <div className={styles.input_box}>
          <div className={styles.input_box_name}>이름</div>
          ...
    );
  };

  export default InputBox;
  ```

  모듈화한 스타일파일을 객체로 받아와서 `className={styles.[클래스명]}`과 같은 형식으로 클래스명을 지정해 줌

### 2. Sass를 활용한 스타일링

  - Sass는 Css Pre-Processor로 기존의 Css의 코드를 획기적으로 줄여줄 수 있음

  - 코드 재사용성이 뛰어나고 복잡한 작업을 쉽게 할 수 있고 가독성도 좋다.

  - 두 가지의 확장자(`.sass`, `.scss`)를 지원하는 데, 두 파일의 문법은 많이 다름

  > node-sass 라이브러리 설치

  ```bash
  npm install node-sass
  yarn add node-sass
  ```

  - 설치 오류 -> Nodejs 버전과 호환이 되는 버전을 확인 후 설치

  ```bash
  # 패키지의 버전 정보 확인
  npm view node-sass versions

  npm uninstall node-sass  
  npm install node-sass@9.0.0
  ```

  > css 파일 변경

  - [공식 홈페이지](https://sass-lang.com/documentation)

  ```scss
  /* .../PhoneItem.scss (<- PhoneItem.css) */

  .phone_item {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border: 1px solid #495057;
    padding: 20px;

    /* .phone_item > .phone_item_right > button */
    .phone_item_right button {
      color: #fa5252;
      font-size: 15px;
      font-weight: bold;
      background: none;
      border: none;
      outline: none;
      cursor: pointer;
    }

    /* .phone_item + .phone_item */
    & + & {
      margin-top: 15px;
    }
  }
  ```

  - 모듈화: 파일명을 `PhoneItem.module.scss`로 변경 후 js파일의 className 변경

## 3. styled-components 라이브를 활용한 스타일링

  - css코드를 javascript 코드 내에 작성하는 형태의 스타일링 방법

  - css/sass 파일을 작성할 필요없이 하나의 파일 안에서 스타일까지 모두 설정이 가능

  - CSS-in-JS 라이브러리 중 가장 많이 사용되는 styled-components 라이브러리

  > 라이브러리 설치

  ```bash
  npm install styled-components@5.3.10
  yarn add styled-components
  ```

  > styled-components 적용

  ```js
  // src/components/PhoneList/PhoneList.js

  import styled from "styled-components";

  const PhoneWrapper = styled.div`
    display: flex;
    flex-direction: column;
  `;

  const PhoneList = () => {
    return (
      <PhoneWrapper>
        <PhoneItem />
        <PhoneItem />
        <PhoneItem />
      </PhoneWrapper>
    );
  };

  export default PhoneList;
  ```

  - `styled.[태그명]`을 통해 스타일링 된 컴포넌트를 생성

    ES6의 Template Literal 문법을 사용

  > Template Literal

    ```js
    // 기존 방식
    const func1 = name => {
      return "Hello " + name + "!";
    }

    // ES6의 Template Literal을 사용한 방식
    const func2 = name => {
      return `Hello ${name}!`;
    }
    ```

  - 특정 상태에 따라 다른 스타일을 적용