## State & Props 전화번호부에 적용하기

### Input 값 State로 관리하기

  - Input 값을 State로 저장하지 않는다면, Ref를 통해 DOM에서 값을 받아와야 함

    React 공식 홈페이지에서는 State로 해결할 수 없는 문제에 대해서만 Ref를 사용하라고 권장

  - 따라서 Input값을 State로 저장해서 관리해야 함
  
  ```js
  // src/App.js

  import React, { Component } from 'react'
  import InputBox from './components/InputBox'
  import PhoneList from './components/PhoneList'
  import './App.css'
  import { dummyData } from './lib/dummyData.js'

  class App extends Component {
    state = {
      dummyData,
      name: "",
      phone: "",
    }

    handleInput = e => {
      this.setState({
        [e.target.name]: e.target.value
      })
    }

    render() {
      const { handleInput } = this
      const { dummyData, name, phone } = this.state

      return (
        <div className='container'>
          <InputBox
            name={name}
            phone={phone}
            onChange={handleInput}
          />
          <PhoneList list={dummyData} />
        </div>
      )
    }
  }

  export default App;
  ```

  1. state에 name과 phone 값을 추가

  2. handleInput이라는 함수를 만들어 InputBox 컴포넌트에 Props로 전달

    `e.target`: 해당 이벤트가 발생한 element를 가리킴

    `e.target.name`: 이벤트가 발생한 Element의 name 속성값

    `e.target.value`: 이벤트가 발생한 Element의 value 속성값

### InputBox

  - App 컴포넌트로부터 `onChange`라는 props를 받아와 input 태그의 이벤트 핸들러로 지정
  
  ```js
  // src/components/InputBox/InputBox.js

  import React from "react"
  import "./InputBox.css"

  const InputBox = ({ name, phone, onChange }) => {
    return (
      <div className='input_boxes'>
        <div className="input_box">
          <div className="input_box_name">이름</div>
          <input type="text" placeholder='이름' name='name' className='input_box_input'
            onChange={onChange} value={name}
          />
        </div>

        <div className="input_box">
          <div className="input_box_name">전화번호</div>
          <input type="text" placeholder='전화번호' name='phone' className="input_box_input"
            onChange={onChange} value={phone}
          />
        </div>
        <button className='input_box_button'>저장</button>
      </div>
    )
  }

  export default InputBox
  ```

### dummyData.js 파일 변경

  - 새로운 전화번호부 아이템을 추가할 때 키 값을 다르게 해야 데이터를 저장하는 데 문제가 발생하지 않음

  - `nextId`라는 변수를 추가해 이를 key 값으로 설정할 수 있게 하고, `setNextId`라는 함수를 통해 데이터를 추가할 때마다 `nextId`값을 1씩 늘려줌

  ```js
  // src/lib/dummyData.js

  export var nextId = Object.keys(dummyData).length

  export const setNextId = () => {
    nextId++
  }
  ```

  - `Object.keys`: key 값으로 배열을 만들어 반환하는 함수