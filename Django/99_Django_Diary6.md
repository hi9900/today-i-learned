## Django Form Class

> ### Form Class 선언

```python
# articles/forms.py
from django import forms

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)
```

- CREATE 수정

```python
# articles/views.py
from .forms import ArticleForm
def create(request):
    ...
    else:
        form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html', context)
```
```django
<!-- articles/create.html -->
...
<form action="{% url 'articles:create' %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="작성">
</form>
...
```

---

## Django ModelForm

```python
# articles/form.py
from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
```

### ModelForm 구현하기

> ### CREATE

- 유효성 검사를 통과하면, 데이터 저장 후 상세페이지로 리다이렉트

- 통과하지 못하면, 작성페이지로 리다이렉트

```python
# articles/views.py
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

- `is_valid()` method

  - 유효성 검사를 실행하고, 데이터가 유효한 지 여부를 boolean으로 반환

  - 데이터 유효성 검사를 보장하기 위한 많은 테스트에 대해 Django는 `is_valid()`를 제공하여 개발자의 편의를 도움

- `save()` method

  - form 인스턴스에 바인딩 된 데이터를 통해 데이터베이스 객체를 만들고 저장

  - ModelForm 하위 클래스는 키워드 인자 `instance` 여부를 통해 생성할 지, 수정할 지를 결정함

    - 제공되지 않은 경우 지정된 모델의 새 인스턴스를 만듦(CREATE)

    - 제공되면 해당 인스턴스를 수정(UPDATE)

> ### UPDATE

- ModelForm의 인자 instance는 수정 대상이 되는 객체(기존 객체)를 지정

1. `request.POST`: 사용자가 form을 통해 전송한 데이터(새로운 데이터)

2. `instance`: 수정이 되는 대상

```python
# articles/view.py
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,}
    return render(request, 'articles/update.html', context)
```

## Widgets 활용하기

> ### 위젯을 작성하는 2가지 방법

- 2번 작성 방식을 권장함

```python
# articles/forms.py

# 1
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
          'title': forms.TextInput(attrs={
            'class': 'title',
            'placeholder': 'Enter the title',
            'maxlength': 10,
          })
        }

# 2
class ArticleForm(forms.ModelForm):
    title = forms.CharField{
      label='제목',
       widget=forms.TextInput(
        attrs={
          'class': 'my-title',
          'placeholder': 'Enter the title',
        }
       )
    }
    class Meta:
        model = Article
        fields = '__all__'
```