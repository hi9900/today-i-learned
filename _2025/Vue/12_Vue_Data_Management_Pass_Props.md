# Vue Data Management

## Data in components

- 컴포넌트는 부모-자식 관계를 가지고 있으므로, 부모-자식 관계만 데이터를 주고받게 함

- 데이터의 흐름을 파악하기 용이

- 유지 보수하기 쉬워짐

---

## Pass Props

- 요소의 속성(property)을 사용하여 데이터 전달

- props는 부모(상위) 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성

- 자식(하위) 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야 함

- 부모 -> 자식으로의 data 전달 방식

- 정적인 데이터를 전달하는 경우 static props라고 명시하기도 함

- 요소에 속성을 작성하듯이 사용 가능하며, `prop-data-name="value"`의 형태로 데이터를 전달

  - 이때 속성의 키 값은 kebab-case를 사용

- 데이터를 받는 쪽, 즉 하위 컴포넌트에서도 props에 대해 명시적으로 작성 해주어야 함

- 전달받은 props를 type과 함께 명시

  - 컴포넌트를 문서화 할 뿐 아니라, 잘못된 타입을 전달하는 경우 브라우저의 자바스크립트 콘솔에서 사용자에게 경고

> ### MyComponent to MyChild

  ```vue
  // MyComponent.vue

  <template>
    <div class="border">
      <h1>This is my component</h1>
      <MyChild static-props="component에서 child로" />
    </div>
  </template>
  ```

  ```vue
  // MyChild.vue

  <template>
    <div>
      <h3>This is child component</h3>
      <p>{{ staticProps }}</p>
    </div>
  </template>

  <script>
    export default {
      name: 'MyChild',
      props: {
        staticProps: String,
      },
    }
  </script>
  ```

### Pass Props convention

- 부모에게서 넘겨주는 props: kebab-case

  - HTML 속성명은 대소문자를 구분하지 않기 때문

- 자식에서 받는 props: camelCase

- 부모 템플릿(html)에서 kebab-case로 넘긴 변수를 자식의 스크립트(vue)에서 자동으로 camelCase로 변환하여 인식함

## Dynamic props

- 변수를 props로 전달할 수 있음

- v-bind directive를 사용해 데이터를 동적으로 바인딩

- 부모 컴포넌트의 데이터가 업데이트 되면 자식 컴포넌트로 전달되는 데이터 또한 업데이트 됨

> Dynamic props

  ```vue
  // MyComponent.vue

  <template>
    <div class="border">
      <h1>This is my component</h1>
      <MyChild 
      :dynamic-props="dynamicProps"
      />
    </div>
  </template>

  <script>
    export default{
      data() {
        return {
          dynamicProps: "It's in data",
        }
      },
    }
  </script>
  ```

  ```vue
  // MyChild.vue

  <template>
    <div>
      <h3>This is child component</h3>
      <p>{{ dynamicProps }}</p>
    </div>
  </template>

  <script>
    export default {
      name: 'MyChild',
      props: {
        dynamicProps: String,
      },
    }
  </script>
  ```

> ## 컴포넌트의 data 함수

- 각 vue 인스턴스는 같은 data 객체를 공유하므로 새로운 data 객체를 반환(return)하여 사용해야 함

```vue
data: function() {
  return {
    // component's data in here
  }
}
```

## Pass Props

- `:dynamic-props="dynamicProps"` 는 

  앞의 key값(dynamic-props)이란 이름으로 뒤의 `""` 안에 오는 데이터(dynamicProps)를 전달하겠다는 뜻

- 즉, `:my-props="dynamicProps"`로 데이터를 넘긴다면, 자식 컴포넌트에서 `myProps`로 데이터를 받아야 함

- v-bind로 묶여있는 `""`안의 구문운 javascript의 구문으로 볼 수 있음

  따라서 `dynamicProps`라고 하는 변수에 대한 data를 전달할 수 있는 것

- 숫자를 props로 전달하기 위한 방법

  ```vue
  // 1
  <SomeComponent num-props="1" />
  // 2
  <SomeComponent :num-props="1" />
  ```

  - 1번 방식은 static props로 string의 "1"을 전달

  - 2번 방식은 dynamic props로 숫자 "1"을 전달

## 단방향 데이터 흐름

- 모든 props는 부모에서 자식으로, 즉 아래로 단방향 바인딩을 형성

- 부모 속성이 업데이트되면 자식으로 흐르지만 반대 방향은 아님

  - 부모 컴포넌트가 업데이트될 때마다 자식 컴포넌트의 모든 prop들이 최신 값으로 새로고침 됨

- 목적: 하위 컴포넌트가 실수로 상위 컴포넌트 상태를 변경하여 앱의 데이터 흐름을 이해하기 힘들게 만드는 것을 방지

- 하위 컴포넌트에서 prop을 변경하려고 시도해서는 안되며, 그렇게 하면 Vue는 콘솔에서 경고를 출력함