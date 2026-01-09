# JOIN

> 두 개 이상의 테이블 사이의 관련 열을 기반으로 행을 결합

- (INNER) JOIN: 두 테이블 모두에서 일치하는 값이 있는 레코드를 반환합니다.

- LEFT (OUTER) JOIN: 왼쪽 테이블의 모든 레코드를, 오른쪽 테이블의 일치하는 레코드를 반환합니다.

- RIGHT (OUTER) JOIN: 오른쪽 테이블의 모든 레코드를 반환하고, 왼쪽 테이블의 일치하는 레코드를 반환합니다.

- FULL (OUTER) JOIN: 왼쪽 또는 오른쪽 테이블 중 하나에 일치하는 항목이 있는 경우 모든 레코드를 반환합니다.

---

## INNER JOIN

- INNER JOIN는 두 테이블 모두에서 일치하는 행만 반환한다.

```SQL
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```

- INNER JOIN은 JOIN의 기본 유형으로 생략 가능하다.

```SQL
SELECT column_name(s)
FROM table1
JOIN table2
ON table1.column_name = table2.column_name;
```

- 3개의 테이블 JOIN

**예시**

```SQL
SELECT Orders.OrderID, Customers.CustomerName, Shippers.ShipperName
FROM ((Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID)
INNER JOIN Shippers ON Orders.ShipperID = Shippers.ShipperID);
```

---

## LEFT (OUTER) JOIN

- 왼쪽 테이블(table1)의 모든 레코드를 반환하고 오른쪽 테이블(table2)에서 일치하는 레코드를 반환

- 일치하는 항목이 없으면, 결과는 왼쪽 테이블의 모든 레코드를, 오른쪽 테이블에서 0개의 레코드를 반환한다.

```SQL
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
```

## RIGHT (OUTER) JOIN

- 오른쪽 테이블(table2)의 모든 레코드를 반환하고 왼쪽 테이블(table1)에서 일치하는 레코드를 반환

- 일치하는 항목이 없으면, 결과는 왼쪽 테이블에서 0개의 레코드를, 오른쪽 테이블의 모든 레코드를 반환한다.

```SQL
SELECT column_name(s)
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;
```

---

## FULL (OUTER) JOIN

- 왼쪽(table1) 또는 오른쪽(table2) 테이블 레코드에 일치하는 항목이 있는 경우 모든 레코드를 반환

```SQL
SELECT column_name(s)
FROM table1
FULL OUTER JOIN table2
ON table1.column_name = table2.column_name
WHERE condition;
```

---

## SELF JOIN

- 테이블이 자체적으로 조인된다.

```SQL
SELECT column_name(s)
FROM table1 T1, table1 T2
WHERE condition;
```

- T1 과 T2는 동일한 테이블에 대한 서로 다른 테이블 별칭
