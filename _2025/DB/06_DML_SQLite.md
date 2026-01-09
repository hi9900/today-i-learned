# DML

> ### sqlite3

  SQL 문 및 commands를 사용하여 SQLite 데이터베이스와 상호작용할 수 있는 간단한 command-line tool

  - 데이터베이스 파일 열기

  ```bash
  $ sqlite3
  sqlite> .open mydb.sqlite3

  <!-- 시작하면서 바로 데이터베이스 열기 -->
  $ sqlite3 mydb.sqlite3
  ```

  - sqlite3 종료하기

  ```bash
  sqlite> .exit
  ```

  - 다양한 commands는 `.help` 명령어를 통해 확인 가능

> CSV 파일을 SQLite 테이블로 가져오기

  1. `DML.sql` 파일 생성

  2. 테이블 생성

    ```sql
    -- DML.sql
    CREATE TABLE users(
      first_name TEXT NOT NULL,
      last_name TEXT NOT NULL,
      age INTEGER NOT NULL,
      country TEXT NOT NULL,
      phone TEXT NOT NULL,
      balance INTEGER NOT NULL
    );
    ```

  3. 데이터베이스 파일 열기

  ```bash
  $ sqlite3 mydb.sqlite3
  ```

  4. 모드(`.mode`)를 csv로 설정

  ```bash
  sqlite> .mode csv
  ```

  5. `.import` 명령어를 사용하여 csv 데이터를 테이블로 가져오기

  ```bash
  sqlite> .import users.csv users
  ```

---

## Simple query

SELECT 문을 사용하여 간단하게 단일 테이블에서 데이터를 조회하기

### SELECT statement

```sql
SELECT column1, column2 FROM table_name;
```

특정 테이블에서 데이터를 조회하기 위해 사용

SELECT 문은 SQLite에서 가장 복잡한 문

문법 규칙

  1. SELECT 절에서 컬럼 또는 쉼표로 구분된 컬럼 목록을 지정

  2. FROM 절에서 데이터를 가져 올 테이블을 지정

다양한 절과 함께 사용할 수 있음

  ORDER BY, DISTINCT, WHERE, LIMIT, LIKE, GROUP BY

> ### SELECT 실습

```sql
-- 전체 데이터 조회
SELECT * FROM users;

-- 이름과 나이 조회
SELECT first_name, age FROM users;

-- rowid 컬럼 조회
SELECT rowid, first_name FROM users;
```

---

### Sorting rows

- ORDER BY clause를 사용하여 쿼리의 결과를 정렬

```sql
SELECT select_list FROM table_name 
ORDER BY column_1 ASC, column_2 DESC;
```

  SELECT 문에 추가하여 결과를 정렬

  ORDEF BY 절은 FROM 절 뒤에 위치함

  하나 이상의 컬럼을 기준으로 결과를 오름차순(ASC, 기본값), 내림차순(DESC)으로 정렬할 수 있음

> ### ORDER BY 실습

```sql
-- 이름과 나이를 나이가 어린 순으로 조회
SELECT first_name, age FROM users ORDER BY age ASC;
SELECT first_name, age FROM users ORDER BY age;

-- 이름과 나이를 나이가 많은 순으로 조회
SELECT first_name, age FROM users ORDER BY age DESC;

-- 이름, 나이, 계좌 잔고를 나이가 어린 순으로
-- 만약 같은 나이라면 계좌 잔고가 많은 순으로 정렬해서 조회
SELECT first_name, age, balance FROM users
ORDER BY age, balance DESC;
```

- ORDER BY 절은 하나 이상의 컬럼을 정렬할 경우 첫번째 열을 사용하여 행을 정렬하고,

  그런 다음 두번째 컬럼을 사용하여 정렬 되어있는 행을 정렬하는 방식

> ### [참고] Sorting NULLs

  NULL의 정렬 방식

  정렬과 관련하여 SQLite는 NULL을 다른 값보다 작은 것으로 간주

  즉, ASC를 사용하는 경우 결과의 시작 부분에 NULL이 표시되고,

  DESC를 사용하는 경우 결과의 끝에 NULL이 표시됨

---

## Filtering data

데이터를 필터링하여 중복 제거, 조건 설정 등 쿼리를 제어하기

### SELECT DISTINCT clause

```sql
SELECT DISTINCT select_list FROM table_name;
```

조회 결과에서 중복된 행을 제거

DISTINCT 절은 SELECT에서 선택적으로 사용할 수 있는 절

문법 규칙

  1. DISTINCT 절은 SELECT 키워드 바로 뒤에 나타나야 함

  2. DISTINCT 키워드 뒤에 컬럼 또는 컬럼 목록을 작성

> ### SELECT DISTINCT 실습

```sql
-- 모든 지역 조회
SELECT country FROM users;

-- 중복없이 모든 지역 조회
SELECT DISTINCT country FROM users;

-- 지역 순으로 오름차순 정렬하여 중복 없이 모든 지역 조회
SELECT DISTINCT country FROM users ORDER BY country;

-- 이름과 지역 중복 없이 모든 이름과 지역 조회
SELECT DISTINCT first_name, country FROM users;

-- 이름과 지역 중복 없이 지역 순으로 오름차순 정렬하여 모든 이름과 지역 조회
SELECT DISTINCT first_name, country FROM users ORDER BY country;
```

- 두 개 이상의 컬럼일 경우, 각 컬럼의 중복을 따로 계산하는 것이 아니라

  두 컬럼을 하나의 집합으로 보고 중복을 제거

> ### [참고] NULL with DISTINCT

  - SQLite는 NULL 값을 중복으로 간주

  - NULL 값이 있는 컬럼에 DISTINCT 절을 사용하면 SQLite는 NULL 값의 한 행을 유지

---

## WHERE clause

```sql
SELECT column_list FROM table_name WHERE search_condition;
```

"Specify the search condition for rows returned by the query"

조회 시 특정 검색 조건을 지정

WHERE 절은 SELECT 문에서 선택적으로 사용할 수 있는 절

  SELECT 문 외에도 UPDATE 및 DELETE 문에서 WHERE 절을 사용할 수 있음

FROM 절 뒤에 작성

### SQLite operators

  - WHERE의 검색 조건 작성 형식

    `left_expression COMPARISON_OPERATOR right_expression`

  1. 비교 연산자(comparison operators)

    - 두 표현식이 동일한 지 테스트

    `=`, `<> or !=`, `<`, `>`, `<=`, `>=`

  2. 논리 연산자(logical operators)

    - 일부 표현식의 truth를 테스트 할 수 있음

    - 1, 0 또는 NULL 값을 반환

    - SQLite는 Boolean 데이터 타입을 제공하지 않으므로 1은 TRUE를 의미하고 0은 FALSE를 의미

    ALL, AND, ANY, BETWEEN, IN, LIKE, NOT, OR 등

> ### WHERE 실습

```sql
-- 나이가 30살 이상인 사람들의 이름, 나이, 계좌 잔고 조회하기
SELECT first_name, age, balance FROM users WHERE age >= 30;

-- 나이가 30살 이상이고 계좌 잔고가 50만원 초과인 사람들의 이름, 나이, 계좌 잔고 조회하기
SELECT first_name, age, balance FROM users WHERE age >= 30 AND balance > 500000;
```

### LIKE operator

"Query data based on pattern matching"

패턴 일치를 기반으로 데이터를 조회

SELECT, DELETE, UPDATE 문의 WHERE 절에서 사용

기본적으로 대소문자를 구분하지 않음

  `'A' LIKE 'a'`: true

SQLite는 패턴 구성을 두 개의 **와일드카드(wildcoard)**를 제공

1. `%` (percent)

  0개 이상의 문자가 올 수 있음을 의미

2. `_` (underscore)

  단일(1개) 문자가 있음을 의미

> ### "wildcards" character

  파일을 지정할 때 구체적인 이름 대신 여러 파일을 동시에 지정할 목적으로 사용하는 특수 기호(`*`, `?` 등)

  주로 특정한 패턴이 있는 문자열 혹은 파일을 찾거나, 긴 이름을 생략할 때 쓰임

  텍스트 값에서 알 수 없는 문자를 사용할 수 있는 특수 문자로, 유사하지만 동일한 데이터가 아닌 여러 항목을 찾기에 매우 편리한 문자

  지정된 패턴 일치를 기반으로 데이터를 수집하는 데도 도움이 될 수 있음

> ### LIKE 실습

```sql
-- 이름에 '호'가 포함되는 사람들의 이름과 성 조회
SELECT first_name, last_name FROM users WHERE first_name LIKE '%호%';

-- 이름이 '준'으로 끝나는 사람들의 이름 조회
SELECT first_name FROM users WHERE first_name LIKE '%준';

-- 서울 지역 전화번호를 가진 사람들의 이름과 전화번호 조회
SELECT first_name, phone FROM users WHERE phone LIKE '02-%';

-- 나이가 20대인 사람들의 이름과 나이 조회
SELECT first_name, age FROM users WHERE age LIKE '2_';

-- 전화번호 중간 4자리가 51로 시작하는 사람들의 이름과 전화번호 조회
SELECT first_name, phone FROM users WHERE phone LIKE '%-51__-%';
```

### IN operator

"Determine whether a value matches any value in a list of values"

값이 값 목록 결과에 있는 값과 일치하는 지 확인

표현식이 값 목록의 값과 일치하는 지 여부에 따라 `true` 또는 `false`를 반환

IN 연산자의 결과를 부정하려면 `NOT IN` 연산자를 사용

> ### IN 실습

```sql
-- 경기도 혹은 강원도에 사는 사람들의 이름과 지역 조회
SELECT first_name, country FROM users WHERE country IN ('경기도', '강원도');
```

### BETWEEN operator

`test_expression BETWEEN low_expression AND high_expression`

값이 값 범위에 있는 지 테스트

값이 지정된 범위에 있으면 `true`를 반환

SELECT, DELETE 및 UPDATE 문의 WHERE 절에서 사용할 수 있음

BETWEEN 연산자의 결과를 부정하려면 `NOT BETWEEN` 연산자를 사용

> ### BETWEEN 실습

```sql
-- 나이가 20살 이상, 30살 이하인 사람들의 이름과 나이 조회
SELECT first_name, age FROM users WHERE age BETWEEN 20 AND 30;

-- 나이가 20살 이상, 30살 이하가 아닌 사람들의 이름과 나이 조회
SELECT first_name, age FROM users WHERE age NOT BETWEEN 20 AND 30;
```

---

## LIMIT clause

```sql
SELECT column_list FROM table_name LIMIT row_count;
```

"Constrain the number of rows returned by a query."

쿼리에서 반환되는 행 수를 제한

SELECT 문에서 선택적으로 사용할 수 있는 절

row_count는 반환되는 행 수를 지정하는 양의 정수를 의미

## OFFSET keyword

LIMIT 절을 사용하면 첫 번째 데이터부터 지정한 수 만큼의 데이터를 받아올 수 있지만, OFFSET과 함께 사용하면 특정 지정된 위치에서부터 데이터를 조회할 수 있음

> ### LIMIT 실습

```sql
-- 첫번째부터 열번째 데이터까지 rowid와 이름 조회
SELECT rowid, first_name FROM users LIMIT 10;

-- 계좌 잔고가 가장 많은 10명의 이름과 계좌 잔고 조회
SELECT first_name, balance FROM users ORDER BY balance DESC LIMIT 10;

-- 나이가 가장 어린 5명의 이름과 나이 조회
SELECT first_name, age FROM users ORDER BY age LIMIT 5;

-- 11번째부터 20번째 데이터의 rowid와 이름 조회
SELECT rowid, first_name FROM users LIMIT 10 OFFSET 10;
```

