# INSERT INTO

> 테이블에 새 레코드를 삽입

1. 삽입할 열 이름과 값을 모두 지정

   ```sql
   INSERT INTO table_name (column1, column2, column3, ...)
   VALUES (value1, value2, value3, ...);
   ```

   - 특정 열에만 데이터를 삽입하면, 입력되지 않은 데이터는 null 값

2. 테이블의 모든 열에 대한 값을 추가하는 경우 SQL 쿼리에서 열 이름을 지정할 필요가 없지만 값의 순서가 테이블의 열 순서와 동일한지 확인해야 함

   ```sql
   INSERT INTO table_name
   VALUES (value1, value2, value3, ...);
   ```

- 여러 행 삽입

```sql
INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
VALUES
('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway'),
('Greasy Burger', 'Per Olsen', 'Gateveien 15', 'Sandnes', '4306', 'Norway'),
('Tasty Tee', 'Finn Egan', 'Streetroad 19B', 'Liverpool', 'L1 0AA', 'UK');
```

---

# UPDATE

> 테이블의 기존 레코드를 수정

```SQL
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

- WHERE 절을 생략하면 테이블의 모든 레코드가 업데이트됨

**예시**

```SQL
-- CustomerID가 1인 고객의 담당자와 도시를 업데이트
UPDATE Customers
SET ContactName='Alfred Schmidt', City='Frankfurt'
WHERE CustomerID = 1;

-- 국가가 "Mexico"인 모든 레코드에 대해 ContactName을 "Juan"으로 업데이트
UPDATE Customers
SET ContactName='Juan'
WHERE Country='Mexico';

-- 모든 레코드의 이름을 업데이트
UPDATE Customers
SET ContactName='Juan';
```

---

# DELETE

> 테이블의 기존 레코드를 삭제

```SQL
DELETE FROM table_name WHERE condition;
```

- WHERE 절을 생략하면 테이블의 모든 레코드가 삭제됨

## DROP TABLE

> 테이블을 제거

```SQL
DROP TABLE table_name;
```
