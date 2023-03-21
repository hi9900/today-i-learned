# Django

## 가상환경 설정

- 가상환경 생성

  `$ python -m venv venv`

- 가상환경 활성화(ON)

  `$ source venv/Scripts/activate`

- 가상환경 비활성화(OFF)

  `$ deactivate`

- 가상환경 패키지 목록 저장

  `$ pip freeze > requirements.txt`

- 파일로부터 패키지 설치

  `$ pip install -r requirements.txt`

- `.gitignore` 파일로 깃으로 관리하지 않을 파일 골라내기

  [Python, Django, Windows, Pycharm, VisualStudioCodw, Vue, Vuejs:](https://www.toptal.com/developers/gitignore/api/python,django,windows,macos,pycharm,visualstudiocode,vue,vuejs)

## Django 설치

`$ pip install django==3.2.18`

- 버전 명시하지 않으면 가장 최신버전 설치됨

## Django 시작하기

## 프로젝트 생성 

  - 현재 폴더 안 `firstpjt` 폴더를 생성 후 그 안에 프로젝트 생성

  `$ django-admin startproject firstpjt`

  - 현재 폴더에 프로젝트 생성

  `$ django-admin startproject firstpjt`

## 애플리케이션(앱) 생성

  `$ python manage.py startapp articles`

  - 일반적으로 애플리케이션 이름은 '복수형'으로 작성하는 것을 권장

  - 앱(APP) == 하나의 큰 단위<br>
  정해진 규칙은 없으며, 개발자가 판단해서 앱 생성<br>
  여러개의 앱이 아닌 단일 앱으로 개발해도 괜찮음

  - 앱을 사용하기 위해서는 반드시 `settings.py`의 `INSTALLED_APPS` 리스트에 추가해야 함

## 서버 실행

`$ python manage.py runserver`

---

## URL -> View -> Template

### URLs

```python
# firstpjt/urls.py
from articles import views

urlpatterns = [
  ...,
  path('articles/', view.index),
]
```

- path 경로 마지막에 `/` 붙여주기

### View

```python
# articles/views.py
def index(request):
    return render(request, 'articles/index.html')
```

- view 함수의 첫번째 인자는 반드시 request를 받도록 되어 있음

> `render()`
>
> `render(request, template_name, context)`
>
> - 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링 된 텍스트와 함께 HttpResponse(응답) 객체를 반환하는 함수
>
> 1. `request`: 응답을 생성하는 데 사용되는 요청 객체
>
> 2. `template_name`: 템플릿의 전체 이름 또는 템플릿의 경로
>
> 3. `context`: 템플릿에서 사용할 데이터(딕셔너리 타입으로 작성)
>
> - context의 key값으로 html 문서에서 value를 나타낼 수 있음
>
>    `context = { 'num': 30 }`
>
>    `{{ num }}`


- templates

  `app_name/templates/app_name/` 위치에 `func.html` 생성

  - 실제 내용을 보여주는 데 사용되는 파일

  - 파일의 구조나 레이아웃을 정의

  