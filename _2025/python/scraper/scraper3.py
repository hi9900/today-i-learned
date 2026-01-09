import requests
from bs4 import BeautifulSoup
"""
동적 웹사이트에 접근: playwright
$ pip install playwright beautifulsoup4 requests
$ playwright install

playwright로 열린 브라우저는 확인 불가 - headless mode
"""
from playwright.sync_api import sync_playwright

p = sync_playwright().start()
# 브라우저 열기
# `headless=False` 브라우저를 보이게 하고 작동이 종료되면 꺼짐 
browser = p.chromium.launch(headless=False)
# 새 탭 생성
page = browser.new_page()
# 페이지 이동
page.goto("https://google.com")
# 스크린샷
page.screenshot(path="screenshot.png")