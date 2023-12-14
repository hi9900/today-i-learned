# 정규 표현식(Regex, Regexp: Regular Expression)

#### 개요

알고 있으면 쓸모 있는 정규 표현식에 대해서 알아보려 한다. 항상 구글링해 표현식을 찾아왔기에 정규식 문법에 대해서는 잘 알지 못했다. 이번 기회에 정규표현식의 문법에 대해 이해하고, 문자열을 다뤄보겠다.

프로그래머스의 [정규표현식](https://school.programmers.co.kr/learn/courses/11/11-%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D) 강의를 보고 학습했다. 강의는 파이썬 코드를 기반으로 설명하고 있으며, 마지막에 언어 별로 정규 표현식을 사용하는 방법을 알려준다.

간단한 정규 표현식 문법과 전화번호를 찾아 출력하는 방법을 알아보자

## 0. 정규 표현식

> 정규표현식은 문자열에서 특정 패턴을 만족하는 부분을 찾아낼 때 사용한다.

- 파이썬에서 `r`은 "Raw String"의 약어로, 백슬래시를 표현하기 위해 사용된다.

  백슬래시를 사용하지 않는 정규표현식이라면 r의 유무에 상관없이 동일한 결과를 얻을 수 있다.

<details>
<summary>전화번호 정규표현식 코드</summary>

```python
# 전화번호를 찾는 정규표현식
regex = r'0\d{1,2}[ -]?\d{3,4}[ -]?\d{3,4}'

# 전화번호를 찾을 주소록
search_target = '''Luke Skywarker 02-123-4567 luke@daum.net
다스베이더 070-9999-9999 darth_vader@gmail.com
princess leia 010 2454 3457 leia@gmail.com'''

# 정규표현식과 일치하는 부분을 모두 찾아주는 파이썬 코드
import re
result = re.findall(regex, search_target)
print("\n".join(result))

'''
02-123-4567
070-9999-9999
010 2454 3457
'''
```

</details>

## 1. 대표 문자(Meta sequence)

1. 숫자 대표문자

- `\d`에서 d는 digit를 뜻하며 숫자를 대표하는 정규표현식이다.

2. 글자 대표문자

- `\w`는 글자를 대표하는 정규표현식이다.

  - 글자는 문자(a, b, c, 가, 나, 다)와 숫자를 포함한다.

  - 특수문자는 포함하지 않지만 언더스코어(`_`)는 포함된다.

## 2. 횟수(Quantifier)

1. 하나 이상

- `+`는 "하나 혹은 그 이상 연결된"이라는 뜻이다.

- `\d+`는 "연결된 숫자"를 의미한다.

2. 0개 이상

- `*`는 "0개 이상"이라는 뜻이다.

- 자연수는 `[1-9]\d*`으로 표현된다.

  - `[1-9]`: 1~9 사이의 숫자

  - `[1-9]\d`: 1~9 중 하나의 숫자로 시작하고, 둘째 자리는 아무 숫자 하나

  - `[1-9]\d*`: 1~9 중 하나의 숫자로 시작하고, 그 뒤에는 연속된 숫자가 0개 이상

3. 있거나 없거나

- `?`는 "있거나 없거나"라는 뜻이다.

- `-?`는 "`-`가 있거나 없다"를 의미한다.

  1. 전화번호는 `-`를 포함하거나, 포함하지 않을 수 있다.

  - 예를 들어 `021234567`, `02-123-4567`은 모두 유효한 전화번호다.

  - `\d+-?\d+-?\d+-?`는 연속되는 숫자 사이에 `-`가 있거나 없는 문자열을 표현한다.

  2. 공백이 포함된 `02 1234 5678`도 유효한 전화번호이다.

  - 따라서 `\d+[- ]?\d+[- ]?\d+[- ]?`는 연속되는 숫자 사이에 `-` 또는 공백(` `)이 있거나 없는 문자열을 표현한다.

  - `[- ]?`: `-`또는 공백(` `)이 있거나 없다

4. n번

- `{n}`은 "n번 반복한다"는 뜻이다.

- `\d{n}`: 숫자가 연속 n번인 문자열

5. n ~ m 번

- `{n,m}`은 "n부터 m까지 반복한다"는 뜻이다. 단, {n,m} 사이에는 공백이 들어갈 수 없다.

  - 예를 들어 `\w{2,3}`은 "문자가 2 ~ 3번 나온다"는 뜻이다.

- 전화번호의 자릿수는 처음 `2~3자리`, 가운데 `3~4자리`, 마지막 `4자리`로 구성되어 있다.

  - 따라서 전화번호는 `\d{2,3}[- ]?\d{3,4}[- ]?\d{4}`로 표현할 수 있다.

## 3. 고르기

1. 몇 개 중에 고르기

- 정규표현식에서 대괄호(`[]`) 안에 글자를 넣으면 해당 글자를 모두 선택할 수 있다.

  - 예를 들어 알파벳 중 소문자 모음(a, e, i, o, u)만 고르려면 `[aeiou]`로 표현한다.

2. 범위에서 고르기

- 소문자 알파벳을 모두 고르고 싶을 때, 대괄호 안에 모든 소문자를 나열하는 대신 간단히 `[a-z]`라고 표현한다.

- `[a-z]+`는 연속된 영어 소문자를 표현한다.

  - `[a-z]`: 소문자(a부터 z까지의 모든 글자 )

  - `+`: 하나 이상

3. 한글 고르기

- 한글의 첫번쨰 글자는 `가`이고 마지막은 `힣`이다. 따라서 한글은 `[가-힣]`으로 표현한다.

  - 단, 이 방식으로는 낱글자(`ㄱ ㄴ ㄷ`이나 `ㅏ ㅑ ㅓ ㅕ`)를 찾을 수 없다.

  - `[가-힣]+`: 연속된 한글 단어를 표현한다.

## 4. 기타 대표문자

- `\s`: 공백 문자(스페이스, 탭, 뉴라인)

- `\S`: 공백 문자를 제외한 문자

- `\D`: 숫자를 제외한 문자

- `\W`: 글자 대표문자를 제외한 글자들(특수문자, 공백 등)

## 5. 다른 프로그래밍 언어의 정규 표현식

1. Java

- Java로 정규 표현식을 다룰 땐 Pattern 클래스와 Matcher 클래스를 이용한다.

- Java에서는 `\` 대신 `\\`를 사용한다.

<details>
<summary>Java 예시 코드</summary>

```java
import java.io.Console;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class MyRegex{
public static void main(String[] args){
String searchTarget = "Luke Skywarker 02-123-4567 luke@daum.net\n다스베이더 070-9999-9999 darth_vader@gmail.com\nprincess leia 010 2454 3457 leia@gmail.com";

        Pattern pattern = Pattern.compile("\\d");       // 정규 표현식
        Matcher matcher = pattern.matcher(searchTarget); // 찾을 문자열
        while(matcher.find()){
            System.out.println(matcher.group(0));
        }
    }

}

```

</details>

2. Javascript

- Javascript로 정규 표현식을 다룰 땐 String class의 match 함수를 이용한다.

- `/`와 `/g`가운데에 정규표현식을 넣는다.

  - g는 global의 약자로, 정규표현식과 일치하는 모든 내용을 찾아오라는 이다..

<details>
<summary>Javascript 예시 코드</summary>

```javascript
var searchTarget =
  "Luke Skywarker 02-123-4567 luke@daum.net\
다스베이더 070-9999-9999 darth_vader@gmail.com\
princess leia 010 2454 3457 leia@gmail.com";

var regex = /\d/g; // 정규 표현식
console.log(searchTarget.match(regex));
```

</details>

3. C# 정규표현식

- C#으로 정규표현식을 다룰 땐 Regex.matches라는 메소드를 이용한다.

- C#에서는 `\` 대신 `\\`를 사용한다.

<details>
<summary>C# 예시 코드</summary>

```C#
using System;
using System.Text.RegularExpressions;

public class RegexTest {
    public static void Main() {
        string regex = "\\d";
        string searchTarget = "Luke Skywarker 02-123-4567 luke@daum.net\n다스베이더 070-9999-9999 darth_vader@gmail.com\nprincess leia 010 2454 3457 leia@gmail.com";

        foreach (Match m in Regex.Matches(searchTarget, regex)){
            Console.WriteLine(m.Value);
        }
    }
}
```

</details>
