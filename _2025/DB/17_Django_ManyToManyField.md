# ManyToManyField

`ManyToManyField(to, **options)`

- 다대다 (M:N, many-to-many) 관계 설정 시 사용하는 모델 필드

- 하나의 필수 인자(M:N 관계로 설정할 모델 클래스)가 필요

- 모델 필드의 RelatedManager를 사용하여 관련 객체를 추가, 제거 또는 만들 수 있음

  add(), remove(), create(), clear()

## 데이터베이스에서의 표현

- Django는 다대다 관계를 나타내는 중개 테이블을 만듦

- 테이블 이름은 ManyToManyField 이름과 이를 포함하는 모델의 테이블 이름을 조합하여 생성됨

- `db_table` arguments를 사용하여 중개 테이블의 이름을 변경할 수도 있음

## ManyToManyField Arguments

### 1. related_name

  - target model이 source model을 참조할 때 사용할 manager name

  - ForeignKey의 related_name과 동일

### 2. through

  - 중개 테이블을 직접 작성하는 경우, through 옵션을 사용하여 중개 테이블을 나타내는 Django 모델을 지정

  - 일반적으로 중개 테이블에 추가 데이터를 사용하는 다대다 관계와 연결하려는 경우(extra data with a many-to-many relationship)에 사용됨

### 3. symmetrical

  - 기본값: True

  - ManyToManyField가 동일한 모델(on self)을 가리키는 정의에서만 사용

  ```python
  class Person(models.Model):
      # friends = models.ManyToManyField('self')
      friends = models.ManyToManyField('self', symmetrical=False)
  ```

  - True일 경우

    `_set` 매니저를 추가하지 않음

    source 모델의 인스턴스가 target 모델의 인스턴스를 참조하면 자동으로 target 모델 인스턴스도 source 모델 인스턴스를 참조하도록 함 (대칭)

    즉, 내가 당신의 친구라면 당신도 나의 친구가 됨

  - 대칭을 원하지 않는 경우 False로 설정

## Related Manager

- N:1 혹은 M:N 관계에서 사용 가능한 문맥(context)

- Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 역참조시에 사용할 수 있는 manager를 생성

  이전 모델 생성 시 objects라는 매니저를 통해 queryset api를 사용했던 것 처럼 related manager를 통해 queryset api를 사용할 수 있음

- 같음 이름의 메서드여도 각 관계(N:1, M:N)에 따라 다르게 사용 및 동작됨

  N:1에서는 target 모델 객체만 사용 가능

  M:N에서는 관련된 두 객체에서 모두 사용 가능

- 메서드 종류

  add(), remove(), create(), clear(), set() 등

## methods

many-to-many relationships 일 때의 동작

- `add()`

  지정된 객체를 관련 객체 집합에 추가

  이미 존재하는 관계에 상요하면 관계가 복제되지 않음

  모델 인스턴스, 필드 값(PK)을 인자로 허용

- `remove()`

  관련 객체 집합에서 지정된 모델 객체를 제거

  내부적으로 `QuerySet.delete()`를 사용하여 관계가 삭제됨

  모델 인스턴스, 필드 값(PK)을 인자로 허용

## 중개 테이블 필드 생성 규칙

1. 소스(source model) 및 대상(target model) 모델이 다른 경우

  - `id`

  - `<containing_model>_id`

  - `<other_model>_id`

2. ManyToManyField가 동일한 모델을 가리키는 경우

  - `id`

  - `from_<model>_id`

  - `to_<model>_id`