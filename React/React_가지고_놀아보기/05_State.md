# State & Props

## State

- State: 컴포넌트 내에서 선언하는 데이터

> Counter 프로젝트

  - 숫자 값을 관리하는 데 State 사용

> 전화번호부

  - State를 통한 데이터 값 선언 및 관리

- UI와 관련하여 작업하는 데에도 사용될 수 있음

### State 정의 방법

- State는 Class Components에서만 사용 가능

  (Functional Components에서는 사용 불가)

> 생성자를 통한 선언

```js
import React, { Component } from 'react';

class Counter extends Component {
	constructor(props) {
		super(props);
		this.state = { number: 0 }
	}

	render() {
		return (
			<div>Number</div>
		);
	}
}

export default Counter;
```

- constructor(생성자) 다음 `super(props)`를 작성한 이유:

  Counter 클래스는 Component 클래스를 상속받음

  해당 클래스에서는 그 클래스에서의 멤버 뿐 아니라 부모 클래스의 모든 멤버까지 포함하게 됨

  따라서 부모 클래스의 멤버를 초기화시켜주기 위해 자식 클래스의 생성자에서 부모 클래스의 생성자를 호출해야 함

  이 때 사용하는 함수가 `super` 함수

> Class Fields 문법

- 클래스 블록 내부에서 할당 연산자(`=`)를 통해 인스턴스 속성을 지정할 수 있는 문법

  인스턴스 속성: 클래스 내부의 변수

```js
import React, { Component } from 'react';

class Counter extends Component {
	state = { number: 0 }

	render() {
		return (
			<div>Number</div>
		);
	}
}

export default Counter;
```

