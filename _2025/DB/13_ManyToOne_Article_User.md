# N:1 (Article-User)

0개 이상의 게시글은 1개의 회원에 의해 작성될 수 있음

Article(N) - User(1)

Article 모델과 User 모델 간 관계 설정

## Referencing the User model

Django에서 User 모델을 참조하는 방법

### 1. settings.AUTH_USER_MODEL

  - 반환 값: 'accounts.User' (문자열)

  - User 모델에 대한 외래 키 또는 M:N 관계를 정의할 때 사용

  - models.py의 모델 필드에서 User모델을 참조할 때 사용

### 2. get_user_model()

  - 반환 값: User Object (객체)

  - 현재 활성화(active)된 User 모델을 반환

  - 커스터마이징 한 User 모델이 있을 경우는 Custom User 모델, 그렇지 않으면 User을 반환

  - models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용

---

## 모델 관계 설정

1. Article 모델에 User 모델을 참조하는 외래키 작성

```python
# articles/models.py
from django.conf import settings

class Aritcle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ...
```

2. Migration

- 기존에 존재하던 테이블에 새로운 컬럼이 추가되어야 하는 상황이기 때문에, 일련의 과정이 필요

  1. 기본적으로 모든 컬럼은 NOT NULL 제약조건이 있기 때문에 데이터가 없이는 새로 추가되는 외래키 필드 `user_id`가 생성되지 않음

    때문에 기본값을 어떻게 작성할 것인지 선택해야 함

    1을 입력하고 Enter 진행(다음 과정에서 직접 기본 값 입력)

  2. article의 user_id에 어떤 데이터를 넣을 것인지 직접 입력

    1을 입력하고 Enter 진행: 기존에 작성된 게시글이 있다면 모두 1번 회원이 작성한 것으로 처리됨

---

## Django에서 User 모델을 참조하는 방법 정리

- 문자열과 객체를 반환하는 특징과 Django의 내부적인 실행 원리에 관련된 것이므로 간단하게 외우기

- User 모델을 참조할 때

  models.py에서는 `settings.AUTH_USER_MODEL`

  다른 모든 곳에서는 `get_user_model()`