# Django REST framework - Single Model

단일 모델의 data를 Serialization하여 JSON으로 변환

> ### 사전 준비

- Postman 설치

> Postman
>
> - API를 구축하고 사용하기 위한 플랫폼
>
> - API를 빠르게 만들 수 있는 여러 도구 및 기능을 제공

- 가상환경 생성, 활성화 및 패키지 설치

- 새로운 drf 프로젝트 생성, articles 앱 생성, urls 등록

- view 임시 작성

  ```python
  # drf/urls.py
  urlpatterns = [
    path('api/v1/', include('articles.urls')),
  ]

  # articles/urls.py
  urlpatterns = [
    path('articles/', views.article_list),
  ]

  # articles/views.py
  def article_list(request):
      pass
  ```

- Article 모델 작성 및 Migration

- fixtures 데이터 load

  ```python
  # articles/models.py

  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  ```

  ```bash
  $ python manage.py makemigrations
  $ python manage.py migrate
  
  $ python manage.py loaddata articles.json
  ```

- DRF 설치, 등록 및 패키지 목록 업데이트

## MoelSerializer

- `articles/serializers.py` 생성

  serializers.py의 위치나 파일명은 자유롭게 작성 가능

- ModelSerializer 작성

```python
# articles/serializers.py

from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', )
```

> ### ModelSerializer

  - ModelSerializer 클래스는 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공

  1. Model 정보에 맞춰 자동으로 필드를 생성

  2. serializer에 대한 유효성 검사기를 자동으로 생성

  3. `.create()` 및 `.update()`의 간단한 기본 구현이 포함됨

---

> ### Serializer 연습

- shell_plus 실행 및 `ArticleListSerializer` import

```bash
$ python manage.py shell_plus
```

```shell
>>> from articles.serializers import ArticleListSerializer
```

- 인스턴스 구조 확인

```shell
>>> serializer = ArticleListSerializer()

>>> serializer
ArticleListSerializer():
    id = IntegerField(label='ID', read_only=True)
    title = CharField(max_length=10)
    content = CharField(style={'base_template': 'textarea.html' })
```

- Model instance 객체 serialize

```shell
>>> article = Article.objects.get(pk=1)

>>> serializer = ArticleListSerializer(article)

>>> serializer
ArticleListSerializer(<Article: Article object (1)>):
    id = IntegerField(label='ID', read_only=True)
    title = CharField(max_length=10)
    content = CharField(style={'base_template': 'textarea.html' })

# serialized data 조회
>>> serializer.data
{'id': 1, 'title': 'Site economic if ...', ... }
```

- QuerySet 객체 serialize

```shell
>>> articles = Article.objects.all()

>>> serializer = ArticleListSerializer(articles)
>>> serializer.data
AttributeError: ...

# many=True 옵션
>>> serializer = ArticleListSerializer(articles, many=True)
>>> serializer.data
[OrderedDict([('id', 1), ('title', '...'), ('content', '...')], ...)]
```

> ### ModelSerializer - 'many' option

  - 단일 객체 인스턴스 대신 QuerySet 또는 객체 목록을 serialize 하려면 `many=True`를 작성해야 함

---