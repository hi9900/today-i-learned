# Django Model

- Model(이하 모델)의 핵심 개념과 ORM을 통한 데이터베이스 조작 이해

- Django는 웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 추상적인 계층(모델)을 제공

## Database

- 체계화된 데이터의 모임
  
- 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템
  
### Database 기본구조

> ### 스키마(Schema)

- 뼈대(Structure)
  
- 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조

- 스키마 예시

  | column | datatype |
  | ------ | -------- |
  | id     | INT      |
  | name   | TEXT     |
  | age    | INT      |
  | email  | TEXT     |

> ### 테이블(Table)

- 필드와 레코드를 사용해 조작된 데이터 요소들의 집합
  
- 관계(Relation)라고도 부름

- 필드(field)
  
  - 속성, 컬럼(Column)
    
  - 각 필드에는 고유한 데이터 형식(INT, TEXT 등)이 지정됨

- 레코드(record)
  
  - 튜플, 행(Row)
    
  - 테이블의 데이터는 레코드에 저장됨
    
- PK(Primary Key)
  
  - 기본 키
    
  - 각 레코드의 고유한 값(식별자로 사용)
    
  - 기술적으로 다른 항목과 절대로 중복될 수 없는 단일값(unique)
    
  - 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용됨

- 쿼리(Query)
  
  - 데이터를 조회하기 위한 명령어
    
  - 조건에 맞는 데이터를 추출하거나 조작하는 명령어(주로 테이블형 자료구조에서)
    
  - "Query를 날린다." 
  
    == "데이터베이스를 조작한다"

---

## Model

- Django는 Model을 통해 데이터에 접근하고 조작
  
- 사용하는 데이터들의 필수적인 필드들과 동작들을 포함
  
- 저장된 데이터베이스의 구조(layout)
  
- 일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑(mapping)
  
  - 모델 클래스 1개 == 데이터베이스 테이블 1개

> ### Model 이해하기

- 모델 클래스를 작성하는 것 == 데이터베이스 테이블의 스키마를 정의하는 것

```python
# articles/models.py

class Article(models.Model):
  title = models.CharField(max_length=10)
  content = models.TextField()
```

`(models.Model)`

- 각 모델은 django.models.Model 클래스의 서브클래스

  - 즉, 각 모델은 django.db.models 모듈의 Model 클래스를 상속받아 구성됨

  - 클래스 상속 기반 형태의 Django 프레임워크

`class Article`

- Article에는 어떤 데이터 구조가 필요한 지 정의

- models 모듈을 통해 어떠한 타입의 DB 필드(컬럼)을 정의할 것인지 정의

`title`, `content`

- 클래스 변수(속성)명

  : DB 필드의 이름

`models.CharField(...)`, `models.TextField()`

- 클래스 변수 값(models 모듈의 Field 클래스)

  : DB 필드의 데이터 타입

> ### Django Model Field

- Django는 모델 필드를 통해 테이블의 필드(컬럼)에 저장할 데이터 유형(INT, TEXT 등)을 정의
  
- 데이터 유형에 따라 다양한 모델 필드를 제공
  
  - `DateField(), CharField(), IntegerField()` 등

- `CharField(max_length=None, **options)`
  
  - 길이의 제한이 있는 문자열을 넣을 때 사용
    
  - `max_length`
    
    - 필드의 최대 길이(문자)
      
    - CharField의 필수 인자
      
    - 데이터베이스와 Django의 유효성 검사(값을 검증하는 것)에서 활용됨
      
- `TextField(**options)`
  
  - 글자의 수가 많을 때 사용
    
  - `max_length` 옵션 작성 시 사용자 입력 단계에서는 반영되지만, 모델과 데이터베이스 단계에는 적용되지 않음(CharField를 사용해야 함)
    
    - 실제로 저장될 때 길이에 대한 유효성을 검증하지 않음

---

## Migrations

- Django가 모델에 생긴 변화(필드 추가, 수정 등)를 실제 DB에 반영하는 방법

> ### makemigrations

- 모델의 변경사항에 대한 새로운 migration을 만들 때 사용

- 파이썬으로 작성된 설계도: `0001_initial.py`

> ### migrate

- makemigrations로 만든 설계도를 실제 데이터베이스에 반영하는 과정(db.sqlite3 파일에 반영)

- 결과적으로 모델의 변경사항과 데이터베이스를 동기화

> ### 기타명령어

1. `$ python manage.py showmigrations`

  - migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 용도

  - `[X]`표시가 있으면 migrate가 완료되었음을 의미

2. `$ python manage.py sqlmigrate articles 0001`

  - 해당 migrations 파일이 SQL 문으로 어떻게 해석될 지 미리 확인할 수 있음

---