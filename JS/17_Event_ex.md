## button 실습

- 버튼을 클릭하면 특정 변수 값 변경하기

```html
<body>
  <button id="btn">버튼</button>
  <p id="counter">0</p>

  <script>
    // 초기값
    let countNumber = 0

    // ID가 btn인 요소를 선택
    const btn = document.querySelector('#btn')
    console.log(btn)

    // btn이 클릭되었을 때마다 함수가 실행됨
    btn.addEventListener('click', function () {
      console.log('버튼 클릭!!')
      // countNumber 증가
      countNumber += 1
      // id가 counter인 내용 변경
      const counter = document.querySelector('#counter')
      counter.innerText = countNumber
    })
  </script>
</body>
```

## 값 입력 실습

- input에 입력하면 입력 값을 실시간으로 출력

```html
<body>
  <input type="text" id="text-input">
  <p></p>

  <script>
    // 1. input 선택
    const textInput = document.querySelector('#text-input')
    // 2. input 이벤트 등록
    textInput.addEventListener('input', function (event) {
      console.log(event)
      // input은 이벤트의 대상
      console.log(event.target)
      // input의 value를 받아오기
      console.log(event.target.value)

      // 3. input에 작성한 값을 p태그에 출력
      const pTag = document.querySelector('p')
      pTag.innerText = event.target.value
    })
  </script>
</body>
```

## 복합 실습

- input에 입력하면 입력 값을 실시간으로 출력하고, 버튼을 클릭하면 출력된 값의 클래스를 토글하기

```html
<head>
  ...
  <style>
    .blue {
      color: blue;
    }
  </style>
</head>
<body>
  <h1></h1>
  <button id="btn">클릭</button>
  <input type="text">

  <script>
    const btn = document.querySelector('#btn')
    // btn을 클릭하면 함수 실행
    btn.addEventListener('click', function () {
      // h1 태그를 선택해서
      const h1 = document.querySelector('h1')
      // 클래스 blue를 토글
      h1.classList.toggle('blue')
    })

    const input = document.querySelector('input')
    // input에 값이 입력되면 함수 실행
    input.addEventListener('input', function (event) {
      // h1 태그를 선택해서
      const h1Tag = document.querySelector('h1')
      // input값의 태그의 컨텐츠로 채우기
      h1Tag.innerText = event.target.value
    })
  </script>
</body>
```

---

## Event 취소 실습

- 웹 페이지 내용을 복사하지 못하도록 하기

```html
...
<body>
  <div>
    <h1>정말 중요한 내용</h1>
  </div>

  <script>
    const h1 = document.querySelector('h1')
    h1.addEventListener('copy', function (event) {
      // copy event의 기본 동작을 막기
      event.preventDefault()
      alert('복사할 수 없습니다.')
    })
  </script>
</body>
```

## Event 종합 실습

- 버튼을 클릭하면 랜덤 로또 번호를 6개 출력하기

```html
...
  <style>
    /* 스타일은 수정하지 않습니다. */
    .ball {
      width: 10rem;
      height: 10rem;
      margin: .5rem;
      border-radius: 50%;
      text-align: center;
      line-height: 10rem;
      font-size: xx-large;
      font-weight: bold;
      color: white;
    }

    .ball-container {
      display: flex;
    }
  </style>
</head>

<body>
  <h1>로또 추천 번호</h1>
  <button id="lotto-btn">행운 번호 받기</button>
  <div id="result"></div>

  <!-- lodash CDN -->
  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
  <script>
    const button = document.querySelector('#lotto-btn')
    button.addEventListener('click', function () {
      // 컨테이너를 만들고
      const ballContainer = document.createElement('div')
      ballContainer.classList.add('ball-container')

      // 랜덤 숫자 6개 만들기
      const numbers = _.sampleSize(_.range(1, 46), 6)
      // console.log(numbers)

      // 공 만들기
      numbers.forEach((number) => {
        const ball = document.createElement('div')
        ball.classList.add('ball')
        ball.innerText = number
        ball.style.backgroundColor = 'crimson'

        // 공을 컨테이너의 자식으로 추가
        ballContainer.appendChild(ball)
      });

      // 컨테이너를 결과 영역의 자식으로 추가
      const result = document.querySelector('#result')
      result.appendChild(ballContainer)
    })
  </script>
</body>
```

## 종합 실습2

- CREATE, READ 기능을 충족하는 todo app 만들기

```html
<body>
  <h1>Todo</h1>
  <form action="#">
    <input type="text" class="inputData">
    <input type="submit" value="Add">
  </form>
  <ul></ul>

  <script>
    const formTag = document.querySelector('form')

    const addTodo = function (event) {
      event.preventDefault()

      const inputTag = document.querySelector('.inputData')
      const data = inputTag.value

      if (data.trim()) {
        const liTag = document.createElement('li')
        liTag.innerText = data

        const ulTag = document.querySelector('ul')
        ulTag.appendChild(liTag)
        event.target.reset()
      } else {
        alert('할 일을 입력하세요.')
      }
    }

    formTag.addEventListener('submit', addTodo)
  </script>
</body>
```