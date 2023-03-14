# CSS 원칙

## 1. 모든 요소는 네모(박스모델)이고,<br> 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다. (좌측 상단에 배치)

---

 # CSS Box model

 - 모든 HTML 요소는 box 형태로 되어있음

 - 하나의 박스는 네 부분(영역)으로 이루어짐

    - `content`: 글이나 이미지 등 요소의 실제 내용

    - `padding`: 테두리 안쪽의 내부 여백<br> 
    요소에 적용된 배경색과 이미지는 `padding` 까지 적용됨

    - `border`: 테두리 영역

    - `margin`: 테두리 바깥의 외부 여백<br>
    배경색을 지정할 수 있음
  
> ## Box model 구성

- `margin`, `padding`:<br>
 상하좌우 여백을 각각 지정 하거나 shorthand를 통해 표현

```css
  .margin{ 
    // margin or padding
    margin-top: 10px;
    margin-right: 20px;
    margin-bottom: 30px;
    margin-left: 40px;
  }

  // margin, padding-shorthand
  .margin-1{
    margin: 10px;
    // 상하좌우
  }

  .margin-2{
    margin: 10px 20px;
    // 상하, 좌우
  }

  .margin-3{
    margin: 10px 20px 30px;
    // 상, 좌우, 하
  }

  .margin-4{
    margin: 10px 20px 30px 40px;
    // 상, 우, 하, 좌: 시계방향
  }
```

- `border`:<br>
테두리 굵기, 스타일, 색 등을 지정

```css
.border{
  border-width: 2px;
  border-style: dashed;
  border-color: black;
}

// border-shorthand
.border{
  border: 2px dashed black;
}
```
---

## Box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box

  - padding을 제외한 순수 contents 영역만을 box로 지정

- 하지만, 일반적으로 영역을 볼 때 border까지의 너비를 지정한 크기로 보는 것을 원함

  - box-sizing을 border-box로 설정

  ```css
  .box{
    box-sizing: border-box;
  }
  ```
