# 인증과 권한

## The Django authentication system

- Django authentication system(인증 시스템)은 인증(Authentication)과 권한(Authorization)부여를 함께 제공(처리)하며, 이러한 기능을 일반적으로 인증 시스템이라고 함
  
- 필수 구성은 `settings.py`에 이미 포함되어 있으며 `INSTALLED_APPS`에서 확인 가능
  
  - `django.contrib.auth`

> Authentication(인증)
  
  - 신원 확인
    
  - 사용자가 자신이 누구인지 확인하는 것
    
> Authorization(권한, 허가)
  
  - 권한 부여
    
  - 인증된 사용자가 수행할 수 있는 작업을 결정

---

## Custom User Model

- "Custom User Model로 대체하기"
  
- 기본 User Model을 필수적으로 Custom User model로 대체하는 이유:
  
  - Django는 기본적인 인증 시스템과 여러가지 필드가 포함된 User Model을 제공, 대부분의 개발 환경에서 기본 User Model을 Custom User Model로 대체함
    
  - 개발자들이 작성하는 일부 프로젝트에서는 django에서 제공하는 built-in User model의 기본 인증 요구사항이 적절하지 않을 수 있음
    
    - 예를 들어, 내 서비스에서 회원가입 시 username 대신 email을 식별 값으로 사용하는 것이 더 적합한 사이트인 경우,
      
      Django 의 User Model은 기본적으로 username을 식별값으로 사용하기 때문에 적합하지 않음
    
- Django는 현재 프로젝트에서 사용할 User Model을 결정하는 `AUTH_USER_MODEL` 설정 값으로 Default User Model을 재정의(override)할 수 있도록 함

> ### AUTH_USER_MODEL

- 프로젝트에서 User을 나타낼 때 사용하는 모델
  
- 프로젝트가 진행되는 동안 (모델을 만들고 마이그레이션 한 후) 변경할 수 없음
  
- 프로젝트 시작 시 설정하기 위한 것이며, 참조하는 모델은 첫번째 마이그레이션에서 사용할 수 있어야 함
  
  - 즉, 첫번째 마이그레이션 전에 확정지어야 하는 값


- 기본 값

```python
# settings.py
AUTH_USER_MODEL = 'auth.User'
```

---

## Login

- 로그인은 Session을 Create하는 과정

> ### AuthenticationForm

- 로그인을 위한 built-in form

  - 로그인 하고자 하는 사용자 정보를 입력 받음

  - 기본적으로 username과 password를 받아 데이터가 유효한 지 검증

- request를 첫번째 인자로 취함

---

## Authentication with User

- base.html에서 context 데이터 없이 user 변수를 사용할 수 있는 이유

  - settings.py의 context processors 설정값 때문

> ### context processors

- 템플릿이 렌더링 될 때 호출 가능한 컨텍스트 데이터 목록

- 작성된 컨텍스트 데이터는 기본적으로 템플릿에서 사용 가능한 변수로 포함됨

- 즉, django에서 자주 사용하는 데이터 목록을 미리 템플릿에 로드해 둔 것

- 현재 user 변수를 담당하는 프로세서는 `django.contrib.auth.context_processors.auth`

---

## Logout

- Session을 Delete하는 과정

> ### logout()

- logout(request)

- HttpRequest 객체를 인자로 받고 반환 값이 없음

- 사용자가 로그인하지 않은 경우 오류를 발생시키지 않음

- 다음 2가지 일을 처리

  1. 현재 요청에 대한 session data를 DB에서 삭제

  2. 클라이언트의 쿠키에서도 sessionid를 삭제

  - 이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인 하고, 이전 사용자의 세션 데이터에 액세스하는 것을 방지하기 위함

  