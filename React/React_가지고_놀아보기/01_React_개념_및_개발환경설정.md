# React 개념 및 개발 환경 설정

## React Application

- 유저의 특정 행동에 따라 동적으로 화면을 보여주기 때문에 웹 애플리케이션이라 부름

- 동적 인터페이스의 수많은 상태 관리를 위해 React와 같은 웹 라이브러리가 필요

- 웹 라이브러리의 도움 없이 HTML, SS, Javascript로 모든 것을 작업한다면 수많은 인터랙션 관리를 위해 수천줄의 코드가 필요할 수도 있음

- React는 재사용 가능한 UI 컴포넌트의 사용으로 코드량을 줄이고 유지보수도 쉬워짐

- Virtual DOM을 사용해 바뀐 부분만 다시 렌더링, 비효율적인 DOM 조작을 줄임으로써 브라우저 내에서 발생하는 연산의 양을 줄여 성능을 개선할 수 있음

## React의 특징: Virtual DOM

  - Virtual DOM: 가상의 DOM

    React에서는 인터렉션이 발생하게 되면 브라우저의 DOM에 접근하여 변화를 반영하는 것이 아니라, 
    
    Virtual DOM에 한 번 렌더링 하고, 이를 기존의 DOM과 비교하여 변화가 필요한 곳만 렌더링함

  - DOM의 조작을 최소화

## React의 장점

  ### 1. 큰 생태계

  - 다양한 라이브러리의 개발과 배포

  ### 2.글로벌 IT 기업을 포함한 여러 기업에서 사용되는 라이브러리

  - Airbnb, Twitch, Khan Academy, Facebook, Kakao, Naver 등

## React 개발 환경설정

  > ### Webpack과 Babel

  - Webpack: 수많은 컴포넌트를 하나로 결합하는 데 사용되는 것

  - Babel: React 프로젝트에서는 ECMA Script라는 표준화된 자바스크립트 문법이 사용되는 데, 이 스크립트를 사용할 수 있게 해주는 것

  ### Node.js

  - V8(자바스크립트 엔진)으로 빌드 된 이벤트 기반의 자바스크립트 런타임

  - [Node.js 공식 사이트](https://nodejs.org/ko/)에서 LTS 버전으로 다운로드 후 확인

  ```bash
  node -v
  npm -v
  ```

  ### Yarn

  - 패키지 매니저 모듈

  - Node.js를 설치하면 npm이라는 패키지 매니저 모듈이 같이 설치되는데, Yarn은 더 빠르고 안정적이기 때문에 사용됨

  - [Yarn 공식 홈페이지](https://yarnpkg.com/en/docs/install)에서 운영체제에 맞는 버전 설치

  ### create-react-app

  - create-react-app 설치: 간단한 React 개발 환경 구성을 위해 페이스북에서 개발한 라이브러리

  ```bash
  # npm을 사용한 설치
  npm install -g create-react-app
  # yarn을 사용한 설치
  yarn global add create-react-app
  ```

  - 프로젝트를 생성할 디렉토리로 이동 후 프로젝트 생성

  ```bash
  create-react-app react-project
  ```

  - 프로젝트 실행 확인

  ```bash
  cd react-project
  npm start
  ```