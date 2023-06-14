## State 활용 방법 (Counter 프로젝트)

```js
// src/App.js
import React, { Component } from 'react';

class App extends Component {
	state = { number: 0 }

	render() {
		return (
			<div>
				<div>
          <button>+</button>
          <button>-</button>
        </div>
        {this.state.number}
			</div>
		)
	}
}
```

- return 구문 안에서 변수를 사용하기 위해 중괄호로 둘러싸야 함

- `this.state.number`: number 출력

  클래스 내부에 선언된 인스턴스 변수에 접근하기 위해 맨 앞의 this 키워드를 적어줌

  state는 json 형태의 객체이므로 `[변수명].number`와 같은 형식으로 받아와야 함

```js
countUp = () => {
  this.setState({ number: this.state.number + 1 })
}
countDown = () => {
  this.setState({ number: this.state.number - 1 })
}
```

- `setState`함수: 전달되는 값만 업데이트, 그러나 객체를 깊게 확인하지 못함

```js
// state가 아래와 같이 선언되어 있다고 가정
state = {
	user: {
		name: "Hong gil dong",
		phone: "010-0000-0000"
	},
	number: 0
}

// user 객체가 통째로 바뀜 (올바르지 않은 예시)
this.setState({
	user: {
		phone: "010-1111-1111"
	}
});

// user 객체가 통째로 바뀌고 number 값이 변경됨 (올바르지 않은 예시)
this.setState({
	user: {
		phone: "010-1111-1111"
	},
	number: 10
});

// number 값만 변경 (올바른 예시)
this.setState({ number: 10 });

// user 값만 변경 (올바른 예시)
this.setState({
	user: {
		...this.state.user,
		phone: "010-1111-1111"
	}
});

// user와 number값 모두 변경 (올바른 예시)
this.setState({
	user: {
		...this.state.user,
		phone: "010-1111-1111"
	},
	number: 10
})
```

> [Destructuring Assignment](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)

배열이나 객체의 속성을 해체하여 그 값을 개별 변수에 담을 수 있게 하는 기능

	```js
	// Example 1
	var a, b, rest;
	[a, b, ...rest] = [10, 20, 30, 40, 50];
	console.log(a, b, rest); // 10 20 [30, 40, 50]

	// Example 2
	var obj = { a: 60, b: 70 };
	var { a, b } = obj;
	console.log(a, b); // 60, 70

	// Example 3
	var obj = { a: 60, b: 70 };
	var { a: num1, b: num2 } = obj;
	console.log(num1, num2); // 60, 70

	// Example 4
	var user = {
		id: 42,
		displayName: "jdoe",
		fullName: {
				firstName: "John",
				lastName: "Doe"
		}
	};

	function whois({ displayName, fullName: { firstName: name }}){
		console.log(displayName + " is " + name);
	}

	whois(user); // jdoe is John
	```

- setState 함수 변경 (2가지 방법)

	주로 두 번째 방식을 사용

```js
// 경로 : src/App.js

import React, { Component } from 'react';

class App extends Component {
	state = { number: 0 }

	// 1. state를 업데이트하는 함수를 전달
	countUp = () => {
		this.setState(
			({ number }) => ({
				number: number + 1
			})
		);
	}

	// 2. setState 함수 앞에서 state 값을 받고 이를 전달
	countDown = () => {
		const { number } = this.state
		this.setState({ number: number - 1 });
	}

	render() {
		return (
			<div>
				<div>
					<button>+</button>
					<button>-</button>
				</div>
				{this.state.number}
			</div>
		)
	}
}

export default App;
```

### State 함수를 버튼에 연결

- onClick 이벤트를 사용해 연결

- 이벤트 명은 CamelCase, 이벤트에 전달하는 값은 함수여야 함

```js
...
<button onClick={this.countUp}>+</button>
<button onClick={this.countDown}>-</button>
...
```

- 클래스형 컴포넌트의 render 함수에도 Destructuring Assignment 문법을 사용할 수 있음

- 함수와 state, props를 받아올 때 사용 가능함

```js
render() {
	// Destructuring Assignment 문법을 사용한 방식
	const { number } = this.state
	const { countUp, countDown } = this

	return (
		<div>
			<div>
				<button onClick={countUp}>+</button>
				<button onClick={countDown}>-</button>
			</div>
			{number}
		</div>
	)
}
```