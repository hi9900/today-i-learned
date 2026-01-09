# JavaScript 기초 문법

## 변수와 식별자

### 식별자의 정의와 특징

- 식별자(identifier): 변수를 구분할 수 있는 변수명

- 식별자는 반드시 문자, 달러(`$`) 또는 밑줄(`_`)로 시작

- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작

- 예약어 사용 불가능

  for, if, function 등

- 카멜 케이스(camelCase)

  변수, 객체, 함수에 사용

- 파스칼 케이스(PascalCase)

  클래스, 생성자에 사용

- 대문자 스네이크 케이스(SNAKE_CASE)

  상수(constants)에 사용

  상수: 개발자의 의도와 상관없이 변경될 가능성이 없는 값을 의미

```js
// 카멜 케이스
// 변수
let dog
let variableName

// 객체
const userInfo = {name: 'Tom', age: 20}

// 함수
function add() {}
function getName() {}

// 파스칼 케이스
// 클래스
class User {
  constructor(options) {
    this.name = options.name
  }
}

// 생성자 함수
function User(options) {
  this.name = options.name
}

// 대문자 스네이크 케이스
// 값이 바뀌지 않을 상수
const API_KEY = 'my-key'
const PI = Math.PI

// 재할당이 일어나지 않는 변수
const NUMBERS = [1, 2, 3]
```

> ### 선언, 할당, 초기화

  - 선언(Declaration): 변수를 생성하는 행위 또는 시점

  - 할당(Assignment): 선언된 변수에 값을 저장하는 행위 또는 시점

  - 초기화(Initialization): 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

  ```js
  let foo           // 선언
  console.log(foo)  // undefined

  foo = 11          // 할당
  console.log(foo)  // 11

  let bar = 0       // 선언 + 할당
  console.log(bar)  // 0
  ```


### 변수 선언 키워드

1. let

  블록 스코프 지역 변수를 선언 (동시에 값을 초기화)

  재할당 가능 & 재선언 불가능

  블록 스코프를 갖는 지역 변수를 선언, 선언과 동시에 원하는 값으로 초기화 할 수 있음

  ```js
  let number = 10   // 선언 및 초기값 할당
  number = 20       // 재할당
  let number = 20   // 재선언 불가능
  ```  

2. const

  블록 스코프 읽기 전용 상수를 선언 (동시에 값을 초기화)

  재할당 불가능 & 재선언 불가능

  선언 시 반드시 초기값을 설정해야 하며, 이후 값 변경이 불가능

  블록스코프를 가짐

  ```js
  const number = 10   // 선언 및 초기값 할당
  number = 20         // 재할당 불가능
  const number = 20   // 재선언 불가능  
  ```

3. var

  변수를 선언 (동시에 값을 초기화)

  재할당 가능 & 재선언 가능

  ES6 이전에 변수를 선언할 때 사용되던 키워드

  "호이스팅" 되던 특성으로 인해 예기치 못한 문제발생 가능

  따라서 ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장

  함수 스코프(function scope)를 가짐

  변수 선언 시 var, const, let 키워드 중 하나를 사용하지 않으면 자동으로 var로 선언됨

> ### 블록 스코프(block scope)

  - if, for, 함수 등의 중괄호 `{}` 내부를 가리킴

  - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

  ```js
  let x = 1

  if (x === 1) {
    let x = 2
    console.log(x)  // 2
  }

  console.log(x)    // 1
  ```

> ### 함수 스코프(function scope)

  - 함수의 중괄호 내부를 가리킴

  - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

  ```js
  function foo() {
    var x = 5
    console.log(x)    // 5
  }

  console.log(x)      // ReferenceError: x is not defined
  ```

> ### 호이스팅(hoisting)

  - 변수를 선언 이전에 참조할 수 있는 현상

  - var로 선언된 변수는 선언 이전에 참조할 수 있으며, 이러한 현상을 호이스팅이라 함

  - 변수 선언 이전의 위치에서 접근 시 `undefined`를 반환

  - 즉, JavaScript에서 변수들은 실제 실행 시에 코드의 최상단으로 끌어올려지게 되며(hoisted) 이러한 이유 때문에 var로 선언된 변수는 선언 시 undefined로 값이 초기화되는 과정이 동시에 일어남

    - 반면 let, const는 호이스팅이 일어나면 에러를 발생시킴

  - 변수를 선언하기 전에 접근이 가능한 것은 코드의 논리적인 흐름을 깨뜨리는 행위이며 이러한 것을 방지하기 위해 let, const가 추가되었음

    즉, var는 사용하지 않아야 하는 키워드

  ```js
  // var name             // undefined로 초기화
  console.log(name)    // undefined => 선언 이전에 참조
  // 암묵적으로 선언한 것으로 이해함

  var name = '홍길동'  // 선언
  ```

---

## 변수 선언 키워드 정리

- 어디에 변수를 쓰고 상수를 쓸 지 결정하는 것은 프로그래머의 몫

- Airbnb 스타일 가이드에서는 기본적으로 const 사용을 권장

  - 재할당해야 하는 경우만 let

| 키워드 | 재선언 | 재할당 | 스코프 | 비고 |
| :----: | :---: | :---: | :---: | :---: |
| let | X | O | 블록스코프 | ES6부터 도입 |
| const | X | X | 블록스코프 | ES6부터 도입 |
| var | O | O | 함수스코프 | 사용 X |
