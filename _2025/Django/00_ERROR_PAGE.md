### Page not found

![](00_ERROR_PAGE_assets/c01a1a8811475e28435050c96c737450004a2e83.png)

- 없는 경로로 요청이 들어왔을 때

---

### TemplateDoesNotExist

![](00_ERROR_PAGE_assets/52c8af1a3faafc028696ae0e111a96d490ad9908.png)

- render 인자 경로에 `애플리캐이션이름/`을 안 넣음
- 주석처리된 `return`이 정답

---

### ValueError

![](00_ERROR_PAGE_assets/bc15a533f231ec723cff01d09f2b4f4a4027b0ad.png)

![](00_ERROR_PAGE_assets/dbda177752d86f88f069aa991a1d58ff6ec5329d.png)

- POST 요청에서 pass라서 none을 반환

---

### UnboundLocalError

![](00_ERROR_PAGE_assets/e5433d082d39293b8455c902c9f4bb2a4facf53b.png)

![](00_ERROR_PAGE_assets/bc1156f639d36ce1094910751b4ecb80dc3915b8.png)

- `form` 변수가 정의되지 않음

---

### NoReverseMatch

![](00_ERROR_PAGE_assets/2023-03-21-22-16-44-image.png)

- url 태그에 app_name 지정 확인:

- urls.py에 app_name을 지정한 경우 url 태그: `{% url 'app_name:url_name' %}`

---

### 
