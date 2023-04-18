# Response JSON

## JSON 형태로의 서버 응답 변화

지금까지 Django로 작성한 서버는 사용자에게 페이지(html)만 응답하고 있었음

하지만 서버는 페이지 뿐만 아니라 다양한 데이터 타입을 응답할 수 있음

JSON 데이터를 받아 화면을 구성하여 사용자에게 보여주는 것은 Front-end Framework(Vue.js)가 담당할 예정

Django는 더 이상 Template 부분에 대한 역할을 담당하지 않게 되며 Front-end와 Back-end가 분리되어 구성됨

## Response

다양한 방법으로 JSON 데이터 응답

### 1. HTML 응답

- 문서(HTML) 한 장을 응답하는 서버 확인하기

- 지금까지 Django로 응답 해오던 방식

### 2. JsonResponse()를 사용한 JSON 응답

- 문서(HTML) 한 장을 응답하는 것이 아닌 JSON 데이터를 응답해보기

- Django가 기본적으로 제공하는 JsonResponse 객체를 활용하여 Python 데이터 타입을 손쉽게 JSON으로 변환하여 응답 가능

```python
# articles/views.py

from django.http.response import JsonResponse

def article_json_1(request):
    articles = Article.objects.all()
    article_json = {}

    for article in articles:
        articles_json.append(
          {
            'id': article.pk,
            'title': article.title,
            'content': article.content,
            'created_at': article.created_at,
            'updated_at': article.updated_at,
          }
        )
    return JsonResponse(articles_json, safe=False)
```

> ### JsonResponse()

  - JSON-encoded response를 만드는 클래스

  - `safe` parameter

    기본 값: True

    False로 설정 시 모든 타입의 객체를 serialization할 수 있음

    (그렇지 않으면 dict 인스턴스만 허용됨)

### 3. Django Serializer를 사용한 JSON 응답

- Django의 내장 HttpResponse()를 활용한 JSON 응답

- 이전에는 JSON의 모든 필드를 작성해야 했지만 이제는 그렇지 않음

```python
from django.http.response import HttpResponse
from django.core import serializers

def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type='application/json')
```

> ### Serialization

  - "직렬화"

  - 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정

    즉, 어떠한 언어나 환경에서도 "나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정"

  - 변환 포맷은 대표적으로 json, xml, yaml이 있으며 json이 가장 보편적으로 쓰임

  - Django의 `serialize()`는 QuerySet 및 Model Instance와 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환할 수 있는 Python 데이터 타입으로 만들어 줌

### 4. Django REST framework를 사용한 JSON 응답

**Django REST framework(DRF)**

  - Django에서 RESTful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리

  - Web API 구축을 위한 강력한 toolkit를 제공

  - REST framework를 작성하기 위한 여러 기능을 제공

  - DRF의 serializer는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 작동

- DRF 설치 및 등록

```bash
$ pip install djangorestframework
```

```python
# settings.py

INSTALLED_APPS = [
  ...,
  'rest_framework',
]
```

- ModelSerializer 작성

```python
# articles/serializers.py

from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

# articles/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializers import ArticleSerializer

@api_view()
def article_json_3(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
```

- JSON 데이터를 DRF 전용 템플릿으로 응답

---