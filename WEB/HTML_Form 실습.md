# HTML 문서 구조화

## Form 활용 실습

```html
<header>
  <a href="https://www.ssafy.com/">
    <img src="ssafy.png" alt="main img" width="300">
  </a>
  <h1>학생 건강 설문</h1>
</header>

<section>
  <form action="#">
    <!-- 이름 -->
    <div>
      <label for="name">이름을 기재해주세요.</label><br>
      <input type="text" id="name" name="name" autofocus>
    </div>
    <hr>
    <!-- 지역 -->
    <div>
      <label for="region">지역을 선택해주세요.</label><br>
      <select name="region" id="region" required>
        <option value="서울">서울</option>
        <option value="대전">대전</option>
        <option value="광주">광주</option>
        <option value="구미">구미</option>
        <option value="부울경">부울경</option>
      </select>
    </div>
    <hr>
    <!-- 체온 -->
    <div>
      <p>오늘의 체온을 선택해주세요.</p>
      <input type="radio" name="body-heat" id="normal" value="normal" checked>
      <label for="normal">37도 미만</label><br>
      <input type="radio" name="body-heat" id="warning" value="warning">
      <label for="warning">37도 이상</label>
    </div>
    <input type="submit" value="제출">
  </form>
</section>

<footer>
  Google 설문지를 통해 비밀번호를 제출하지 마시오.
</footer>
```
---
## 텍스트 요소

`<a></a>`: href속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성

`<img>`: src 속성을 활용하여 이미지 표현

`<br>`: 텍스트 내에 줄바꿈 생성

## 그룹 컨텐츠

`<div></div>`: 의미없는 블록레벨 컨테이너

`<p></p>`: 하나의 문단(paragragh)

`<hr>` 주제를 분리하기 위한 수평선 (A Horizontal Rule)

### `<form></form>`

사용자의 정보(데이터)를 제출하기 위한 영역

- `action`: form을 처리할 서버의 URL

### `<input>`

다양한 타입을 가지는 입력 데이터 유형과 위젯 

- `name`: form control에 적용되는 이름

- `value`: form control에 적용되는 값
  
  > ### `<input> type`
  
- 일반 유형
  
  `text`: 일반 텍스트 입력

  `password`: 입력 시 값이 보이지 않고 문자를 특수기호로 표현
  
  `email`: 이메일 형식이 아닌 경우 form 제출 불가
  
  `number`: min, max, step 속성을 활용하여 숫자 범위 설정 가능
  
  `file`: accept 속성을 활용하여 파일 타입 지정 가능
  
- 항목 중 선택 유형

  `label`로 선택에 대한 내용을 작성하고, 항목으로 선택할 수 있는 `input` 제공

  동일한 범주에 속하는 항목들은 `name`을 통일하고, 선택된 항목의 값은 `value`로 지정
  
  `checkbox`: 다중 선택
  
  `radio`: 단일 선택

- 종합 유형

  `input`요소의 동작은 type에 따라 달라지므로, 각각의 내용 숙지

  https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input

### `<label>`

label을 클릭하여 input자체에 초점을 맞추거나 활성화시킬 수 있음

`<input>`의 id속성, `<label>`의 for속성을 활용하여 상호연관
