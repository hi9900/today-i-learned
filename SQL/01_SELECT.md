# SELECT

```SQL
SELECT column1, column2 FROM table_name;
```

> 특정 테이블에서 데이터를 조회하기 위해 사용

1. SELECT 절에서 컬럼 또는 쉼표로 구분된 컬럼 목록을 지정

2. FROM 절에서 데이터를 가져올 테이블을 지정

- ORDER BY, DISTINCT, WHERE, LIMIT, LIKE, GROUP BY 등 다양한 절과 함께 사용할 수 있다.

## SELECT DISTINCT

```SQL
SELECT DISTINCT select_list FROM table_name;
```

> 조회 결과에서 중복된 행을 제거

1. DISTINCT 절은 SELECT 키워드 바로 뒤에 나타나야 함

2. DISTINCT 키워드 뒤에 컬럼 또는 컬럼 목록을 작성함

---

# ORDER BY

> 결과를 오름차순 또는 내림차순으로 정렬

```SQL
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
-- or
ORDER BY column1 ASC, column2 DESC;
```

- ORDER BY 절은 FROM 절 뒤에 위치한다.

- 하나 이상의 컬럼을 기준으로 결과를 오름차순(ASC) 또는 내림차순(DESC)으로 정렬할 수 있다.

---

# LIMIT

> 반환되는 행 수를 지정

```SQL
SELECT column_name(s) FROM table_name
WHERE condition
LIMIT number;
```

> 다른 언어

```SQL
-- SQL Server/MS 액세스 구문
SELECT TOP number|percent column_name(s)
FROM table_name
WHERE condition;

-- 오라클 12
SELECT column_name(s)
FROM table_name
ORDER BY column_name(s)
FETCH FIRST number ROWS ONLY;
```

## OFFSET

> 특정 위치에서부터 데이터를 조회

```SQL
-- 11번째부터 20번째 데이터의 rowid와 이름 조회
SELECT rowid, first_name FROM users LIMIT 10 OFFSET 10;
```
