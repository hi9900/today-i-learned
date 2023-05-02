# Vue Style Guide

Vue의 스타일 가이드 규칙은 우선순위를 기준으로 4가지 범주를 설정

- 우선순위

  - A: 필수(Essential)

    오류를 방지하는 데 도움이 되므로 어떤 경우에도 규칙을 학습하고 준수

  - B: 적극 권장 (Strongly Recommended)

    규칙을 어겨도 코드는 여전히 실행되겠지만, 규칙 위반은 드물어야 함

  - C: 권장 (Recommended)

    일관성을 보장하도록 임의의 선택을 할 수 있음

  - D: 주의 필요 (Use with Caution)

    잠재적 위험 특성을 고려함

## 우선순위 A

### v-for은 항상 key와 함께 사용

- 내부 컴포넌트의 상태를 일관되게 유지하기 위해 v-for에 항상 key를 사용하기

- 데이터의 예측 가능한 행동을 유지시키기 (객체 불변성)

### v-for을 쓴 엘리먼트에 절대 v-if 사용하지 않기

- 함께 쓸 수 있다고 생각되는 2가지 경우

> ### 1. 목록의 항목을 필터링 할 때

  `v-for="user in users" v-if="user.isActive"`

  - Vue가 디렉티브를 처리할 때 v-for은 v-if보다 우선순위가 높음

  - 즉, user의 일부분만 렌더링하고 싶은데도 불구하고 v-for가 우선순위를 가지기 때문에 모든 user에 대해 반복해야 함

  ```html
  <div id="app">
    <!-- 1. 목록의 항목을 필터링할 때 -->
    <!-- bad 1 -->
    <ul>
      <li
        v-for="user in users"
        v-if="user.isActive"
        :key="user.id"
      >
        {{ user.name }}
      </li>
    </ul>

    <!-- good 1 : computed 속성을 대신 반복하여 해결 -->
    <ul>
      <li
        v-for="user in activeUsers"
        :key="user.id"
      >
        {{ user.name }}
      </li>
    </ul>

  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        users: [
          { id: 1, name: 'adam', isActive: false, },
          { id: 2, name: 'barry', isActive: true, },
          { id: 3, name: 'caleb', isActive: false, },
        ],
      },
      computed: {
        activeUsers: function () {
          return this.users.filter((user) => {
            return user.isActive
          })
        }
      },
    })
  </script>
  ```

> ### 2. 숨김 목록의 렌더링을 피할 때

  `v-for="user in users" v-if="shouldShowUsers"`

  - v-if를 컨테이너 엘리먼트로 옮기기

    - 더이상 목록의 모든 사용자에 대해 shouldShowUsers를 확인하지 않도록 함

  - 한 번 확인하고 shouldShowUsers가 false인 경우 v-for을 평가하지도 않음

  ```html
  <div id="app">
    <!-- 2. 숨김 목록의 렌더링을 피할 때 -->
    <!-- bad 2 -->
    <ul>
      <li
        v-for="user in users"
        v-if="shouldShowUsers"
        :key="user.id"
      >
        {{ user.name }}
      </li>
    </ul>

    <!-- good 2 : v-if를 컨테이너 엘리먼트로 옮기기 -->
    <ul v-if="shouldShowUsers">
      <li
        v-for="user in users"
        :key="user.id"
      >
        {{ user.name }}
      </li>
    </ul>
  </div>
  
  <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: '#app',
      data: {
        users: [
          { id: 1, name: 'adam', isActive: false, },
          { id: 2, name: 'barry', isActive: true, },
          { id: 3, name: 'caleb', isActive: false, },
        ],
        shouldShowUsers: true,
      },
    })
  </script>
  ```