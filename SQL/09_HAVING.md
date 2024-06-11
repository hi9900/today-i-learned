# HAVING

- WHERE 키워드를 집계 함수와 함께 사용할 수 없기 때문에 HAVING절을 사용한다.

```SQL
SELECT column_name(s)
FROM table_name
WHERE condition
GROUP BY column_name(s)
HAVING condition
ORDER BY column_name(s);
```
