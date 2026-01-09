# Vue Router

- Vue의 공식 라우터

- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공

- 라우트(routes)에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링 할 지 알려줌

  - 즉, SPA를 MPA처럼 URL을 이동하면서 사용 가능

  - SPA의 단점 중 하나인 "URL이 변경되지 않는다."를 해결

> ### MPA(Multiple Page Application)

  - 여러 개의 페이지로 구성된 애플리케이션

  - SSR 방식으로 렌더링

## Vue Router 시작하기

- Vuex와 마찬가지의 방식으로 설치 및 반영

```bash
$ vue create vue-router-app
$ cd vue-router-app
$ vue add router
```

- 기존 프로젝트를 진행하고 있던 도중에 router를 추가하게 되면 `App.vue`를 덮어쓰므로 필요한 경우 명령을 실행하기 전에 파일을 백업해두어야 함

- history mode 사용여부 -> Yes

> ### History mode

- 브라우저의 History API를 활용한 방식

  - 새로고침 없이 URL 이동 기록을 남길 수 있음

- 우리에게 익숙한 URL 구조로 사용 가능

  `https://localhose:8080/index`

- History mode를 사용하지 않으면 Default값인 Hash mode로 설정됨

  '#'을 통해 URL을 구분하는 방식

  `https://localhose:8080#index`

### App.vue

- `router-link` 요소 및 `router-view`가 추가됨

> ### router-link

- a 태그와 비슷한 기능 -> URL을 이동시킴

  - routes에 등록된 컴포넌트와 매핑됨

  - 히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 a 태그와 달리 브라우저가 페이지를 다시 로드하지 않도록 함

- 목표 경로는 'to' 속성으로 지정됨

- 기능에 맞게 HTML에서 a 태그로 rendering 되지만, 필요에 따라 다른 태그로 바꿀 수 있음

> ### router-view

- 주어진 URL에 대해 일치하는 컴포넌트를 렌더링 하는 컴포넌트

- 실제 component가 DOM에 부착되어 보이는 자리를 의미

- router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링

- Django에서의 block tag와 비슷함

  - App.vue는 base.html의 역할

  - router-view는 block 태그로 감싼 부분

### src/router/index.js

- 라우터에 관련된 정보 및 설정이 작성되는 곳

- Django에서의 urls.py에 해당

- routes에서 URL과 컴포넌트를 매핑

### src/Views

- router-view에 들어갈 component 작성

- 기존에 컴포넌트를 작성하던 곳은 components 폴더 뿐이었지만, 이제 두 폴더로 나뉘어짐

- 각 폴더 안의 `.vue` 파일들이 기능적으로 다른 것은 아님

- 폴더 별 컴포넌트 배치

  - `views/`

    - routes에 매핑되는 컴포넌트

      즉, `<router-view>`의 위치에 렌더링되는 컴포넌트를 모아두는 폴더

    - 다른 컴포넌트와 구분하기 위해 `View`로 끝나도록 만드는 것을 권장

  - `components/`

    - routes에 매핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더

