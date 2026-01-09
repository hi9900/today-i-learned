# State & Props

## Props

### styled-components를 통해 App 컴포넌트 스타일링

```bash
$ yarn add styled-components
```

```js
// src/App.js
...
import styled from 'styled-components'

const Wrapper = styled.div`
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100px;
  margin-top: 100px;
`;

const ButtonWrapper = styled.div`
  width: 100%;
  display: flex;
  justify-content: space-between;
  margin-bottom: 50px;
`;

class App extends Component {
  ...
  render() {
      // Destructuring Assignment 문법을 사용한 방식
      const { number } = this.state
      const { countUp, countDown } = this

      return (
        <Wrapper>
          <ButtonWrapper>
            <button onClick={countUp}>+</button>
            <button onClick={countDown}>-</button>
          </ButtonWrapper>
          {number}
        </Wrapper>
      )
    }
}
```

### 함수를 Props로 받는 CountButton, state를 Props로 받는 Number

- CountButton, Number 폴더 내의 index.js 파일 설정

  확장자는 생략 가능

  ```js
  export { default } from "./[File Name]"
  ```

- App.js 연결

  ```js
  // src/App.js

  import CountButton from "./components/CountButton"
  import Number from "./components/Number"
  ```

- index.js 파일에 export를 해주지 않았다면,

  `import Number from "./components/Number/Number.js"`와 같이 작성해야 함

> index.js 파일을 만들어 export 해 주는 이유

  서버에서 index.html 파일을 업로드하면 서버에 접속했을 때, 어떤 파일을 열라는 지시 없이도  index.html파일을 띄워준다.

  다르게 말하면 서버는 파일 이름이 index인 것을 제일 먼저 탐색

  React에서도 index.js 파일을 가장 먼저 찾음

  index.js 파일에서는 같은 폴더 내의 컴포넌트를 다시 export 해줬으므로, import 문을 디렉토리까지만 적어도 어떤 컴포넌트를 가져와야 할 지 알 수 있음