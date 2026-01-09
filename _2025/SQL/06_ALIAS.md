# ALIAS

- `AS` 키워드 뒤에 별칭을 지정할 수 있다.

- AS 생략하고 사용할 수도 있다.

```SQL
-- 열에 별칭을 지정
SELECT column_name AS alias_name
FROM table_name;
-- AS 키워드 생략
SELECT column_name alias_name
FROM table_name;

-- 테이블에 별칭을 지정
SELECT column_name(s)
FROM table_name AS alias_name;
```

- 공백을 포함하려면, 대괄호나 큰 따옴표로 묶는다.

```SQL
SELECT column_name AS [Alias Name]
FROM table_name;

SELECT column_name AS "Alias Name"
FROM table_name;
```
