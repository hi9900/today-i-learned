## Authentication with User

## 회원가입

> ### 회원가입 페이지 작성

```python
# accounts/urls.py
urlpatterns = [
    path('signup/', views.signup, name='signup'),
]
# accounts/views.py
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
```
```django
<!-- accounts/signup.html -->
{% extends 'base.html' %}

{% block content %}
<h1>SIGNUP</h1>
<form action="{% url 'accounts:signup' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="회원가입">
</form>
{% endblock content %}
```

> ### UserCreationForm(), UserChangeForm() 커스텀

```python
# accounts/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
```

> ### 회원가입 후 바로 로그인

```python
# accounts/views.py
def signup(request):
  ...
    if form.is_valid():
                user = form.save()
                auth_login(request, user)
                return redirect('articles:index')
```

---

## 회원 탈퇴

```python
# accounts/urls.py
urlpatterns = [
    path('delete/', views.delete, name='delete'),
]

# accounts/views.py
def delete(request):
    request.user.delete()
    return redirect('articles:index')
```
```django
<!-- base.html -->
<form action="{% url 'accounts:delete' %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="회원탈퇴">
</form>
```

> ### 탈퇴 후 세션정보도 함께 지우기

- 탈퇴 후 로그아웃

```python
# accounts/views.py
def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('articles:index')
```

---

## 회원정보 수정

```python
# accounts/urls.py
urlpatterns = [
    path('update/', views.update, name='update'),
]

# accounts/views.py
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)
```
```django
<!-- accounts/update.html -->
{% extends 'base.html' %}

{% block content %}
<h1>회원정보 수정</h1>
<form action="{% url 'accounts:update' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="수정">
</form>
{% endblock content %}
```

> ### CustomUserChangeForm fields 재정의

```python
# accounts/forms.py
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)
```

---

## 비밀번호 변경

```python
# accounts/urls.py
urlpatterns = [
    path('password/', views.change, name='change'),
]

# accounts/views.py
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change.html', context)
```
```django
<!-- accounts/change.html -->
{% extends 'base.html' %}

{% block content %}
<h1>비밀번호 변경</h1>
<form action="{% url 'accounts:change' %}" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit" value="변경">
</form>
{% endblock content %}
```

---

## is_authenticated 적용하기

```
{% if request.user.is_authenticated %}
{% else %}
{% endif %}
```

- 로그인과 비로그인 상태에서 출력되는 링크를 다르게 설정하기

- 인증된 사용자만 게시글 작성 링크를 볼 수 있도록 처리하기

- 인증된 사용자라면 로그인 로직을 수행할 수 없도록 처리하기