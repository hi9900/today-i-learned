const body = document.body

// 숫자 후보
const numbers = [1,2,3,4,5,6,7,8,9]
// 랜덤 숫자 4자리
const number = [];

// 랜덤 숫자 뽑기
for (let i=0; i<4; i++) {
  // splice(위치, 개수): 위치부터 갯수만큼 배열에서 뽑기
  let choice = numbers.splice(Math.floor(Math.random() * (9-i)), 1)
  number.push(...choice)
}
console.log(number)

const result = document.createElement('h1')
body.appendChild(result)

const form = document.createElement('form')
form.innerHTML = `
<input type="text" pattern="[1-9]{4}" placeholder="4자리 숫자" required>
<button>입력</button>
`
body.appendChild(form)

const formInput = document.querySelector('input')
form.addEventListener('submit', function(event) {
  event.preventDefault()
  // 내가 입력한 답
  const ans = document.querySelector('input').value
  console.log(ans)

  // 문자.split(구분자) -> 배열
  // 배열.join(구분자) -> 문자
  if (ans === number.join('')) { // 답이 맞으면
    result.innerText = "홈런!"
  } else { // 답이 틀리면
    const ansArr = ans.split('')
    // console.log(ans.split(''))
    let strike = 0
    let ball = 0
    for (let i=0; i<4; i++) {
      // console.log(number.indexOf(ansArr[i]))
      let isHR = Number(ansArr[i])
      if (isHR === number[i]) {
        strike++
      } else if (number.indexOf(isHR) >= 0) {
        // 배열.indexOf(값): 값의 위치를 반환, 없으면 -1
        ball++
      } 
    }
    result.innerText = `${strike}스트라이크 ${ball}볼`
  }
  form.reset()
})