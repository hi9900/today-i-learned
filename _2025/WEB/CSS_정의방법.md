# CSS 정의 방법

## 1. 인라인(inline)

- 해당 태그에 직접 `style` 속성을 활용

```html
<h1 style="color: blue; font-size: 100px">HELLO</h1>
```

## 2. 내부참조(embedding)

- `<head>` 태그 내에 `<style>` 지정

```html
<head>
  <style>
    h1{
        color: blue;
        font-size: 100px;
    }
  </style>
</head>
```

## 3. 외부참조(link file)

- 외부 CSS 파일을 `<head>`내 `<link>`를 통해 불러오기

```html
<head>
  <link rel="stylesheet" href="CSS파일명.css">
</head>
```
---