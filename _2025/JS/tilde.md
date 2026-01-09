# 틸드(tilde, `~`) 연산자

## 1. 개념

틸드(`~`)는 **비트 NOT(Bitwise NOT) 연산자**로, 숫자의 모든 비트를 반전(invert)시킨 값을 반환한다.

## 2. 동작 방식

- 숫자의 2진수 비트 표현을 반전한다. (0 → 1, 1 → 0)
- 반전된 값은 **2의 보수(컴퓨터에서 음수를 표현하는 방식)**로 해석된다.

```plaintext
5  →  0000 0101
~5 →  1111 1010  (이진수 음수 표현: -6)

indexOf("banana") → 1
~1 → -2 (Truthy, 값이 존재함)

indexOf("orange") → -1
~-1 → 0 (Falsy, 값이 없음)
```

## 3. 활용

틸드(`~`) 연산자는 **비트 연산자이므로 정수 연산만 수행**할 수 있는데, 이를 이용해 **소수점 이하를 강제로 버리는 효과**를 만들 수 있다.

### ✅ 소수점 버리기

```javascript
console.log(~~4.9); // 4
console.log(~~-4.9); // -4

// Math.trunc
console.log(~~5.7); // 5
console.log(~~-5.7); // -5
console.log(Math.trunc(5.7)); // 5 (동일한 결과)
console.log(Math.trunc(-5.7)); // -5 (동일한 결과)

// parseInt
console.log(parseInt(6.9)); // 6
console.log(~~6.9); // 6
```

### ✅ 몫 나누기 (`Math.floor` 대체)

```javascript
console.log(~~(10 / 3)); // 3
console.log(Math.floor(10 / 3)); // 3 (동일한 결과)
console.log(~~(9 / 2)); // 4
console.log(Math.floor(9 / 2)); // 4 (동일한 결과)
```

### ✅ `Math.floor()`와의 차이

음수일 때 결과가 다를 수 있다.

- `Math.floor()`는 **음수를 내림(더 작은 값)** 하지만,
- `~~`는 단순히 **소수점을 버려서 0에 가까운 값**이 나옴.

```javascript
console.log(~~5.7); // 5
console.log(Math.floor(5.7)); // 5

console.log(~~-5.7); // -5
console.log(Math.floor(-5.7)); // -6
```

## 4. 결론

- `~~` 연산자는 `Math.trunc()`와 동일한 방식으로 **소수점 이하를 버리는 효과**를 낸다.
- `Math.floor(a / b)` 대신 `~~(a / b)`를 사용하여 몫 연산을 수행할 수 있다.
- 코드를 짧고 빠르게 만들 수 있지만, **음수 처리 시 예상과 다를 수 있음**에 주의해야 한다.
