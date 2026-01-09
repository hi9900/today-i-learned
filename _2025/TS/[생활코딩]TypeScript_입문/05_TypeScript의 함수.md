# TypeScript의 함수

## TypeScript에서 함수의 데이터 타입

- TypeScript에서 함수를 사용할 때, 매개변수와 반환 값에 대한 데이터 타입을 지정할 수 있다.

  이를 통해 코드의 안정성과 가독성이 높아진다.

### 매개변수와 반환 값의 데이터 타입 지정

```ts
function add(a: number, b: number): number {
  return a + b;
}
```

- 함수 add는 두 개의 숫자를 매개변수로 받고, 두 숫자의 합을 반환한다.

  각 매개변수와 반환 값에 데이터 타입을 지정해줄 수 있다.

### 선택적 매개변수 사용하기

- 함수에서 일부 매개변수는 선택적으로 받을 수 있게 만들고 싶을 때, 매개변수 뒤에 `?`를 사용한다.

  해당 매개변수는 선택적이 되어, 값을 전달하지 않아도 된다.

```ts
function greet(name: string, greeting?: string): string {
  if (greeting) {
    return `${greeting}, ${name}!`;
  } else {
    return `Hello, ${name}!`;
  }
}
```

- 함수 greet는 이름과 인사말을 매개변수로 받는다.

  인사말은 선택적 매개변수로 지정되어, 값을 전달하지 않으면 기본 인사말이 사용된다.
