# Serializer 활용

## 특정 게시물의 모든 댓글 조회

- 댓글 목록 조회 + 댓글 생성

```python
# articles/urls.py

urlpatterns = [
		...,
    # path('comments/', views.comment_list),
		# path('articles/<int:article_pk>/comments/', views.comment_create),
    path('articles/<int:article_pk>/comments/', views.comment_list),
]

# articles/views.py
@api_view(['GET', 'POST'])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'GET':
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
```

## 필드 명 및 필드 수정

- comment_set 대신 "comments" 사용

- 댓글 조회 시 "article id" 삭제

> ### to_representation

- `to_representation(self, instance)`

- 직렬화가 필요한 개체 인스턴스를 가져오고 기본 표현을 반환

- 표현 스타일을 수정하기 위해 재지정

- 반대의 경우 `.to_internal_value()`

```python
# articles/serializer.py

class ArticleListSerializer(serializser.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'comment_set', 'comment_count', )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = rep.pop('comment_set', [])
        return rep


class CommentSerializer(serializers.ModelSerializer):
    model = Comment
    fields = '__all__'
    read_only_fields = ('article', )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.pop('article', None)
        return rep
```

## 상속 이용하기

- 게시글 상세조회 시 작성자 정보도 함께 출력

  목록 조회에서는 변화 없음

```python
# articles/serializer.py

class ArticleListSerializer(serializser.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', )


class ArticleDetailSerializer(ArticleListSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta(ArticleListSerializer.Meta):
        fields = ArticleListSerializer.Meta.fields + ('comment_set', 'comment_count', )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['comments'] = rep.pop('comment_set', [])
        return rep
    

# articles/views.py

@api_view(['GET'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()      
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleDetailSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```
