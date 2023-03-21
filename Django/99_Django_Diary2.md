## 템플릿 상속 예시

- `project/templates/base.html`에 skeleton 템플릿을 작성

```django
<!DOCTYPE html>
...
<!-- bootstrap CSS CDN -->

{% block content %}
{% endblock content %}

<!-- bootstrap JS CDN -->
```

- `settings.py`에 `base.html` 경로 추가

```python
...
TEMPLATES = [
  {
    'DIRS': [BASE_DIR / 'templates'],
  }
]
...
```

- 상속받을 html 파일

```django
{% extends 'base.html' %}

{% block content %}
<!-- 해당 템플릿 본문 -->
{% endblock content %}
```

---

## Variable routing

- `urls.py`

```python
urlpatterns=[
  ...,
  path('hello/<name>/', views.hello),
]
```

- variable routing으로 할당된 변수를 인자로 받고, 템플릿 변수로 사용할 수 있음

- `articles/view.py`

```python
def hello(request, name):
  context = {
    'name': name,
  }
  return render(request, 'hello.html', context)
```

- `templates/articles/hello.html`

```django
{% extends 'base.html' %}

{% block content %}
  <h1>안녕하세요, {{ name }}</h1>
{% endblock content %}
```

---

## App URL mapping, Naming URL patterns

- 각각의 app 폴더 안에 `urls.py`를 생성 후 관리

```python
# project/urls.py

from django.urls import path, include

urlpatterns = [
  ...,
  path('articles/', include('articles.urls')),
]
```

```python
# articles/urls.py

from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
  path('index/', views.index, name='index'),
  path('greeting/', views.greeting, name='greeting'),
]
```

```django
<!-- templates/articles/index.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>INDEX</h1>
  <a href="{% url 'greeting' %}">바로가기</a>
{% endblock content %}
```