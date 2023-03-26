# Authentication with User

## 회원가입

- 회원 가입은 User Create하는 것이며 UserCreationForm built-in form을 사용

> ### UserCreationForm

- 주어진 username과 password로 권한이 없는 새 user를 생성한 ModelForm
  
- 3개의 필드를 가짐
  
  1. username(from the user model)
    
  2. password1
    
  3. Password2

---

### AbstractBaseUser의 모든 subclass와 호환되는 forms

- 아래 Form 클래스는 User 모델을 대체하더라도 커스텀 하지 않아도 사용 가능
  
  1. AutheticationForm
    
  2. SetPasswordForm
    
  3. PsswordChangeForm
    
  4. AdminPasswordChangeForm
    
- 기존 User 모델을 참조하는 Form이 아니기 때문

### 커스텀 유저 모델을 사용하려면 다시 작성하거나 확장해야 하는 forms

1. UserCreationForm
  
2. UserChangeForm
  
- 두 form 모두 `class Meta: model = User`가 등록된 form이기 때문에 반드시 커스텀(확장)해야 함

> ### get_user_model()

- 현재 프로젝트에서 활성화 된 사용자 모델(active user model)을 반환

---

## 회원 탈퇴

- DB에서 유저를 Delete하는 것과 같음

> ### 탈퇴하면서 해당 유저의 세션 정보도 함께 지우고 싶을 경우

- 탈퇴(1) 후 로그아웃(2)

  - 먼저 로그아웃 해버리면 해당 요청 객체 정보가 없어지기 때문에 탈퇴에 필요한 정보 또한 없어짐

---

## 회원정보 수정

- User를 Update 하는 것이며 UserChangeForm built-in form을 사용

> ### UserChangeForm

- 사용자의 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 ModelForm
  
- UserChangeForm 또한 ModelForm이기 때문에 instance 인자로 기존 user 데이터 정보를 받는 구조 또한 동일함
  
- 이미 이전에 CustomUserChangeForm으로 확장했기 때문에 CustomUserChangeForm 사용

> ### UserChangeForm 사용 시 문제점

- 일반 사용자가 접근해서는 안 될 정보들(fields) 까지 모두 수정이 가능해짐

  - admin 인터페이스에서 사용되는 ModelForm이기 때문

- CustomUserChangeForm에서 접근 가능한 필드를 조정해야 함

---

## 비밀번호 변경

### PasswordChangeForm

- 사용자가 비밀번호를 변경할 수 있도록 하는 Form
  
- 이전 비밀번호를 입력하여 비밀번호를 변경할 수 있도록 함
  
- 이전 비밀번호를 입력하지 않고 비밀번호를 설정할 수 있는 SetPasswordForm을 상속받는 서브 클래스

> ### 암호 변경 시 세션 무효화 방지

- 비밀번호가 변경되면 기존 세션과의 회원 인증번호가 일치하지 않게 되어버려 로그인 상태가 유지되지 못함

- 비밀번호는 잘 변경 되었으나 비밀번호가 변경되면서 기존 세션과의 회원 인증 정보가 일치하지 않기 때문

> ### update_session_auth_hash()

- `update_session_auth_hash(request, user)`

- 현재 요청(current request)과 새 session data가 파생 될 업테이트된 사용자 객체를 가져오고, session data를 적절하게 업데이트 해 줌

- 암호가 변경되어도 로그아웃 되지 않도록 새로운 password의 session data로 session을 업데이트

---

## View decorators

> ### 데코레이터(Decorator)

- 기존에 작성된 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 추가해주는 함수
  
- Django는 다양한 HTTP기능을 지원하기 위해 view 함수에 적용할 수 있는 여러 데코레이터를 제공

### Allowed HTTP methods

- django.views.decorators.http의 데코레이터를 사용하여 요청 메서드를 기반으로 접근을 제한할 수 있음
  
- 일치하지 않는 메서드요청이라면 405 Method Not Allowed를 반환
  
- 메서드 목록
  
  1. `require_http_methods()`

    - view 함수가 특정한 요청 method만 허용하도록 하는 데코레이터
    
  2. `require_POST()`

    - view 함수가 POST 요청 method만 허용하도록 하는 데코레이터
    
  3. `require_safe()`

    - `require_GET`이 있지만 Django에서는 `require_safe`을 사용하는 것을 권장


  ```python
  from django.views.decorators.http import require_http_methods

  @require_http_methods(['GET', 'POST'])
  @require_POST
  @require_safe
  ```

> ### 405 Method Not Allowed

- 요청 방법이 서버에게 전달되었으나 사용 불가능한 상태

---

## Limiting access to logged-in users

- 로그인 사용자에 대한 접근 제한하기
  
  `is_autheticated` attribute

> ### is_authenticated

- User model의 속성 중 하나

- 사용자가 인증 되었는지 여부를 알 수 있는 방법

- 모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성

  - AnonymousUser에 대해서는 항상 False

- 일반적으로 `request.user`에서 이 속성을 사용

  (`request.user.is_authenticated`)

- 권한(permission)과는 관련이 없으며, 사용자가 활성화 상태(active)이거나 유효한 세션(valid session)을 가지고 있는지도 확인하지 않음