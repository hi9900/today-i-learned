# Vue Data Management

## Data in components

- 컴포넌트는 부모-자식 관계를 가지고 있으므로, 부모-자식 관계만 데이터를 주고받게 함

- 데이터의 흐름을 파악하기 용이

- 유지 보수하기 쉬워짐

## Pass Props

- 요소의 속성(property)을 사용하여 데이터 전달

- props는 부모(상위) 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성

- 자식(하위) 컴포넌트는 props 옵션을 사용하여 수신하는 props를 명시적으로 선언해야 함

- 부모 -> 자식으로의 data 전달 방식

- 정적인 데이터를 전달하는 경우 static props라고 명시하기도 함

- 요소에 속성을 작성하듯이 사용 가능하며, `prop-data-name="value"`의 형태로 데이터를 전달

  - 이때 속성의 키 값은 kebab-case를 사용

- 데이터를 받는 쪽, 즉 하위 컴포넌트에서도 props에 대해 명시적으로 작성 해주어야 함

- 전달받은 props를 type과 함께 명시

- 컴포넌트를


> ### props in HelloWorld

  - App.vue의 `<HelloWorld />` 요소에 `msg="..."` 라는 property를 설정하였고, 하위 컴포넌트인 HelloWorld는 자신에게 부여된 msg property를 template에서 `{{ msg }}` 형태로 사용한 것

## Emit event

- 자식 -> 부모로의 데이터 흐름