# Basic of Syntax

## Template Syntax

- Vue2 guide > Template Syntax 참고

- 렌더링 된 DOM을 기본 Vue instance의 data에 선언적으로 바인딩 할 수 있는 HTML 기반 template syntax를 사용

  - 렌더링 된 DOM: 브라우저에 의해 보기 좋게 그려질 HTML 코드

  - HTML 기반 template syntax: HTML 코드에 직접 작성할 수 있는 문법 제공

  - 선언적으로 바인딩: Vue instance와 DOM을 연결

## Text Interpolation

- 가장 기본적인 바인딩(연결) 방법

- 중괄호 2개로 표기

- DTL과 동일한 형태로 작성

- Text interpolation 방법은 모두 일반 텍스트로 표현

```html
<!-- text interpolation -->
<div id="app">
  <p>메시지: {{ msg }}</p>
  <p>HTML 메시지: {{ rawHTML }}</p>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      msg: 'Text Interpolation',
      rawHTML: '<span style="color:red;">빨간 글씨</span>',
    }
  })
</script>
```

## RAW HTML

- `v-html` directive를 사용하여 data와 바인딩

  - derective: HTML 기반 template syntax

  - HTML의 기본 속성이 아닌 Vue가 제공하는 특수 속성의 값응로 data를 작성

```html
<div id="app">
  <span v-html="rawHTML"></span>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      msg: 'Text Interpolation',
      rawHTML: '<span style="color:red;">빨간 글씨</span>',
    }
  })
</script>
```

> ### JS 표현식

- 표현식 형태로 작성 가능

```html
  <div id="app">
    <p>{{ msg.split('').reverse().join('') }}</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        msg: 'Text Interpolation',
      }
    })
  </script>
```