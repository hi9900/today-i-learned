# 데이터베이스 정규형

데이터베이스를 구조화하는 방법론

데이터의 중복을 최소화하고 일관성과 무결성을 보장하기 위함

데이터의 구조를 더 좋은 구조로 바꾸는 것을 정규화라고 함

관계형 데이터베이스의 경우 6개의 정규형이 있음

## 제 1정규형

하나의 속성값이 복수형을 가지면 안 됨

하나의 속성에는 하나의 값만 들어감

## 제 2정규형

테이블의 기본키에 종속되지 않는 컬럼은 테이블이 분리되어야 함

테이블과 관련없는 컬럼은 분리

테이블에서 부분 함수적 종속성을 제거한 것

  부분 함수적 종속성(Partial Functional Dependency): 키가 아닌 속성이 기본키의 일부분에 종속되는 것

+Composite PK와 Partial Dependency를 키워드로 추가 학습

## 제 3정규형

다른 속성에 의존(종속)하는 속성은 따로 분리할 것

+Transitive Dependency 키워드로 추가 학습

---

## JOIN

두 개 이상의 테이블에서 데이터를 가져와 결합하는 것

- articles의 userID와 users의 id가 같은 데이터 조회

### CROSS JOIN

```sql
SELECT * FROM articles, users WHERE articles.userID=users.rowID;
SELECT * FROM articles, users WHERE userID=users.rowID;
```

### INNER JOIN

`[테이블1] INNER JOIN [테이블2] ON [조건식]`

```sql
SELECT * FROM articles INNER JOIN users ON userid=users.rowID;
```

### LEFT/RIGHT (OUTER) JOIN

```sql
-- articles는 누락되지 않으면서, users 데이터가 있으면 같이 가져오기, 없으면 NULL

SELECT * FROM articles LEFT JOIN users ON userID=users.rowID;

-- users는 누락되지 않으면서, articles 데이터가 있으면 같이 가져오기, 없으면 NULL
SELECT * FROM articles RIGHT JOIN users ON userID=users.rowID;
```

