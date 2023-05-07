# Vue Data Management

## Emit Event

- 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때는 이벤트를 발생시킴

  1. 데이터를 이벤트 리스너의 콜백함수의 인자로 전달

  2. 상위 컴포넌트는 해당 이벤트를 통해 데이터를 받음

## $emit

- $emit 메서드를 통해 부모 컴포넌트에 이벤트를 발생

  - `$emit('event-name')` 형식으로 사용하며 부모 컴포넌트에 `event-name`이라는 이벤트가 발생했다는 것을 알림

  - 마치 사용자가 마우스 클릭을 하면 `click` 이벤트가 발생하는 것처럼, $emit('event-name')이 실행되면 `event-name` 이벤트가 발생하는 것

- `$`

  - javascript는 변수에 `_`, `$` 두 개의 특수문자를 사용 가능

  - 이때, 기존에 사용하던 변수, 메서드들과 겹치지 않게 하기 위해서 vue는 `$emit`을 이벤트 전달을 위한 방식으로 택함

> ### Emit Event

- 자식 컴포넌트에 버튼을 만들고 클릭 이벤트를 추가

- `$emit`을 통해 부모 컴포넌트에게 `child-to-parent` 이벤트를 트리거

```vue
// MyChild.vue

<template>
  <div>  
    <button @click="ChildToParent">클릭!</button>
  </div>
</template>

<script>
export default {
  ...
  methods: {
    ChildToParent() {
      this.$emit('child-to-parent')
    }
  }
}
</script>
```
- emit된 이벤트를 상위 컴포넌트에서 청취 후 핸들러 함수 실행

```vue
// MyComponent.vue

<template>
  <div class="border">  
    <MyChild 
    @child-to-parent="parentGetEvent"
    />
  </div>
</template>

<script>
export default {
  ...
  methods: {
    parentGetEvent() {
      console.log("자식컴포넌트에서 발생한 이벤트")
    }
  }
}
</script>
```

### Emit Event 흐름 정리

1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수 ChildToParent 호출

2. 호출된 함수에서 $emit을 통해 상위 컴포넌트에 이벤트(child-to-parent) 발생

3. 상위 컴포넌트는 자식 컴포넌트가 발생시킨 이벤트(child-to-parent)를 청취하여 연결된 핸들러 함수(parentGetEvent) 호출
---
## Emit with data

- 이벤트를 발생(emit) 시킬 때 인자로 데이터를 전달 가능

```vue
// MyChild.vue

<template>
  <div>  
    <button @click="ChildToParent">클릭!</button>
  </div>
</template>

<script>
export default {
  ...
  methods: {
    ChildToParent() {
      this.$emit('child-to-parent', 'child data')
    }
  }
}
</script>
```

- 이렇게 전달한 데이터는 이벤트와 연결된 부모 컴포넌트의 핸들러 함수의 인자로 사용 가능

```vue
// MyComponent.vue

<template>
  <div class="border">  
    <MyChild 
    @child-to-parent="parentGetEvent"
    />
  </div>
</template>

<script>
export default {
  ...
  methods: {
    parentGetEvent(inputData) {
      console.log("자식컴포넌트에서 발생한 이벤트")
      console.log(`child component로부터 ${inputData}를 받음!`)
    }
  }
}
</script>
```

## emit with data 흐름 정리

1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취하여 연결된 핸들러 함수(ChildToParent) 호출

2. 호출된 함수에서 $emit을 통해 부모 컴포넌트에 이벤트(child-to-parent)를 발생

  - 이벤트에 데이터(child data)를 함께 전달

3. 부모 컴포넌트는 자식 컴포넌트의 이벤트(child-to-parent)를 청취하여 연결된 핸들러 함수(parentGetEvent) 호출, 함수의 인자로 전달된 데이터(child data)가 포함되어 있음

4. 호출된 함수에서 console.log(`~child data~`) 실행
---
## emit with dynamic data

- pass props와 마찬가지로 동적인 데이터도 전달 가능

- 자식 컴포넌트에서 입력받은 데이터를 부모 컴포넌트에 전달하여 출력

```vue
// MyChild.vue

<template>
  <div>  
    <input type="text"
    v-model="childInputData"
    @keyup.enter="childInput"
    >
  </div>
</template>

<script>
export default {
  ...
  data() {
    return {
      childInputData: null,
    }
  },
  methods: {
    childInput() {
      this.$emit('child-input', this.childInputData)
      this.childInputData = ""
    }
  }
}
</script>
```

```vue
// MyComponent.vue

<template>
  <div class="border">  
    <MyChild 
    @child-input="getDynamicData"
    />
  </div>
</template>

<script>
export default {
  ...
  methods: {
    getDynamicData(inputData) {
      console.log(`child component로부터 ${inputData}를 입력 받음!`)
    }
  }
}
</script>
```

## emit with dynamic data 흐름 정리

1. 자식 컴포넌트에 있는 keyup.enter 이벤트를 청취하여 연결된 핸들러 함수(ChildInput) 호출

2. 호출된 함수에서 $emit을 통해 부모 컴포넌트에 이벤트(child-input)를 발생

  - 이벤트에 v-model로 바인딩 된 입력받은 데이터를 전달

3. 상위 컴포넌트는 자식 컴포넌트의 이벤트(child-input)를 청취하여 연결된 핸들러 함수(getDynamicData) 호출, 함수의 인자로 전달된 데이터가 포함되어 있음

4. 호출된 함수에서 console.log(`~입력받은 데이터~`) 실행

---

## pass props / emit event 컨벤션

- HTML요소에서 사용할 때는 kebab-case

  JavsScript에서 사용할 때는 camelCase

- props

  - 상위 -> 하위 흐름에서 HTML 요소로 내려줌: kebab-case

  - 하위에서 받을 때 JavaScript에서 받음: camelCase

- emit

  - emit 이벤트를 발생시키면 HTML 요소가 이벤트를 청취함: kebab-case

  - 메서드, 변수 명 등은 JavaScript에서 사용함: camelCase