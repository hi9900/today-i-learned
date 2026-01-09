## Static files

> ### Django 에서 정적 파일을 구성하고 사용하기 위한 몇가지 단계

1. `INSTALLED_APPS`에 `django.contrib.staticfiles` 포함 확인

2. `settings.py`에서 `STATIC_URL`을 정의하기

3. 앱의 `static` 폴더에 정적 파일을 위치하기

  ex) `articles/static/sample_img.jpg`

4. 템플릿에서 static 템플릿 태그를 사용하여 지정된 경로에 있는 정적파일의 URL 만들기

  ```django
  {% load static %}
  <img src="{% static 'sample_img.jpg' %}" alt="">
  ```

---

## Media Files

> ### FileField/ ImageField를 사용하기 위한 단계

- settings.py에 MEDIA_ROOT, MEDIA_URL 설정

- upload_to 속성을 정의하여 업로드 된 파일에 사용할 MEDIA_ROOT의 하위 경로를 지정(선택사항)

```python
# settings.py
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'
```

### 개발 단계에서 사용자가 업로드한 미디어파일 제공하기

- 사용자로부터 업로드 된 파일이 프로젝트에 업로드 되고 나서, 실제로 사용자에게 제공하기 위해서는 업로드 된 파일의 URL이 필요함

```python
# project/urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [...] 
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

## CREATE

> ### ImageField 작성

```python
# articles/models.py
class Article(models.Model):
  image = models.ImageField(blank=True)
```

- 기존 컬럼 사이에 작성해도 실제 테이블에 추가될 때는 가장 우측(뒤)에 추가됨

> ### Migrations

- ImageField를 사용하려면 Pillow 라이브러리가 필요

```bash
pip install pillow

python manage.py makemigrations
pathon manage.py migrate

pip freeze > requirements.txt
```

> ### image 필드 출력 확인

- 파일 또는 이미지 업로드 시에는 form 태그에 enctype 속성을 변경해야 함

```django
<!-- articles/create.html -->

<form enctype="multipart/form-data">
```

> request.FILES

- 파일 및 이미지는 request의 FILES 속성값에 담겨 넘어감

```python
# articles/views.py

def create(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST, request.FILES)
```

## READ

- 업로드 된 파일의 상대 URL은 Django가 제공하는 url 속성을 통해 얻을 수 있음

  - `article.image.url`: 업로드 파일의 경로

  - `article.image`: 업로드 파일의 파일 이름

```django
<!-- articles/detail.html -->

<img src="{{ article.image.url }}">
```

> ### 이미지 출력

- 이미지를 업로드하지 않은 게시물은 detail 템플릿을 출력할 수 없는 문제 해결하기

  - 이미지 데이터가 있는 경우만 이미지 출력할 수 있도록 처리

```django
<!-- articles/detail.html -->

{% if article.image %}
  <img src="{{ article.image.url }}">
{% endif %}
```

---

## UPDATE

- enctype 속성값 추가

- 이미지 파일이 담겨있는 request.FILES 추가 작성