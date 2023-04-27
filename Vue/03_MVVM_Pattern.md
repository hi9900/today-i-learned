## MVVM Pattern

- 소프트웨어 아키텍처 패턴의 일종 (Model-View-ViewModel)

- 마크업 언어로 구현하는 그래픽 사용자 인터페이스(`view`)의 개발을 Back-end(`model`)로부터 분리시켜 view가 어느 특정한 모델 플랫폼에 종속되지 않도록 함

- View: 우리 눈에 보이는 부분 = DOM

- Model: 실제 데이터 = JSON

- View Model (Vue)

  - View를 위한 Model

  - View와 연결(binding)되어 Action을 주고 받음

  - Model이 변경되면 View Model도 변경되고 바인딩 된 View도 변경됨

  - View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩 된 다른 View도 변경됨

> ### MVVM Pattern 정리

- MVC 패턴에서 Controller를 제외하고 View Model을 넣은 패턴

- View는 Model을 모르고, Model도 View를 모른다

  == DOM은 Data를 모르고, Data도 DOM을 모른다 (독립성 증가, 적은 의존성)

- View에서 데이터를 변경하면 View Model의 데이터가 변경되고, 연관된 다른 View도 함께 변경된다.

