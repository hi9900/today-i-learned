# SQL

Structured Query Language

관계형 데이터베이스에서 데이터를 관리하기 위해 사용하는 언어

## SQL Commands

명령어는 특성에 따라 세가지 그룹으로 분류

### 1. DDL(Data Definition Language)

  데이터 정의 언어

  관계형 데이터베이스 구조(테이블, 스키마)를 정의(생성, 수정 및 삭제)하기 위한 명령어

  CREATE, DROP, ALTER

### 2. DML(Data Manipulation Language)

  데이터 조작 언어

  데이터를 조작(추가, 조회, 변경, 삭제)하기 위한 명령어

  INSERT, SELECT, UPDATE, DELETE

### 3. DCL(Data Control Language)

  데이터 제어 언어

  데이터의 보안, 수행제어, 사용자 권한 부여 등을 정의하기 위한 명령어

  GRANT, REVOKE, COMMIT, ROLLBACK

  - SQLite는 파일로 관리되는 DB이기 때문에 SQL을 이용한 접근 제한이 아닌 운영체제의 파일 접근 권한으로만 제어 가능

    SQLite에는 권한 설정을 담당하는 GRANT(권한부여)와 REVOKE(권한회수)는 지원하지 않음

## SQL Syntax

> SQL Syntax 예시
>
> ```sql
> SELECT column_name FROM table_name;
> ```

모든 SQL문(statement)은 SELECT, INSERT, UPDATE 등과 같은 키워드로 시작

  SQL 키워드는 대소문자를 구분하지 않지만, 대문자로 작성하는 것을 권장

하나의 statement는 세미콜론(`;`)으로 끝남

  세미콜론은 각 SQL문을 구분하는 표준 방법

> ### Statement(문)

  독립적으로 실행할 수 있는 완전한 코드조각

  statement는 clause로 구성됨

> ### Clause(절)

  statement의 하위 단위

- SQL Syntax 예시는

  SELECT statement라 부름

  2개의 clause로 구성됨

  1. SELECT column_name

  2. FROM table_name