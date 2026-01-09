# Axios

- JavaScript의 HTTP 웹 통신을 위한 라이브러리

- 확장 가능한 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공

- Node 환경은 npm을 이용해서 설치 후 사용할 수 있고,

  browser 환경은 CDN을 이용해서 사용할 수 있음

- [Axios 공식문서](https://axios-http.com/kr/docs/intro) 및 [github](https://github.com/axios/axios)

## Axios 기본 구조

```html
<!-- axios CDN -->
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>\
<script>
  axios.get('요청할 URL')
    .then(성공하면 수행 할 콜백 함수)
    .catch(실패하면 수행 할 콜백 함수)
</script>
```

- get, post 등 여러 method 사용 가능

- `then`을 이용해서 성공하면 수행 할 로직을 작성

- `catch`를 이용해서 실패하면 수행 할 로직을 작성

> ### 고양이 사진 가져오기

- [The Cat API](https://api.thecatapi.com/v1/images/search)

  - 이미지를 요청해서 가져오는 작업을 비동기로 처리

- response 구조

```js
// https://api.thecatapi.com/v1/images/search
[
  {
    "id": "d6n",
    "url": "https::cdn2.thecatapi.com/images/d6n.jpg",
    "width": 333,
    "height":500
  }
]
```

> ### python

- Python으로 요청 (동기)

```python
import requests

print('고양이는 야옹')

cat_image_search_url = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(cat_image_search_url)

if response.status_code == 200:
  print(response.json())
else:
  print('실패했다옹')

print('야옹야옹')
```

```bash
고양이는 야옹
[{'id': 'b2n', 'url': 'https://cdn2.thecatapi.com/images/b2n.jpg', 'width': 4608, 'height': 3456}]
야옹야옹
```

> ### Axios

- Axios로 요청 (비동기)

```html
<body>
  <button>야옹아 이리온</button>
  <!-- axios CDN -->
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    console.log('고양이는 야옹')
    // cat API
    const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'

    axios.get(catImageSearchURL)
      // 성공했을 때
      .then((response) => {
        console.log(response.data)
      })
      // 실패했을 때
      .catch((error) => {
        console.log('실패했다옹')
      })

    console.log('야옹야옹')
  </script>
</body>
```

```
<!-- console -->
고양이는 야옹
야옹야옹
Array(1)
  > 0: {id: 'bon', url: 'https://cdn2.thecatapi.com/images/bon.jpg', width: 640, height: 463}
  length: 1
  > [[Prototype]]: Array(0)
```

## 결과 비교

- 동기식 코드(python)는 위에서부터 순서대로 처리가 되기 때문에 첫번째 print가 출력되고 이미지를 가져오는 처리를 기다렸다가 다음 print가 출력

- 비동기식 코드(JavaScript)는 바로 처리가 가능한 작업(console.log)은 바로 처리하고, 오래 걸리는 작업인 이미지를 요청하고 가져오는 일은 요청을 보내 놓고 기다리지 않고 다음 코드로 진행 후 완료가 된 시점에 결과 출력이 진행됨

> ### 고양이 사진 가져오기 완성

- 버튼을 누르면 고양이 이미지를 요청하고

  요청이 처리되어 응답이 오면 처리된 response에 있는 url을 img 태그에 넣어 보여주기

```html
<body>
  <button>야옹아 이리온</button>

  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
    console.log('고양이는 야옹')
    const catImageSearchURL = 'https://api.thecatapi.com/v1/images/search'
    const btn = document.querySelector('button')

    btn.addEventListener('click', function () {
      // 버튼을 누르면 비동기 요청을 보냄
      axios.get(catImageSearchURL)
        // 응답이 오면 처리하기
        .then((response) => {
          // img 태그에 url 넣기
          imgEl = document.createElement('img')
          imgEl.setAttribute('src', response.data[0].url)
          document.body.appendChild(imgEl)
        })
        .catch((error) => {
          console.log('실패했다옹')
        })
    })
    console.log('야옹야옹')
  </script>
</body>
```

---

## 정리

- axios는 비동기로 데이터 통신을 가능하게 하는 라이브러리

- 같은 방식으로 우리가 배운 Django REST API로 요청을 보내서 데이터를 받아온 후 처리할 수 있음