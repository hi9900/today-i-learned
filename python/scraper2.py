import requests
from bs4 import BeautifulSoup

all_jabs = []

# 페이지를 스크래핑 해서 all_jobs에 추가하는 함수
def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]
    for job in jobs:
        title = job.find("span", class_="title").text
        company, position, region = job.find_all("span", class_="company")
        url = job.find("div", class_="tooltip").next_sibling["href"]
        job_data = {
            "title": title,
            "company": company.text,
            "position": position.text,
            "region": region.text,
            "url": f"https://weworkremotely.com{url}"
        }
        all_jabs.append(job_data)

# 전체 페이지의 수를 반환하는 함수
def get_pages(url):
    response = requests.get("url")
    soup = BeautifulSoup(response.content, "html.parser")

    # 페이지 버튼의 개수
    return len(soup.find("div", class_="pagination").find_all("span", class_="page"))

total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs?page=1")

for x in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape_page(url)

print(len(all_jabs))