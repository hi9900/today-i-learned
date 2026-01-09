# LifeCycle API

- React에서 모든 컴포넌트는 여러 종류의 LifeCycle Method를 가짐

- 각 컴포넌트에서는 이 메소드를 오버라이딩하여 특정 시점에서 코드가 실행될 수 있도록 설정할 수 있음

## Component Mount LifeCycle API

- 컴포넌트 마운트와 관련된 API

- 다음 순서로 호출됨

### 1. Constructor()

  - React 컴포넌트의 생성자

  - 생성자는 해당 컴포넌트가 마운트되기 전에 호출됨

  - 보통 두 가지 목적을 위해 사용되고, 그 외의 목적을 위해서는 다른 LifeCycle API를 사용해야 함

    - `this.state`에 객체를 할당하여 state 초기화

    - 인스턴스에 이벤트 처리 메서드 바인딩

  ```js
  // Example
  constructor(props) {
    super(props)

    // this.state에 객체를 할당하여 state 초기화
    this.state = {number: 0}
    // 인스턴스에 이벤트 처리 메서드 바인딩
    this.countUp = this.countUp.bind(this)
  }
  ```

### 2. static getDerivedStateFromProps()

  - 시간의 흐름에 따라 변하는 props를 state로 동기화하는 작업이 필요한 경우 사용

  - state를 갱신하기 위한 객체를 반환하거나, null을 반환해 갱신 작업을 하지 않을 수 있음

  - 컴포넌트 인스턴스 접근이 불가능

  ```js
  static getDerivedStateFromProps(props, state) {}
  ```

### 3. render()

  - 반드시 클래스 컴포넌트에서 구현해야 함

  - render 함수는 순수해야 함: 컴포넌트의 state를 변경하지 않고, 호출될 때마다 동일한 결과를 반환해야 하며, 브라우저와 직접적인 상호작용을 하지 않음

  - shouldComponentUpdate 메소드가 false를 반환할 시 호출되지 않음

  ```js
  render() {}
  ```

### 4. componentDidMount()

  - 컴포넌트가 마운트된 직후에 호출됨

  - DOM을 사용해야 하는 라이브러리를 불러와 초기화를 한다거나, 외부에서 데이터를 불러오기 위해 네트워크 요청을 보내는 등의 작업이 필요할 때 사용

  ```js
  componentDidMount() {}
  ```