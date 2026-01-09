## State & Props 전화번호부에 적용하기

### 데이터 추가 함수 만들기

  - 입력받은 값을 전화번호부 목록에 추가하는 handleSubmit 함수

  ```js
  // src/App.js

  import React, { Component } from 'react'
  import InputBox from './components/InputBox'
  import PhoneList from './components/PhoneList'
  import './App.css'
  import { dummyData, nextId, setNextId } from './lib/dummyData.js'
  ...
    handleSubmit = () => {
      const { dummyData, name, phone } = this.state

      if (name === "" || phone === "") return

      this.setState({
        dummyData: {
          ...dummyData,
          [nextId]: {
            id: nextId,
            name,
            phone
          }
        },
        name: "",
        phone: ""
      })

      setNextId()
    }

    render() {
      const { handleInput, handleSubmit } = this
      const { dummyData, name, phone } = this.state

      return (
        <div className='container'>
          <InputBox
            name={name}
            phone={phone}
            onChange={handleInput}
            onSubmit={handleSubmit}
          />
          <PhoneList list={dummyData} />
        </div>
      )
    }
  }

  export default App;
  ```

  > 입력받은 값을 dummyData에 추가

  ```js
  this.setState({
    dummyData: {
      ...dummyData,
      [nextId]: {
        id: nextId,
        name,
        phone
      }
    },
    name: "",
    phone: ""
  })
  ```

  - input 태그의 값을 모두 지워주기 위해 name, phone값을 빈 값으로 설정

  - dummyData에는 Spread 문법으로 기존에 있던 내용을 모두 넣어준 뒤, 새로 입력받은 값을 추가

  `this.state.dummyData[nextId] = {id: nextId, name, phone}`과 같은 방법으로 추가하지 않음 (불변성을 지켜야 하기 때문)
  
  컴포넌트 리렌더링을 보장받을 수 있고, 성능 개선이 가능하기 때문

### InputBox

  - `onSubmit`이라는 이름으로 handleSubmit 함수가 props로 넘어옴

  - 이를 button의 onClick 이벤트 핸들러로 지정

  ```js
  // src/components/InputBox/InputBox.js
  import React from "react"
  import "./InputBox.css"

  const InputBox = ({ name, phone, onChange, onSubmit }) => {
    return (
      <div className='input_boxes'>
      ...
        <button className='input_box_button' onClick={onSubmit}>저장</button>
      </div>
    )
  }
  ```

---

### 데이터 삭제 함수 만들기

  - 전화번호부 아이템을 삭제하는 handleRemove 함수

  ```js
  // src/App.js

  ...
  handleRemove = id => {
    const { [id]: _, ...dummyData } = this.state.dummyData

    this.setState({ dummyData })
  }
  ...
  render() {
    const { handleInput, handleSubmit, handleRemove } = this
    const { dummyData, name, phone } = this.state

    return (
      <div className='container'>
        ...
        <PhoneList list={dummyData} deleteItem={handleRemove} />
      </div>
    )
  }
  ```

  `[id]:_`: 제거하고 싶은 아이템을 `_`라는 변수에 할당

  `...dummyData`: Spread 문법을 통해 앞에서 제외한 아이템을 뺀 데이터를 dummyData에 저장

  그 후 setState 함수에 dummyData를 넘겨주면 불변성을 위반하지 않고 올바르게 데이터를 변경할 수 있음

### PhoneList

  - PhoneList에서 props를 받고 PhoneItem 컴포넌트에 onClick이라는 이름으로 props를 전달

  ```js
  // src/components/PhoneList/PhoneList.js

  ...
  const PhoneList = ({ list, deleteItem }) => {
    return (
      <PhoneWrapper>
        {Object.values(list).map(item => {
          return <PhoneItem {...item} key={item.id} onClick={deleteItem} />
        })}
      </PhoneWrapper>
    )
  }
  ```

### PhoneItem

  ```js
  // src/components/PhoneItem/PhoneItem.js

  const PhoneItem = ({ id, name, phone, onClick }) => {
    return (
      <div className="phone_item">
        <div className="phone_item_left">
          <div className="phone_item_name">{name}</div>
          <div className="phone_item_phone">{phone}</div>
        </div>

        <div className="phone_item_right">
          <button onClick={() => onClick(id)}>삭제</button>
        </div>
      </div>
    )
  }
  ```

  - onClick 함수를 button의 onClick 이벤트 핸들러로 지정

    `onClick={onClick(id)}`라고 적지 않은 이유는 React에서 이벤트 핸들러로 함수 레퍼런스, 즉 함수 그 자체를 전달해야 하기 때문

    보통 `onClick={onClick}`과 같이 소괄호를 제외하고 보내지만, onClick 함수가 id 파라미터를 받기 때문에 Arrow Function으로 새 함수를 만들고 이를 전달
