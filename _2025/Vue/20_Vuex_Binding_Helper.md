# Vuex Binding Helper

- Vuex store의 state, mutations, actions 등을 간단하게 사용할 수 있도록 만들어진 헬퍼함수

- mapState, mapActions와 같은 형식으로 사용

- 사용하기 위해서는 import 받아와야 함

```vue
// App.vue

<script>
  import { mapState, mapActions } from 'vuex'
</script>
```

## mapState

- Vuex store의 상태를 컴포넌트의 데이터에 매핑할 때 사용

- 객체 혹은 배열 형태로 상태를 매핑하여 사용할 수 있음

### 객체 형태로 매핑

1. mapState를 import

2. Spread operator를 사용하여 mapState를 전개

3. mapState 내부에 불러오고자 하는 값을 정의
   
   화살표 함수를 사용하여 message key에 state의 message 값을 할당
- key 값은 컴포넌트에서 사용하고자 하는 다른 이름으로 변경하여 사용할 수 있음
  
  ```vue
  // App.vue
  
  <template>
  <div id="app">  
    <h1>{{ message }}</h1>
  </div>
  </template>
  
  <script>
  import { mapState } from 'vuex'
  
  export default {
    ...
    computed: {
      ...mapState({
        message: state => state.message
      })
    }
  }
  </script>
  ```

### 배열 형태로 매핑

1. mapState를 import

2. Spread operator를 사용하여 mapState를 전개

3. vuex store의 상태 중 불러오고자 하는 대상을 배열의 원소로 정의
   
   ```vue
   // App.vue
   
   <template>
   <div id="app">  
    <h1>{{ message }}</h1>
   </div>
   </template>
   
   <script>
   import { mapState } from 'vuex'
   
   export default {
    ...
    computed: {
      ...mapState(['message'])
    }
   }
   </script>
   ```

## mapActions

- 컴포넌트에서 `this.$store.dispatch()`를 호출하는 대신 액선 메서드를 직접 호출하여 사용할 수 있음

- mapState와 같이 객체 혹은 배열 형태로 매핑 가능

### 배열 형태로 매핑

1. mapState와 동일한 형식으로 사용
- 단, 이 경우 changeMessage에 넘겨주어야 할 inputData를 changeMessage 호출 시 인자로 직접 값을 넘겨주어야 함
  
  ```vue
  // App.vue
  
  <template>
  <div id="app">  
    <h1>{{ message }}</h1>
    <input type="text" @keyup.enter="changeMessage(inputData)" v-model="inputData">
  </div>
  </template>
  
  <script>
  import { mapActions } from 'vuex'
  
  export default {
    ...
    methods: {
      ...mapActions(['changeMessage'])
    }
  }
  </script>
  ```

### 객체 형태로 매핑

1. Actions의 changeMessage를 actionsChangeMessage에 매핑

2. this.actionsChangeMessage 형식으로 사용

3. payload를 넘겨주거나 추가적인 로직 작성 가능
   
   ```vue
   // App.vue
   
   <template>
   <div id="app">  
    <h1>{{ message }}</h1>
    <input type="text" @keyup.enter="onSubmit" v-model="inputData">
   </div>
   </template>
   
   <script>
   import { mapActions } from 'vuex'
   
   export default {
    ...
    methods: {
      ...mapActions({
        actionsChangeMessage: 'changeMessage'
      }),
      onSubmit() {
        const newMessage = this.inputData
        this.actionsChangeMessage(newMessage)
        this.inputData = ''
      }
    }
   }
   </script>
   ```

## mapGetters

- mapState, mapActions와 동일한 방식으로 사용가능

```vue
  // App.vue

  <template>
    <div id="app">  
      <h1>{{ message }}의 길이는 {{ messageLength }}</h1>
      <h3>길이 x2: {{ doubleLength }}</h3>
      <input type="text" @keyup.enter="onSubmit" v-model="inputData">
    </div>
  </template>

  <script>
    import { mapGetters } from 'vuex'

    export default {
      ...
      computed: {
        ...mapGetters(['messageLength', 'doubleLength'])
      }
    }
  </script>
```

> ### [참고]

- 상황에 따라서는 배열과 객체 형태로 각각 매핑하여 사용할 수 있음

```vue
// App.vue

  <template>
    <div id="app">  
      <h1>{{ message }}</h1>
    </div>
  </template>

  <script>
    import { mapState } from 'vuex'

    export default {
      ...
      computed: {
        ...mapState(['message'])
        ...mapState({
          age: state => state.age
        })
      }
    }
  </script>
```