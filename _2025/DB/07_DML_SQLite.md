## Aggregate function

집계함수

각 집합의 최댓값, 최솟값, 평균, 합계 및 갯수를 계산을 수행하고 단일 값을 반환

  여러 행으로부터 하나의 결괏값을 반환

  MAX(), MIN(), AVG(), SUM(), COUNT()

  AVG, MAX, MIN, SUM은 숫자를 기준으로 계산이 되어져야 하기 때문에 반드시 컬럼의 데이터 타입이 숫자(INTEGER)일 때만 사용 가능

SELECT 문의 GROUP BY 절과 함께 사용됨

> ### Aggregate function 예시

```sql
-- users 테이블의 전체 행 수 조회
SELECT COUNT(*) FROM users;

-- 전체 유저의 평균 balance 조회
SELECT AVG(balance) FROM users;

-- 전라북도의 평균 balance 조회
SELECT country, AVG(balance) FROM users WHERE country="전라북도";
```

## GROUP BY clause

```sql
SELECT column_1, aggregate_function(column_2) FROM table_name
GROUP BY column_1, column_2;
```

"Make a set of summary rows from a set of rows"

특정 그룹으로 묶인 결과를 생성

선택된 컬럼 값을 기준으로 데이터(행)들의 공통 값을 묶어 결과로 나타냄

SELECT 문에서 선택적으로 사용 가능한 절

SELECT 문의 FROM 절 뒤에 작성 (WHERE절이 포함된 경우 WHERE절 뒤에 작성)

각 그룹에 대해 집계함수(aggregate function)를 적용하여 각 그룹에 대한 추가적인 정보 제공가능

```sql
-- 지역 별 평균 balance
SELECT country, AVG(balance) FROM users GROUP BY country;
SELECT country, AVG(balance) FROM users
GROUP BY country ORDER BY AVG(balance) DESC;

-- 나이가 30살 이상인 사람들의 평균 나이
SELECT AVG(age) FROM users WHERE age>=30;

-- 각 지역별로 몇명씩 살고 있는 지 조회
SELECT country, COUNT(*) FROM users GROUP BY country;
-- 각 지역별로 그룹이 나눠졌기 때문에 COUNT(*)은 지역 별 데이터 개수를 셈
```

> ### [참고] COUNT 참고사항

  - 이전 쿼리에서 COUNT(), COUNT(age), COUNT(last_name) 등 어떤 컬럼을 넣어도 결과는 같음

  - 현재 쿼리에서는 그룹화 된 country를 기준으로 카운트하는 것이기 때문에 어떤 컬럼을 카운트해도 전체 개수는 동일하기 때문

> ### GROUP BY 실습

```sql
-- 각 성씨가 몇명씩 있는 지 조회
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
-- AS 키워드를 사용해 조회된 컬럼명을 임시로 변경
SELECT last_name, COUNT(*) AS number_of_name FROM users 
GROUP BY last_name;

-- 인원이 가장 많은 성씨 순으로 조회
SELECT last_name, COUNT(*) FROM users 
GROUP BY last_name ORDER BY COUNT(*) DESC;

-- 각 지역 별 평균 나이 조회
SELECT country, AVG(age) FROM users GROUP BY country;
```
---