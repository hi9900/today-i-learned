# Fixtures

Fixtures를 사용해 모델에 초기 데이터를 제공하는 방법

> ### 초기 데이터의 필요성

  - 여러 사람이 협업 시, gitignore 설정으로 인해 DB는 업로드하지 않기 때문에 개발하면서 사용한 데이터는 올라가지 않는다.

  - Django 프로젝트의 앱을 처음 설정할 때 동일하게 준비 된 데이터로 데이터베이스를 미리 채우는 것이 필요한 순간이 있다.

  - Django에서는 fixtures를 사용해 앱에 초기 데이터(initial data)를 제공할 수 있다.

  - 즉, migrations와 fixtures를 사용하여 data와 구조를 공유하게 된다.

## Providing data with fixtures

### fixtures

  - Django가 데이터베이스로 가져오는 방법을 알고 있는 데이터 모음

  - 가져오는 방법?

    Django가 직접 만들기 때문에 데이터베이스 구조에 맞추어 작성되어 있음

### fixtures 생성 및 로드

1. 생성(데이터 추출)

- dumpdata

  - 응용 프로그램과 관련된 데이터베이스의 모든 데이터를 표준 출력으로 출력함

  - 여러 모델을 하나의 json 파일로 만들 수 있음

  > 작성 예시
  `$ python manage.py dumpdata [app_name[.ModelName] app_name[.ModelName] ...] > {filename}.json`

  - articles app의 article 모델에 대한 data를 json 형식으로 저장하기

  - manage.py와 동일한 위치에 data가 담긴 articles.json 파일이 생성됨

  - dumpdata의 출력 결과물은 loaddata의 입력으로 사용됨

  - fixtures 파일은 직접 만드는 것이 아니라 dumpdata를 사용하여 생성하는 것

  ```bash
  $ python manage.py dumpdata --indent 4 articles.article > articles.json
  $ python manage.py dumpdata --indent 4 accounts.user > users.json
  $ python manage.py dumpdata --indent 4 articles.comment > comments.json
  ```

  - 모든 모델을 한번에 dump

  ```bash
  # 3개의 모델을 하나의 json 파일로
  $ python manage.py dumpdata --indent 4 articles.article articles.comment accounts.user > data.json

  # 모든 모델을 하나의 json 파일로
  $ python manage.py dumpdata --indent 4 > data.json
  ```

2. 로드(데이터 입력)

- loaddata

  - fixtures의 내용을 검색하여 데이터베이스로 로드

  > 작성 예시

  `$ python manage.py loaddata data.json`

  - fixtures 기본 경로

    `app_name/fixtures/`

    Django는 설치된 모든 app의 디렉토리에서 fixtures 폴더 이후의 경로로 fixtures 파일을 찾음

  - 해당 위치로 fixture 파일을 이동 후 fixtures load

  ```bash
  $ python manage.py loaddata articles.json users.json comments.json
  ```

  > loaddata를 하는 순서

  - loaddata를 한번에 실행하지 않고 하나씩 실행한다면 모델 관계에 따라 오류가 날 수 있음

    - comment는 article에 대한 key 및 user에 대한 key 필요

    - article은 user에 대한 key 필요

  - 즉, 현재 모델 관계에서는 user -> article -> comment 순으로 data를 넣어야 오류가 발생하지 않음

  > loaddata 시 encoding codec 관련 에러가 발생하는 경우

  - 2가지 방법 중 택 1

  1. dumpdata 시 추가 옵션 작성

    `$ python -Xutf8 manage.py dumpdata ...`

  2. 메모장 활용

    - 메모장으로 json 파일 열기 -> "다른이름으로 저장" -> 인코딩을 UTF8로 저장