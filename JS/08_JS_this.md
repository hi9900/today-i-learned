# this

- 어떠한 object를 가리키는 키워드

  (Java에서의 this와 python에서의 self는 인스턴스 자기자신을 가리킴)

- JavaScript의 함수는 호출될 때 this를 암묵적으로 전달 받음

- JavaScript에서의 this는 일반적인 프로그래밍 언어에서의 this와 조금 다르게 동작

  해당 함수 호출 방식에 따라 this에 바인딩되는 객체가 달라짐

- 즉, 함수를 선언할 때 this에 객체가 결정되는 것이 아니고,

  함수를 호출할 때 함수가 어떻게 호출되었는지에 따라 동적으로 결정됨

## 전역 문맥에서의 this

- 브라우저 전역 객체인 window를 가리킴

  전역 객체는 모든 객체의 유일한 최상위 객체를 의미

```js
console.log(this)   // window
```

## 함수 문맥에서의 this

- 함수의 this 키워드는 다른 언어와 조금 다르게 동작

  함수를 호출한 방법에 의해 결정됨

  함수 내부에서 this의 값은 함수를 호출한 방법에 좌우됨

### 1. 단순 호출

  - 전역 객체를 가리킴

  - 브라우저에서 전역은 window를 의미함

  ```js
  const myFunc = function() {
  console.log(this)
  }
  // 브라우저
  myFunc()  // window
  ```

### 2. Method (Function if Object, 객체의 메서드로서)

  - 메서드로 선언하고 호출한다면, 객체의 메서드이므로 해당 객체가 바인딩

  ```js
  const myObj = {
    data: 1,
    myFunc() {
      console.log(this)       // myObj
      console.log(this.data)  // 1
    }
  }

  myObj.myFunc()  // myObj
  ```

### 3. Nested 

- Function 키워드

  - forEach의 콜백 함수에서의 this가 메서드의 객체를 가리키지 못하고 전역 객체 window를 가리킴

  - 단순 호출방식으로 사용되었기 때문에

  - 이를 해결하기 위해 등장한 함수 표현식이 "화살표 함수"

```js
const myObj = {
  numbers: [1], 
  myFunc() {
    console.log(this)   // myObj
    this.numbers.forEach(function (num) {
      console.log(num)  // 1
      console.log(this) // window
    })
  }
}

myObj.myFunc() 
```

- 화살표 함수

  - 이전에 일반 function 키워드와 달리 메서드의 객체를 잘 가리킴

  - 화살표 함수에서 this는 자신을 감싼 정적 범위

  - 자동으로 한 단계 상위의 scope의 context를 바인딩

```js
const myObj = {
  numbers: [1], 
  myFunc() {
    console.log(this)   // myObj
    this.numbers.forEach((num) => {
      console.log(num)  // 1
      console.log(this) // myObj
    })
  }
}

myObj.myFunc()
```

> ### 화살표 함수

  - 화살표 함수는 호출의 위치와 상관없이 상위 스코프를 가리킴(Lexical scope this)

  - Lexical scope this

    함수를 어디서 호출하는지가 아니라 어디에 선언하였는 지에 따라 결정

    Static scope라고도 하며 대부분의 프로그래밍 언어에서 따르는 방식

  - 따라서 함수 내의 상황에서 화살표 함수를 쓰는 것을 권장

---

## this 정리

- 함수(메서드)를 하나만 만들어 여러 객체에서 재사용할 수 있다는 것은 장점이지만, 이러한 유연함이 실수로 이어질 수 있다는 것은 단점

- this의 동작 방식을 충분히 이해하고 장점을 취하면서 실수를 피하는 것에 집중