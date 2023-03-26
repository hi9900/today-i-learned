## 인증과 권한

### 사전 설정

- 두 번째 app accounts 생성 및 등록

  - auth와 관련한 경로나 키워드들을 Django 내부적으로 account라는 이름으로 사용하고 있기 때문에 되도록 accounts로 지정하는 것을 권장

  - 다른 이름으로 설정해도 되지만 나중에 추가 설정을 해야 할 일들이 생김

- url 분리 및 매핑

---

### custom User model로 대체하기

- AbstractUser을 상속받는 커스텀 User 클래스 작성

- 기존 User 클래스도 AbstractUser를 상속받기 때문에 커스텀 User 클래스도 완전히 같은 모습을 가지게 됨

```python
# account/models.py

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

- Django 프로젝트에서 User을 나타나는 데 사용한 모델을 방금 생성한 커스텀 User 모델로 지정

```python
# settings.py

AUTH_USER_MODEL = 'accounts.User'
```

- admin.py에 커스텀 User 모델을 등록

  - 기본 User 모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음

```python
# accounts/admin.py
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

> [참고] AbstractUser

  - 관리자 권한과 함께 완전한 기능을 가지고 있는 User model을 구현하는 추상 기본 클래스

  - Abstract base classes (추상 기본 클래스)

    - 몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스

    - 데이터베이스 테이블을 만드는 데 사용되지 않으며, 대신 다른 모델의 기본 클래스로 사용되는 경우 해당 필드가 하위 클래스의 필드에 추가됨

- 데이터베이스 초기화 후 auth_user테이블이 아니라 accounts_user 테이블을 사용

---

## Login

> ### 로그인 페이지 작성

```python
# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
]

# accounts/views.py
from django.contrib.auth.forms import AuthenticationForm

def login(request):
    if request.method == 'POST':
        pass
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```

```django
<!-- accounts/login.html -->
{% extends 'base.html' %}

{% block content %}
<h1>LOGIN</h1>
<form action="{% url 'accounts:login' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="LOGIN">
</form>
{% endblock content %}
```

> ### login()

- login(request, user, backend=None)

- 인증된 사용자를 로그인 시키는 로직으로 view 함수에 사용됨

- 현재 세션에 연결하려는 인증된 사용자가 있는 경우 사용

- HttpRequest 객체와 User 객체가 필요

> ### 로그인 로직 작성

- view 함수 login과의 충돌을 방지하기 위해 import한 login 함수 이름을 auth_login으로 변경해서 사용

```python
# accounts/views.py
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
      ...
```

> ### get_user()

- AuthenticationForm의 인스턴스 메서드

- 유효성 검사를 통과했을 경우 로그인 한 사용자 객체를 반환

---

> ## 세션 데이터 확인하기

- 로그인 후 개발자 도구와 DB에서 django로부터 발급받은 세션확인

  (로그인은 관리자 계정을 만든 후 진행)

1. django_session 테이블에서 확인

2. 브라우저에서 확인

  `개발자도구-Application-Cookies`

---

## Authentication with User

- 템플릿에서 인증 관련 데이터를 출력하는 방법

> ### 현재 로그인 되어있는 유저 정보 출력하기

```django
<!-- base.html -->
<h3>Hello, {{ user }}</h3>
```

- 현재 로그인 한 사용자를 나타내는 User 클래스의 인스턴스가 템프릿 변수 `{{ user }}`에 저장됨

- 클라이언트가 로그인 하지 않은 경우 AnonymousUser 클래스의 인스턴스로 생성

---

## Logout

> ### 로그아웃 로직 작성하기

```python
# accounts/urls.py
urlpatterns = [
    path('logout/', views.logout, name='logout'),
  ]

# accounts/views.py
from django.contrib.auth import logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```
```django
<!-- base.html -->
<form action="{% url 'accounts:logout' %}" method="POST">
  {% csrf_token %}
  <input type="submit" value="logout">
</form>
```