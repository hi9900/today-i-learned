## input 상태 관리하기

- 리액트에서 사용자가 입력할 수 있는 input 태그의 상태를 관리하는 방법

- input에 입력하는 값이 하단에 나타나게 하고, 초기회버튼을 누르면 input 값이 비워지도록 구현

- `useState`와 input의 `onChange`라는 이벤트를 사용한다.

  이벤트에 등록하는 함수에서는 이벤트 객체 `e`를 파라미터로 받아와서 사용할 수 있는데, 이 객체의 `e.target`은 이벤트가 발생한 DOM인 input DOM을 가르키게 된다.

- 이 DOM의 value 값, 즉 `e.target.value`를 조회하면 현재 input에 입력한 값이 무엇인지 알 수 있다.

  이 값을 useState를 통해 관리해주면 된다.

- input의 상태를 관리할 때는 input 태그의 `value` 값도 설정해주는 것이 중요하다.

  그렇게 해야, 상태가 바뀌었을 때 input의 내용도 업데이트 된다.
