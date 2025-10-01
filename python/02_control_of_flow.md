# 02_control_of_flow

# Python 02

## 제어문(Control Statement)

- 순차, 선택, 반복
- 파이썬은 기본적으로 위에서부터 아래로 차례대로 명령을 수행
- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건)하거나,
계속하여 실행(반복)하는 제어가 필요함
- 제어문은 순서도(flowchart)로 표현이 가능

> 코드스타일 가이드
> 
- 코드를 “어떻게 작성할지”에 대한 가이드라인
- 파이썬에서 제안하는 스타일 가이드(강의에서도 사용): [PEP8](https://www.python.org/dev/peps/pep-0008/)
- 각 회사/프로젝트마다 따로 스타일 가이드를 설정하기도 함: [Google Style guide](https://google.github.io/styleguide/pyguide.html) 등

> 들여쓰기(Space Sensitive)
> 
- 문장을 구분할 때, 중괄호 `{}` 대신 들여쓰기(indentation)를 사용
- 들여쓰기를 할 때는 4칸(`space` 4번) 혹은 1탭(`Tab` 1번)을 입력
    - 한 코드 안에서는 반드시 한 종류의 들여쓰기를 사용: 혼용 금지
    - 원칙적으로는 공백(빈칸, space) 사용을 권장 *PEP8 권장사항

## 조건문(Conditional Statement)

- 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용
    
    ```python
    if 조건 == True:
    	# Run this Code block
    	if 중첩 조건문:
    		# 들여쓰기에 유의
    elif 조건2:
    	# 복수 조건문
    else:
    	# Run this Code bloce
    ```
    

### 조건 표현식(Conditional Expression)

- 조건 표현식을 일반적으로 조건에 따라 값을 정할 때 활용
- 삼항 연산자(Ternary Operator)로 부르기도 함
    
    ```python
    # (True인 경우 값) if (조건) else (False인 경우 값)
    
    # ex. 절댓값을 저장하기 위한 코드
    value = num if num >= 0 else -num
    
    # 홀짝을 판별하는 코드
    result = "홀수" if num % 2 else "짝수"
    ```
    

## 반복문

- 특정 코드를 만족할 때까지 같은 동작을 계속 반복하고 싶을 때 사용
- 반복 제어
    - `break`: 반복문을 종료
    - `continue`: continue 이후의 코드블록은 수행하지 않고, 다음 반복을 수행
    - `for-else`: 끝까지 반복문을 실행한 후 else문 실행
        - break를 통해 중간에 종료되는 경우 else문은 실행되지 않음
    - `pass`: 아무것도 하지 않음, 문법적으로 필요하지만 할 일이 없을 때 사용

### while 문

- 조건식이 참인경우 들여쓰기 되어있는 코드블록을 실행
- 코드블록이 모두 실행되고, 다시 조건식을 검사하여 반복적으로 실행
- 무한루프를 하지 않도록 종료조건이 필요
    - 종료 조건에 해당하는 코드를 통해 반복문을 종료시켜야 함

### for 문

- 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)의 요소를 모두 순회
- 반복 가능한 객체를 모두 순회하면 종료하므로 별도의 종료조건이 필요없음
- Iterable
    - 순회할 수 있는 자료형: String, list, dict, tuple, range, set 등
    - 순회형 함수: range, enumerate
    
    > 추가 메서드를 활용한 딕셔너리(Dictionary) 순회
    > 
    > - `keys()`, `values()`, `items()`: (Key, value)의 튜플
    
    > `enumerate()`
    > 
    > - 인덱스와 객체를 쌍으로 담은 열거형(enumerate)객체 반환
    > - (Index, value) 형태의 tuple로 구성된 열거 객체를 반환

## Comprehension

### List Comprehension

- 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

### Dictionary Comprehension

- 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성하는 방법

```python
# code for (변수) in iterable
# code for (변수) in iterable if (조건식)

# ex. 1 ~ 3 세제곱의 결과가 담긴 리스트
# 기존 방법
cubic_lst = []
for number in range(1, 4):
	cubic_lst.append(number ** 3)
#comprehension
cubic_lst = [number ** 3 for number in range(1, 4)]

# dictionary
# {key: value for 변수 in iterable}
# {key: value for 변수 in iterable if 조건식}
```