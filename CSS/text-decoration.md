# text-decoration

- 텍스트에 장식을 추가한다.

- text-decoration-line, text-decoration-style, text-decoration-color, text-decoration-thickness의 단축속성

## 특징

- text-decoration은 모든 자손 텍스트 요소에 걸쳐서 적용된다. 따라서, 자식 요소에서는 부모가 적용한 데코레이션을 제거할 수 없다.

## 초기값

- text-decoration-color: currentcolor

- text-decoration-style: solid

- text-decoration-line: none

## 속성 별 값

### color

선의 색상을 지정하여 사용한다.

### style

`solid` 한 줄을 그린다.

`double` 이중선을 그린다.

`dotted` 점선을 그린다.

`dashed` 파선을 그린다.

`wavy` 물결모양의 선을 그린다.

### line

`none` 줄을 생성하지 않는다.

`underline` 텍스트 아래에 줄을 생성한다.

`overline` 택스트 위에 줄을 생성한다.

`line-through` 텍스트 중앙을 통과하는 줄을 생성한다.

## 예제

<p class="codepen" data-height="300" data-default-tab="html,result" data-slug-hash="poYGaeL" data-user="lbdasdbt-the-selector" style="height: 300px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;">
  <span>See the Pen <a href="https://codepen.io/lbdasdbt-the-selector/pen/poYGaeL">
  Text decoration</a> by hi (<a href="https://codepen.io/lbdasdbt-the-selector">@lbdasdbt-the-selector</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://cpwebassets.codepen.io/assets/embed/ei.js"></script>
