# HTML

Hyper Text Markup Language

- Hyper Text: 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

- Markup Language: 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어

## HTML 기본 구조

```html
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>

</body>
</html>
```

### html

문서 최상위(root) 요소

### head

문서 메타데이터 요소

- 문서제목, 인코딩, 스타일, 외부파일 로딩 등

- 일반적으로 브라우저에 나타나지 않는 내용
  
  > head 예시
  
  - `<title>` :브라우저 상단 타이틀
  
  - `<link>` :외부 리소스 연결요소 (CSS 파일 등)
  
  - `<style>` :CSS 직접 작성

### body

문서 본문 요소

- 실제 화면 구성과 관련된 내용

---

### 요소(element)

- HTML의 요소는 태그(element, 요소)와 내용(contents)으로 구성되어 있다.

- 태그는 내용을 감싸는 것으로 그 정보의 성격과 의미를 정의한다.

- 요소는 중첩될 수 있고, 중첩을 통해 하나의 문서를 구조화 한다.

> 내용이 없는 태그들

- br, hr, img, input, link, meta

### 속성(attribute)

- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공한다.

- 요소의 시작 태그에 작성하며, 보통 이름과 값이 하나의 쌍으로 존재한다.

> HTML Global Attribute

- 태그와 상관없이 사용 가능한 속성

- 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성

- 몇몇 요소에는 아무 효과가 없을 수 있다.

- `id`: 문서 전체에서 유일한 고유 식별자 지정

- `class`: 공백으로 구분된 해당 요소의 클래스 목록. CSS, JS에서 요소를 선택하거나 접근

- `style`: inline 스타일
