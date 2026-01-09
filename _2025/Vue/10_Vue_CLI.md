# Vue CLI

- Vue 개발을 위한 표준 도구

- 프로젝트의 구성을 도와주는 역할

- 확장 플러그인, GUI, Babel 등 다양한 tool 제공

### Vue CLI Quick Start

- 설치

```bash
$ npm install -g @vue/cli
```

- 프로젝트 생성

  - vscode terminal에서 진행

  - Vue 버전 [Vue 2] 선택

```bash
$ vue create vue-cli
```

- 프로젝트 디렉토리로 이동 후 프로젝트 실행

```bash
$ cd vue-cli
$ npm run serve
```

---

## Vue CLI 프로젝트 구조

```
프로젝트 폴더
│
└── vue-cli
    │
    ├── node_modules
    │  
    ├── public
    │  ├── favicon.ico
    │  └── index.html 
    │
    ├── src
    │  │  
    │  ├── assets
    │  │  └── logo.png
    │  │
    │  ├── components
    │  │  │
    │  │  └── HelloWorld.vue
    │  │
    │  ├── App.vue
    │  │
    │  └── main.js
    │      
    ├── .gitignore
    │      
    ├── babel.config.js
    │      
    ├── package.json
    │ 
    └── README.md
```

## node_modules

- node.js 환경의 여러 의존성 모듈

- python의 venv와 비슷한 역할을 함

  - 따라서, `.gitignore`에 넣어주어야 하며, Vue 프로젝트를 생성하면 자동으로 추가됨

> ### node_modules: Babel

  - JavaScript compiler

  - 자바스크립트의 ES6+ 코드를 구버전으로 번역/변환 해주는 도구

  - 자바스크립트의 파편화, 표준화의 영향으로 작성된 코드의 스펙트럼이 매우 다양

    - 최신 문법을 사용해도 브라우저의 버전 별로 동작하지 않는 상황이 발생

    - 버전에 따른 같은 의미의 다른 코드를 작성하는 등의 대응이 필요해졌고, 이러한 문제를 해결하기 위한 도구

    - 원시 코드(최신 버전)를 목적 코드(구 버전)으로 옮기는 번역기가 등장하면서 더 이상 코드가 특정 브라우저에서 동작하지 않는 상황에 대해 크게 고민하지 않을 수 있음

  ```javascript
  // Babel Input: ES2015 arrow function
  // 원시 코드(ES6+)
  [1, 2, 3].map((n) => n+1)

  // Babel Output: ES5 equivalent
  // 목적코드(ES5)
  [1, 2, 3].map(function (n) {
    return n+1
  })
  ```

> ### node_modules: Webpack

  - Static module bundler

  - 모듈 간의 의존성 문제를 해결하기 위한 도구

  - 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함

### Module

- 개발하는 애플리케이션의 크기가 커지고 복잡해지면 파일 하나에 모든 기능을 담기가 어려워짐

- 따라서 자연스럽게 파일을 여러 개로 분리하여 관리를 하게 되었고, 이 때 분리된 파일 각각이 모듈(module). 즉, js 파일 하나가 하나의 모듈

- 모듈은 대개 기능 단위로 분리하며, 클래스 하나 혹은 특정한 목적을 가진 복수의 함수로 구성된 라이브러리 하나로 구성됨

- 여러 모듈 시스템

  - ESM(ECMA Script Module), AMD, CommonJS, UMD

> ### Module 의존성 문제

  - 모듈의 수가 만하지고 라이브러리 혹은 모듈 간의 의존성(연결성)이 깊어지면서 특정한 곳에서 발생한 문제가 어떤 모듈 간의 문제인지 파악하기 어려움

  - Webpack은 이 모듈간의 의존성 문제를 해결하기 위해 등장

### Bundler

- 모듈 의존성 문제를 해결해주는 작업이 Bundling

- 이러한 일을 해주는 도구가 Bundler이고, Webpack은 다양한 Bundler 중 하나

- 모듈들을 하나로 묶어주고 묶인 파일은 하나 (혹은 여러 개)로 만들어짐

- Bundling 된 결과물은 개별 모듈의 실행 순서에 영향을 받지 않고 동작하게 됨

- snowpack, parcel, rollup.js 등의 webpack 이외에도 다양한 모듈 번들러 존재

- "Vue CLI는 이러한 Babel, Webpack에 대한 초기 설정이 자동으로 되어 있음"

## package.json

- 프로젝트의 종속성 목록과 지원되는 브라우저에 대한 구성 옵션을 포함

## package-lock.json

- node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정 및 관리

- 협업 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현

- 사용 할 패키지의 버전을 고정

- 개발 과정 간의 의존성 패키지 충돌 방지

- python의 requirements.txt 역할

## public/index.html

- Vue 앱의 뼈대가 되는 html 파일

- Vue 앱과 연결될 요소가 있음

## src/

- src/assets

  - 정적 파일을 저장하는 디렉토리

- src/components

  - 하위 컴포넌트들이 위치

- src/App.vue

  - 최상위 컴포넌트

  - public/index.html과 연결됨

- src/main.js

  - webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point

  - public/index.html과 src/App.vue를 연결시키는 작업이 이루어지는 곳

  - Vue 전역에서 활용할 모듈을 등록할 수 있는 파일