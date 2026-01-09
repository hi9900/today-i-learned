# Component

- UI를 독립적이고 재사용 가능한 조각들로 나눈 것

  즉, 기능별로 분화한 코드 조각

- CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미

- 하나의 app을 구성할 때 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적임

  - src/App.vue를 root node로 하는 tree의 구조

- 컴포넌트는 유지보수를 쉽게 만들어 줄 뿐만 아니라 재사용성의 측면에서도 매우 강력한 기능을 제공

### Component based architecture 특징

- 관리가 용이: 유지/보수 비용 감소

- 재사용성

- 확장 가능

- 캡슐화

- 독립적

---

### component in Vue

- Vue에서의 component: 이름이 있는 재사용 가능한 Vue instance

- Vue instance: `new Vue()`로 만든 인스턴스

## SFC (Single File Component)

- 하나의 `.vue` 파일이 하나의 Vue instance이고, 하나의 컴포넌트이다.

  즉, Single File Component

- Vue instance에서는 HTML, CSS, JavaScript 코드를 한번에 관리

  - Vue의 instance를 기능 단위로 작성하는 것이 핵심

- 컴포넌트 기반 개발의 핵심 기능

### 정리

- HTML, CSS, JavaScript를 `.vue`라는 확장자를 가진 파일 안에서 관리하며 개발

- 이 파일을 Vue instance 또는 Vue component라고 하며, 기능 단위로 작성

- Vue CLI가 Vue를 Component based하게 사용하도록 도와줌

---

## Vue Component 구조

- 템플릿(HTML)

  - HTML의 body 부분

  - 눈으로 보여지는 요소 작성

  - 다른 컴포넌트를 HTML 요소처럼 추가 가능

- 스크립트(JavaScript)

  - JavaScript 코드가 작성되는 곳

  - 컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성됨

- 스타일(CSS)

  - CSS가 작성되며 컴포넌트의 스타일을 담당

## Vue Component 구조 정리

- 컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만듦

- root에 해당하는 최상단의 component가 `App.vue`

- 이 App.vue를 index.html과 연결

- 결국 index.html 파일 하나만을 rendering: 이게 바로 SPA

---

## Component 등록 3단계

### 0. Component.vue 생성

- `src/components/` 안에 생성

- script에 이름 등록

- template에 요소 추가

  - template안에는 반드시 하나의 요소만 추가 가능

  - 비어 있어도 안됨, 해당 요소 안에 추가 요소를 작성해야 함

### 1. 불러오기

`import {instance name} from {위치}`

- instance name은 instance 생성 시 작성한 name

- `@`은 src의 shortcut

- `.vue` 생략 가능

```html
<script>
import MyComponent from '@/components/MyComponent'
</script>
```

### 2. 등록하기

```html
<script>
...
export default {
  ...
  components: {
    MyComponent
  }
}
</script>
```

### 3. 보여주기

- 닫는 태그만 있는 요소처럼 사용

```html
<template>
<div id="app">
  <MyComponent />
</div>
</template>
```