# GROUP BY

> 특정 그룹으로 묶인 결과를 생성

- SELECT 문의 FROM절 뒤에 작성한다. WHERE 절이 포함된 경우 WHERE 절 뒤에 작성한다.

- 집계 함수( COUNT(), MAX(), MIN(), SUM(), AVG())와 함께 사용되어 결과 집합을 하나 이상의 열로 그룹화하는 경우가 많다.

```SQL
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
ORDER BY column_name(s);
```
