# 함수

- 참조타입 중 하나로써 function 타입에 속함

## 함수 선언식

- 일반적인 프로그래밍 언어의 함수 정의 방식

## 함수 표현식(Fuction expression)

- 표현식 내에서 함수를 정의하는 방식

- 함수 표현식은 함수의 이름을 생략한 익명 함수로 정의 가능

- 표현식에서 함수 이름을 명시하는 것도 가능

  단, 이 경우 함수 이름은 호출에 사용되지 못하고 디버깅 용도로 사용됨

---

## 기본 인자(Default arguments)

- 인자 작성 시 `=` 문자 뒤 기본 인자 선언 가능

```js
const greeting = function (name = 'Anonymous') {
  return `Hi ${name}`
}

greeting()  // Hi Anonymous
```

## 매개변수와 인자의 개수 불일치 허용

- 매개변수보다 인자의 개수가 많을 경우

```js
const noArg = function() {  // 인자 0개
  return 0
}

console.log(noArg(1, 2, 3))  // 0

const twoArgs = function (arg1, arg2) {
  return [arg1, arg2]
}

console.log(twoArgs(1, 2, 3))  // [1, 2]
```

- 매개변수보다 인자의 개수가 적을 경우

```js
const threeArgs = function(arg1, arg2, arg3) { 
  return [arg1, arg2, arg3]
}

console.log(threeArgs())      // [undefined, undefined, undefined]
console.log(threeArgs(1))     // [1, undefined, undefined]
console.log(threeArgs(1, 2))  // [1, 2, undefined]
```

## Spread syntax(`...`)

- 전개 구문

- 전개 구문을 사용하면 배열이나 문자열과 같이 반복 가능한 객체를 배열의 경우는 요소, 함수의 경우는 인자로 확장할 수 있음

1. 배열과의 사용(배열 복사)

```js
let parts = ['어깨', '무릎']
let lyrics = ['머리', ...parts, '발']
console.log(lyrics)   // [ '머리', '어깨', '무릎', '발' ]
```

2. 함수와의 사용(Rest parameters)

  - 정해지지 않은 수의 매개변수를 배열로 받을 수 있음

```js
function func (a, b, ...theArgs) {
  //
}

const restOpr = function (arg1, arg2, ...restArgs) {
  console.log([arg1, arg2, restArgs])
  return [arg1, arg2, restArgs]
}

restOpr(1, 2, 3, 4, 5)  // [ 1, 2, [ 3, 4, 5 ] ]
restOpr(1, 2)           // [ 1, 2, [] ]
```

---

# 선언과 표현식

## 함수의 타입

- 선언식 함수와 표현식 함수 모두 타입은 function으로 동일

```js
// 함수 표현식
const sum = function (args) {}

// 함수 선언식
function sub(args) {}
```

## 호이스팅 - 선언식

- 함수 선언식으로 정의된 함수는 var로 정의된 변수처럼 호이스팅이 발생

- 즉, 함수 호출 이후에 선언해도 동작함

## 호이스팅 - 표현식

- 함수 표현식으로 선언한 함수는 함수 정의 전에 호출 시 에러 발생

- 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름

---

# 화살표 함수 (Arrow Fucntion)

- 함수를 비교적 간결하게 정의할 수 있는 문법

- function 키워드와 중괄호를 이용한 구문을 짧게 사용하기 위해 탄생

  1. function 키워드 생략 가능

  2. 함수의 매개변수가 하나 뿐이라면 매개변수의 `()` 생략 가능

    명확성과 일관성을 위해 항상 인자 주위에는 괄호`()`를 포함하는 것을 권장

  3. 함수의 내용이 한 줄이라면 `{}`와 `return`도 생략 가능

- 화살표 함수는 항상 익명 함수 === 함수 표현식에서만 사용가능

```js
const arrow1 = function (name) {
  return `hello, ${name}`
}

// 1. function 키워드 삭제
const arrow2 = (name) => { return `hello, ${name}` }
// 2. 인자가 1개일 경우에만 () 생략 가능
const arrow3 = name => { return `hello, ${name}` }
// 3. 함수 바디가 return을 포함한 표현식 1개일 경우에는 {}, return 생략 가능
const arrow4 = name => `hello, ${name}`

// 응용
// 1. 인자가 없다면 () or _ 로 표시 가능
let noArgs = () => 'No args'
noArgs = _ => 'No args'
// 2-1. object를 return한다면, return을 명시적으로 적어준다.
let returnObject = () => { return {key: 'value'} }  
// 2-2. return을 적지 않으려면, 괄호 붙이기
returnObject = () => ({key: 'value'})
```