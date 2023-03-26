# Django ModelForm

- Form Class는 Model이랑 중복되는 부분이 많음

  - 이미 Model Class 필드에 대한 정보를 작성했는데, Form Class에 필드를 재정의 해야 했음

- ModelForm을 사용하면 더 쉽게 Form을 작성할 수 있음

## ModelForm Class

- Model을 통해 Form Class를 만들 수 있는 helper class

> ### ModelForm 선언

- forms 라이브러리에서 파생된 ModelForm 클래스를 상속받음

- 정의한 ModelForm 클래스 안에 Meta 클래스를 선언

- 어떠한 모델을 기반으로 form을 작성할 것인지에 대한 정보를 Meta 클래스에 지정

> ### ModelForm에서의 Meta Class

- ModelForm의 정보를 작성하는 곳

- ModelForm을 사용할 경우 참조할 모델이 있어야 하는데, Meta class의 model 속성이 이를 구성함

  - 참조하는 모델에 정위된 field 정보를 Form에 적용함

- `fields` 속성에 `__all__`를 사용하여 모델의 모든 필드를 포함할 수 있음

- 또는 `exclude` 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수 있음

- fields와 exclude를 함께 작성해도 되나 권장하지 않음

```python
class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    # fields = '__all__'
    exclude = ('title',)
```

---

## Form과 ModelForm

- 뭐가 더 좋은 것이 아니라 각자 역할이 다른 것

- Form

  - 사용자의 입력을 필요로 하며 직접 입력 데이터가 DB 저장에 사용되지 않거나 일부 데이터만 사용될 때

  - ex. 로그인: 사용자의 데이터를 받아 인증 과정에서만 사용 후 별도로 DB에 저장하지 않음

- ModelForm

  - 사용자의 입력을 필요로 하며 입력을 받은 것 그대로 DB 필드에 맞춰 저장할 때

  - 데이터 유효성 검사가 끝나면 데이터를 각각 어떤 레코드에 맵핑해야 할 지 이미 알고있기 때문에 곧바로 `save()` 호출이 가능

---