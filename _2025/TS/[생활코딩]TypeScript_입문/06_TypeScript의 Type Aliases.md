# TypeScript의 Type Aliases

- Type Aliases는 타입스크립트에서 기존 타입에 사용자 정의 이름을 부여할 수 있는 방법이다.

  이를 통해 코드의 가독성을 높이고 복잡한 타입 구조를 단순화할 수 있다.

- Type Aliases는 원시 데이터 타입, Array, Tuple, 객체, 함수 등 다양한 타입에 적용할 수 있다.

## 원시 데이터 타입의 별칭

- 원시 데이터 타입의 별칭을 사용하면 특정 데이터 타입을 명확히 표현할 수 있다.

- 예를 들어, 'age'와 같은 숫자를 나타내는 변수를 다룰 때, 'number' 타입 대신 'Age'라는 별칭을 사용할 수 있다.

```ts
type Age = number;
const myAge: Age = 20;
```

## Array와 Tuple, 객체, 함수에 적용

- Array, Tuple, 객체, 함수와 같은 컬렉션 데이터 타입에도 Type Aliases를 적용할 수 있다.

```ts
// Array
type Names = string[];
const myFriends: Names = ["Alice", "Bob", "Charlie"];

// Tuple
type Coordinates = [number, number];
const myLocation: Coordinates = [37.7749, -122.4194];

// 객체
type User = {
  id: string;
  name: string;
  age: number;
};
const user: User = { id: "1", name: "John Doe", age: 20 };

// 함수
type GreetingFunction = (name: string) => string;
const greet: GreetingFunction = (name) => `Hello, ${name}!`;
```

## 더 복잡한 형태

- 원시 데이터 타입의 별칭을 컬렉션 데이터 타입의 원소로 사용할 수도 있다.

```ts
type UserID = string;
type UserName = string;
type Age = number;

type User = {
  id: UserID;
  name: UserName;
  age: Age;
};

const user: User = { id: "1", name: "John Doe", age: 28 };
```
