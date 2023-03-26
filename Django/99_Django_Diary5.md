## Admin site

- Django의 가장 강력한 기능 중 하나: automatic admin interface

- "관리자 페이지"

  - 사용자가 아닌 서버의 관리자가 활용하기 위한 페이지

  - 모델 class를 admin.py에 등록하고 관리

  - 레코드 생성 여부 확인에 매우 유용, 직접 레코드를 삽입할 수 도 있음

> ### admin 계정 생성

`$ python manage.py createsuperuser`

username과 password를 입력해 관리자 계정을 생성

- email은 선택사항이기 때문에 입력하지 않아도 됨

- 비밀번호 생성 시 보안상 터미널에 입력되지 않으니 무시하고 입력

> ### admin site 로그인

`http://--/admim/`으로 접속 후 로그인

> ### admin에 모델 클래스 등록

```python
# articles/admin.py

from .models import Article

admin.site.register(Article)
```

---

## CRUD with view functions

### 사전준비

- base 템플릿 작성
`templates/base.html`

- url 분리 및 연결
```python
# crud/urls.py
from django.urls import include

urlpatterns = [
    path('articles/', include('articles.urls')),
]
```
```python
# articles/urls.py
from django.urls import path
from . import views

app_name='articles'
urlpatterns = [
    path('', views.index, name='index'),
]
```

- index 페이지 작성
```django
<!-- templates/articles/index.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>INDEX PAGE</h1>
{% endblock content %}
```
- Article Model 작성
```python
# articles/models.py

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
```

- 관리자 페이지에서 글 3개 작성하기

---

## READ 1_index page

- index 페이지에서는 전체 게시글을 조회해서  출력한다.

```python
# articles/views.py

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
```
```django
<!-- templates/articles/index.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>INDEX PAGE</h1>
  <hr>
  {% for article in articles %}
    <p>{{ article.pk }}번째 글</p>
    <p>제목: {{ article.title }}</p>
    <p>내용: {{ article.content }}</p>
  {% endfor %}
{% endblock content %}
```

## READ 2_detail page

- 개별 게시글 상세 페이지 제작

  - 글의 번호(pk)를 활용해서 하나의 뷰 함수와 템플릿 파일로 대응

- urls

```python
# articles/urls.py

urlpatterns = [
  ...,
    path('<int:pk>/', views.detail, name='detail'),
```

  - variable routing을 통해 특정 게시글 조회

- views

```python
# articles/views.py

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)
```

  - `Article.objects.get(pk=pk)`

    오른쪽 pk는 variable routing을 통해 받은 pk,

    왼쪽 pk는 DB에 저장된 레코드의 id 컬럼

- templates

```django
<!-- articles/detail.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>DETAIL PAGE</h1>
  <h3>{{ article.pk }}번째 글</h3>
  <hr>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>작성 시간: {{ article.updated_at }}</p>
  <p>수정 시간: {{ article.created_at }}</p>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}

<!-- artielcs/index.html -->
<p><a href="{% url 'articles:detail' article.pk %}">제목: {{ article.title }}</a></p>
```

---

## CREATE

- 사용자의 입력을 받을 페이지를 렌더링하는 함수 `new`

- 사용자가 입력한 데이터를 전송받아 DB에 저장하는 함수 `create`

> ### NEW

```python
# articles/urls.py
urlpatterns = [
    path('new/', views.new, name='new'),
]

# articles/views.py
def new(request):
    return render(request, 'articles/new.html')
```
```django
<!-- templates/articles/new.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>NEW</h1>
  <form action="{% url 'articles:create' %}" method="GET">
    <label for="title">Title: </label>
    <input type="text" name="title"><br>
    <label for="content">Content: </label>
    <textarea type="text" name="content"></textarea><br>
    <input type="submit" value="작성">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}
```

> ### create

```python
# articles/urls.py
urlpatterns = [
    path('create/', views.create, name='create'),
]

# articles/views.py
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    article = Article(title=title, content=content)
    article.save()
    return redirect('article:detail', article.pk)
```

- Django shortcut function: `redirect()`

  - 인자에 작성된 곳으로 다시 요청을 보냄

  - 사용 가능한 인자

    1. view name (URL pattern name)

      `return redirect('articles:index`)`

    2. absolute or relative URL

      `return redirect(/articles/)`

- NEW form의 `method="POST"`로 변경 후 csrf 템플릿 태그 작성하기

  - 데이터가 담긴 위치가 바뀌었기 때문에 view함수에서도 수정 필요(GET -> POST)

---

## DELETE

```python
# articles/urls.py
urlpatterns = [
    path('<int:pk>/delete/', views.delete, name='delete'),
]

# articles/views.py
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```
```django
<!-- templates/articles/detail.html -->
...
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
...
```

- detail 페이지에 작성하며 DB에 영향을 미치기 때문에 POST method 사용

---

## UPDATE

- 사용자의 입력을 받을 페이지를 렌더링하는 함수 `edit`

- 사용자가 입력한 데이터를 전송받아 DB에 저장하는 함수 `update`

```python
# articles/urls.py
urlpatterns = [
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]

# articles/views.py
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
```
```django
<!-- articles/edit.html -->
{% extends 'base.html' %}

{% block content %}
  <h1>EDIT</h1>
  <form action="{% url 'articles:update' article.pk %}" method="POST">
    {% csrf_token %}
    <label for="title">Title: </label>
    <input type="text" name="title" value="{{ article.title }}"><br>
    <label for="content">Content: </label>
    <textarea type="text" name="content">{{ article.content }}</textarea><br>
    <input type="submit" value="수정">
  </form>
  <hr>
  <a href="{% url 'articles:index' %}">[back]</a>
{% endblock content %}
```

- html 태그의 value 속성을 사용해 기존에 입력되어 있던 데이터를 출력

- textarea태그는 value 속성이 없으므로 태그 내부 값으로 작성

---

## Hangling HTTP requests

- request.method 값을 기준으로 각각의 역할을 나눠서 합침

```python
# articles/views.py
def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        return render(request, 'articles/create.html')

def update(request, pk):
  article = Article.objects.get(pk=pk)
  if request.method == 'POST':
      article.title = request.POST.get('title')
      article.content = request.POST.get('content')
      article.save()
      return redirect('articles:detail', article.pk)
  else:
      context = {'article': article,}
      return render(request, 'articles/update.html', context)    
```

- delete: POST 요청에 대해서만 삭제가 가능하도록 수정

```python
# articles/views.py
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)
```