## 조건부 렌더링

- 특정 조건에 따라 다른 결과물을 렌더링하는 것

ex. App 컴포넌트에서 Hello 컴포넌트를 사용할 때, `isSpecial` 이라는 props를 설정

  - `true`는 자바스크립트 값이기 때문에 중괄호로 감싸줌

- Hello 컴포넌트에서는 isSpecial이 `true`이냐 `false` 이냐에 따라 컴포넌트 좌측에 `*` 표시를 보여준다.

### 삼항 연산자

- 가장 기본적인 방법은 삼항연산자를 사용하는 것

`{isSpecial ? <b>*</b> : null}`

- `isSpecial` 값이 `true` 라면 `<b>*</b>` 를, 그렇지 않다면 `null` 을 보여주도록 한다.

  참고로 JSX 에서 null, false, undefined 를 렌더링하게 된다면 아무것도 나타나지 않게 됩니다.

- 보통 삼항연산자를 사용한 조건부 렌더링은 주로 특정 조건에 따라 보여줘야하는 내용이 다를 때 사용한다.

### `&&` 연산자

- 지금은 내용이 달라지는 것이 아니라, 특정 조건이 `true` 이면 보여주고, 그렇지 않다면 숨겨주는 데, 이러한 상황에서는 `&&` 연산자를 사용해서 처리하는 것이 더 간편하다.

`{isSpecial && <b>*</b>}`

  - `isSpecial`이 `false` 이면 `false`, `true`이면 `<b>*</b>`: 단축 평가 논리 계산법

### props 값 설정을 생략하면 ={true}

- props 값을 설정하게 될 때 만약 props 이름만 작성하고 값 설정을 생략한다면, 이를 `true`로 설정한 것으로 간주한다.

`<Hello name="react" color="red" isSpecial />`