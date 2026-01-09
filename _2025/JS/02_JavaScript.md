# JavaScript

> ### ECMAScript

  - ECMAScript란, ECMA International(전자 정보 통신 시스템 표준화 기구)이 ECMA-262 규격에 따라 정의하고 있는 표준화된 스크립트 프로그래밍 언어를 뜻함

  - 즉, JavaScript를 표준화하기 위해 만들어짐

  - JavaScript의 기본적인 문법, 데이터 타입, 객체 모델, 함수, 연산자 등을 정의

    앞으로의 코드는 ES6+(2015년 이후) 정의된 내용을 토대로 작성

### 주석

  - 한 줄 주석(`//`)과 여러 줄 주석(`/* */`)

  ```js
  // console.log('주석')

  /* 
  여러 줄 주석
  */
  ```

### 들여쓰기와 코드블럭

  - JavaScript는 2칸 들여쓰기를 사용

  - 블럭(block)은 if, for, 함수에서 중괄호 `{}` 내부를 말함

    - JavaScript는 중괄호를 사용해 코드 블럭을 구분

  ```js
  if (isClean) {  // 중괄호를 사용해서 코드블럭 구분
    console.log('clean!')   // 2칸 들여쓰기
  }
  ```

### 코드 스타일 가이드

  - JavaScript는 여러 코드 스타일 가이드가 회사마다 존재함

  - 앞으로의 코드는 Airbnb Stype Guide를 기반으로 사용

  - JavaScript 코드 스타일 가이드 종류

    - Airbnb JavaScript Style Guide

    - Google JavaScript Style Guide

    - JavaScript Standard Style

### 세미콜론(semicolon)

  - 자바 스크립트는 세미콜론을 선택적으로 사용 가능

  - 세미콜론이 없으면 ASI(Automatic Semicolon Insertion, 자동 세미콜론 삽입 규칙)에 의해 자동으로 세미콜론이 삽입됨

  - 세미콜론 사용 여부에 대해서는 논란이 많기 때문에 일관성 있게 회사/팀의 스타일 가이드에 맞춰서 사용

    - TC39(ECMAScript 기술 위원회)는 세미콜론 사용을 권장

    - BrendanEich(JavaScript 개발자)는 세미콜론 사용을 반대