const body = document.body

const result = document.createElement('h1')
const form = document.createElement('form')
form.innerHTML = `
<input type="text" pattern="[1-9]{4}" placeholder="4자리 숫자" required>
<button>입력</button>
`
body.append(result, form)

// 숫자 후보
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
// 정답 숫자
const ansNumber = []

// 랜덤 숫자 뽑기
for (let i = 0; i < 4; i++) {
  let choice = numbers.splice(Math.floor(Math.random() * (9 - i)), 1)
  ansNumber.push(...choice)
}
console.log(ansNumber)

form.addEventListener('submit', function (event) {
  event.preventDefault()
  // 내가 입력한 답
  const ans = document.querySelector('input').value
  // console.log(ans)

  if (ans === ansNumber.join('')) { // 답이 맞으면
    result.innerText = "홈런!"
  } else { // 답이 틀리면
    const ansArr = ans.split('')
    let strike = 0
    let ball = 0
    for (let i = 0; i < 4; i++) {
      let isHR = Number(ansArr[i])
      if (isHR === ansNumber[i]) {
        strike++
      } else if (ansNumber.indexOf(isHR) >= 0) {
        ball++
      }
    }
    result.innerText = `${strike}스트라이크 ${ball}볼`
  }
  form.reset()
})