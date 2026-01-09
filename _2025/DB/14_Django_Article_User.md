# N:1 (Article - User)

## CREATE

인증된 회원의 게시글 작성 구현하기

작성하기 전 로그인을 먼저 진행한 상태로 진행

1. ArticleForm

- ArticleForm 출력 시 create 템플릿에서 불필요한 필드(user)가 출력 됨

  (이전에 CommentForm에서 외래키 필드 article이 출력되는 상황과 동일한 상황)

- user 필드에 작성해야 하는 user 객체는 view 함수의 request 객체를 활용

```python
# articles/forms.py
class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = ('title', 'content',)
```

2. 외래 키 데이터 저장

- Form 수정 후 게시글 작성 시 `NOT NULL constraint failed: articles_article.user_id` 에러 발생

- "NOT NULL 제약 조건이 실패했다. articles_article 테이블의 user_id 컬럼에서"

- 게시글 작성 시 외래 키에 저장되어야 할 작성자 정보가 누락됨

- 작성자 정보 함께 저장될 수 있도록 save의 commit 옵션 활용

```python
# articles/views.py

@login_required
@require_http_method(['GET', 'POST'])
def crete(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
```

## DELETE

게시글 삭제 시 작성자 확인

- 현제 삭제를 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 삭제할 수 있도록 함

```python
# articles/views.py

@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
    return redirect('articles:detail', article.pk)
```

## UPDATE

게시글 수정 시 작성자 확인

- 수정을 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 수정 할 수 있도록 함

```python
# articles/views.py

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
```

- 추가로 해당 게시글의 작성자가 아니면, 수정/삭제 버튼을 출력하지 않도록 함

```django
<!-- articles/detail.html -->
...
{% if request.user == article.user %}
    <!-- 수정/삭제 버튼 출력 -->
{% endif %}
...
```

## READ

index와 detail 템플릿에서 각 게시글의 작성자 출력

```django
<!-- .html -->

<p>작성자: {{ article.user }}</p>
```
