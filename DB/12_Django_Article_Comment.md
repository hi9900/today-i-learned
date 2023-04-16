a# Comment 구현

## CREATE

1. 사용자로부터 댓글 데이터를 입력받기 위한 CommentForm 작성

```python
# articles/forms.py
from .models import Article, Comment

class CommentForm(forms.ModelForm):
    class Meta:
      model = Comment
      fields = '__all__'
```

2. detail 페이지에서 CommentForm 출력 (view 함수)

```python
# artlcies/views.py
from .forms import ArticleForm, CommentForm

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # 기존 ArticleForm 클래스의 인스턴스 명을 form으로 작성했기 때문에
    # 헷갈리지 않도록 comment_form으로 작성
    comment_form = CommentForm()
    context = {
      'article': article,
      'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)
```

3. detail 페이지에서 CommentForm 출력 (템플릿)

```djagno
<!-- articles/detail.html -->
{% extends 'base.html' %}

{% block content %}
  ...
  <a href="{% url 'articles:index %}>back</a>  
  <hr>
  <form action="#" method="POST">
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit">
  </form>
{% endblock content %}
```

4. 외래 키 필드를 출력에서 제외

- detail 페이지에 출력된 CommentForm을 보면 Comment 클래스의 외래 키 필드인 `article` 또한 데이터 필력이 필요하기 때문에 출력됨

- 하지만, 외래키 필드는 사용자의 입력으로 받는 것이 아니라 view 함수 내에서 받아 별도로 처리되어 저장되어야 함

```python
# articles/forms.py

class CommentForm(forms.ModelForm):
    class Meta:
      model = Comment
      exclude = ('article',)
```

5. 외래 키 받아오기

- detail 페이지의 url에는 해당 게시글의 pk값이 사용되고 있고, 게시글의 pk 값을 댓글의 외래 키로 받아와야 함

```python
# articles/urls.py
urlpatterns = [
  ...,
  path('<int:pk>/comments/', views.comments_create, name='comments_create'),
]

# articles/views.py
def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        # DB에 저장되기 전 article 객체 저장하기
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)
```

> ### save() method

`save(commit=False)`

  - Create, but don't save the new instance.

  - 아직 데이터베이스에 저장되지 않은 인스턴스를 반환

  - 저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용

## READ

작성한 댓글 목록 출력하기

1. 특정 article에 있는 모든 댓글을 가져온 후 context에 추가

```python
# articles/views.py
from .models import Article, Comment

def detail(request, pk):
  ...
  comments = article.comment_set.all()
  context = {
    ...,
    'comments': comments,
  }
```

2. detail 템플릿에서 댓글 목록 출력하기
```django
<!-- articles/detail.html -->
...
  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>{{ comment.content }}</li>
    {% endfor %}
  </ul>
  <hr>
...
```

## DELTE

댓글 삭제 구현하기

```python
# articles/urls.py
urlpatterns = [
  ...,
  path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
]

# articles/views.py
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)
```

댓글 삭제 버튼을 각각의 댓글 옆에 출력

```django
<!-- articles/detail.html -->
...
  <h4>댓글 목록</h4>
  <ul>
    {% for comment in comments %}
      <li>{{ comment.content }}
        <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
          {% csrf_token %}
          <input type="submit" value="DELETE">
        </form>
      </li>
    {% endfor %}
  </ul>
  <hr>
...
```

> ### 댓글 수정

- 댓글 수정도 게시글 수정과 마찬가지로 구현이 가능하지만, 댓글 수정 페이지가 필요하게 됨

- 하지만, 일반적으로 댓글 수정은 수정 페이지로 이동 없이 현재 페이지가 유지된 상태로 댓글 작성 Form 부분만 변경되어 수정할 수 있음

- 이처럼 페이지의 일부 내용만 업데이트 하는 것은 JavaScript의 영역이므로 이후에 진행

---

## Comment 추가사항

### 댓글 갯수 출력하기

1. DTL filter - `length`

2. Queryset API - `count()`

```django
{{ comments|length }}
{{ article.comment_set.all|length }}

{{ comments.count }}
{{ article.comment_set.count }}
```

## 댓글이 없는 경우 대체 컨텐츠 출력

DTL `for empty`

```django
{% for comment in comments %}
  <li>{{ comment.content }}
    <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="DELETE">
    </form>
  </li>
{% empty %}
  <p>댓글이 없어요..</p>
{% endfor %}
```