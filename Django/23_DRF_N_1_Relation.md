# Django REST framework - N:1 Relation

N:1 관계에서의 모델 data를 Serialization하여 JSON으로 변환

> ### 사전 준비

- Comment 모델 작성 및 데이터베이스 초기화

```python
# articles/models.py

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

- Migration 진행

- 준비된 fixtures 데이터 load

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py loaddata articles.json comments.json
```

|             | GET     | POST | PUT     | DELETE  |
| ----------- | :-------: | :----: | :-------: | :-------: |
| comments/   | 전체 댓글 조회 |  |  |  |
| comments/1/ | 1번 댓글 조회 |  | 1번 댓글 수정 | 1번 댓글 삭제 |
| comments/1/comments/ |  | 1번 게시글에 댓글 생성 |  |  |

### GET - List

- 댓글 데이터 목록 조회

```python
# articles/serializers.py

from .models import Article, Comment

class CommentSerializer(serizalizers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'

# articles/urls.py

urlpatterns = [
	...,
	path('comments/', views.comment_list),
]

# articles/views.py

from .models import Article, Comment
from .serializers import ..., CommentSerializer


@api_view(['GET'])
def comment_list(request):
	comments = Comment.object.all()
	serializer = CommentSerializer(comments, many=True)
	return Response(serializer.data)
```

### GET - Detail

- 단일 댓글 데이터 조회

- 같은 serializer 사용

```python
# articles/urls.py

urlpatterns = [
	...,
	path('comments/<int:comment_pk>/', views.comment_detail),
]

# articles/views.py

@api_view(['GET'])
def comment_detail(request, comment_pk):
	comment = Comment.objects.get(pk=comment_pk)
	if request.method == 'GET':
		serializer = CommentSerializer(comment)
		return Response(serializer.data)
```

### POST

- 단일 댓글 데이터 생성

> ### Passing Additional attribuets to save()

- `save()` 메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음

- `CommentSerializer`를 통해 Serialize되는 과정에서 Parameter로 넘어온 `article_pk`에 해당하는 article 객체를 추가적인 데이터를 넘겨 저장

```python
# articles/urls.py

urlpatterns = [
	...,
	path('articles/<int:article_pk>/comments/', views.comment_create),
]

# articles/views.py

@api_view(['POST'])
def comment_create(request, article_pk):
	article = Article.objects.get(pk=article_pk)
	serializer = CommentSerializer(data=request.data)
	if serializer.is_valid(raize_exception=True):
		serializer.save(article=article)
		return Response(serializer.data, status=status.HTTP_201_CREATED)
```

- 에러: CommentSerializer에서 article field 데이터 또한 사용자로부터 입력받도록 설정되어 있기 때문에

	- 읽기 전용 필드로 설정 필요

> ### 읽기 전용 필드 설정

- `read_only_fields`를 사용해 외래 키 필드를 '읽기 전용 필드'로 설정

- 읽기 전용 필드는 데이터를 전송하는 시점에 '해당 필드를 유효성 검사에서 제외시키고 데이터 조회 시에는 출력'하도록 함

```python
# articles/serializers.py

class CommentSerializer(serizalizers.ModelSerializer):
	class Meta:
		model = Comment
		fields = '__all__'
		read_only_fields = ('articles', )
```

### DELETE & PUT

- 댓글 삭제 및 수정

- article 정보가 이미 있기 때문에 save()에 데이터를 넘기지 않아도 됨

```python
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
	...
	elif request.method == 'DELETE':
		comment.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	elif request.method == 'PUT':
		serializer = CommentSerializer(comment, data=request.data)
		if serializer.is_valid(raise_exception=True)
			serializer.save()
			return Response(serializer.data)
```