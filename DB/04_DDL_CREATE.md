# DDL

테이블 구조를 관리: CREATE, ALTER, DROP

## CREATE TABLE

"Create a new table in the database"

> ### CREATE TABLE statement

```sql
CREATE TABLE table_name(
  column_1 data_type constraints,
  column_2 data_type constraints,
)
```

---

## SQLite Data Types

### NULL

  Null value

  정보가 없거나 알 수 없음을 의미 (missing information or unknown)

### INTEGER

  정수
    
  크기에 따라 0, 1, 2, 3, 4, 6 또는 8바이트와 같은 가변 크기를 가짐

### REAL

  실수
  
  8바이트 부동 소수점을 사용하는 10진수 값이 있는 실수

### TEXT

  문자 데이터

### BLOB

  입력된 그대로 저장된 데이터 덩어리(대용 타입 없음)
  
  바이너리 등 멀티미디어 파일

### Boolean type

  SQLite에는 별도의 Boolean타입이 없음
  
  대신 Boolean 값은 정수 0(false)과 1(true)로 저장됨

### Date & Time Datatype

  SQLite에는 날짜 및 시간을 저장하기 위한 타입이 없음
  
  대신 built-in "Date And Time Functions"로 TEXT, REAL 또는 INTEGER 값으로 저장할 수 있음

### Binary Data

  데이터의 저장과 처리를 목적으로 0과 1의 이진 형식으로 인코딩 된 파일
  
  기본적으로 컴퓨터의 모든 데이터는 binary data
  
  다만, 이를 필요에 따라서 텍스트 타입으로 변형해서 사용하는 것

## Type Affinity

  타입 선호도

  특정 컬럼에 저장된 데이터에 권장되는 타입
  
  데이터 타입 작성 시 SQLite의 5가지 데이터 타입이 아닌 다른 데이터타입을 선언한다면, 
  내부적으로 각 타입에 지정된 선호도에 따라 5가지 선호도로 인식됨
  
  1. INTEGER
    
  2. TEXT
    
  3. BLOB
    
  4. REAL
    
  5. NUMERIC

- 타입 선호도 존재 이유

  다른 데이터베이스 엔진간의 호환성을 최대화
  
  정적이고 엄격한 타입을 사용하는 데이터베이스의 SQL문을 SQLite에서도 작동하도록 하기 위함

---

## Constraints

제약 조건
  
입력하는 자료에 대해 제약을 정함
  
제약에 맞지 않다면 입력이 거부됨
  
사용자가 원하는 조건의 데이터만 유지하기 위한 
즉, **데이터의 무결성**을 유지하기 위한 보편적인 방법으로 테이블의 특정 컬럼에 설정하는 제약

> ### 데이터 무결성

  데이터 베이스 내의 데이터에 대한 정확성, 일관성을 보장하기 위해 데이터 변경 혹은 수정 시 여러 제한을 두어 데이터의 정확성을 보증하는 것
  
  무결성이란 데이터의 정확성, 일관성을 나타냄

  데이터 베이스에 저장된 데이터의 무결성을 보장하고 데이터베이스의 상태를 일관되게 유지하는 것이 목적

## Constraints 종류

### NOT NULL

  컬럼이 NULL 값을 허용하지 않도록 지정
  
  기본적으로 테이블의 모든 컬럼은 NOT NULL 제약 조건을 명시적으로 사용하는 경우를 제외하고는 NULL 값을 허용함

### UNIQUE

  컬럼의 모든 값이 서로 구별되거나 고유한 값이 되도록 함

### PRIMARY KEY

  테이블에서 행의 고유성을 식별하는 데 사용되는 컬럼
  
  각 테이블에는 하나의 기본키만 있음
  
  암시적으로 NOT NULL 제약 조건이 포함되어 있음

  INTEGER 타입에만 사용 가능

### AUTOINCREMENT

  사용되지 않은 값이나 이전에 삭제한 행의 값을 재사용하는 것을 방지
  
  INTEGER PRIMARY KEY 다음에 작성하면 해당 **rowid**를 다시 재사용하지 못하도록 함

  Django에서 테이블 생성 시 id 컬럼에 기본적으로 사용하는 제약조건

### 기타 Constraints

> ### rowid의 특징

  테이블을 생성할 때마다 rowid라는 암시적인 자동 증가 컬럼이 자동으로 생성됨
  
  테이블의 행을 고유하게 식별하는 64비트 부호있는 정수 값
  
  테이블에 새 행을 삽입할 때마다 정수 값을 자동으로 할당
  
  - 값은 1에서 시작
    
  - 데이터 삽입 시에 rowid 또는 INTEGER PRIMARY KEY 컬럼에 명시적으로 값이 지정되지 않은 경우, SQLite는 테이블에서 가장 큰 rowid보다 하나 큰 다음 순차 정수를 자동으로 할당 (AUTOINCREMENT와 관계 없이)
    
  만약 INTEGER PRIMARY KEY 키워드를 가진 컬럼을 직접 만들면 이 컬럼은 rowid컬럼의 별칭(alias)이 됨
  
  - 즉, 새 컬럼 이름으로 rowid에 엑세스 할 수 있으며 rowid 이름으로도 여전히 엑세스 가능
  
  데이터가 최대 값에 도달하고 새 행을 삽입하려고 하면 SQLite는 사용되지 않은 정수를 찾아 사용
  
  만약 SQLite가 사용되지 않은 정수를 찾을 수 없으면 SQLITE_FULL 에러가 발생
  
  또한 일부 행을 삭제하고 새 행을 삽입하면 SQLite는 삭제된 행에서 rowid값을 재사용하려고 시도