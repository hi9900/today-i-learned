# DOM 조작

- Document가 제공하는 기능을 사용해 웹 페이지 문서 조작

- DOM 조작 순서

  1. 선택 (Select)

  2. 조작 (Manipulation): 생성, 추가, 삭제 등

## 선택 관련 메서드

- `document.querySelector(selector)`

  제공한 선택자와 일치하는 element 한 개 선택

  제공한 CSS selector를 만족하는 첫 번쨰 element 객체를 반환, 없다면 null 반환

- `document.querySelectorAll(selctor)`

  제공한 선택자와 일치하는 여러 element를 선택

  매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음

  제공한 CSS selector를 만족하는 NodeList를 반환

> ### NodeList

  - DOM 메서드를 사용해 선택한 노드의 목록

  - 배열과 유사한 구조를 가짐

  - Index로만 각 항목에 접근 가능

  - 배열의 forEach 메서드 및 다양한 배열 메서드 사용 가능

    단, 배열의 모든 메서드를 사용할 수 있는 것은 아님

  - `querySelectorAll()`에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않음

## 조작 관련 메서드

### 생성

- `document.createElement(tagName)`

  작성한 tagName의 HTML 요소를 생성하여 반환

### 입력

- `HTMLElement.innerText`

  Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text)

  사람이 읽을 수 있는 요소만 남김

  즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현됨

  > `node.textContent` vs `HTMLElement.innerText`

    textContent는 노드의 모든 요소를 반환한다. 그에 비해 innerText는 스타일링을 고려하며, "hidden" 요소의 텍스트는 반환하지 않는다.

### 추가

- `Node.appendChild()`

  한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입

  한번에 오직 하나의 Node만 추가할 수 있음

  추가된 Node 객체를 반환

  새롭게 생성한 Node가 아닌 이미 문서에 존재하는 Node를 다른 Node의 자식으로 삽입하는 경우, 위치를 이동

### 삭제

- `Node.removeChild()`

  DOM에서 자식 Node를 제거

  제거된 Node를 반환

## 속성 조회 및 설정

- `Element.getAttribute(attributeName)`

  해당 요소의 지정된 값(문자열)을 반환

  인자(attributeName)는 값을 얻고자 하는 속성의 이름

- `Element.setAttribute(name, value)`

  지정된 요소의 값을 설정

  속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가

- `Element.classList.add(value)`

  클래스에 값을 추가

- `Element.classList.toggle(value)`

  클래스에 존재한다면 제거하고 false를 반환, 존재하지 않으면 클래스를 추가하고 true를 반환