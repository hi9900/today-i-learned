## CREATE

- 새 글을 작성할 new

- new 글을 생성할 create

## READ

- 인덱스페이지 전체 조회

- 상세페이지 단일 조회

`views.py`

```python
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
```

`articles/index.html`

```django
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

## UPDATE

- 

## DELETE