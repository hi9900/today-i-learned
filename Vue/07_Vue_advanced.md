# Vue advanced

## computed

- Vue instance가 가진 options 중 하나

- computed 객체에 정의한 함수를 페이지가 최초로 렌더링 될 때 호출하여 계산

  - 계산 결과가 변하기 전까지 함수를 재호출하는 것이 아닌 계산된 값을 반환

### methods vs computed

- methods

  - 호출될 때마다 함수를 실행

  - 같은 결과여도 매번 새롭게 계산

- computed

  - 함수의 종속 대상의 변화에 따라 계산 여부가 결정됨

  - 종속 대상이 변하지 않으면 항상 저장(캐싱)된 값을 반환

```html
<div id="app">
  <h1>data_01 : {{ number1 }}</h1>
  <h1>data_02 : {{ number2 }}</h1>
  <hr>
  <h1>add_method : {{ add_method() }}</h1>
  <h1>add_method : {{ add_method() }}</h1>
  <h1>add_method : {{ add_method() }}</h1>
  <hr>
  <h1>add_computed : {{ add_computed }}</h1>
  <h1>add_computed : {{ add_computed }}</h1>
  <h1>add_computed : {{ add_computed }}</h1>
  <hr>
  <button v-on:click="dataChange">Change Data</button>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      number1: 100,
      number2: 100
    },
    computed: {
      add_computed: function () {
        console.log('computed 실행됨!')
        return this.number1 + this.number2
      },
    },
    methods: {
      add_method: function () {
        console.log('method 실행됨!')
        return this.number1 + this.number2
      },
      dataChange: function () {
        this.number1 = 200
        this.number2 = 300
      },
    }
  })
</script>
```

## watch

- 특정 데이터의 변화를 감지하는 기능

  1. watch 객체를 정의

  2. 감시할 대상 data를 지정

  3. data가 변할 시 실행할 함수를 정의

- 첫 번째 인자는 변동 후 data

  두 번째 인자는 변동 전 data

```html
<div id="app">
  <h3>Increase number</h3>
  <p>{{ number }}</p>
  <button @click="number++">+</button>
  <hr>

  <h3>Change name</h3>
  <p>{{ name }}</p>
  <input type="text" v-model="name">
  <hr>

  <h3>push myObj</h3>
  <p>{{ myObj }}</p>
  <button @click="itemChange">change Item</button>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      number: 0,
      name: '',
      myObj: {completed: true}
    },
    methods: {
      nameChange: function () {
        console.log('name is changed')
      },

      itemChange: function () {
        this.myObj.completed = !this.myObj.completed
      }
    },
    watch: {
      number: function (val, oldVal) {
        console.log(val, oldVal)
      },

      name: {
        handler: 'nameChange'
      },

      myObj: {
        handler: function (val) {
          console.log(val)
        },
        deep: true
      },
    }
  })
</script>
```

- 실행 함수를 Vue method로 대체 가능

  1. 감시 대상 data의 이름으로 객체 생성

  2. 실행하고자 하는 method를 handler에 문자열 형태로 할당

- Array, Object의 내부 요소 변경을 감지하기 위해서는 `deep` 속성 추가 필요

## filters

- 텍스트 형식화를 적용할 수 있는 필터

- interpolation 혹은 v-bind를 이용할 때 사용 가능

- 필터는 자바스크립트 표현식 마지막에 `|`와 함께 추가되어야 함

- Chaining 가능

```html
<div id="app">
  <p>{{ numbers }}</p>
  <p>{{ numbers|getOddNums|getUnderTenNums }}</p>
  <p>{{ numbers|getUnderTenNums }}</p>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
  const app = new Vue({
    el: '#app',
    data: {
      numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    },
    filters: {
      getOddNums: function (nums) {
        const oddNums = nums.filter((num) => {
          return num % 2
        })
        return oddNums
      },
      
      getUnderTenNums: function (nums) {
        const underTen = nums.filter((num) => {
          return num < 10
        })
        return underTen
      }
    }
  })
</script>
```