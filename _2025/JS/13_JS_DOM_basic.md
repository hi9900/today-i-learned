# DOM 기본 구조

## DOM Tree

- DOM은 문서를 논리 트리로 표현

- DOM에서 모든 것은 `Node`

  즉, HTML 요소, 속성, 텍스트 모든 것이 노드

- 각 노드는 부모, 자식 관계를 형성하고, 이에 따라 상속 개념도 동일하게 적용됨

## Node

- DOM의 구성요소 중 하나

- HTML 문서의 모든 요소를 나타냄

  - 각각의 HTML 요소는 DOM Node로서 특정한 노드 타입을 가짐

  - Document Node === HTML 문서 전체를 나타내는 노드

  - Element Node === HTML 요소를 나타내는 노드 (ex. `<p>`)

  - Text Node === HTML 텍스트, Element Node 내의 텍스트 컨텐츠를 나타냄

  - Attribute Node === HTML 요소의 속성을 나타내는 노드

## DOM에 접근하기

- DOM을 사용하기 위해 특별히 해야할 일은 없음

- 모든 웹 브라우저는 스크립트 언어가 손쉽게 웹 페이지의 요소에 접근할 수 있도록 만들기 위해 DOM 구조를 항상 사용

- "DOM의 주요 객체"들을 활용하여 문서를 조작하거나 특정 요소들을 얻을 수 있음

## DOM의 주요 객체

> ### window object

  - DOM을 표현하는 창

  - 가장 최상위 객체 (작성 시 생략 가능)

  - 탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타냄

  > window의 메서드 예시

  ```js
  // 새 탭 열기
  window.open()

  //경고 대화 상자 표시
  window.alert()

  //인쇄 대화 상자 표시
  window.print()
  ```

> ### document object

  - 브라우저가 불러온 웹 페이지

  - 페이지 컨텐츠의 진입점 역할을 하며, `<body>` 등과 같은 수많은 다른 요소들을 포함하고 있음

  - document는 window의 속성이다.

### Node vs Element

  - 예시 코드의 모든 것은 Node

  - `<head>`, `<body>`는 HTML 요소로 element

  - `<title>`, `<p>`는 Text Node 이면서 element

  - `id="unique"`는 DOM에서 Attr Node이고, 
  
    HTML 요소인 `<p>`의 속성이므로 element는 아님