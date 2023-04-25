# Callback과 Promise

### 비동기 처리의 단점

- 비동기 처리의 핵심은 Web API로 들어오는 순서가 아니라 작업이 완료되는 순서에 따라 처리하는 것

- 개발자의 입장에서 코드의 실행 순서가 불명확하다는 단점이 있음

  이와 같은 단점은 실행 결과를 예상하면서 코드를 작성할 수 없게 함

- 이를 해결하기 위해 콜백 함수를 사용

---

## 콜백 함수(Callback Function)

- 콜백 함수는 연쇄적으로 발생하는 비동기 작업을 순차적으로 동작할 수 있게 함

- 보통 어떤 기능의 실행 결과를 받아서 다른 기능을 수행하기 위해 많이 사용하는 데, 이 과정을 작성하다 보면 비슷한 패턴이 계속 발생하게 됨

  A를 처리해서 결과가 나오면 첫 번째 callback 함수를 실행하고

  첫 번째 callback 함수가 종료되면, 두 번째 callback 함수를 실행하고

  두 번째 callback 함수가 종료되면, 세 번째 callback 함수를 실행하고 ...

### 콜백 지옥(Callback Hell)

- 비동기 처리를 위한 콜백을 작성할 때 마주하는 문재를 Callback Hell(콜백 지옥)이라 하며,

  그 때의 코드 작성 형태가 마치 피라미드와 같다고 하여 "Pyramid of doom(파멸의 피라미드)" 라고도 부름

## 정리

- 콜백 함수는 비동기 작업을 순차적으로 실행할 수 있게 하는 반드시 필요한 로직

- 비동기 코드를 작성하다 보면 콜백 함수로 인한 콜백 지옥은 반드시 나타나는 문제

- 코드의 가독성을 해치고 유지보수가 어려워짐

---

## 프로미스(Promise)

- Callback Hell 문제를 해결하기 위해 등장한 비동기 처리를 위한 객체

- "작업이 끝나면 실행 시켜준다"는 약속(promise)

- 비동기 작업의 완료 또는 실패를 나타내는 객체

- Promise 기반의 클라이언트가 바로 이전에 사용한 Axios 라이브러리

  - Promise based HTTP client for the browser and node.js

  - 성공에 대한 약속 `then()`

  - 실패에 대한 약속 `catch()`

### then & catch

- then(callback)

  - 요청한 작업이 성공하면 callback 실행

  - callback은 이전 작업의 성공 결과를 인자로 전달 받음

- catch(callback)

  - then()이 하나라도 실패하면 callback 실행

  - callback은 이전 작업의 실패 객체를 인자로 전달 받음

- then과 catch 모두 항상 promise 객체를 반환

  즉, 계속해서 chaining을 할 수 있음

- axios로 처리한 비동기 로직이 항상 promise 객체를 반환

  그래서 then을 계속 이어나가면서 작성할 수 있음

```html
axios.get('요청할 URL')
  .then(성공하면 수행 할 1번 콜백 함수)
  .then(1번 콜백 함수가 성공하면 수행 할 2번 콜백 함수)
  ...
  .catch(실패하면 수행 할 콜백 함수)
```

---

## 비동기 콜백 vs Promise

- 기존 콜백 함수 작성 방식

```html
<script>
  work1(function () {
    // 첫 번째 작업 ...
    work2(result1, function (result2) {
      // 두 번째 작업 ...
      work3(result2, function (result3) {
        console.log('최종 결과:' + result3)
      })
    })
  })
</script>
```

- Promise 방식은 비동기 처리를 마치 우리가 일반적으로 위에서 아래로 적는 방식처럼 코드를 작성할 수 있음

```html
<script>
  work1()
    .then((result1) => {
      // work2
      return result2
    })
    .then((result2) => {
      // work3
      return result3
    })
    .catch((error) => {
      // error handling
    })
</script>
```

## Promise가 보장하는 것 (vs 비동기 콜백)

- 비동기 콜백 작성 스타일과 달리 Promise가 보장하는 특징

1. callback 함수는 JavaScript의 Event Loop가 현재 실행 중인 Call Stack을 완료하기 이전에는 절대 호출되지 않음

  - Promise callback 함수는 Event Queue에 배치되는 엄격한 순서로 호출됨

2. 비동기 작업이 성공하거나 실패한 뒤에 `.then()` 메서드를 이용하여 추가한 경우에도 1번과 똑같이 동작

3. `.then()`을 여러 번 사용하여 여러 개의 callback 함수를 추가할 수 있음 (Chaining)

  - 각각의 callback은 주어진 순서대로 하나하나 실행 됨

  - Chaining은 Promise의 가장 뛰어난 장점