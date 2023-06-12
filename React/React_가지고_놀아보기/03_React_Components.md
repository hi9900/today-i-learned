# React Components

## Class Component

- LifeCycle API와 state를 위해 꼭 class 문법을 활용한 컴포넌트를 정의해야 함

- 그러나 React 16.8.0 업데이트 이후로 Hooks에 대한 기능이 추가되며 Functional Component에서 LifeCycle API와 state기능을 구현할 수 있어 이제는 class component는 잘 사용하지 않음

> ## Class Component Example

```js
// Class Component Example

import React, { Component } from 'react';

class Component1 extends Component {
  render() {
    return (<div>Hello World!</div>);
  }
}

export default Component1;
```

- 1: `import React, { Component } from 'react';`

  react 라이브러리에서 함수 또는 클래스를 import

  import 문법은 표준화된 자바스크립트(ECMA Script 6)의 문법 중 하나로써 export 된 다른 파일의 함수 또는 클래스를 불러와 사용할 수 있도록 하는 기능이 있음

- 3: `class Component1 extends Component`

  `Component1`이라는 컴포넌트를 class 문법을 사용해 선언

- 4: `render()`

  `React.Component`의 하위 class에서 반드시 정의해야 하는 메서드

  리액트에서 사용하는 컴포넌트를 생성

- 5: `return (<div>Hello World!</div>);`

  render 함수를 통해 컴포넌트를 만들기 위한 HTML을 반환

- 9: `export default Component1;`

  다른 자바스크립트 파일에서 `Component1`이라는 class를 사용할 수 있도록 export

---

## Functional Component

- 부모 컴포넌트로 받은 값을 출력해주는 컴포넌트였지만 업데이트 이후 거의 모든 컴포넌트 선언에 사용됨

- React Hooks 업데이트 이후로 Functional Components에서도 상태 관리(state)와 LifeCycle API 사용이 가능해짐

> ## Functional Components Example

```js
// Functional Component Example

import React from 'react';

const Component2 = () => {
  return (
    <div>Hello World!</div>
  );
}

export default Component2;
```

> ### Arrow Function

  `[변수 선언부] [함수명] = [함수 인자값] => [함수 내부 코드]`