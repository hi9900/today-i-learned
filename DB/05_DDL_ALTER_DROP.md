# DDL

## ALTER TABLE

"Modify the structure of an existing table"

## ALTER TABLE statement

SQLite의 ALTER TABLE 문을 사용하면 기존 테이블을 다음과 같이 변경할 수 있음

```sql
-- 1. Rename a table
ALTER TABLE table_name RENAME TO new_table_name;

-- 2. Rename a column
ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name;

-- 3. Add a new column to a table
ALTER TABLE table_name ADD COLUMN column_definition;

-- 4. Delete a column
ALTER TABLE table_name DROP COLUMN column_name;
```

### 1. Rename a table

  테이블 명 변경
  
### 2. Rename a column

  컬럼 명 변경
  
### 3. Add a new column to a table

  새 컬럼 추가

  - 만약 테이블에 기존 데이터가 있을 경우 에러 발생

  ```bash
  Cannot add NOT NULL column with default value NULL
  ```

    이전에 이미 저장된 데이터들을 새롭게 추가되는 컬럼에 값이 없기 때문에 NULL이 작성됨

    그런데 새로 추가되는 컬럼에 NOT NULL 제약조건이 있기 때문에 기본 값 없이는 추가될 수 없다는 에러가 발생한 것

  - DEFAULT 제약조건을 사용하여 해결할 수 있음

  ```sql
  ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL DEFAULT 'no address';
  ```

    address 컬럼이 추가되면서 기존에 있던 데이터들의 address 컬럼 값은 'no address'가 됨

> ### DEFAULT 제약조건

  column 제약조건 중 하나

  데이터를 추가할 때 값을 생략할 시에 기본 값을 설정함
  
### 4. Delete a column

  컬럼 삭제

  - 단, 삭제하지 못하는 경우가 있음

    컬럼이 다른 부분에서 참조되는 경우

    FOREIGN KEY(외래키) 제약조건에서 사용되는 경우

    PRIMARY KEY인 경우

    UNIQUE 제약조건이 있는 경우

      ```bash
      Cannot drop UNIQUE column: "email"
      ```
---
## DROP TABLE

"Remove a table from the database"

```sql
DROP TABLE table_name;
```

- 존재하지 않는 테이블을 제거하면 SQLite에서 오류 발생

```bash
no such table: table_name
```

  한 번에 하나의 테이블만 삭제할 수 있음

  여러 테이블을 제거하려면 여러 DROP TABLE 문을 실행해야 함

  DROP TABLE 문은 실행 취소하거나 복구할 수 없음 따라서 각별히 주의하여 수행해야 함