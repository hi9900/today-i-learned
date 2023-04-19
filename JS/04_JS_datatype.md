# 데이터 타입

JavaScript의 모든 값은 특정한 데이터타입을 가짐

크게 원시 타입(Primitive type)과 참조 타입(Reference type)으로 분류

## 원시 타입(Primitive type)

### 1. Number

  - 정수 또는 실수형 숫자를 표현하는 자료형

  ```js
  const a = 13
  const b = -5
  const c = 3.14    // float - 숫자 표현
  const d = 2.99e8  // 2.998 * 10^8
  const e = Infinity
  const f = -Infinity
  const g = NaN     // Not a Number
  ```

  > NaN을 반환하는 경우

  - 숫자로서 읽을 수 없음: `parseInt("숫자아님")`, `Number(undefined)`

  - 결과가 허수인 수학 계산식: `Math.sqrt(-1)`

  - 피연산자가 NaN: `7 ** NaN`

  - 정의할 수 없는 계산식: `0 * Infinity`

  - 문자열을 포함하면서 덧셈이 아닌 계산식: `"가" / 3`

### 2. String

  - 문자열을 표현하는 자료형

  - 작은 따옴표 또는 큰 따옴표 모두 가능

    - 따옴표를 사용하면 선언 시 줄바꿈 불가능

      대신 escape sequence를 사용할 수 있기 때문에 `\n`을 사용

  - 덧셈을 통해 문자열끼리 붙일 수 있음

  - Template Literal을 사용하면 줄바꿈, 문자열 사이에 변수도 삽입 가능

  ```js
  const sentence1 = 'Ask and go th the blue'    // single quote
  const sentence2 = "Ask and go th the blue"    // double quote

  const firstName = 'Tony'
  const lastName = 'Stark'
  const fullName = firstName + lastName

  console.log(fullName)   // TonyStark

  const word1 = "안녕\n하세요"
  ```

> ### Template literals (템플릿 리터럴)

  - 내장된 표현식을 허용하는 문자열 작성 방식

  - ES6+ 부터 지원

  - Backtick(`)을 이용하며, 여러 줄에 걸쳐 문자열을 정의할 수도 있고 JavaScript의 변수를 문자열 안에 바로 연결할 수 있는 이점이 생김

  - `$`와 중괄호로 표현식을 표기할 수 있음(`${expression}`)

### Empty Value

  - 값이 존재하지 않음을 표현하는 값으로 JavaScript에서는 null과 undefined가 존재

  - null과 undefined의 가장 대표적인 차이점은 `typeof` 연산자를 통해 타입을 확인했을 때 나타남

    null이 원시 타입임에도 불구하고 object로 출력되는 이유는 설계 당시 버그를 지금까지 해결하지 못한 것

    쉽게 해결할 수 없는 이유는 이미 null 타입에 의존성을 띄고 있는 많은 프로그램들이 망가질 수 있기 떄문(하위호환 유지)

  - 동일한 역할을 하는 두 개의 키워드가 존재하는 이유는 단순한 JavaScript의 설계 실수

### 3. null

  - null 값을 나타내는 특별한 키워드

  - 변수의 값이 없음을 의도적으로 표현할 때 사용

### 4. undefined

  - 값이 정의되어 있지 않음을 표현하는 값

  - 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨

```js
let lastName = null
console.log(lastName)   // null

let firstName   // 선언만 하고 할당하지 않음
console.log(firstName)  // undefined

typeof null       // "object"
typeof undefined  // "undefined"
```

### 5. Boolean

  - `true`와 `false`

  - 참과 거짓을 표현하는 자료형

  - 조건문 또는 반복문에서 유용하게 사용

    조건문 또는 반복문에서 boolean이 아닌 데이터타입은 자동 형변환 규칙에 따라 `true` 또는 `false`로 반환됨

### 6. Symbol

  - 유일한 값을 표현하는 자료형 (ES6에서 추가)

## 참조 타입(Reference type)

### 1. 객체 (Object)

  - 이름과 값을 가진 속성(property)들의 집합으로 이루어진 자료구조

  - 객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현

  - key

    문자열 타입만 가능

    key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현

  - value 

    모든 타입(함수 포함) 가능

  - 객체 요소 접근

    - 점(`.`) 또는 대괄호(`[]`)로 가능

    - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

  ```js
  const me = {
    name: 'jack',
    phonNumber: '01012345678',
    'samsung products': {
      buds: 'Galaxy Buds pro',
      galaxy: 'Galaxy s99',
    },
  }

  console.log(me.name)
  console.log(me['name'])
  console.log(me['samsung products'])
  // console.log(me.samsung products)
  console.log(me['samsung products'].buds)
  ```

### 2. 배열(Array)

  - 여러 개의 값을 순서대로 저장하는 자료구조

  - 키와 속성들을 담고있는 참조 타입의 객체

  - 순서를 보장하는 특징이 있음

  - 주로 대괄호(`[]`)를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능

  - 배열의 길이는 `array.length` 형태로 접근 가능

    배열의 마지막 원소는 `array.length - 1`로 접근

  ```js
  const numbers = [1, 2, 3, 4, 5]
  console.log(numbers[0])     // 1
  console.log(numbers[-1])    // undefined
  console.log(numbers.length) // 5

  console.log(numbers[numbers.length - 1])  // 5
  console.log(numbers[numbers.length - 2])  // 4
  ```

### 3. 함수(function)

  - function 키워드를 통해 생성하며, 호출 시 실행될 코드를 정의

  - 참조 타입 중 하나로, function 타입에 속함 

  - JavaScript에서 함수를 정의하는 방법은 주로 2가지로 구분됨

    - 함수 선언식(fuction declaration)

    - 함수 표현식(fuction expression)

> ### 함수 선언식(Fuction declaration)

  - 일반적인 프로그래밍 언어의 함수 정의 방식

  ```js
  function add (num1, num2) {
    return num1 + num2
  }

  add(2, 7)   // 9
  ```

> ### 함수 표현식(Fuction expression)

  - 표현식 내에서 함수를 정의하는 방식

  - 함수 표현식은 함수의 이름을 생략한 익명 함수로 정의 가능

  - 표현식에서 함수 이름을 명시하는 것도 가능

    단, 이 경우 함수 이름은 호출에 사용되지 못하고 디버깅 용도로 사용됨

  ```js
  const sub = fuction (num1, num2) {
    return num1 - num2
  }

  sub(7, 2)   // 5

  const mySub = function namedSub (num1, num2) {
    return num1 - num2
  }

  mySub(1, 2)     // -1
  namedSub(1, 2)  // ReferenceError
  ```

### ToBoolean Conversions (자동 형변환)

| 데이터 타입 | false | true |
| :--------: | :---: | :---: |
| undefined | 항상 false | X |
|  null  | 항상 false | X |
| Number | 0, -0, NaN | 나머지 모든 경우 |
| String | 빈 문자열 | 나머지 모든 경우 |
| Object | X | 항상 true |
