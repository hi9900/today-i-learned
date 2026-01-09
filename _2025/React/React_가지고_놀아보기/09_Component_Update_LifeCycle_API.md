# LifeCycle API

## Component Update LifeCycle API

- 컴포넌트 업데이트와 관련된 API

- 아래와 같은 순서로 호출됨

### 1. state getDerivedStateFromProps()

  - Component Mount LifeCycle API에서 설명

### 2. shouldComponentUpdate()

  - props 또는 state가 새로운 값으로 갱신되어서 렌더링이 발생하기 직전에 호출됨

  - 기본적으로 true를 반환하지만, 특정 조건에 따라 false를 반환하면 render 함수를 실행하지 않음

    따라서 이 메소드는 성능 최적화가 필요할 때 유용하게 사용됨

    불필요한 리렌더링을 막아 자원 낭비를 줄일 수 있음

  ```js
  shouldComponentUpdate(nextProps, nextState) {}
  ```

### 3. render()

  - Component Mount LifeCycle API에서 설명

### 4. getSnapshotBeforeUpdate()

  - DOM 변화가 일어나기 직전의 상태를 가져올 수 있고, 반환 값은 componentDidUpdate 메소드의 인자로 전달됨

  - 메소드를 사용하는 예시는 흔하지 않지만, 채팅 화면과 같이 스크롤의 위치를 따로 처리하는 작업이 필요한 경우 고려해볼 수 있음

  > 예시: [React 공식 홈페이지](https://ko.legacy.reactjs.org/docs/react-component.html#getsnapshotbeforeupdate)

  ```js
  class ScrollingList extends React.Component {
    constructor(props) {
      super(props);
      this.listRef = React.createRef();
    }

    getSnapshotBeforeUpdate(prevProps, prevState) {
      // Are we adding new items to the list?
      // Capture the scroll position so we can adjust scroll later.
      if (prevProps.list.length < this.props.list.length) {
        const list = this.listRef.current;
        return list.scrollHeight - list.scrollTop;
      }
      return null;
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
      // If we have a snapshot value, we've just added new items.
      // Adjust scroll so these new items don't push the old ones out of view.
      // (snapshot here is the value returned from getSnapshotBeforeUpdate)
      if (snapshot !== null) {
        const list = this.listRef.current;
        list.scrollTop = list.scrollHeight - snapshot;
      }
    }

    render() {
      return (
        <div ref={this.listRef}>{/* ...contents... */}</div>
      );
    }
  }
  ```

### 5. componentDidUpdate()

  - render 메소드가 호출되고 난 다음 발생함

  - 컴포넌트가 갱신되었을 때 DOM을 조작하는 경우 사용할 수 있음

  - 또, props의 변경 여부를 파악해 특정 함수를 실행되게 하는 작업도 가능함

  ```js
  componentDidUpdate(prevProps, prevState, snapshot) {}
  ```