# SUBQUERY

- SELECT 문 내부에 SELECT 문이 포함된 경우를 의미.

- 내부 SELECT 문을 SUBQUERY라 하며, 외부 SELECT 문은 MAIN QUERY라 한다.

- SUBQUERY는 MAIN QUERY에 의해 실행된다.

- SUBQUERY는 WHERE절, FROM절, HAVING절 등에 사용할 수 있다.

```SQL
-- WHERE절에 SUBQUERY 사용
SELECT *
FROM table_name
WHERE column_name = (SELECT column_name FROM subquery_table_name);
```
