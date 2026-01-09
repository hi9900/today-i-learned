# Front-end Development

- Fromt-end 개발은 Web App 또는 Web Site의 UI/UX를 제작하고 관리하는 과정

- Front-end 프레임워크와 라이브러리(React, Angular, Vue.js)를 사용하여 개발 효율을 높이고, Web App의 복잡성을 관리

- Front-end 개발에 사용되는 주요 기술은 HTML, CSS, JavaScript

## Web App

- 웹 브라우저에서 실행되는 어플리케이션 소프트웨어

- 개발자 도구 > 디바이스 모드

- 웹 페이지가 그대로 보이는 것이 아닌 디바이스에 설치된 App처럼 보이는 것

- 웹 페이지가 디바이스에 맞는 적절한 UX/UI로 표현되는 형태

## SPA(Single Page Application)

- Web App과 함께 자주 등장할 용어 SPA

- 이전까지는 사용자의 요청에 대해 적절한 페이지 별 template를 반환

- SPA는 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식

  - CSR(Client Side Rendering) 방식으로 요청을 처리하기 때문에 한 페이지로 모든 요청에 대응할 수 있음

### SSR(Server Side Rendering)

- 기존의 요청 처리 방식은 SSR

- Server가 사용자의 요청에 적합한 HTML을 렌더링하여 제공하는 방식

- 전달받은 새 문서를 보여주기 위해 브라우저는 새로고침을 진행

### CSR(Client Side Rendering)

- 최초 한 장의 HTML을 받아오는 것은 동일하지만, server로부터 최초로 받아오는 문서는 빈 html 문서

- 각 요청에 대한 대응을 JavaScript를 사용하여 필요한 부분만 다시 렌더링

  1. 필요한 페이지를 서버에 AJAX로 요청

  2. 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달

  3. JSON 데이터를 JavaScript로 처리, DOM 트리에 반영(렌더링)

> ### CSR 방식을 사용하는 이유

- 모든 HTML 페이지를 서버로부터 받아서 표시하지 않아도 됨

  == 클라이언트-서버 간 통신(트래픽) 감소 == 응답 속도가 빨라진다

- 매번 새 문서를 받아 새로고침하는 것이 아니라 필요한 부분만 고쳐나가므로 각 요청이 끊김없이 진행

- BE와 FE의 작업 영역을 명확히 분리할 수 있음

  협업이 용이해짐

> ### CSR의 한계

- 첫 구동 시 필요한 데이터가 많을수록 최초 작동시작까지 오랜 시간이 소요됨

- 검색엔진 최적화(SEO, Search Engine Optimization)가 어려움

  서버가 제공하는 것은 빈 HTML

  내용을 채우는 것은 AJAX 요청으로 얻은 JSON 데이터로 클라이언트(브라우저)가 진행

### CSR vs SSR

- 내 서비스에 적합한 렌더링 방식을 적절하게 활용

- SPA 서비스에서도 SSR을 지원하는 Framework가 발전하고 있음

  Vue의 Nuxt.js, React의 Next.js, Angular Universal 등