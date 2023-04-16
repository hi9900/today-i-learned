# Improve Query

## Django ORM

### 장점

  - SQL을 몰라도 사용 가능

  - SQL을 사용하는 대신 객체 지향적으로 데이터를 조회할 수 있음

  - 재사용, 유지보수에 용이

  - DBMS에 대한 의존도가 떨어짐

### 단점

  - 복잡한 SQL문을 그대로 재현하기 어려움

  - 자세히 모르고 사용하면 이상한 쿼리가 나갈 수 있음

    N+1 Problem이 대표적

### 특징

  - Django ORM은 기본적으로 `Lazy Loading` 전략을 사용한다.

  ORM을 작성하면 Database에 Query 하는 것이 아니라, 실제로 데이터를 사용할 때 Database에 Query를 날린다.

  ORM 함수를 호출할 때가 아닌, QuerySet이 실제로 평가될 때 DB를 호출한다.

  QuerySet이 실제로 모습을 드러내야 할 때 DB를 부른다는 것!

    print, slicing, len, list, iteration, ...

  똑같은 데이터를 사용한다면 캐싱을 내부적으로 해둔다.

## Lazy Loading (지연 로딩)

  - Django ORM은 기본적으로 Lazy Loading 전략을 사용한다.

  - 성능 개선을 위해 사용

    객체와 RDB를 연결하는 ORM 입장에서는, 객체 코드로 다루는 모든 경우에 호출을 하는 것은 매우 비용이 많이 드는 작업이다.

    따라서 실제로  해당 데이터가 필요한 시점에 데이터베이스를 호출하는 것

> ### N+1 Problem

  지연 로딩으로 인해 발생하는 문제

  ```python
  def get_pet_data():
      reset_queries()

      pet_qs = Pet.objects.all()
      for pet in pet_qs:
          print(pet.name, pet.pet_sitter.first_name)
      
      query_info = connection.queries
      for query in query_info:
          print(query['sql'])
  ```

## Eager Loading (즉시 로딩)

  - Lazy Loading: 지금 사용하지 않으면 안 가져옴

  - Eager Loading: 지금 사용하지 않더라도 가져옴. 보통 여러 테이블의 데이터를 한 번에 가져올 때 사용

  - Django ORM에서는 select_related(정참조 관계)와 prefetch_related(역참조 관계)로 사용

> ### 문제 해결

  ```python
  def get_pet_data():
    reset_queries()

    # pet_qs = Pet.objects.all()
    pets = Pet.objects.all().select_related('pet_sitter')
    for pet in pets:
        print(pet.name, pet.pet_sitter.first_name)
    
    query_info = connection.queries
    for query in query_info:
        print(query['sql'])
  ```

> ### select_related

- 1:1 또는 N:1 참조 관계에서 사용

- SQL에서 INNER JOIN 절을 활용

  SQL의 INNER JOIN을 사용하여 참조하는 테이블의 일부를 가져오고, SELECT FROM을 통해 관련된 필드들을 가져옴

> ### prefetch_related

- M:N 또는 N:1 역참조 관계에서 사용

- SQL이 아닌 Python을 통한 JOIN이 진행됨

> ### Django ORM - Caching

- 특정 데이터를 불러온 후 재사용 할 경우 ORM은 저장해둔 캐싱을 사용한다.

- 불러온 데이터에 변화를 일으키는 쿼리가 아니라면 저장해둔 데이터를 사용한다는 것

## Django ORM 특징

- 기본적으로 모든 ORM은 지연로딩이다.

  실제로 필요할 때 데이터베이스에서 데이터를 가져온다.

- ORM을 이용해서 가져온 데이터는 캐싱된다.

- 순서를 변경하는 것만으로 데이터베이스의 콜을 줄일 수 있으니 ORM의 동작 원리를 잘 알고 사용하는 것이 중요하다.

