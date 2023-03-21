# Template Inheritance

## 템플릿 상속

- 템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춤

- 템플릿 상속을 사용하면 사이트의 모든 공통요소를 포함하고, 하위 템플릿이 재정의(override)할 수 있는 블록을 정의하는 기본 'skeleton' 템플릿을 만들 수 있음

## 관련 태그

`{% extends '' %}`

- 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림

- 반드시 템플릿 최상단(1번 줄)에 작성되어야 하며, 2개 이상 사용할 수 없음

`{% block content %}{% endblock content %} or {% endblock %}`

- 하위 템플릿에서 재지정(overridden)할 수 있는 블록을 정의

- 즉, 하위 템플릿이 채울 수 있는 공간

- 가독성을 높이기 위해 선택적으로 `endblock` 태그에 이름을 지정

---

## Trailing URL Slashes

- Django는 URL 끝에 `/`(Trailing slash)가 없다면 자동으로 붙여주는 것이 기본 설정

  - 모든 주소가 `/`로 끝나도록 구성되어 있음

  - 그러나 모든 프레임워크가 이렇게 동작하는 것은 아님

- Django의 url 설계 철학을 통해 설펴보면,

  - "기술적인 측면에서, `foo.com/bar`와 `foo.com/bar/`는 서로 다른 URL이다."

  - 검색엔진 로봇이나 웹 트래픽 분석 도구에서는 그 둘을 서로 다른 페이지로 본다.

  - 그래서 Django는 URL을 정규화하여 검색엔진 로봇에 혼동하지 않게 해야 한다.

---

## Variable routing

- URL 주소를 변수로 사용하는 것

- URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음

- 즉, 변수 값에 따라 하나의 `path()`에 여러 페이지를 연결시킬 수 있음

### Variable routing 작성 방법

- 변수는 `< >`에 정의하며 view 함수의 인자로 할당됨

- 기본 타입은 string이며, 5가지 타입으로 명시할 수 있음

  1. str
    
    - `/`를 제외하고 비어있지 않은 모든 문자열

    - 작성하지 않을 경우 기본값

  2. int

    - 0 또는 양의 정수와 매치

  3. slug

  4. uuid

  5. path

---

## App URL mapping

- 앱이 많아졌을 때, url과 view 모두 `urls.py`에서 관리하게 되면 코드 가독성도 떨어지고, 프로젝트 유지 보수에 좋지 않음

- 하나의 프로젝트에 여러 앱이 존재한다면, 각각의 앱안에 `urls.py`를 만들고 프로젝트 `urls.py`에서 각 앱의 `urls.py` 파일로 URL 매핑을 위탁할 수 있음

### Including othr URLconfs

- `urlpattern`은 언제든지 다른 URLconf 모듈을 포함(include)할 수 있음

- include되는 앱의 `url.py`에 `urlpatterns`가 작성되어 있지 않다면 에러가 발생함. 빈 리스트라도 작성되어 있어야 한다.

> ### `include()`

- 다른 `URLconf(app/urls.py)`들을 참조할 수 있도록 돕는 함수

- 함수 `include()`를 만나게 되면 URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속처리를 위해 include된 URLconf로 전달

## Naming URL patterns

- `path()`함수의 name인자를 정의해서 사용

- DTL의 Tag중 하나인 URL태그를 사용해서 `path()` 함수에 작성한 name을 사용할 수 있음

- URL 설정에 정의된 특정한 경로들의 의존성을 제거할 수 있음

> ### Built-in tag: url
>
> `{% url 'url_name' %}`

- 주어진 URL 패턴 이름 및 선택적 매개변수와 일치하는 절대경로 주소 반환

- app_name을 지정한 후에는 url태그에서 반드시 `app_name:url_name` 형태로만 사용해야 함.

  그렇지 않으면 NoReverseMatch 에러

### URL namespace

- URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용할 수 있음

---