# N:1 (Comment - User)

Comment(N) - User(1)

0개 이상의 댓글은 1개의 회원에 의해 작성될 수 있음

Comment 모델과 User 모델 간 관계 설정

## 모델 관계 설정

1. Comment 모델에 User 모델을 참조하는 외래 키 작성

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```

2. Migration

- 이전에 User-Article 모델 관계 설정때와 마찬가지로 기존에 존재하던 테이블에 데이터 처리 후 Migration 진행

## CREATE

인증된 회원의 댓글 작성 구현하기

작성하기 전 로그인을 먼저 진행한 상태로 진행

1. CommentForm

- create 템플릿에서 불필요한 필드 제외

```python
# articles/forms.py

class CommentForm(form.ModelForm):
    class Meta:
        model = Comment
        exclude = ('article', 'user',)
```

2. 외래 키 데이터 추가

```python
# articles/views.py

def comments_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save
    return redirect('articles:detail', article.pk)
```

## READ

detail 템플릿에서 각 댓글의 작성자 출력

```django
<!-- articles/detail.html -->
...
{% for comment in comments %}
  <li>
    {{ comment.user }} - {{ comment.content }}
...
```

## DELETE

- 댓글 삭제 시 작성자 확인

```python
# articles/views.py

def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)
```

- 해당 댓글의 작성자가 아니라면, 삭제 버튼을 출력하지 않도록 함

```django
<!-- articles/detail.html -->
...
{% for comment in comments %}
  <li>
    {{ comment.user }} - {{ comment.content }}
    {% if request.user == comment.user %}
      <!-- 삭제 버튼 -->
    {% endif %}
...
```

---

## 인증된 사용자에 대한 접근 제한하기

`is_authenticated`와 View `decorator`를 활용한 코드 정리

- 인증된 사용자인 경우에만 댓글 작성 및 삭제하기

```python
# articles/views.py

@require_POST
def comments_create(request, pk):
    if request.user.is_authenticated:
        # comments_create 코드
    return redirect('accounts:login')

@require_POST
def comments_delete(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        # comments_delete 코드
    return redirect('articles:detail', article_pk)
```

- 비인증 사용자는 CommentForm을 볼 수 없도록 하기

```django
<!-- articles/detail.html -->
...
{% if request.user.is_authenticated %}
  <!-- 댓글 작성 Form -->
{% else %}
  <a href="{% url 'accounts:login' %}>[댓글을 작성하려면 로그인하세요.]</a>
{% endif %}
...
```