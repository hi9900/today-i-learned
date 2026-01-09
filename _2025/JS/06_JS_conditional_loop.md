# 조건문

## if statement

- 조건 표현식의 결과값을 boolean 타입으로 변환 후 참/거짓을 판단

- `if{} else if{} else{}`

  조건은 소괄호(condition)안에 작성

  실행할 코드는 중괄호 `{}`안에 작성

  블록 스코프 생성

---

# 반복문

## while

- 조건문이 참이기만 하면 문장을 계속해서 수행

```js
while ('조건문') {
  // do something
}
```

## for

- 특정한 조건이 거짓으로 반별될 때까지 반복

```js
for ([초기문]; [조건문]; [증감문]) {
  // do something
}
```

## for ... in

- 객체(object)의 속성을 순회할 때 사용

- 배열도 순회 가능하지만 인덱스 순으로 순회한다는 보장이 없으므로 권장하지 않음

```js
for (variable in object) {
  statements
}
```

## for ... of

- 반복 가능한 객체를 순회할 때 사용

- 반복 가능한(iterable) 객체의 종류: Array, Set, String 등

```js
for (variable of object) {
  statements
}
```

> ### for-in과 for-of의 차이

  - `for ... in`은 속성 이름을 통해 반복

  - `for ... of`는 속성 값을 통해 반복

> ### for 문과 const

- for문

  - `for (let i=0; i<arr.length; i++) {...}` 의 경우에는 최초 정의한 i를 재할당하면서 사용하기 때문에 const를 사용하면 에러 발생

- for-in, for-of

  - 재할당이 아니라, 매 반복 시 해당 변수를 새로 정의하여 사용하므로 에러가 발생하지 않음

## Array.forEach

- 배열의 메서드 중 하나

```js
Array.forEach(function (params {
  // 배열이 가진 각 요소를 순회하면서 함수를 실행
  // 실행 할 코드 작성
}))
```

---

## 조건문과 반복문 정리

| 키워드        | 종류  | 연관 키워드          | 스코프    |
|:----------:|:---:|:---------------:|:------:|
| if         | 조건문 | -               | 블록 스코프 |
| while      | 반복문 | break, continue | 블록 스코프 |
| for        | 반복문 | break, continue | 블록 스코프 |
| for ... in | 반복문 | 객체 순회           | 블록 스코프 |
| for ... of | 반복문 | iterable 순회     | 블록 스코프 |

