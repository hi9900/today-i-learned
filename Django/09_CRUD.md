# CRUD

- 대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능 4가지를 묶어서 일컫는 말

- Create: 생성

- Read: 조회

- Update: 수정

- Delete: 삭제

---

## CREATE

- 데이터 객체를 생성하는 3가지 방법

1. 첫번째 방법

```python
# 클래스를 통한 인스턴스 생성
article = Article()

# 클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당
article.title = title
article.content = content

# 인스턴스 save() 메서드 호출 (DB에 데이터 저장)
article.save()
```

2. 두번째 방법

```python
# 인스턴스 생성 시 초기 값을 함께 작성하여 생성
article = Article(title='title', content='content')

article.save()
```

3. 세번째 방법

```python
# QuerySet API 중 create() 메서드 활용
Article.objects.create(title='title', content='content')
```

> ### .save()

- "Saving object"

- 객체를 데이터베이스에 저장함

- 데이터 생성 시 save를 호출하기 전의 객체의 id 값은 `None`

  - id 값은 Django가 아니라 데이터베이스에서 계산되기 때문

- 단순히 모델 클래스를 통해 인스턴스를 생성하는 것은 DB에 영향을 미치지 않기 때문에 반드시 save를 호출해야 테이블에 레코드가 생성됨

---

## READ

- QuerySet API method를 사용해 데이터를 다양하게 조회

- QuerySet API method는 크게 2가지로 분류됨

  1. Methods that "return new querysets"
  
  2. Methods that "do not return querysets"

> ### `all()`

- QuerySet return

- 전체 데이터 조회

> ### `get()`

- 단일 데이터 조회

- 객체를 찾을 수 없으면 `DoesNotExist` 예외를 발생시키고,

  둘 이상의 객체를 찾으면 `MultipleObjectsReturned` 예외를 발생시킴 

- 위와 같은 특징을 가지고 있기 때문에 primary key와 같이 고유성(uniqueness)을 보장하는 조회에서 사용해야 함

> ### `filter()`

- 지정된 조회 매개변수와 일치하는 객체를 포함하는 새 QuerySet을 반환

- 조회된 객체가 없거나 1개여도 반환

### Field lookups

- 특정 레코드에 대한 조건을 설정하는 방법

- QuerySet 메서드 `filter(), exclude(), get()`에 대한 키워드인자로 지정됨

---

## UPDATE

1. 수정하고자 하는 article 인스턴스 객체를 조회 후 반환값을 저장

2. article 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당

3. `save()` 인스턴스 메서드 호출

---

## DELETE

1. 삭제하고자 하는 article 인스턴스 객체를 조회 후 반환값을 저장

2. `delete()` 인스턴스 메서드 호출