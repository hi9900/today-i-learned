> 노마드코더 타입스크립트로 블록체인 만들기 강의 내용 #2.1 - #2.4

---

## Implicit Types vs Explicit Types in TypeScript

### Implicit Types (암시적 타입)

- 변수의 초기값을 보고 타입을 자동으로 추론

```ts
let message = "Hello, TypeScript!"; // 자동으로 string 타입으로 추론
let count = 42; // 자동으로 number 타입으로 추론
let isActive = true; // 자동으로 boolean 타입으로 추론

// message = 10; // 오류 (message는 string 타입으로 추론됨)
```

### Explicit Types (명시적 타입)

- 변수 선언 시 직접 타입을 지정

```ts
let username: string = "John";
let age: number = 25;
let isPremiumUser: boolean = false;

let numbers: number[] = [1, 2, 3, 4, 5]; // 배열의 타입 지정
let user: { name: string; age: number } = { name: "Alice", age: 30 }; // 객체 타입 지정
```

> 함수에서의 예시

```ts
// 암시적 타입 (TypeScript가 자동 추론)
function add(a: number, b: number) {
  return a + b; // 반환 타입은 자동으로 number로 추론됨
}

// 명시적 타입 (직접 선언)
function multiply(a: number, b: number): number {
  return a * b; // 반환 타입을 number로 명시적으로 지정
}
```

---

## Types

### Optional Properties (선택적 속성)

Typescript 에서는 객체의 특정 속성이 필수가 아니라 선택적으로 존재할 수도 있음을 나타낼 수 있다.
이를 위해 `?`(물음표)를 사용한다.

```ts
const player: {
  name: string;
  age?: number;
} = {
  name: "hi",
};

// player.age가 undefined일 수 있기 때문에
if (player.age && player.age < 10) {
}
```

### Type Aliases (타입 별칭)

타입 별칭(Type Alias)을 사용하면 복잡한 타입을 재사용 가능하도록 이름을 지정할 수 있다.
`type` 키워드를 사용하여 객체, 유니언 타입, 배열 등 다양한 타입을 정의할 수 있다.

```ts
type Age = number;
type Player = {
  name: string;
  age?: Age;
};

const me: Player = {
  name: "me",
};
const you: Player = {
  name: "you",
  age: 20,
};
```

### function

함수의 타입을 지정할 때 매개변수 타입과 반환값 타입을 정의한다.
반환값이 없는 단순 실행 함수일 경우, `void`를 사용한다.

```ts
function playerMaker(name: string): Player {
  return {
    name,
  };
}
const playerMaker2 = (name: string): Player => ({ name });

// 반환값 없음
const logMessage(message: string): void {
  console.log(message);
}

// 함수 타입 별칭
type PlayerMakerType = (name: string) => Player;
const playerMaker3: PlayerMakerType = (name: string) => ({ name });
```

### readonly

`readonly` 키워드는 객체의 속성이 수정되지 않도록 보호하는 역할을 한한다.
즉, 한 번 값을 할당하면 재할당할 수 없다.

```ts
type Player = {
  readonly name: string;
  age?: Age;
};
// hi.name='las' // ❌ name 수정 불가
hi.age = 12;

const numbers: readonly number[] = [1, 2, 3, 4];
// numbers.push(1); // ❌ 배열 수정 불가
```

## Tuple & any

```ts
// tuple
// 정해진 개수에 맞는 요소 array
const player: [string, number, boolean] = ["hi", 12, false];
const player1: readonly [string, number, boolean] = ["hi", 12, false];

let a: undefined = undefined;
let b: null = null;

// any: 비어있는 값 []
// typescript의 규칙을 따르지 않음: 자바스크립트
const c: any[] = [1, 2, 3, 4];
const d: any = true;

// 가능
c + d;
```

## unknown

```ts
// unknown
// 변수의 타입을 미리 알지 못할 때 지정
let a: unknown;

if (typeof a === "number") {
  let b = a + 1;
}
if (typeof a === "string") {
  let b = a.toUpperCase();
}
```

## void

```ts
// void
// 아무것도 return 하지 않는 함수
// 따로 지정해 줄 필요는 없음. 타입스크립트가 자동으로 인식한다
function hello() {
  console.log("hello");
}
const a = hello();
```

## never

```ts
// never
// 함수가 절대 return 하지 않을 때
// ex. 함수에서 exception이 발생할 때

// 리턴하지 않고 오류를 발생시키는 함수
function hello(): never {
  throw new Error("xxx");
}

// 타입이 두가지일 수 있는 상황에 발생
function helloN(name: string | number) {
  if (typeof name === "string") {
    // name: string
  } else if (typeof name === "number") {
    // name: number
  } else {
    // name: never
    name;
  }
}
```
