# Identifying Resources on the Web

- 웹에서의 리소스 식별

- HTTP 요청의 대상을 리소스(resource, 자원)라고 함

- 리소스는 문서, 사진 또는 기타 어떤 것이든 될 수 있음

- 각 리소스는 식별을 위해 **URI**로 식별됨

## URI

- Uniform Resource Identifier, 통합 자원 식별자

- 인터넷에서 리소스를 식별하는 문자열

- 가장 일반적인 URI는 웹 주소로 알려진 **URL**

  ```
  # URL 예시

  http://docs.djangoproject.com
  http://docs.djangoproject.com/en/4.1/intro
  http://docs.djangoproject.com/en/4.1/search/?q=model
  ```

- 특정 이름 공간에서 이름으로 리소스를 식별하는 URI는 **URN**

  리소스를 찾아가는 경로를 제공하지 않음

  ```
  # URN 예시

  # ISBN(국제 표준 도서번호)에서 식별되는 "로미오와 줄리엣" 도서
  urn:isbn:9788937461736

  # ISAN(국제 표준 시청각 자료번호)에서 식별되는 "2002년작 영화 스파이더맨"
  urn:isbn:0000-0000-2CEA-0000-1-0000-0000-Y
  ```

### URL

- Uniform Resource Locator, 통합 자원 위치

- 웹에서 주어진 리소스의 주소

- 네트워크 상에 리소스가 어디 있는지(주소)를 알려주기 위한 약속

  이러한 리소스는 HTML, CSS, 이미지 등이 될 수 있음

- URL은 여러 부분으로 구성되며 일부는 필수이고 나머지는 선택사항

> ### URL 구조

`http://www.example.com:80/path/to/myfile.html?key=value#quick-start`

- Scheme (or protocol)

  `https`

  - 브라우저가 리소스를 요청하는 데 사용해야 하는 프로토콜

  - URL의 첫 부분은 브라우저가 어떤 규약을 사용하는지를 나타냄

  - 기본적으로 웹은 HTTP(S)를 요구하며 메일을 열기위한 `mailto:`, 파일을 전송하기 위한 'ftp:` 등 다른 프로토콜도 존재

- Authority

  `www.exampel.com:80`

  - Schema 다음은 문자 패턴 `://`으로 구분된 Authority(권한)이 작성됨

  - Authority는 domain과 port를 모두 포함하며 둘은 `:`(콜론)으로 구분됨

  1. Domain Name

    `www.exampel.com`

    - 요청중인 웹 서버를 나타냄

    - 어떤 웹 서버가 요구되는 지를 가리키며 직접 IP 주소를 사용하는 것도 가능

      하지만, 사람이 외우기 어렵기 때문에 주로 Domain Name으로 사용

    - 예를 들어 도메인 `google.com`의 IP 주소는 `142.251.42.142`

  2. Port

    `80`

    - 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문(Gate)

    - HTTP 프로토콜의 표준 포트는 다음과 같고 생략이 가능 (나머지는 생략 불가능)

      - HTTP - 80

      - HTTPS - 443

    - Django의 경우 8000(80+00)이 기본 포트로 설정되어 있음

- Path

  `/path/to/myfile.html`

  - 웹 서버의 리소스 경로

  - 초기에는 실제 파일이 위치한 물리적 위치를 나타냈지만, 오늘날은 실제 위치가 아닌 추상화된 형태의 구조를 표현

  - 예를 들어 `/articles/create/`가 실제 articles 폴더 안에 create 폴더 안을 나타내는 것은 아님

- Parameters

  `?key=value`

  - 웹 서버에 제공하는 추가적인 데이터

  - 파라미터는 `&` 기호로 구분되는 key-value 쌍 목록

  - 서버는 리소스를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행할 수 있음

- Anchor

  `#quick-start`

  - 리소스의 다른 부분에 대한 앵커

  - 리소스 내부 일종의 '북마크'를 나타내며 브라우저에 해당 북마크 지점에 있는 콘텐츠를 표시

    - 예를 들어 HTML 문서에서 브라우저는 앵커가 정의한 지점으로 스크롤 함

  - fragment identifier(부분 식별자)라고 부르는 `#` 이후 부분은 서버에 전송되지 않음

> ### Anchor(앵커)
>
> 하이퍼링크와 비슷한 기능을 하는 인터넷 상의 다른 문서와 연결된 문자 혹은 그림

### URN

- Uniform Resource Name, 통합 자원 이름

- URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름 역할을 함 (독립적 이름)

- URL의 단점을 극복하기 위해 등장했으며 자원이 어디에 위치한 지 여부와 관계없이 이름만으로 자원을 식별

- 하지만 이름만으로 실제 리소스를 찾는 방법은 보편화 되어있지 않아 현재는 URL을 대부분 사용

- 예시: 

  ISBN (국제표준 도서번호): 국제적으로 책에 붙이는 고유 식별자

  ISAN (국제 표준 시청각 자료번호): 도서의 ISBN과 유사한 시청각 작품 및 관련 버전의 고유 식별자

---

## 웹에서의 리소스 식별 정리

- 자원의 식별자: URI

  - 자원의 위치로 자원을 식별: URL

  - 고유한 이름으로 자원을 식별: URN