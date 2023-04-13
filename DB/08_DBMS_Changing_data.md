## Changing data

```sql
-- 실습 테이블 생성
CREATE TABLE classmates(
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);
```

## INSERT statement

```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...)
```

문법 규칙

  1. 먼저 INSERT INTO 키워드 뒤에 데이터를 삽입할 테이블의 이름을 지정

  2. 테이블 이름 뒤에 쉼표로 구분된 컬럼 목록을 추가

    컬럼 목록은 선택사항이지만 컬럼 목록을 포함하는 것이 권장됨

  3. VALUES 키워드 뒤에 쉼표로 구분된 값 목록을 추가

    만약 컬럼 목록을 생략하는 경우, 값 목록의 모든 컬럼에 대한 값을 지정해야 함

    값 목록의 값 개수는 컬럼 목록의 컬럼 개수와 같아야 함

> ### INSERT 실습

```sql
-- 단일 행 삽입
INSERT INTO classmates (name, age, address)
VALUES ('홍길동', 23, '서울');

INSERT INTO classmates VALUES ('홍길동', 23, '서울');

-- 여러 행 삽입
INSERT INTO classmates
VALUES ('김철수', 30, '경기'),
('이영미', 31, '강원');
```

---

## UPDATE statement

```sql
UPDATE table_name 
SET column_1=new_value_1, column_2=new_value_2
WHERE search_condition;
```

문법 규칙

  1. UPDATE 절 이후에 업데이트 할 테이블을 지정

  2. SET 절에서 테이블의 각 컬럼에 대해 새 값을 설정

  3. WHERE 절의 조건을 사용하여 업데이트할 행을 지정

    WHERE 절 생략 시 테이블의 모든 행에 있는 데이터를 업데이트함

  4. 선택적으로 ORDER BY 및 LIMIT 절을 사용하여 업데이트 할 행 수를 지정할 수 있음

> ### UPDATE 실습

```sql
-- 2번 데이터의 이름과 주소를 수정
UPDATE classmates
SET name='김철수한무두루미', address='제주도'
WHERE rowid=2;
```

---

## DELETE statement

```sql
DELETE FROM table_name WHERE search_condition;
```

테이블에서 한 행, 여러 행 및 모든 행을 삭제할 수 있음

문법 규칙

  1. DELETE FROM 키워드 뒤에 행을 제거하려는 테이블의 이름을 지정

  2. WHERE 절에 검색 조건을 추가하여 제거할 행을 식별

    생략 시 테이블의 모든 행을 삭제

  3. 선택적으로 ORDER BY 및 LIMIT 절을 사용하여 삭제할 행의 수를 지정할 수 있음

> ### DELETE 실습

```sql
-- 이름에 '영'이 포함되는 데이터 삭제하기
DELETE FROM classmates WHERE name LIKE '%영%';

-- 테이블의 모든 데이터 삭제하기
DELETE FROM classmates;
```