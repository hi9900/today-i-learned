# [Tailwind CSS](https://tailwindcss.com/)

- Tailwind CSS는 클래스(class) 이름을 검색하고 해당 스타일을 생성한 다음 정적 CSS 파일에 작성하여 작동한다.

## Play CDN

- Play CDN을 사용해 빌드 프로세스 없이 바로 사용할 수 있다.

```js
<script src="//cdn.tailwindcss.com"></script>
```

### 커스텀 토큰 확장

`tailwind.config` 객체를 통해 사용자 정의 고유 토큰(token)을 확장할 수 있다.

```js
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          'tailwind': '#38bdf8'
        }
      }
    }
  }
</script>
```

### 커스텀 모듈 확장

`type="text/tailwindcss"`를 사용해 Tailwind CSS 기능을 지원하는 커스텀 CSS를 추가할 수 있다.

```html
<style type="text/tailwindcss">
  @layer utilities {
    .underline-a {
      padding: 0.12em 0;
      border-bottom: 3px solid currentColor;
      text-decoration: none;
    }
  }
</style>
```

[참고] [Play CDN](https://tailwindcss.com/docs/installation/play-cdn)

---

### 공식 플러그인 사용

Tailwind CSS가 공식 제공하는 플러그인을 바로 사용할 수 있다.

```html
<script src="//cdn.tailwindcss.com**?plugins=typography**"></script>
```

플러그인이 제공하는 산문(`prose`) 유틸리티를 사용해 HTML 문서에 타이포그래피를 적용할 수 있습니다.

```html
<article **class="prose prose-slate prose-sm lg:prose-base lg:prose-xl" **>
  ...
</article>
```

[참고] [tailwindcss/typography](https://github.com/tailwindlabs/tailwindcss-typography)
