# CSR SSR

## 개요

Vue와 React는 대표적인 Single Page Application(SPA) framework 로 Client Side Rendering(CSR) 방식으로 View를 만든다. 이와 대조적으로 PHP는 Multi Page Application(MPA)으로 Server Side Rendering(SSR) 방식으로 View를 만든다.

## SPA, MPA 접속(test URL 생략)

service에서 a<->b 로 page 전환 시, browser에 보이는 화면의 차이는 없어 보이지만 내부 동작은 다르다.

## CSR vs SSR

> ### 1. CSR

  Browser(Client)에서 js에 의해 View(HTML)를 동적으로 생성한다.

  따문에 page 전환이 SSR보다 상대적으로 빠르다. 대신 최초 접속 시, 모든 js(java script)와 static 파일(HTML, image)을 가져와야 한다.

  따라서 최초 접속 시 로딩은 SSR에 비해 늦다.

> ### 2. SSR

  Web Server에서 View를 생성한다.

  Page가 전환될 때 마다, Client가 Server에 View 요청을 하고, Server는 그것을 생성 후 Client에게 보내준다.

  때문에 View 전환 속도가 CSR에 비해 상대적으로 늦다.

  그리고 Page 요청이 빈번해질수록 CSR에 비해 Server 부하가 더 커진다.

## Wire Shark

  SPA, MPA에서 page 전환 시, 네트워크 요청&응답이 어떻게 되는 지 살펴보자.

  [Wire Shark 설치](https://www.wireshark.org/download.html) 후 IP 필터를 설정하고 packet을 capture

## MPA

  Browser로 MPA에 접속 후 page a <-> page b 를 번갈아 가면서 전환

  Wire Shark에서 View가 바뀔 때마다, client와 server간에 View를 요청&응답 하는 packet이 생성되는 지 확인

  다음으로 server 응답을 더블 클릭해서 자세히 보면 응답에 View가 포함 된 것이 보인다.

## SPA

  Browser로 SPA에 접속 후 Wire Shark에서 최초 접속 시 js 및 static file을 download 받는 지 확인

  보통 Browser에서 download cache 기능이 있기 때문에, download 하지 않는 경우가 있다.

  개발자 도구 - Network - Disable cache 체크 후 접속

  js & static packet을 더블 클릭하여 자세히 보면 js 및 static 파일의 내용을 확인할 수 있다.

  다음으로 page a <-> page b 로 전환해도 server에 요청을 보내지 않는 지 확인

  page를 전환할 때, MPA와는 다르게 wire shark에서 packet이 capture되지 않음

## HTTP Packet

> ### HTTP 요청 메시지 구조

  - 요청 라인: 버전 정보를 담고 있는 행으로 "요청 메소드 / 요청URI / HTTP 버전" 으로 이루어져 있음

  - 요청 헤더: 여러 헤더들로 구성되며 각각 정보는 개행(공백)으로 구분됨

    (헤더명:헤더값<개행>...헤더명:헤더값<개행>)

  - 공백 라인: 헤더의 끝을 의미하는 개행

  - 본문: 직접적인 데이터가 담겨있는 곳

- Host: 요청한 서버의 "도메인 명 / 호스트명 포트번호"

- User-Agent: 요청 클라이언트 어플리케이션 OS 정보

- `\r\n`: 개행, 헤더의 끝

- Full request URI ... : 메시지 바디부, 실질적인 데이터가 들어 있음

> ### HTTP 응답 메시지 구조

  - 상태 라인: 요청 메시지와 마찬가지로 버전 정보를 담고있는 행 "HTTP 버전 / 상태코드 / 응답구문" 으로 이루어져 있음

  - 응답 헤더: 여러 헤더들로 구성되며 각 정보는 개행으로 구분됨

  - 공백 라인: 헤더의 끝을 의미하는 개행

  - 본문: 서버에서 클라이언트로 전송된 데이터가 담겨져 있는 곳