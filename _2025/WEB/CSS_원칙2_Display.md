# CSS 원칙

### 1. 모든 요소는 네모(박스모델)이고, 좌측 상단에 배치

## 2. display에 따라 크기와 배치가 달라진다.

---

# CSS Display

## 대표적으로 활용되는 display

### `display: block`

- 줄바꿈이 일어나는 요소 (다른 elem를 밀어낸다)

- 화면크기 전체의 가로폭을 차지한다.

  - block의 기본 너비는 가질 수 있는 너비의 100%

  - 너비를 가질 수 없다면 자동으로 부여되는 margin

- 블록 레벨요소 안에 인라인 레벨요소가 들어갈 수 있다.

> 대표적인 블록 레벨요소

  - div, ul, ol, li, p, hr, form 등

  - https://developer.mozilla.org/ko/docs/Web/HTML/Block-level_elements

### `display: inline`

- 줄바꿈이 일어나지 않는 행의 일부 요소

- content를 마크업 하고 있는 만큼만 가로폭을 차지한다.

  - inline의 기본 너비는 컨텐츠 영역만큼

- width, height, margin-top, margin-bottom을 지정할 수 없다.

  - inline이 정렬하는 것이 아닌 block이 정렬

- 상하여백은 `line-height`로 지정한다.

> 대표적인 인라인 레벨요소

  - span, a, img, input, label, b, em, i, strong 등

  - https://developer.mozilla.org/ko/docs/Web/HTML/Inline_elements

---

## 속성에 따른 수평정렬

```css
// block
.box-block{
  margin-right: auto;
  margin-left: auto;
}

// inline
// inline 요소를 감싼 block 요소에서 정렬
.box-inline{
  text-align: center;
}
```

## `display`

### `display: inline-block`

- block과 inline 레벨요소의 특징을 모두 가짐

- inline처럼 한 줄에 표시 가능하고, block처럼 width, height, margin 속성을 모두 지정할 수 있음

### `display: none`

- 해당 요소를 화면에 표시하지 않고 공간조차 부여되지 않음

- `visibility: hidden`은 해당 요소가 공간은 차지하나, 화면에 표시만 하지 않음

- 다양한 display 속성: https://developer.mozilla.org/ko/docs/Web/CSS/display