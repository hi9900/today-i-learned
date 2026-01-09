# M:N (Article - User)

Article과 User의 M:N 관계 설정을 통한 좋아요 기능 구현

# LIKE

## 모델 관계 설정

1. ManyToManyField 작성

```python
# articles/models.py

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTN_USER_MODEL)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

2. Migration 진행 후 에러 확인

  - like_users 필드 생성 시 자동으로 역참조에는 `.article_set` 매니저가 생성 됨

  - 그러나 이전 N:1(Article-User) 관계에서 이미 해당 매니저를 사용 중

    `user.article_set.all()`: 해당 유저가 작성한 모든 게시글 조회

    user가 작성한 글들과 user가 좋아요 누른 글을 구분할 수 없게 됨

  - user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 related_name을 작성해야 함

3. ManyToManyField에 related_name 작성 후 Migration

```python
class Article(models.Model):
    like_users = models.ManyToManyField(settings.AUTN_USER_MODEL, related_name='like_articles')
```

## Like 구현

1. url 및 view 함수 작성

> ### `.exists()`

  - QuerySet에 결과가 포함되어 있으면 True, 그렇지 않으면 False를 반환

  - 특히 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용

```python
# articles/urls.py
urlpatterns = [
  ...,
  path('<int:article_pk>/likes/', views.likes, name='likes'),
]

# articles/views.py
def likes(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
    else:
        article.like_user.add(request.user)
    return redirect('articles:index')
```

2. index 템플릿에서 각 게시글에 좋아요 버튼 출력하기

```django
<!-- articles/index.html -->
...
{% for article in articles %}
  ...
  <form action="{% url 'articles:likes' article.pk %}" metod="POST">
    {% csrf_token %}
    {% if request.user in article.like_user.all %}
      <input type="submit" value="좋아요 취소">
    {% else %}
      <input type="submit" value="좋아요">
    {% endif %}
  </form>
...
```

3. 데코레이터 및 `is_authenticated` 추가

```python
# articles/views.py

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        ...
    return redirect('accounts:login')
```

---

# M:N (Article - User)

User 자기자신과의 M:N 관계 설정을 통한 팔로우 기능 구현

# Follow

자연스러운 follow 흐름을 위한 프로필 페이지를 먼저 작성

## Profile 구현

1. url 및 view 함수 작성

```python
# accounts/urls.py
urlpatterns = [
  ...,
  path('profile/<username>/', views.profile, name='profile'),
]

# accounts/views.py
from django.contrib.auth import get_user_model

def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    context = {
      'person': person,
    }
    return render(request, 'accounts/profile.html', context)
```

2. profile 템플릿 작성

```django
<!-- accoutns/profile.html -->
{% extends 'base.html' %}
{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <hr>
  <h2>{{ person.username }}님의 게시글</h2>
  {% for article in person.article_set.all %}
    <div>{{ article.title }}</div>
  {% endfor %}
  <hr>
  <h2>{{ person.username }}님의 댓글</h2>
  {% for comment in person.comment_set.all %}
    <div>{{ comment.content }}</div>
  {% endfor %}
  <hr>
  <h2>{{ person.username }}님이 좋아요한 게시글</h2>
  {% for article in person.like_articles.all %}
    <div>{{ article.title }}</div>
  {% endfor %}
  <hr>
  <a href="{% url 'articles:index' %}">back</a>
{% endblock content %}
```

3. Profile 템플릿으로 이동할 수 있는 하이퍼링크 작성

```django
<!-- base.html -->
{% if user.is_authenticated %}
<h3>Hello, <a href="{% url 'accounts:profile' user.username %}">{{user}}</a> 님 !</h3>

<!-- articles/index.html -->
작성자: <a href="{% url 'accounts:profile' article.user.username %}">{{article.user}}</a>
```

## Follow 모델 관계 설정

- ManyToManyField 작성 및 Migration 진행

```python
# accounts/models.py
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='follwers')
```

## Follow 구현

1. url 및 view 함수 작성

```python
# accounts/urls.py
urlpatterns = [
  ...,
  path('<int:user_pk>/follow/', views.follow, name='follow'),
]

# accounts/views.py
def follow(request, user_pk):
    User = get_user_model()
    person = User.objects.get(pk=user_pk)
    if person != request.user:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)
    return redirect('accounts:profile', person.username)
```

2. 프로필 유저의 팔로잉, 팔로워 수 & 팔로우, 언팔로우 버튼 작성

```django
<!-- accoutns/profile.html -->
...
<h1>{{ person.username }}님의 프로필</h1>
  <div>
    <div>팔로잉: {{ person.followings.count }} | 팔로워: {{ person.followers.count }}</div>
    <form action="{% url 'accounts:follow' person.pk %}" method="POST">
      {% csrf_token %}
      {% if request.user in person.followers.all %}
        <button type="submit">언팔로우</button>
      {% else %}
      <button type="submit">팔로우</button>
      {% endif %}
    </form>
  </div>
...
```

3. 데코레이터 및 `is_authenticated` 추가

```python
# accounts/views.py
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
      ...
    return redirect('accounts:login')
```