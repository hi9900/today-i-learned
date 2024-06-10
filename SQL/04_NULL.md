# NULL

> 값이 없는 필드

- 테이블의 필드가 선택 사항인 경우 이 필드에 값을 추가하지 않고도 새 레코드를 삽입하거나 레코드를 업데이트할 수 있다.

- 그 필드는 NULL 값으로 저장됩니다.

## IS NULL and IS NOT NULL

```sql
SELECT column_names
FROM table_name
WHERE column_name IS NULL;

SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
```
