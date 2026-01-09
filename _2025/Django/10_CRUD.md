# CRUD with view functions

- django diary 5

---

## HTTP Method

- HTTP: 네트워크 상에서 데이터를 주고 받기 위한 약속

- HTTP Method: 데이터(리소스)에 어떤 요청(행동)을 원하는 지를 나타낸 것

> ### GET

- 어떠한 데이터(리소스)를 조회하는 요청

- GET 방식으로 데이터를 전달하면 Query String 형식으로 보내짐

- DB에 변화를 주지 않음

- CRUD에서 R 역할 담당

> ### POST

- 어떠한 데이터(리소스)를 생성(변경)하는 요청

- POST 방식으로 데이터를 전달하면 Query String이 아닌 Body에 담겨서 보내짐

- 서버로 데이터를 전송할 때 사용, 서버에 변경사항을 만듦

- 리소스를 생성/변경하기 위해 HTTP body에 담아 전송

- CRUD에서 C/U/D 역할을 담당

> ### 403 Forbidden

- 서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미

- 서버가 요청에 대한 접근을 거부할 때 반환됨

- 모델(DB)을 조작하는 것은 단순 조회와 달리 최소한의 신원 확인이 필요하기 때문

> ### CSRF

- Cross-Site-Request-Forgery: 사이트 간 요청 위조

- 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지 보안에 최약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격방법

> ### CSRF Token

- CSRF 공격 방어: Security Token 사용 방식

- 사용자의 데이터에 임의의 난수 값(token)을 부여해 매 요청마다 해당 난수 값을 포함시켜 전송시키도록 함

- 이후 서버에 요청을 받을 때 마다 전달된 token 값이 유효한 지 검승

- 일반적으로 데이터 변경이 가능한 POST, PATCH, DELETE Method 등에 적용

- Django는 DTL에서 `csrf_token` 템플릿 태그를 제공

  - 템플릿에서 내부 URL로 향하는 POST form을 사용하는 경우에 사용

  - 외부 URL로 향하는 POST form에 대해서는 CSRF 토큰이 유출되어 취약성을 유발할 수 있기 때문에 사용해서는 안됨

  - 해당 태그가 없다면 403 forbidden으로 응답

---

## Handling HTTP requests

- HTTP requests 처리에 따른 view 함수 구조 변화

- new-create: CREATE 로직을 구현하기 위한 공통 목적

- edit-update: UPDATE 로직을 구현하기 위한 공통 목적

- new와 edit은 GET요청에 대한 처리만을, create와 update는 POST요청에 대한 처리만을 진행

- 이 점을 기반으로 하나의 view 함수에서 method에 따라 로직이 분리되도록 변경함

---