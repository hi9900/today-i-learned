# WHERE

```SQL
SELECT column_list FROM table_name WHERE condition;
```

> 특정 조건을 만족하는 레코드만 추출

- FROM 절 뒤에 작성한다.

- SELECT 문 외에도 UPDATE 및 DELETE 문에서 WHERE 절을 사용할 수 있다.

> 검색 조건 작성 형식
>
> `left_expression COMPARISON_OPERATOR right_expression`

- 비교 연산자(comparison operators)

  - 두 표현식이 동일한 지 테스트

  `=`, `<>`, `<`, `>`, `<=`, `>=`

- 논리 연산자(logical operators)

  - 일부 표현식의 truth를 테스트 할 수 있음

  - 1, 0 또는 NULL 값을 반환

  ALL, AND, ANY, BETWEEN, IN, LIKE, NOT, OR 등

---

## LIKE

> 패턴 일치를 기반으로 데이터 조회

- SELECT, DELETE, UPDATE 문의 WHERE 절에서 사용한다.

- 기본적으로 대소문자를 구분하지 않는다.

### 와일드 카드(wildcard)

- `%`: 0개 이상의 문자

- `_`: 단일(1개) 문자

---

## IN

- 여러 조건 OR에 대한 약어

```SQL
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1, value2, ...);
```

- 서브 쿼리와 함께 사용할 수 있다.

**예시**

```SQL
-- Orders 테이블 에 주문이 있는 모든 고객을 반환
SELECT * FROM Customers
WHERE CustomerID IN (SELECT CustomerID FROM Orders);

-- 주문을 하지 않은 모든 고객을 반환
SELECT * FROM Customers
WHERE CustomerID NOT IN (SELECT CustomerID FROM Orders);
```

---

## BETWEEN

```SQL
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN | NOT BETWEEN value1 AND value2;
```

---

```SQL

```
