# LifeCycle API

## Component Unmount LifeCycle API

- 컴포넌트 마운트와 관련된 API

### componentWillUnmount()

  - 컴포넌트가 제거될 때 호출됨

  - 해당 메소드를 통해 컴포넌트 내의 setTimeout, setInterval 제거, 네트워크 요청 취소, 데이터 구독 해제 등의 작업을 수행할 수 있음

  - 이 컴포넌트가 호출되었다는 말은 곧 컴포넌트가 리렌더링되지 않을 것이라는 말이므로 해당 메소드 내에는 절대 setState를 호출하면 안됨

  ```js
  componentWillUnmount() {}
  ```