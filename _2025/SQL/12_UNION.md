# UNION

> 두 개 이상의 SELECT 문의 결과 집합을 결합하는 데 사용된다.

- 모든 SELECT문에는 동일한 수의 열이 있어야 합니다.

- 열의 데이터 유형도 유사해야 합니다.

- 모든 SELECT문의 열은 동일한 순서로 되어 있어야 합니다.

```SQL
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2;
```

## UNION ALL

- UNION는 기본적으로 고유한 값만 선택한다.

- 중복 값을 허용하려면, UNION ALL을 사용한다.

```SQL
SELECT column_name(s) FROM table1
UNION ALL
SELECT column_name(s) FROM table2;
```

- 결과 집합의 열 이름은 일반적으로 첫 번째 SELECT문의 열 이름과 동일
