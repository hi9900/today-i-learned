# ORM

- Object-Relational-Mapping

- 객체지향 프로그래밍(Django:python)에서 데이터베이스(DB)를 연동할 때, 데이터베이스와 객체지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

- Django는 내장 Django ORM을 사용하기 때문에 SQL을 사용하지 않고 데이터베이스를 조작할 수 있음

- 장점

  - SQL을 잘 알지 못해도 객체지향 언어로 DB 조작이 가능

  - 객체 지향적 접근으로 인한 높은 생산성

- 단점

  - ORM만으로 세밀한 데이터베이스 조작을 구현하기 어려운 경우가 있음

---

## Database API

- Django가 제공하는 ORM을 사용해 데이터베이스를 조작하는 방법

- Model을 정의하면 데이터를 만들고, 읽고, 수정하고, 지울 수 있는 API를 제공

```
Article.objects.all()
Model class.Manager.Queryset API
```

> ### objects manager

- Django 모델이 데이터베이스 쿼리 작업을 가능하게 하는 인터페이스

- DB를 Python class로 조작할 수 있도록 여러 메서드를 제공하는 manager

- Django는 기본적으로 모든 Django 모델 클래스에 대해 `objects`라는 Manager 객체를 자동으로 추가하고, 이 객체를 통해 특정 데이터를 조작할 수 있음

## Query

- 데이터베이스에 특정한 데이터를 보여달라는 요청

  - 쿼리문 작성

    == 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성

- 파이썬으로 작성된 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료형태로 변환하여 전달

> ### QuerySet

- 데이터베이스에게서 전달받은 객체 목록(데이터 모음)

  - 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음

- Django ORM을 통해 만들어진 자료형이며, 필터를 걸거나 정렬 등을 수행할 수 있음

- `object manager`을 사용하여 복수의 데이터를 가져오는 `queryset method`를 사용할 때 반환되는 객체

- 단, 데이터베이스가 단일한 객체를 반환할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨

- QuerySet API를 활용해 데이터를 생성하고 읽고 수정하고 삭제 == CRUD