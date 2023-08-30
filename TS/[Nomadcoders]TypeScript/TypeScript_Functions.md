## Call Signature

```ts
type Add = (a: number, b: number) => number;

const add: Add = (a, b) => a + b;
```

## 오버로딩 overloading

```ts
// 오버로딩: 함수가 서로 다른 여러개의 call signatures를 가지고 있을 때 발생시킴

type Add = {
  (a: number, b: number): number;
  (a: number, b: string): number;
};
const add: Add = (a, b) => {
  if (typeof b === "string") return a;
  return a + b;
};

// route 라이브러리 예시 아마도
type Config = {
  path: string;
  state: object;
};
type Push = {
  (path: string): void;
  (config: Config): void;
};

const push: Push = (config) => {
  if (typeof config === "string") console.log(config);
  else {
    console.log(config.path);
  }
};

// 파라미터의 갯수가 다른 경우 -> 옵션
type Add = {
  (a: number, b: number): number;
  (a: number, b: number, c: number): number;
};

const add: Add = (a, b, c?: number) => {
  if (c) return a + b + c;
  return a + b;
};
```

## 다형성 polymorphism

```ts
// 배열을 받고 그 배열의 요소를 하나씩 print

// concrete type: 우리가 전부터 봐왔던 타입(number, boolean, string, void 등)
// 모든 경우마다 call signature 작성해 줘야 함
// type SuperPrint = {
//     (arr: number[]): void
//     (arr: boolean[]): void
//     (arr: string[]): void
// }
// generic: 타입의 placeholder
// concrete type을 모를 때
// 타입을 유추하고 유추한 타입으로 call signature 대체
type SuperPrint = {
  // <TypePlaceholder>(arr: TypePlaceholder[]): void
  <T>(arr: T[]): void;
};

const superPrint: SuperPrint = (arr) => {
  arr.forEach((i) => console.log(i));
};

superPrint([1, 2, 3, 4]);
superPrint([true, false, false]);
superPrint(["a", "b", "c"]);
superPrint([1, 2, true, false]);
```

### Generics Recap
