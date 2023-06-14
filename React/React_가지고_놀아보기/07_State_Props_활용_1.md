## State & Props 전화번호부에 적용하기

- 부모 컴포넌트에게서 전화번호 리스트를 state로 관리

- props로 전달해 데이터를 띄워주기

- 인풋 박스와 삭제 버튼을 구현해 데이터를 변경할 수 있게 만들기

### 더미 데이터 만들기

  ```js
  // src/lib/dummyData.js

  export const dummyData = {
    "0": {
      id: "0",
      name: "John",
      phone: "010-0000-0000"
    },
    "1": {
      id: "1",
      name: "Peter",
      phone: "010-1111-1111"
    },
    "2": {
      id: "2",
      name: "Elise",
      phone: "010-2222-2222"
    },
    "3": {
      id: "3",
      name: "Chris",
      phone: "010-3333-3333"
    },
    "4": {
      id: "4",
      name: "Austin",
      phone: "010-4444-4444"
    }
  };
  ```

  - dummyData의 타입은 배열이어도 상관없지만, 데이터 업데이트 속도를 고려하여 Json 형식으로 데이터를 만듦

### 데이터를 state로 정의하기

  - App.js에서 더미데이터를 불러온 후 그 값을 state로 정의

  - state를 사용하기 위해 App 컴포넌트를 클래스 컴포넌트로 수정 후 state 선언

  - PhonList 컴포넌트에 list라는 이름의 props 전달

  ```js
  // src/App.js

  import React, { Component } from 'react'
  import InputBox from './components/InputBox'
  import PhoneList from './components/PhoneList'
  import './App.css'
  import { dummyData } from './lib/dummyData.js'

  class App extends Component {
    state = dummyData

    render() {
      return (
        <div className='container'>
          <InputBox />
          <PhoneList list={this.state} />
        </div>
      )
    }
  }

  export default App;
  ```

### PhoneList 컴포넌트

  - 전화번호 부 리스트 내의 개별 데이터를 PhoneItem 컴포넌트에 전달

  - Destruction Assignment 문법을 사용해 props 전달 가능

  `<PhoneItem {...list["0"]} />`

  `<PhoneItem id={list["0"].id} name={list["0"].name} phone={list["0"].phone} />`

  - list["0"]에는 id, name, phone 속성이 들어있기 때문에 props 객체의 속성으로 id, name, phone이 전달

  ```js
  // src/components/PhoneList/PhoneList.js

  import React from "react"
  import PhoneItem from "../PhoneItem"
  import styled from "styled-components"

  const PhoneWrapper = styled.div`
    display: flex;
    flex-direction: column;
  `

  const PhoneList = ({ list }) => {
    return (
      <PhoneWrapper>
        <PhoneItem {...list["0"]} />
        <PhoneItem {...list["1"]} />
        <PhoneItem {...list["2"]} />
        <PhoneItem {...list["3"]} />
        <PhoneItem {...list["4"]} />
      </PhoneWrapper>
    )
  }

  export default PhoneList
  ```

> ### map 함수

  - map 함수: 배열 내의 모든 요소 각각에 대하여 주어진 함수를 호출한 결과를 모아 새로운 배열을 반환

  ```js
  // ex 1
  var arr1 = [1, 2, 3, 4, 5]
  var arr2 = arr1.map(x => x * 2)
  console.log(arr2) // [2, 4, 6, 8, 10]

  // ex 2
  var jsonArr = [
    {key: 1, value: 10},
    {key: 2, value: 20},
    {key: 3, value: 30}]
  var reformatted = jsonArr.map(obj => {
    var tmp = {}
    tmp[obj.key] = obj.value
    return tmp
  })
  console.log(reformatted) // [{1:10}, {2:20}, {3:30}]

  // ex 3
  var num = [1, 4, 9, 16]
  var roots = num.map(Mate.sqrt)
  console.log(roots) // [1, 2, 3, 4]
  ```

> ### PhoneList 컴포넌트 수정

  - `Object.values()`로 Json 형식을 value값으로만 이루어져있는 배열로 변경 후 map 함수 적용

  ```js
  // src/components/PhoneList/PhoneList.js

  const PhoneList = ({ list }) => {
    return (
      <PhoneWrapper>
        {Object.values(list).map(item => {
          return <PhoneItem {...item} key={item.id} />
        })}
      </PhoneWrapper>
    )
  }
  ```

  - map 함수를 통해 반복적으로 컴포넌트를 생성해줄 때 key 값을 지정해줘야 함 (보통 데이터의 id 값과 같은 고유 값으로 설정)

    React는 업데이트된 부분만 변경해주는데, key 값을 지정하지 않았다면 업데이트가 된 부분을 잡아내기 위해 일일이 비교를 하게 됨

    key값을 지정해준다면 그 값을 통해 업데이트된 부분을 빠르게 잡아낼 수 있어 속도가 엄청나게 향상됨

    O(n^3)에서 O(n)까지 속도 향상이 가능함

### PhoneItem

  ```js
  // src/components/PhoneItem/PhoneItem.js

  import React from "react"
  import './PhoneItem.scss'

  const PhoneItem = ({ name, phone }) => {
    return (
      <div className="phone_item">
        <div className="phone_item_left">
          <div className="phone_item_name">{name}</div>
          <div className="phone_item_phone">{phone}</div>
        </div>

        <div className="phone_item_right">
          <button>삭제</button>
        </div>
      </div>
    )
  }

  export default PhoneItem
  ```
