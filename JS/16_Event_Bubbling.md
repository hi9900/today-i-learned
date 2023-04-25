# Event 전파와 취소

## Event 전파

- DOM 요소에서 발생한 이벤트가 상위 노드에서 하위 노드 혹은, 하위 노드에서 상위 노드로 전파되는 현상을 의미

- `addEventListner` 메서드를 사용하여 전파 방식을 제어할 수 있음

  기본 값은 하위 노드에서 상위 노드로 전파되는 방식을 사용 - Event Bubbling

- 또한, 이러한 이벤트 전파 상황을 필요에 따라 제어할 수도 있음

> ### event.preventDefault()

  - 현재 Event의 기본 동작을 중단

  - HTML 요소의 기본 동작을 작동하지 않게 막음

  - HTML 요소의 기본 동작 예시

    - a 태그: 클릭 시 특정 주소로 이동

    - form 태그: form 데이터 전송

> ### lodash

  - 모듈성, 성능 및 추가 기능을 제공하는 JavaScript 유틸리티 라이브러리

  - array, object 등 자료 구조를 다룰 때 사용하는 유용하고 간편한 유틸리티 함수들을 제공

    reverse, sortBy, range, random 등
  
  - https://lodash.com/

> ### this와 addEventListener

  - addEventListener에서 콜백 함수는 특별하게 function 키워드의 경우 addEventListener를 호출한 대상(event.target)을 뜻함

  - 반면 화살표 함수의 경우 상위 스코프를 지칭하기 때문에 window 객체가 바인딩 됨

  - 따라서, addEventListener의 콜백 함수는 function 키워드를 사용하기