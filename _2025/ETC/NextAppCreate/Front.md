# 프론트엔드 토대쌓기

## 개요

> ### React

  React는 사용자 인터페이스를 만들기 위한 JavaScript 라이브러리이다.

  국내에서는 이미 Angular나 Vue.js보다 시장 지배적인 위치를 차지했고 대부분의 개발 회사에서는 프론트엔드 개발을 위해서 React를 선택하는 분위기이기 때문에 취업을 준비하는 입장에서는 React를 하지 않을 이유가 없다.

  React는 입문자에게는 학습의 난이도가 있는 편이지만 공식 문서를 학습하면서 천천히 따라간다면 프로젝트에 사용할 만큼 이해하는 것이 충분히 가능하다.

> ### CSR과 SSR

  SPA(Single Page Application)이 프론트엔드 개발의 대세가 되면서 CSR(Client Side Rendering)을 활용한 서비스들이 등장하기 시작했는데 여러가지 장점들로 인해서 기존의 SSR을 완전하게 대체할 것처럼 보였다.

  하지만 많은 회사들이 실제로 서비스를 운영해보니 CSR의 치명적인 문제를 알게 되었는데, 바로 대부분의 검색 엔진들이 CSR로 개발된 페이지를 제대로 인식하지 못한다는 것이다.

  회사들의 입장에서는 서비스를 홍보하기 위해서 막대한 마케팅 비를 지출하게 되는데, 구글이나 네이버 등의 검색엔진을 통한 노출은 비용 지출 없이도 자연적으로 유저의 유입이 발생하는 수단이었다.

  하지만 CSR로 개발한 페이지들은 검색 엔진이 분석할 수 없었기 때문에 next.js와 같은 대체적인 방법을 활용하게 되었다.

  최근 검색 엔진의 성능이 조금씩 좋아져서 CSR로 구현된 페이지도 조금씩 분석이 가능해지고 있지만 여전히 최상위 페이지에 노출되기에는 부족한 수준이다.

> ### TypeScript

  TypeScript는 JavaScript를 기반으로 정적 타입 문법을 추가한 프로그래밍 언어이다.

  JavaScript는 동적 타입의 인터프리터 언어로 런타임에서야 오류를 발견할 수 있었던 반면, TypeScript는 정적 타입의 컴파일 언어이며 컴파일러를 통해서 JavaScript 코드로 변환된다.

  TypeScript는 코드 작성 단계에서 타입을 체크해서 오류를 확인할 수 있기 때문에 실행하기 전에 많은 오류들을 잡아낼 수 있다는 장점이 있다.

  JavaScript로 개발하는 대부분의 회사에서 TypeScript를 사용하고 있기 때문에 프론트엔드로 취업을 준비하는 개발자라면 반드시 익혀야 할 기술 스택이다.
  
## 필수 지식 학습

  [React 공식문서](https://ko.reactjs.org/)

  [Next.js 공식문서](https://nextjs.org/)

  [TypeScript 공식문서](https://www.typescriptlang.org/)

  [Router](https://nextjs.org/docs/api-reference/next/router)

## 과제

> ### React + next.js + TypeScript

  - 공식 문서를 보면서 React의 기본 개념과 철학을 익힌다.

  - next.js를 공부하면서 SSR(Server Side Rendering)의 중요성을 익힌다.

  - TypeScript를 사용하면서 프론트엔드의 정적 타입 문법을 사용해본다.

  - 개발에 필요한 환경을 구축해보고 기초적인 쉘 사용법을 익힌다.
