# Retrieving the data(Server)

- 서버는 클라이언트로 받은 key-value쌍의 목록과 같은 데이터를 받게 됨

## request 객체

- 모든 요청 데이터는 view 함수의 첫번째 인자 request에 들어있다.

> print 출력을 통해 살펴보기

```python
def catch(request):
    print(request) 
    # <MSGIRequest: GET '/catch/?message=%...'>
    print(type(request))
    # <class 'django.core.handlers.wsgi.WSGIRequest'>
    print(request.GET)
    # <QueryDict: {'message': ['데이터']}>
    print(request.GET.get('message'))
    # '데이터'
    return render(request, 'catch.html')
```

---

## Request and Responce objects

요청과 응답 객체 흐름

1. 페이지가 요청되면 Django는 요청에 대한 메타데이터를 포함하는 HttpRequest object를 생성

2. 해당하는 적절한 view 함수를 로드하고 HttpRequest를 첫번째 인자로 전달

3. view 함수는 HttpResponse object를 반환