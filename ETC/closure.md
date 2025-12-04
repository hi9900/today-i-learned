# 클로저(Closure)

클로저는 함수와 그 함수가 선언된 렉시컬 환경(Lexical Environment)의 조합이다.
내부함수가 외부함수의 변수에 접근할 수 있는 것을 말한다.
이를 통해 데이터 은닉, 캡슐화, 팩토리 함수 등을 구현할 수 있다.
예를 들어, 카운터 함수를 만들 때 클로저를 활용하면 내부 상태를 외부에서 직접 접근하지 못하게 보호할 수 있다.

### 주요 활용 사례: 데이터 은닉(Data Encapsulation)

클로저는 주로 상태를 안전하게 은닉하고 유지하기 위해 사용된다. 전역 변수를 사용하지 않고 함수 내부에서 변수를 관리하여, 외부에서의 무분별한 접근을 막을 수 있다.

> 예제: 카운터

```javascript
function createCounter() {
  let count = 0; // 외부에서 직접 접근할 수 없는 은닉된 변수

  return function () {
    count++; // 외부 함수의 변수(count)를 참조 및 변경
    return count;
  };
}

const counter = createCounter();

console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3
```

위 코드에서 `createCounter` 함수의 실행이 끝나더라도 반환된 내부 함수는 `count` 변수를 계속 기억하고 있다. `count` 변수는 외부에서 직접 수정할 수 없으며, 오직 반환된 함수를 통해서만 상태를 변경할 수 있다.
