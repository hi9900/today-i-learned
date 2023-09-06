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
type SuperPrint = {
  (arr: number[]): void;
  (arr: boolean[]): void;
  (arr: string[]): void;
};
// generic: 타입의 placeholder
// concrete type을 모를 때
// 타입을 유추하고 유추한 타입으로 call signature 대체
type SuperPrint = {
  // <TypePlaceholder>(arr: TypePlaceholder[]): void;
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

```ts
// 제네릭: 요청에 따라 call signature를 생성

// 제네릭을 하나 더 추가
// 제네릭이 처음 사용되는 지점을 기반으로 이 타입을 알게 된다.
// 제네릭을 처음 인식했을 때와 제네릭의 순서를 기반으로 제네릭의 타입을 안다.
type SuperPrint = {
  // 제네릭 설명이 아닌 이름만 말해주면 됨
  <T, M>(arr: T[], b: M): void;
};

const superPrint: SuperPrint = (arr) => arr[0];

const a = superPrint([1, 2, 3, 4], "x");
const b = superPrint([true, false, false], 1);
const c = superPrint(["a", "b", "c"], true);
const d = superPrint([1, 2, true, false], 0);
```

### Conclusions

- 우리는 제네릭을 통해 call signature를 사용할 일은 거의 없다.

- 다른 패키지와 라이브러리를 사용하고 그 라이브러리들이 제네릭을 통해 생성된다.

- 다시말해, 라이브러리를 만들거나 다른 개발자가 사용할 기능을 개발하는 경우에 제네릭이 유용하다.

  그 외 대부분의 경우에는 제네릭을 직접 작성할 일은 없다.

```ts
// 제네릭의 call signature 외의 다른 사용 방법
function superPrint<V>(a: V[]) {
  return a[0];
}

type Player<E> = {
  name: string;
  extraInfo: E;
};

type hiExtra = {
  favFood: string;
};
type hiPlayer = Player<hiExtra>;

const hi: hiPlayer = {
  name: "hi",
  extraInfo: {
    favFood: "kimchi",
  },
};

const lynn: Player<null> = {
  name: "lynn",
  extraInfo: null,
};

// 제네릭을 사용한 타입이 지정된 Array 함수 사용 시 타입 명시하기

type A = Array<number>;
function printAllNumbers(arr: Array<number>) {}

// ReactJS
useState<number>();
```
