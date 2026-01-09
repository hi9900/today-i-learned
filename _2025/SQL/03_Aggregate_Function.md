# Aggregate Function (집계 함수)

- 각 집합의 최댓값, 최솟값, 평균, 합계 및 개수를 계산하고 단일 값을 반환한다.

- AVG, MAX, MIN, SUM은 숫자를 기준으로 계산이 되어져야 하기 때문에 반드시 컬럼의 데이터 타입이 숫자(INTEGER)일 때만 사용 가능하다.

- 집계 함수는 COUNT를 제외하고 NULL 값을 무시한다.

  - `MIN()`: 선택한 열 내에서 가장 작은 값 반환

  - `MAX()` - 선택한 열 내에서 가장 큰 값을 반환

  - `COUNT()` - 세트의 행 수를 반환

  - `SUM()` - 숫자 열의 총 합을 반환

  - `AVG()` - 숫자 열의 평균값을 반환

- 주로 SELECT 문의 GROUP BY 절과 함께 사용됨

---

## MIN, MAX

```SQL
SELECT MIN(column_name)
FROM table_name
WHERE condition;

SELECT MAX(column_name)
FROM table_name
WHERE condition;
```

---

## COUNT

```SQL
SELECT COUNT(column_name)
FROM table_name
WHERE condition;
```

---

- 별표 기호(`*`) 대신 컬럼 이름을 지정하면, NULL 값이 계산되지 않는다.

### 중복 무시

- DISTINCT 사용해 중복을 무시할 수 있다.

- 지정된 열에 대해 동일한 값을 갖는 행이 1개로 계산된다.

```SQL
SELECT COUNT(DISTINCT Price)
FROM Products;
```

---

## SUM

```SQL
SELECT SUM(column_name)
FROM table_name
WHERE condition;
```

### 표현식 추가

```SQL
-- 예시
SELECT SUM(Quantity * 10)
FROM OrderDetails;
```

---

## AVG

- NULL 값은 무시된다.

```SQL
SELECT AVG(column_name)
FROM table_name
WHERE condition;
```
