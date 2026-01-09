# JavaScript

쉽게 배울 수 있고 강력한 스크립트 언어

JavaScript는 클라이언트 측 웹(브라우저)에서 실행

웹 페이지가 이벤트 발생 시 어떻게 작동하는 지 디자인 / 프로그래밍

웹 페이지 동작을 제어하는 데 널리 사용

## JavaScript Engine

JavaScript Engine은 자바스크립트 코드를 실행하는 프로그램 또는 인터프리터

여러 목적으로 JavaScript Engine을 사용하지만, 대체적으로 웹 브라우저에서 사용

  - 웹 브라우저 외에서 활용: `Node.js`

    Node.js는 V8엔진을 사용하여 서버 측에서 자바스크립트 코드를 실행 가능. 
    
    브라우저 조작 이외의 역할도 수행

각 브라우저마다 자체 JavaScript Engine을 개발 및 사용하고 있음

  - V8 - Chrome

  - Chakra - Microsoft Edge

  - JSC (JavaScript Core) - Apple(safari)

  - SpiderMonkey - FireFox

> ### 웹 브라우저의 역할

  - URL을 통해 Web(WWW)을 탐색함

  - HTML/CSS/JavaScript를 이해한 뒤 해석해서 사용자에게 하나의 화면으로 보여줌

  - 웹 서비스 이용 시 클라이언트의 역할을 함

  - 즉, 웹 페이지 코드를 이해하고, 보여주는 역할을 하는 것이 웹 브라우저

---

## JavaScript 실행 환경 구성

### Web Browser로 실행하기

1. HTML 파일에 포함시키기

  - HTML 파일에 직접 JavaScript 코드를 작성 후 웹 브라우저로 파일 열기

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
    ...
    </head>
    <body>
      <script>
        console.log('hello, javascript')
      </script>
    </body>
    </html>
    ```

  - Chrome의 개발자 도구 - Console 탭에서 결과 확인 가능

2. 외부 JavaScript 파일 사용하기

  - `.js` 확장자를 가진 파일에 JavaScript를 작성하고, 해당 파일을 HTML에 포함

  ```js
  console.log('hello, javascript')
  ```

  ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
    ...
    </head>
    <body>
      <script type="text/javascript" src="hello.js"></script>
    </body>
    </html>
  ```

3. Web Browser에서 바로 입력하기

  - 웹 브라우저의 console에서 바로 JavaScript를 입력해도 됨 (엔진이 있기 떄문)

- 특별하게 웹 브라우저에서 바로 실행할 수 있는 JavaScript 문법들을 Vanilla JavaScript라고 부름

---

