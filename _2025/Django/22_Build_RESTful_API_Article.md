# Article - RESTful API

## URL과 HTTP requests methods 설계

|             | GET     | POST | PUT     | DELETE  |
| ----------- | :-------: | :----: | :-------: | :-------: |
| articles/   | 전체 글 조회 | 글 작성 | 전체 글 수정 | 전체 글 삭제 |
| articles/1/ | 1번 글 조회 |      | 1번 글 수정 | 1번 글 삭제 |

---

### GET - List

- 게시글 데이터 목록 조회

- DRF에서 `api_view` 데코레이터 작성은 필수

> ### api_view decorator

  - DRF view 함수가 응답해야 하는 HTTP 메서드 목록을 받음

  - 기본적으로 GET 메서드만 허용되며 다른 메서드 요청에 대해서는 `405 Method Not Allowed`로 응답

```python
# articles/urls.py

urlpatterns = [
    path('articles/', views.article_list),
]

# articles/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Article
from .serializers import ArticleListSerializer


@api_view(['GET'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
```

### GET - Detail

- 단일 게시글 데이터 조회

- 각 데이터의 상세 정보를 제공하는 ArticleSerializer 정의

```python
# articles/serializers.py

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
```

- url 및 view 함수 작성

```python
# articles/urls.py

urlpatterns = [
    ...,
    path('articles/<int:article_pk>/', views.article_detail),
]

# articles/views.py

from .serializers import ArticleListSerializer, ArticleSerializer


@api_view(['GET'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
```

### POST

- 게시글 데이터 생성

- 요청에 대한 데이터 생성이 성공했을 경우는 `201 Create` 상태코드를 응답하고

  실패했을 경우는 400 `Bad request`를 응답

> ### Raising an exception on invalid data

  - 유효하지 않은 데이터에 대해 예외 발생시키기

  - `is_valid()`는 유효성 검사 오류가 있는 경우 `ValidationError` 예외를 발생시키는 선택적 `raise_exception` 인자를 사용할 수 있음

  - DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 `HTTP 400` 응답을 반환

```python
# articles/views.py

from rest_framwork import status


@api_view(['GET', 'POST'])
def article_list(request):
    ...
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # raise_exception으로 대체
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

### DELETE

- 단일 게시글 데이터 삭제

- 요청에 대한 데이터 삭제가 성공했을 경우 `204 NO Content` 상태코드 응답

  (명령을 수행했고, 더 이상 제공할 정보가 없는 경우)

```python
# articles/views.py

@api_view(['GET', 'DELETE'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    ...
    elif request.method == 'DELETE':
        article.delete()      
        return Response(status=status.HTTP_204_NO_CONTENT)
```

### PUT

- 단일 게시글 데이터 수정

- 요청에 대한 데이터 수정이 성공했을 경우 `200 OK` 상태코드 응답

```python
# articles/views.py

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    ...
    elif request.method == 'PUT':
        # instance가 첫번째 인자이기 때문에 'instance=' 생략
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # status 기본 값은 `200 OK`이기 때문에 생략
            return Response(serializer.data)
```