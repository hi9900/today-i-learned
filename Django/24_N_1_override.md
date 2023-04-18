# 역참조 데이터 조회

## 특정 게시글에 작성된 댓글 목록 출력하기

### 기존 필드 override

  - 게시글 조회 시 해당 게시글의 댓글 목록까지 함께 출력

  - Serializer는 기존 필드를 override 하거나 추가적인 필드를 구성할 수 있음

### 1. PrimaryKeyRelatedField()

  - models.py에서 `related_name`을 통해 이름 변경 가능

  ```python
  # articles/models.py

  class Comment(models.Model):
      article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
      ...
  ```

  - 역참조 시 생성되는 `comment_set`을 override 할 수 있음

  ```python
  # articles/serializers.py

  class ArticleSerializer(serializser.ModelSerializer):
      comment_set = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
      ...
  ```

### 2. Nested relationships

  - 모델 관계 상으로 참조 된 대상은 참조하는 대상의 표현에 포함되거나 중첩(nested)될 수 있음

  - 이러한 중첩된 관계는 serializers를 필드로 사용하여 표현할 수 있음

  - 두 클래스의 상/하 위치를 변경해야 함

  ```python
  # articles/serializers.py

  class CommentSerializer(serializers.ModelSerializer):
      ...

  class ArticleSerializer(serializser.ModelSerializer):
      comment_set = CommentSerializer(many=True, read_only=True)
      ...
  ```

## 특정 게시글에 작성된 댓글의 개수 출력하기

- 새로운 필드 추가: Article Detail

  게시글 조회 시 해당 게시글의 댓글 갯수까지 함께 출력

- soruce

  - serializers field's argument

  - 필드를 채우는 데 상요할 속성의 이름

  - 점 표기법(dotted notation)을 사용하여 속성을 탐색할 수 있음

```python
class ArticleSerializer(serializser.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    ...
```

> ### 읽기 전용 필드 지정 이슈

- 특정 필드를 override 혹은 추가한 경우 read_only_fields가 동작하지 않으니 주의

- 사용 불가 예시

  ```python
  class ArticleSerializer(serializser.ModelSerializer):
      comment_set = CommentSerializer(many=True)
      comment_count = serializers.IntegerField(source='comment_set.count')
      class Meta:
          ...
          read_only_fields = ('comment_set', 'comment_count', )
  ```