# Vue instance

1. Vue CDN 가져오기

2. `new` 연산자를 사용한 생성자 함수 호출

  - vue instance 생성

3. 인스턴스 출력 및 확인

  - vue instance === 1개의 객체

  - 아주 많은 속성과 메서드를 이미 가지고 있고, 이러한 기능들을 사용하는 것

> ### el (element)

- Vue instance와 DOM을 mount(연결)하는 옵션

  - View와 Model을 연결하는 역할

  - HTML `id` 혹은 `class와` 마운트 가능

- Vue instance와 연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음

  - Vue 속성 및 메서드 사용 불가

- el(element)

  1. 새로운 Vue instance 생성

  2. 생성자 함수 첫번째 인자로 `Object` 작성

  3. `el` 옵션에 `#app` 작성 (DOM 연결)

  4. 인스턴스 출력

  ```html
  <body>
    <div id="app"></div>

    <!-- Vue CDN -->
    <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: '#app'
      })
      console.log(app)
    </script>
  </body>
  ```

  5. Vue와 연결되지 않은 div 생성

    - 두 div 모두에 `{{ message }}` 작성 후 결과 확인

    - `message` 속성이 정의되지 않았다는 경고와 `{{ message }}`가 그대로 출력되는 차이

  ```html
  <!-- 속성 정의 오류 -->
  <div id="app">{{ message }}</div>

  <!-- `{{ message }}`가 그대로 출력 -->
  <div>{{ message }}</div>
  ```

> ### data

- Vue instance의 데이터 객체 혹은 인스턴스 속성

- 데이터 객체는 반드시 기본 객체 `{} (Object)`여야 함

- 객체 내부의 아이템들은 value로 모든 타입의 객체를 가질 수 있음

- 정의된 속성은 `interpolation {{ }}`을 통해 view에 렌더링 가능함

- data

  1. Vue instance에 `data` 객체 추가

  2. data 객체에 `message` 값 추가 후 결과 확인

  3. 추가된 객체의 각 값들은 `this.message` 형태로 접근 가능

  ```html
  <body>
  <div id="app">{{ message }}</div>
  <!-- Vue CDN -->
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        message: 'Hello, Vue!'
      }
    })
  </script>
</body>
  ```

> ### methods

- Vue instance의 method들을 정의하는 곳

- methods 객체 정의

  - 객체 내 print method 정의

  - print method 실행 시 Vue instance의 data 내 message 출력

- 콘솔창에서 `app.print()` 실행

```html
<body>
  <div id="app">{{ message }}</div>
  <!-- Vue CDN -->
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        message: 'Hello, Vue!'
      },
      methods: {
        print: function () {
          console.log(this.message)
        }
      }
    })
  </script>
</body>
```

- method를 호출하여 data 변경 가능

  - 객체 내 bye method 정의

  - print method 실행 시 Vue instance의 data 내 message 변경

- 콘솔 창에서 `app.bye()` 실행

  - DOM에 바로 변경된 결과 반영

  - Vue의 강력한 반응성(reactivity)

```html
<body>
  <div id="app">{{ message }}</div>
  <!-- Vue CDN -->
  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        message: 'Hello, Vue!'
      },
      methods: {
        print: function () {
          console.log(this.message)
        },
        bye: function () {
          this.message = 'Bye, Vue!'
        }
      }
    })
  </script>
</body>
```

> ### methods with Arrow Function

- 메서드를 정의할 때, Arrow Function을 사용하면 안됨

- Arrow Function의 this는 함수가 선언될 때 상위 스코프를 가리킴

  즉, this가 상위 객체 window를 가리킴

- 호출은 문제 없이 가능하나, this로 Vue의 data를 변경하지 못함