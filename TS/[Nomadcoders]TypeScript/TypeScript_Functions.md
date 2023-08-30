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
