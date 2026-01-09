# EXISTS

> subquery에 레코드가 있는 지 테스트

- subquery가 하나 이상의 레코드를 반환하면, TRUE를 반환한다.

```SQL
SELECT column_name(s)
FROM table_name
WHERE EXISTS (SELECT column_name FROM table_name WHERE condition);
```
