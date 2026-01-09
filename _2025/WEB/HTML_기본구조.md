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

### `<html></html>`

문서 최상위(root) 요소

### `<head></head>`

문서 메타데이터 요소

- 문서제목, 인코딩, 스타일, 외부파일 로딩 등

- 일반적으로 브라우저에 나타나지 않는 내용
  
  > ### head 예시
  
  - `<title></title>`: 브라우저 상단 타이틀
  
  - `<link>`: 외부 리소스 연결요소 (CSS 파일 등)
  
  - `<style>`: CSS 직접 작성

### `<body></body>`

문서 본문 요소

- 실제 화면 구성과 관련된 내용

---