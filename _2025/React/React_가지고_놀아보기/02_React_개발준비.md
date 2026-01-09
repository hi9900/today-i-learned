# React 개발 - 전화번호부 만들기

> ## 프로젝트 초기 설정

- 프로젝트 생성

  ```bash
  create-react-app [project-name]
  ```

- 사용하지 않는 파일 삭제

  src 디렉토리 내의 `App.test.js`, `index.css`, `logo.svg`파일 삭제

  `index.js` 파일의 세번째 줄 `import './index.css';` 구문 삭제

> ## React Project 구조

- src/index.js

  `ReactDOM.render(<App />, document.getElementById('root'));`

  'App 컴포넌트를 root라는 id를 가진 element에 render 하라'

> ## React 기초 문법

- React에서는 `className`이라는 속성을 사용하여 클래스명을 지정

  class 속성을 사용하여 클래스명 지정 시 콘솔 오류 출력

- React Component에서 반환하는 HTML 코드에서의 최상위 Element는 한 개여야 함

  프로젝트의 규모가 커진다면 쓸모없는 div element가 여러 개 생긴다는 문제 발생

  이에 대한 해결책으로 React에서는 빈 태그를 사용할 수 있도록 지원

  빈 태그를 사용하게 되면 최상위 Element가 존재하는 것으로 인식하고, 브라우저에서 빈 태그는 HTML 코드에서는 존재하지 않는 것으로 보여짐 -> 의미없는 div의 남용 방지 가능