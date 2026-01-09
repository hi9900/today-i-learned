# React Hooks 전화번호부에 적용

## Custom Hooks로 Input 값 관리

### useInput

- lib 디렉토리에 Custom Hooks인 useInput.js 파일 작성

  - Custom Hooks는 보통 파일 이름에 use를 붙이는 것이 관례

```js
// src/lib/useInput.js

import { useState } from 'react'

const useInput = (initialValue) => {
  const [value, setValue] = useState(initialValue)

  const onChange = e => {
		// Destructing Assignment
    const { target: { value } } = e
    setValue(value)
  }

  return [ value, setValue, onChange ]
}

export default useInput
```

- `const [value, setValue] = useState(initialValue)`

  useState를 사용하여 상태 값과 그 값을 바꿔주는 함수 선언

- onChange 함수

  input 값이 변경되었을 때 실행시켜 줄 함수

- `return [ value, setValue, onChange ]`

  상태 값, 그 값을 바꿔주는 함수, input 값이 변경되었을 때 실행시켜줄 함수를 반환

---

```js
// src/App.js

import React, { useState } from "react";
import InputBox from "./components/InputBox";
import PhoneList from "./components/PhoneList";
import "./App.css";
import { dummyData, nextId, setNextId } from "./lib/dummyData.js";
import useInput from './lib/useInput';

const App = () => {
  const [data, setData] = useState(dummyData);
  const [name, setName, onChangeName] = useInput("");
  const [phone, setPhone, onChangePhone] = useInput("");

  const handleSubmit = () => {
    if (name === "" || phone === "") return

    setData({
      ...data,
      [nextId]: {
        id: String(nextId),
        name,
        phone
      }
    })
    setName("")
    setPhone("")

    setNextId()
  }

  const handleRemove = id => {

  };

  return (
    <div className="container">
      <InputBox
        name={name}
        phone={phone}
        onChangeName={onChangeName}
        onChangePhone={onChangePhone}
        onSubmit={handleSubmit}
      />
      <PhoneList list={data} deleteItem={handleRemove} />
    </div>
  );
}

export default App;
```

- Hooks를 사용하기 위해 클래스형 컴포넌트에서 함수형 컴포넌트로 변환

- 기존에 state로 선언했던 것을 모두 Hooks로 선언한 것으로 변경

- inputBox로 넘겨주는 props에 변화

  name 값을 받는 input과 phone 값을 받는 input에 각각의 onChange 함수가 들어감

### inputBox

```js
// 경로 : src/components/InputBox/InputBox.js

import React from "react";
import styles from "./InputBox.module.css";

const InputBox = ({ name, phone, onChangeName, onChangePhone, onSubmit }) => {
  return (
    <div className={styles.input_boxes}>
      <div className={styles.input_box}>
        <div className={styles.input_box_name}>이름</div>
        <input
          type="text"
          placeholder="이름"
          name="name"
          className={styles.input_box_input}
          onChange={onChangeName}
          value={name}
        />
      </div>
      <div className="input_box">
        <div className={styles.input_box_name}>전화번호</div>
        <input
          type="text"
          placeholder="전화번호"
          name="phone"
          className={styles.input_box_input}
          onChange={onChangePhone}
          value={phone}
        />
      </div>
      <button className={styles.input_box_button} onClick={onSubmit}>
        저장
      </button>
    </div>
  );
};

export default InputBox;
```