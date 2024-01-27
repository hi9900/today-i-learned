from requests import get

# https://httpstat.us/xxx http코드를 생성해주는 사이트
websites = (
    "google.com",
    "airbnb.com",
    "twitter.com",
    "facebook.com",
    "tiktok.com",
    "https://httpstat.us/404"
)

results = {}
for website in websites:
    # https:// 로 시작하는 지 확인
    if not website.startswith("https://"):
        website = f"https://{website}"

    response = get(website)
    # airbnb 429 뜨는 것 막기 위해 headers 작성
    # response = get(website, headers = {'User-agent': 'your bot 0.1'})
    print(website, response.status_code)
    if response.status_code == 200:
        results[website] = "OK"
    else:
        results[website] = "FAILED"
    
print(results)
