## sending data: form

- `urls.py`

```python
urlpatterns = [
  ...,
  path('throw/', views.throw, name='throw'),
]
```

- `views.py`

```python
def throw(request):
    return render(request, 'throw.html')
```

- `templates/articles/throw.html`

```django
{% extends 'base.html' %}

{% bolck content %}
  <h1>Throw</h1>
  <form action="{% url 'articles:catch' %}" method="GET">
    <label for="message">Throw</label>
    <input type="text" id="message" name="massage">
    <input type="submit">
  </form>
{% endbolck content %}
```

## retrieving data: GET

- `urls.py`

```python
urlpatterns = [
  ...,
  path('catch/', views.catch, name='catch'),
]
```

- `views.py`

```python
def catch(request):
    message = request.GET.get('message')
    context = {
      'message': message,
    }
    return render(request, 'catch.html', context)
```

- `templates/articles/catch.html`

```django
{% extends 'base.html' %}

{% bolck content %}
  <h1>Catch</h1>
  <h2>여기서 데이터{{ message }}를 받았어</h2>
  <a href="{% url 'articles:throw' %}>
  다시 던지러
  </a>
{% endbolck content %}
```

---

## Model 작성하기

- 새 프로젝트, 앱 작성 및 앱 등록

### `models.py` 작성

- 모델 클래스(== 테이블 스키마) 작성

- id컬럼은 테이블 생성 시 Django가 자동으로 생성

```python
# articles/models.py
from django.db import models

class Article(models.Model):
    title = models.CharFireld(max_length=10)
    content = models.TextField()
```

### Migrations

- 모델에 생긴 변화(필드 추가, 수정 등)를 실제 DB에 반영해야 함

```bash
$ python manage.py makemigrations

$ python manage.py migrate
```

- `makemigrations` 명령어 실행 후 `migrations/0001_initial.py` (파이썬으로 작성된 설계도) 생성

- `migrate` 명령어 실행 후 설계도를 실제 데이터베이스(`db.sqlite3` 파일)에 반영

---

## ORM 사전준비

- vscode extension: SQLite 설치

  - db실행: 우클릭 - `Open Database`

  - 좌측 하단 `SQLITE EXPLORER`

- 외부라이브러리 설치 및 설정

  `$ pip install ipython django-extensions`

  설치 후 항상 가상환경 패키지 목록 업데이트하기

  `pip freeze > requirements.txt`

  `settings.py`의 INSTALLED_APPS 설정

  ```python
  # settings.py

  INSTALLED_APPS = [
    # local apps
    'articles',
    
    # third part library
    'django_extensions',
    ...
  ]
  ```

## Django shell

- Django 환경 안에서 진행할 수 있는 Django shell을 사용

  - Django shell 사용

  `$ python manage.py shell`

  - 기본 shell 말고 Django-extension이 제공하는 더 강력한 shell_plus 사용

  `$ python manage.py shell_plus`

---

