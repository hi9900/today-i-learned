> 노마드코더 타입스크립트로 블록체인 만들기 강의 내용

## object

```ts
// object type
// const [objectName]: [Type] = value
const player: {
  name: string;
  age?: number;
} = {
  name: "hi",
};

// player.age가 undefined일 수 있기 때문에
if (player.age && player.age < 10) {
}

// Alias
type Age = number;
type Player = {
  name: string;
  age?: Age;
};

const Me: Player = {
  name: "me",
};

// function(인수:타입): 결과타입
function playerMaker(name: string): Player {
  return {
    name,
  };
}

const playerMaker2 = (name: string): Player => ({ name });

const hi = playerMaker("hi");
hi.age = 12;
```

### readonly

```ts
// readonly
type Player = {
  readonly name: string;
  age?: Age;
};
// 수정 불가
// hi.name='las'

const numbers: readonly number[] = [1, 2, 3, 4];
// 수정 불가
numbers.push(1);
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
