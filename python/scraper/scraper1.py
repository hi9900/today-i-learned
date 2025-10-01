import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"

response = requests.get(url)

# response.content -> html 데이터
# beautifulsoup -> html 파싱
soup = BeautifulSoup(response.content, "html.parser")

# find: 첫 번쩨 요소를 반환함
# id가 category-2인 section 태그 찾기
# jobs = soup.find("section", id="category-2")

# class가 jobs인 section 태그 찾기
# class는 예약어이므로 언더바를 붙여 표기(`class_`)
# jobs = soup.find("section", class_="jobs")

# find를 여러번 사용해서 내부 태그를 찾을 수 있다.
# 전체 요소를 찾으려면 `find_all`
# 첫 번째 li와 마지막 li를 제외: 인덱스 슬라이싱
jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

all_jabs = []

for job in jobs:
    title = job.find("span", class_="title").text
    # region = job.find("span", class_="region").text
    company, position, region = job.find_all("span", class_="company")

    # a태그의 href를 찾기 -> a 태그가 없으면 오류가 발생함
    # url = job.find("a")["href"]
    # 오류를 막기 위한 분기처리
    # url = job.find("a")
    # if url:
    #     url = url["href"]

    # div.tooltip 다음의 a 태그 찾기
    url = job.find("div", class_="tooltip").next_sibling["href"]

    job_data = {
        "title": title,
        "company": company.text,
        "position": position.text,
        "region": region.text,
        "url": f"https://weworkremotely.com{url}"
    }

    all_jabs.append(job_data)

print(all_jabs)