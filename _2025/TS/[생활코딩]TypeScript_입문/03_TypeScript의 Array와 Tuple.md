# TypeScript의 Array와 Tuple

## TypeScript 에서 Array와 Tuple의 데이터 타입

- 타입스크립트는 자바스크립트의 타입을 확장하여 개발자에게 더 강력한 타입 검사와 편의성을 제공한다.

- Array와 Tuple 데이터 타입을 사용하여 TypeScript에서 배열과 고정 길이 배열을 손쉽게 정의할 수 있다.

### Array 타입

- TypeScript에서 배열 타입을 선언하는 방법은 두 가지이다.

  두 방법 모두 동일한 결과를 가져오며 개인의 취향에 따라 선택할 수 있다.

```ts
// 첫 번째: 타입 + []
let arr1: number[] = [1, 2, 3];

// 두 번째: Array<타입>
let arr2: Array = [1, 2, 3];
```

### Tuple 타입

- Tuple은 고정된 길이와 타입의 배열이다. 각 요소의 타입과 순서가 정해져있다.

```ts
let tuple: [string, number, boolean] = ["Hello", 20, true];
```

- tuple이라는 변수에 길이가 3이고, 각각 string, number, boolean 타입을 가지는 Tuple을 선언

## Array와 Tuple의 차이점

- Array는 길이가 가변적이며, 동일한 타입의 요소로 구성된다.

- Tuple은 길이가 고정되어 있으며, 각 요소의 타입이 정해져 있다.

  자바스크립트에는 없는 데이터 타입이며, 타입스크립트에서만 사용할 수 있다.
