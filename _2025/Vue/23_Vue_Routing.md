# Vue Router

## Routing

- 네트워크에서 경로를 선택하는 프로세스

- 웹 서비스에서의 라우팅

  - 유저가 방문한 URL에 대해 적절한 결과를 응답하는 것

- 예시

  - `/articles/index/`에 접근하면 articles의 index에 대한 결과를 보내줌

## Routing in SSR

- Server가 모든 라우팅을 통제

- URL로 요청이 들어오면 응답으로 완성된 HTML 제공

  - Django로 보낸 요청의 응답 HTML은 완성본인 상태였음

- 결론적으로, Routing(URL)에 대한 결정권을 서버가 가짐

## Routing in SPA / CSR

- 서버는 하나의 HTML(index.html)만을 제공

- 이후에 모든 동작은 하나의 HTML 문서 위에서 JavsScript 코드를 활용

  - DOM을 그리는데 필요한 추가적인 데이터가 있다면 axios와 같은 AJAX 요청을 보낼 수 있는 도구를 사용하여 데이터를 가져오고 처리

- 즉, 하나의 URL만 가질 수 있음

## Why routing

- 동작에 따라 URL이 반드시 바뀌지 않아도 되지만, 유저의 사용성 관점에서는 필요함

- Routing이 없다면,

  - 유저가 URL을 통한 페이지의 변화를 감지할 수 없음

  - 페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음

    - 새로고침 시 처음 페이지로 돌아감

    - 링크를 공유할 시 처음 페이지만 공유 가능

  - 브라우저의 뒤로가기 기능을 사용할 수 없음