## 새 프로젝트 만들기

```bash
$ npx create-react-app begin-react

$ cd begin-react
$ npm start
```

## 리액트 컴포넌트

- 리액트 컴포넌트를 만들 땐, `import React from 'react'`를 통해 리액트를 불러와줘야 한다.

- 리액트 컴포넌트는 함수형태로 작성할 수도 있고, 클래스 형태로 작성할 수도 있다.

  지금 단계에서는 함수로 작성하는 방법에 대해서만 알아본다.

- 리액트 컴포넌트에서는 XML 형식의 값을 반환해 줄 수 있는데 이를 JSX라고 부른다.

- 코드의 최하단 `export default Hello;`은 Hello라는 컴포넌트를 내보내겠다는 의미이다.

  다른 컴포넌트에서 불러와 사용할 수 있다.

- 컴포넌트는 일종의 UI 조각으로 쉽게 재사용할 수 있다.

