# Django shortcuts functions

`django.shortcuts` 패키지는 개발에 도움될 수 있는 여러 함수와 클래스를 제공

- 제공되는 shortcuts 목록

  render(), redirect(), get_object_or_404(), get_list_or_404()

> ### get_object_or_404()

  - 모델 manager objects에서 `get()`을 호출하지만, 

    해당 객체가 없을 땐 기존 `DoesNotExist` 예외 대신 `Http404`를 raise 함

  - 코드 변경

  ```python
  # articles/views.py

  from django.shortcuts import get_object_or_404

  article = Article.objects.get(pk=article_pk)
  comment = Comment.objects.get(pk=comment_pk)

  # 위 코드를 모두 다음과 같이 변경
  article = get_object_or_404(Article, pk=article_pk)
  comment = get_object_or_404(Comment, pk=comment_pk)
  ```

> ### get_list_or_404()

  - 모델 manager objects에서 `filter()`의 결과를 반환하고

    해당 객체목록이 없을 땐 `Http404`를 raise 함

  - 존재하지 않는 게시글 조회 시 이전에는 500 상태코드를 응답했지만, 수정 후 404 상태코드를 응답

    - "서버에 오류가 발생하여 요청을 수행할 수 없다(500)"라는 원인이 정확하지 않은 에러를 전달하기 보다는, 서버가 적절한 예외 처리를 하고 클라이언트에게 올바른 에러를 전달 하는 것이 중요

  - 코드 변경

  ```python
  # articles/views.py

  from django.shortcuts import get_object_or_404

  articles = Article.objects.all()
  comments = Comment.objects.all()

  # 위 코드를 모두 다음과 같이 변경
  articles = get_list_or_404(Article)
  comments = get_list_or_404(Comment)
  ```

