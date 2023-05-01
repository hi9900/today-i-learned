# Directives

## 기본 구성

- v-접두사가 있는 특수 속성에는 값을 할당할 수 있음

  - 값에는 단일 JS 표현식을 작성할 수 있음

- directive의 역할은 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것

`v-on:submit.prevent="onSubmit"`

`[Name]:[Argument].[Modifiers]=[Value]`

- `:`을 통해 전달인자를 받을 수 있음

- `.`으로 표시되는 특수 접미사 - directive를 특별한 방법으로 바인딩 해야 함

### 새 Vue instance 생성

- 각각의 instance들은 연결된 DOM element에만 영향을 미침

- 연결되지 않은 DOM이 Vue의 영향을 받지 않았던 것과 동일한 상황

### v-text

- Template InterPolation과 함께 가장 기본적인 바인딩 방법

- `{{ }}`와 동일한 역할

  정확히 동일한 역할인 것은 아님

```html
  <div id="app2">
    <p v-text="message"></p>
    <p>{{ message }}</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app2 = new Vue({
      el: '#app2',
      data: {
        message: 'Hello!'
      }
    })
  </script>
```

### v-html

- RAW HTML을 표현할 수 있는 방법

- 단, 사용자가 입력하거나 제공하는 컨텐츠에는 절대 사용 금지

  - XSS 공격 참고

```html
  <div id="app2">
    <p v-html="html"></p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app2 = new Vue({
      el: '#app2',
      data: {
        html: '<a href="https://www.google.com">GOOGLE</a>',
      }
    })
```

### v-show

- 표현식에 작성된 값에 따라 element를 보여 줄 것인지 결정

  - boolean 값이 변경될 때마다 반응

- 대상 element의 display 속성을 기본 속성과 none으로 toggle

- 요소 자체는 항상 DOM에 렌더링 됨

- 바인딩 된 `isActive`의 값이 false이므로 첫 방문 시 `p tag`는 보이지 않음

  - vue dev tools에서 isActive 변경 시 화면에 출력

  - 값을 false로 변경 시 다시 사라짐

- 화면에서만 사라졌을 뿐, DOM에는 존재함

  - display 속성이 변경 된 것

```html
  <div id="app3">
    <p v-show="isActive">보이니? 안보이니?</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app3 = new Vue({
      el: '#app3',
      data: {
        isActive: false
      }
    })
```

### v-if

- v-show와 사용 방법은 동일

- `isActive`의 값이 변경될 때 반응

- 단, 값이 false인 경우 DOM에서 사라짐

- `v-if v-else-if v-else` 형태로 사용

```html
  <div id="app3">
    <p v-if="isActive">안보이니? 보이니?</p>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app3 = new Vue({
      el: '#app3',
      data: {
        isActive: false
      }
    })
```

> ### v-show vs v-if

- v-show (Expensive initial load, cheap toggle)

  - 표현식 결과와 관계 없이 렌더링 되므로 초기 렌더링에 필요한 비용은 v-if보다 높을 수 있음

  - display 속성 변경으로 표현 여부를 판단하므로 렌더링 후 toggle 비용은 적음

- v-if (Cheap initial load, expensive toggle)

  - 표현식 결과가 false인 경우 렌더링조차 되지 않으므로 초기 렌더링 비용은 v-show보다 낮을 수 있음

  - 단, 표현식 값이 자주 변경되는 경우 잦은 재 렌더링으로 비용이 증가할 수 있음

### v-for

- `for ... in` 형식으로 작성

- 반복한 데이터 타입에 모두 사용 가능

- index를 함께 출력하고자 한다면 `(char, index)` 형태로 사용 가능

```html
  <div id="app4">
    <h2>String</h2>
    <div 
      v-for="(char, index) in myStr">
      <p>{{ index }}번째 문자열 {{ char }}</p>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app4 = new Vue({
      el: '#app4',
      data: {
        myStr: 'Hello, World!'
      }
    })
```

- 배열 역시 문자열과 동일하게 사용 가능

- 각 요소가 객체라면 `dot notation`으로 접근할 수 있음

> 특수속성 key

  - v-for 사용 시 반드시 key 속성을 각 요소에 작성

  - 주로 v-for directive 작성 시 사용

  - vue 화면 구성 시 이전과 달라진 점을 확인하는 용도로 활용

    - 따라서 key가 중복되어서는 안됨

  - 각 요소가 고유한 값을 가지고 있다면 생략할 수 있음

```html
  <div id="app4">
    <h2>String</h2>
    <div 
      v-for="(item, index) in myArr"
      :key="`array-${index}`">
      <p>{{ index }}번째 아이템</p>
      <p>{{ item.name }}</p>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app4 = new Vue({
      el: '#app4',
      data: {
        myArr: [
          {id: 1, name: 'python'},
          {id: 2, name: 'javascript'}
        ]
      }
    })
```

- 객체 순회 시 value가 할당되어 출력

- 2번째 변수 할당 시 key 출력 가능

```html
<div id="app4">
    <div
      v-for="(value, key) in myObj"
      :key="key">
      <p>{{ key }} : {{ value }}</p>
    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app4 = new Vue({
      el: '#app4',
      data: {
        myObj: {
          name: 'harry',
          age: 27
        }
      }
    })
```

### v-on

- `:`을 통해 전달받은 인자를 확인

- 값으로 JS 표현식 작성

- addEventListener의 첫 번째 인자와 동일한 값들로 구성

- 대기하고 있던 이벤트가 발생하면 할당된 표현식 실행

- method를 통한 data 조작도 가능

- method에 인자를 넘기는 방법은 일반 함수를 호출할 때와 동일한 방식

- `:`을 통해 전달된 인자에 따라 특별한 수식어(modifiers)가 있을 수 있음

  - `v-on: keyup.enter` 등

- `@` shortcut 제공

  - `@keyup.click`

```html
  <div id="app5">
    <button v-on:click="number++">increase Number</button>
    <p>{{ number }}</p>

    <button v-on:click="toggleActive">toggle isActive</button>
    <p>{{ isActive }}</p>

    <button @click="checkActive(isActive)">check isActive</button>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app5 = new Vue({
      el: '#app5',
      data: {
        number: 0,
        isActive: false,
      },
      methods: {
        toggleActive: function () {
          this.isActive = !this.isActive
        },
        checkActive: function (check) {
          console.log(check)
        }
      }
    })
```

### v-bind

- HTML 기본 속성에 Vue data를 연결

- class의 경우 다양한 형태로 연결 가능

  - 조건부 바인딩

    `{'class Name': '조건 표현식'}`

    삼항 연산자도 가능

  - 다중 바인딩

    `['JS표현식', 'JS표현식']`

- Vue data 변화에 반응하여 DOM에 반영하므로 상황에 따라 유동적 할당 가능

- `:` shortcut 제공

```html
<div id="app6">
  <a v-bind:href="url">GO TO GOOGLE</a>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app6 = new Vue({
    el: '#app6',
    data: {
      url: 'https://www.google.com'
    }
  })
```

### v-model

- Vue instance와 DOM의 양방향 바인딩

- Vue data 변경 시 v-model로 연결된 사용자 입력 element에도 적용