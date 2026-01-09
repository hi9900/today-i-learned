import React from 'react'

function Hello({ color, name, isSpecial }) {
  return (
    <>
      <div style={{ color }}>
        {isSpecial ? <b>*</b> : null}
        삼항연산자 {name}
      </div>
      <div style={{ color }}>
        {isSpecial && <b>*</b>}
        && 연산자 {name}
      </div>
    </>
  )
}

Hello.defaultProps = {
  name: '이름없음'
}

export default Hello