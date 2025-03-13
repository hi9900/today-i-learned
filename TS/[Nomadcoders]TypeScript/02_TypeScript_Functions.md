> 노마드코더 타입스크립트로 블록체인 만들기 강의 내용 #3.0 - #3.4

---

## Call Signature (호출 시그니처)

Call Signature(호출 시그니처)는 함수의 타입을 정의하는 방식이다.
특히 익명 함수 타입이나 객체 내에서 함수 타입을 명확히 할 때 사용한다.

```typescript
// Call Signature를 사용한 함수 타입 정의
type Add = (a: number, b: number) => number;
// 위 타입을 가진 함수 선언
const add: Add = (a, b) => a + b;

// call signature를 사용하지 않은 함수 선언
const add1 = (a: number, b: number) => a + b;
```

---

## Overloading (오버로딩)

오버로딩은 하나의 함수 이름으로 다양한 매개변수 타입 또는 개수를 처리할 수 있도록 정의하는 것을 말한다.

Typescript에서 함수 오버로딩은 여러 개의 함수 시그니처(선언부)를 작성한 후, 하나의 구현부에서 처리하는 방식으로 이뤄진다.
구현부에서 공통 로직을 처리해야 하므로, 타입 검사를 적절히 활용해야 한다.

```typescript
// 오버로드 시그니처(선언부)
function getInfo(value: string): string;
function getInfo(value: number): number;

// 구현부 (실제 함수 정의)
function getInfo(value: string | number): string | number {
  if (typeof value === "string") {
    return `Hello, ${value}`; // 문자열 입력 시 문자열 반환
  } else {
    return value * 10; // 숫자 입력 시 숫자 반환
  }
}

// 사용 예시
console.log(getInfo("Alice")); // ✅ "Hello, Alice"
console.log(getInfo(5)); // ✅ 50
// console.log(getInfo(true)); ❌ 오류 (boolean 타입은 허용되지 않음)
```

- 매개변수 개수에 따른 오버로딩

```typescript
// 오버로드 시그니처
function multiply(a: number, b: number): number;
function multiply(a: number): number;

// 구현부
function multiply(a: number, b?: number): number {
  if (b !== undefined) {
    return a * b; // 두 개의 매개변수 제공 시 곱셈 수행
  } else {
    return a * a; // 하나만 제공 시 제곱 연산 수행
  }
}

// 사용 예시
console.log(multiply(5, 3)); // ✅ 15  (5 * 3)
console.log(multiply(4)); // ✅ 16  (4 * 4)
// console.log(multiply()); ❌ 오류 (최소 1개의 인자가 필요)
```

- 다양한 형태를 처리하는 함수

```typescript
// 오버로드 시그니처
function sum(numbers: number[]): number;
function sum(a: number, b: number, c: number): number;

// 구현부
function sum(a: number | number[], b?: number, c?: number): number {
  if (Array.isArray(a)) {
    return a.reduce((acc, num) => acc + num, 0); // 배열이면 합계 계산
  }
  return a + (b ?? 0) + (c ?? 0); // 숫자 3개 입력 시 더하기
}

// 사용 예시
console.log(sum([1, 2, 3, 4])); // ✅ 10  (배열 요소 합)
console.log(sum(1, 2, 3)); // ✅ 6   (1 + 2 + 3)
// console.log(sum(1, 2)); ❌ 오류 (매개변수 2개는 정의되지 않음)
```

---

## Polymorphism (다형성)

Polymorphism(다형성)은 같은 인터페이스 또는 부모 클래스를 공유하면서도, 각기 다른 동작을 수행할 수 있는 능력을 의미한다. 즉, 같은 메서드나 속성을 다른 방식으로 구현할 수 있다.
Typescript에서 다형성을 활용하면 유연하고 확장 가능한 객체 지향 프로그래밍(OOP)을 구현할 수 있다.

다형성은 제네릭(Generic)과 결합하여 활용할 수 있다.

```typescript
type ConsolePrint = {
  <T>(arr: T[]): void;
};

const consolePrint: ConsolePrint = (arr) => {
  console.log(arr);
};

consolePrint([1, 2, 3, 4]);
consolePrint([false, false]);
consolePrint(["a", "b", "c"]);
consolePrint([1, false, "a"]);
```

---

## Generics

제네릭(Generics)은 여러 타입에서 재사용할 수 있도록 만든 유연한 타입시스템이다.
즉, 특정 타입에 의존하지 않고, 다양한 타입을 처리할 수 있도록 타입을 동적으로 설정하는 기능을 제공한다.

- 기본적인 Generics 사용법

제네릭은 함수, 인터페이스, 클래스에서 사용할 수 있다.
기본적으로 `<T>`를 사용하여 타입을 동적으로 정의한다.
`<T>`는 제네릭 타입 변수로, 함수 내부에서 실제 타입이 결정됩니다.

```typescript
function identity<T>(value: T): T {
  return value;
}

console.log(identity<string>("Hello")); // "Hello"
console.log(identity<number>(42)); // 42
console.log(identity<boolean>(true)); // true
```

---
