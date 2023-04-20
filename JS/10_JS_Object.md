# 객체(Object)

객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value의 쌍으로 표현

- key

  문자열 타입만 가능

  key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현

- value 

  모든 타입(함수 포함) 가능

- 객체 요소 접근

  점(`.`) 또는 대괄호(`[]`)로 가능

  key 이름에 띄워쓰기 같은 구분자가 있으면 대괄호 접근만 가능

> ### 생성자 함수

- 동일한 구조의 객체를 여러 개 만들고 싶을 때 사용하는 함수

- 함수 이름은 반드시 대문자로 시작

- 생성자 함수를 사용할 때는 반드시 new 연산자를 사용

```js
function Member(name, age, sId) {
  this.name = name
  this.age = age
  this.sId = sId
}

const member1 = new Memeber('newmem', 21, 2022123456)
```

---

## 객체 관련 문법

ES6에 새로 도입된 문법들로 객체 생성 및 조작에 유용하게 사용 가능

### 1. 속성명 축약

- 객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 예시와 같이 축약 가능

```js
const books = ['Learning JS', 'Learning Python']
const magazines = ['Vogue', 'Science']

const bookShop = {
  books,
  magazines,
}
console.log(bookShop)
/*
{
  books: [ 'Learning JS', 'Learning Python' ],
  magazines: [ 'Vogue', 'Science' ]
}
*/
```

### 2. 메서드명 축약

- 메서드 선언 시 function 키워드 생략 가능

```js
const obj = {
  // greeting: function(){
  greeting() {
    console.log('Hi!')
  }
}

obj.greeting()  // Hi!
```

### 3. 계산된 속성명(computed property name) 사용

- 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능

```js
const key = 'country'
const value = ['한국', '미국', '일본', '중국']

const myObj = {
  [key]: value,
}

console.log(myObj)          // { country: [ '한국', '미국', '일본', '중국' ] }
console.log(myObj.country)  // [ '한국', '미국', '일본', '중국' ]
```

### 4. 구조 분해 할당(destructing assignment)

- 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법

```js
const userInformation = {
  name: 'kim',
  userId: 'kimStudent',
  email: 'kim@email.com'
}

// const name = userInfromation.name
const { name } = userInformation
const { userId, email } = userInformation
```

### 5. 객체 전개 구문(Spread syntax) (`...`)

- 배열과 마찬가지로 전개 구문을 사용해 객체 내부에서 객체 전개 가능

- 얕은 복사에 활용 가능

```js
const obj = {b: 2, c: 3, d: 4}
const newObj = {a: 1, ...obj, e: 5}

console.log(newObj)   // { a: 1, b: 2, c: 3, d: 4, e: 5 }
```

---

## JSON

- JavaScript Object Notation

- Key-Value 형태로 이루어진 자료 표기법

- JavaScript의 Object와 유사한 구조를 가지고 있지만 Object는 그 자체로 타입이고, JSON은 형식이 있는 "문자열"

- 즉, JSON을 Object로 사용하기 위해서는 변환 작업이 필요

  Django와 같은 API 서버에서 JSON을 응답한 것을 받아 변환해야 함

> ### JSON 변환

```js
const jsObject = {
  coffee: 'Americano',
  iceCream: 'Cookie and Cream',
}

// Object -> JSON
const objToJson = JSON.stringify(jsObject)

console.log(objToJson)  // {"coffee":"Americano","iceCream":"Cookie and Cream"}
console.log(typeof objToJson)   // string

// JSON -> Object
const jsonToObj = JSON.parse(objToJson)

console.log(jsonToObj)  // { coffee: 'Americano', iceCream: 'Cookie and Cream' }
console.log(typeof jsonToObj)   // object
```

### 배열은 객체다

- 배열은 키와 속성들을 담고있는 참조 타입의 객체

- 배열은 인덱스를 키로 가지며 length 프로퍼티를 갖는 특수한 객체