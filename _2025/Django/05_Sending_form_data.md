# Sending form data(Client)

## HTML `<form>` element

- 데이터가 전송되는 방법을 정의

- 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit 등)을 제공

- 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당

- 핵심 속성: `action`, `method`

> ## HTML form's attributes

### 1. action

- 입력 데이터가 전송될 URL을 지정

- 데이터를 어디로 보낼 것인지 지정하는 것이며 이 값은 반드시 유효한 URL이어야 함

- 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐

### 2. method

- 데이터를 어떻게 보낼 것인지 정의
  
- 입력 데이터의 HTTP request methods를 지정
  
- HTML form 데이터는 오직 2가지 방법으로만 전송할 수 있는데, 바로 GET 방식과 POST 방식

---

## HTML `<input>` element

- 사용자로부터 데이터를 입력 받기 위해 사용
  
- `type` 속성에 따라 동작 방식이 달라진다

  - type을 지정하지 않은 경우, 기본값은 "text"
    
- 핵심 속성: name

> ## HTML input's attribute

### name

- form을 통해 데이터를 제출(submit)했을 때 name 속성에 설정된 값을 서버로 전송하고, 

  서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근할 수 있음
  
- 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑하는 것

---

## HTML request methods

- HTTP: HTML 문서와 같은 리소스(데이터, 자원)들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)

  웹에서 이루어지는 모든 데이터 교환의 기초
  
- HTTP는 주어진 리소스가 수행할 원하는 작업을 나타내는 request methods를 정의
  
  자원에 대한 행위(수행하고자 하는 동작)를 정의
  
  주어진 리소스(자원)에 수행하길 원하는 행동을 나타냄
  
- HTTP Method: 
  
  GET, POST, PUT, DELETE

### GET

- 서버로부터 정보를 조회하는 데 사용
  
  - 즉, 서버에서 리소스를 요청하기 위해 사용

- 데이터를 가져올 때만 사용해야 함
  
- 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송
  
  - 데이터는 URL에 포함되어 서버로 보내짐

- GET과 get 모두 대소문자 관계없이 동일하게 동작하지만 명시적 표현을 위해 대문자 사용을 권장
  
> ### Query String Parameters

- Query String이라고도 함

- 사용자가 입력 데이터를 전달하는 방법 중 하나로, URL 주소에 데이터를 파라미터를 통해 넘기는 것
  
- 이러한 문자열은 앰퍼샌드(`&`)로 연결된 `key=value` 쌍으로 구성되며 기본 URL과 물음표(`?`)로 구분됨
  
  - ex. `http://host:port/path?key=value&key=value`
  
- 정해진 주소 이후에 물음표를 쓰는 것으로 Query String이 시작함을 알림
  
- `key=value`로 필요한 파라미터의 값을 적음
  
  - `=`로 key와 value가 구분됨

- 파라미터가 여러 개일 경우 `&`를 붙여 여러개의 파라미터를 넘길 수 있음
  
---