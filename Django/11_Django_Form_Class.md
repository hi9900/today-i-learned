# Django Form

- 사용자가 입력한 데이터가 우리가 원하는 데이터 형식이 맞는 지에 대한 유효성 검증이 필요

## Form에 대한 Django의 역할

- Form은 Django의 유효성 검사 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어수단

- Django는 Form과 관련한 유효성 검사를 단순화하고 자동화 할 수 있는 기능을 제공하여, 개발자가 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있다.

## Django는 Form에 관련한 작업의 세 부분을 처리

1. 렌더링을 위한 데이터 준비 및 재구성

2. 데이터에 대한 HTML forms 생성

3. 클라이언트로부터 받은 데이터 수신 및 처리

---

## Django Form Class

- Form Class: Django Form 관리 시스템의 핵심

> ### Form Class 선언

- Model과 마찬가지로 상속을 통해 선언, forms 라이브러리의 Form 클래스를 상속받음

- 앱폴더에 `forms.py`를 생성 후 `ArticleForm Class` 선언

  - Form Class를 forms.py에 작성하는 것은 규약이 아니지만, 더 나은 유지보수 관점 그리고 관행적으로 `forms.py` 파일 안에 작성하는 것을 권장함

- form에는 model field와 달리 TextField가 존재하지 않음

> ### Form rendering options

- `<label> & <input>` 쌍에 대한 3가지 출력 옵션

1. `as_p()`

  - 각 필드가 단락(`<p>` 태그)으로 감싸져서 렌더링
  
2. `as_ul()`

  - 각 필드가 목록 항목(`<li>` 태그)으로 감싸져서 렌더링

  - `<ul>` 태그는 직접 작성해야 한다.

3. `as_table()`

  - 각 필드가 테이블(`<tr>` 태그) 행으로 감싸져서 렌더링

> ### Django의 2가지 HTML input 요소 표현

1. Form fields

  - 입력에 대한 유효성 검사 로직을 처리

  - 템플릿에서 직접 사용됨

2. Widgets

  - 웹페이지의 HTML input 요소 렌더링을 담당

    - 단순히 input 요소의 보여지는 부분을 변경

  - Widgets은 반드시 form fields에 할당됨

---

## Widgets

- Django의 HTML input element의 표현을 담당

- 단순히 HTML 렌더링을 처리하는 것이며 유효성 검증과 아무런 관계가 없음

  - 웹 페이지에서 input element의 단순 raw한 렌더링만을 처리하는 것 뿐

---

