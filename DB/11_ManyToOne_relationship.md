# N:1

Comment(N) - Article(1)

Comment 모델과 Article 모델 간 관계 설정

0개 이상의 댓글은 1개의 게시글에 작성될 수 있음

## 모델 관계 설정

게시판의 게시글과 N:1 관계를 나타낼 수 있는 댓글 구현

N:1 관계에서 댓글을 담당할 Comment 모델은 N, Article 모델은 1이 될 것

---

## Django Relationship fields

### 1. OneToOneField()

### 2. ForeignKey()

### 3. ManyToManyField()

> ### ForeignKey

  `ForeignKey(to, on_delete, **options)`

  - A many-to-one relationship을 담당하는 Django의 모델 필드 클래스

  - Django 모델에서 관계형 데이터베이스의 외래 키 속성을 담당

  - 2개의 필수 위치 인자가 필요함

    1. 참조하는 model class

    2. on_delete 옵션

> ### ForeignKey arguments - on_delete

  - 외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할 지를 정의

  - 데이터 무결성을 위해 매우 중요한 설정

  - `on_delete` 옵션 값:

    CASCADE: 부모 객체(참조된 객체)가 삭제되었을 때, 이를 참조하는 객체도 삭제

    PROTECT, SET_NULL, SET_DEFAULT, ... 등 여러 옵션 값들 존재

---

## Related manager

N:1 혹은 M:N 관계에서 사용 가능한 문맥(context)

Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 역참조할 때 사용할 수 있는 manager를 생성

  related manager를 통해 queryset api를 사용할 수 있음

### 역참조

나를 참조하는 테이블(나를 외래키로 지정한)을 참조하는 것

즉, 본인을 외래키로 참조 중인 다른 테이블에 접근하는 것

N:1 관계에서는 1이 N을 참조하는 상황

  외래 키를 가지지 않은 1이 외래 키를 가진 N을 참조

`article.comment_set.method()`

  - Article 모델이 Comment 모델을 참조(역참조)할 때 사용하는 매니저

  - `article.comment` 형식으로는 댓글 객체를 참조할 수 없음

    실제로 Article 클래스에는 Comment와 어떠한 관계도 작성되어 있지 않음

  - 대신 django가 역참조 할 수 있는 `comment_set` manager를 자동으로 생성해 `article.comment_set` 형태로 댓글 객체를 참조할 수 있음

  - N:1 관계에서 생성되는 Related manager의 이름은 참조하는 `모델명_set`이름 규칙으로 만들어짐

  - 반면 참조 상황(Comment -> Article)에서는 실제 ForeignKey 클래스로 작성한 인스턴스가 Comment 클래스의 클래스 변수이기 때문에 `comment.article` 형태로 작성 가능

> ### ForeignKey artuments - related_name

  - ForeignKey 클래스의 선택 옵션

  - 역참조 시 사용하는 매니저 이름(model_set manager)을 변경할 수 있음

  - 선택 옵션이지만 상황에 따라 반드시 작성해야 하는 경우가 생기기도 함

  - 작성 후, migration 과정 필요

  - 변경하면 기존 `article.comment_set`은 `article.[related_name]`로 대체됨

---

> ### Comment 모델 정의

```python
# article/models.py

class Comment(models.Model):
    article = models.ForeignKey(Ariticle, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_langth=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
      return self.content
```

  - 외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계없이 필드의 마지막에 작성됨

  - ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장

    - ForeignKey 모델 필드로 인해 작성된 컬럼의 이름은 `article_id`: `[인스턴스]_id`

    - 명시적인 모델 관계 파악을 위해 참조하는 클래스 이름의 소문자로 작성하는 것을 권장

---

> ### 댓글 생성 연습

```bash
$ python manage.py shell_plus
```

1. 댓글 생성

```shell
# Comment 클래스의 인스턴스 comment 생성
comment = Comment()

# 인스턴스 변수 저장
comment.content = 'first comment'

# DB에 댓글 저장
comment.save()

# 에러 발생: 
django.db.urils.IntegrityError: NOT NULL constraint failed: articles_comment.article_id
# articles_comment 테이블의 ForeignKeyField, article_id 값이 저장 시 누락되어서

# 게시글 생성 및 확인
article = Article.object.create(title='title', content='content')
article
=> <Article: title>

# 외래키 데이터 입력: 
# article 객체 자체를 넣을 수 있음
comment.article = article
# comment.article_id = article.pk
# 또는 pk 값을 직접 외래 키 컬럼에 넣을 수 있지만 권장하지 않음

# DB에 댓글 저장 및 확인
comment.save()
comment
=> <Comment: first comment>
```

2. 댓글 속성값 확인

```shell
comment.pk
=> 1

comment.content
=> 'first comment'

# 클래스 변수명인 article로 조회 시 해당 참조하는 게시물 객체 조회
# 존재하지 않는 필드는 사용 불가
comment.article
=> <Article: title>
comment.article_id
=> 1
```

3. comment 인스턴스를 통한 article 값 접근

```shell
# 1번 댓글이 작성된 게시물의 pk 조회
comment.article.pk
=> 1

# 1번 댓글이 작성된 게시물의 content 조회
comment.article.content
=> 'content'
```
---

> ### Related manager 연습

```shell
# 1번 게시글 조회
article = Article.object.get(pk=1)
# 1번 게시글에 작성된 모든 댓글 조회(역참조)
# article.comment_set.all()
article.comments.all()

# 1번 게시글에 작성된 모든 댓글 출력
# comments = article.comment_set.all()
comments = article.comments.all()
for comment in comments:
    print(comment.content)
```