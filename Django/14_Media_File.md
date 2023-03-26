## Media Files

> ### ImageField()

- 이미지 업로드에 사용하는 모델 필드

- FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능

- 더해서 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사

- ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성되며, max_length 인자를 사용하여 최대 길이를 변경할 수 있음

> ### FileField()

- `FileField(upload_to='', storage=None, max_length=100, **options)

- 파일 업로드에 사용하는 모델 필드

- 2개의 선택 인자를 가지고 있음(`upload_to`, `storage`)

---

### MEDIA_ROOT

- Default: `''` (Empty string)

- 사용자가 업로드 한 파일(미디어 파일)들을 보관할 디렉토리의 절대 경로

- Django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음

  - 데이터베이스에 저장되는 것은 '파일 경로'

- MEDIA_ROOT는 STATIC_ROOT와 반드시 다른 경로로 지정해야 함

### MEDIA_URL

- Default: `''` (Empty string)

- MEDIA_ROOT에서 제공되는 미디어파일을 처리하는 URL

- 업로드 된 파일의 주소(URL)를 만들어 주는 역할

  - 웹 서버 사용자가 사용하는 public URL

- 비어있지 않은 값으로 설정한다면 반드시 slash(`/`)로 끝나야 함

- MEDIA_URL은 STATIC_URL과 반드시 다른 경로로 지정해야 함

---

## Model field option

> blank

- default: False

- True인 경우 필드를 비워둘 수 있음

  - 이럴 경우 DB에는 `''` (빈 문자열)이 저장됨

- 유효성 검사에 사용됨(`is_valid`)

  - "Validation-related"

  - 필드에 `blank=True`가 있으면 form 유효성 검사에서 빈 값을 입력할 수 있음

> null

- default: False

- True인 경우 Django는 빈 값을 DB에 NULL로 저장함

  - "Database-related"

- CharField, TextField와 같은 문자열 기반 필드에는 null 옵션 사용을 피해야 함

  - 문자열 기반 필드에 `null=True`로 설정 시 데이터 없음에 대한 표현에 빈 문자열과 NULL 2가지 모두 가능하게 됨

  - Django는 문자열 기반 필드에 빈 문자열을 사용하는 것이 규칙

