# Array와 Object

- JavaScript의 참조 타입(referance)에 해당하는 타입은 Array와 Object며, 객체라고도 말함

- 객체는 속성들의 모음(collection)

## 배열(Array)

- 키와 속성들을 담고 있는 참조 타입의 객체

- 순서를 보장

- 주로 대괄호(`[]`)를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능

- 배열의 길이는 `array.length` 형태로 접근 가능

### 배열 메서드 1

- `array.reverse()`

  원본 배열 요소들의 순서를 반대로 정렬

- `array.push(num)` & `array.pop()`

  배열의 가장 뒤에 요소를 추가 또는 제거

- `array.unshift(num)` & `array.shift()`

  배열의 가장 앞에 요소를 추가 또는 제거

- `array.include(num)`

  배열에 특정 값이 존재하는 지 판별 후 참(true)/거짓(false) 반환

- `array.indexOf(num)`

  배열에 특정 값이 존재하는 지 판별 후 인덱스 반환, 없다면 -1 반환

  해당 값이 여러 개일 경우 가장 첫 번째 요소의 인덱스 반환 

```js
const numbers = [1, 2, 3, 4, 5]

numbers.reverse()
console.log(numbers)  // [ 5, 4, 3, 2, 1 ]

numbers.push(100)
console.log(numbers)  // [ 5, 4, 3, 2, 1, 100 ]

numbers.pop()
console.log(numbers)  // [ 5, 4, 3, 2, 1 ]

numbers.unshift(0)
console.log(numbers)  // [ 0, 5, 4, 3, 2, 1 ]
numbers.shift()
console.log(numbers)  // [ 5, 4, 3, 2, 1 ]

console.log(numbers.includes(1))    // true
console.log(numbers.includes(100))  // false

console.log(numbers.indexOf(3))     // 2
console.log(numbers.indexOf(100))   // -1
```

### 배열 메서드 2

- Array Helper Methods

- 배열을 순회하며 특정 로직을 수행하는 메서드

- 메서드 호출 시 인자로 콜백 함수(callback function)를 받는 것이 특징

> ### 콜백 함수

  - 어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수

  > 콜백함수 예시

  ```js
  const callBackFunc = function (num) {
    console.log(num ** 2)
  }

  const numbers = [1, 2, 3]
  numbers.forEach(callBackFunc)
  // 1
  // 4 
  // 9
  ```

  - forEach 메서드에 callBackFunc 함수를 인자로 넘겨 numbers 배열의 각 요소를 callBackFunc 함수의 인자로 사용용

- `array.forEach`

  ```js
  array.forEach(callback (element, index, array) {
    //do somthing
  }) 
  ```

  - 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행

  - 콜백 함수는 3가지 매개변수로 구성
  
    1. element: 배열 요소

    2. index: 배열 요소의 인덱스

    3. array: 배열 자체

  - 반환 값(return) 없음

- `array.map`

  ```js
  array.map(function (element, index, array) {
    // do something
  })
  ```

  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  - 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환

  - 기존 배열 전체를 다른 형태로 바꿀 때 유용 (forEach + return)

- `array.filter`

  ```js
  array.filter(fuction (element, index, array) {
    // do something
  })
  ```

  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  - 콜백 함수의 반환 값이 `true`인 요소들만 모아서 새로운 배열을 반환

  - 기존 배열의 요소들을 필터링할 때 유용

- `array.reduce`

  ```js
  array.reduce(function (acc, element, index, array) {
    // do something
  }, initialValue)
  ```

  - 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행해서, 하나의 결과값을 반환

  - 배열을 하나의 값으로 계산하는 동작이 필요할 때 사용 (총합, 평균 등)

  - map, filter 등 여러 배열 메서드 동작을 대부분 대체할 수 있음

  > reduce의 주요 매개변수

  - acc: 이전 callback 함수의 반환 값이 누적되는 변수

  - initialValue (optional): 최초 callback 함수 호출 시 acc에 할당되는 값. default 값은 배열의 첫 번째 값

  - 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생

- `array.find`

  ```js
  array.find(function (element, index, array) {
    // do something
  })
  ```

  - 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행

  - 콜백 함수의 반환 값이 `true`이면 조건을 만족하는 첫번째 요소를 반환

  - 찾는 값이 배열에 없으면 `undefined` 반환

- `array.some`

  ```js
  array.some(function (element, index, array) {
    // do something
  })
  ```

  - 배열의 요소 중 하나라도 판별 함수를 통과하면 `true`을 반환

  - 모든 요소가 통과하지 못하면 `false` 반환

  - 빈 배열은 항상 `false` 반환

- `array.every`

  ```js
  array.every(fuction (element, index, array) {
    // do something
  })
  ```

  - 배열의 모든 요소가 판별 함수를 통과하면 `true` 반환

  - 하나의 요소라도 통과하지 못하면 `false` 반환

  - 빈 배열은 항상 `true` 반환