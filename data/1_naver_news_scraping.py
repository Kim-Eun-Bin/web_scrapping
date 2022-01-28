import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def print_news_info(section):
    url_dict = {'정치': 100, '경제': 101, '사회': 102, '생활/문화': 103, '세계': 104, 'IT/과학': 105}
    code = url_dict.get(section)
    if code:
        url = f'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1={code}'
        print(url)

    req_header_dict = {
        # request header : browser information
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
    }
    res = requests.get(url, headers=req_header_dict)
    print(res.status_code, res.ok)
    print(type(res))
    print('res header', res.headers)
    print('req header', res.request.headers)

    if res.ok:
        # html file
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        # a > href attribute -> include read.naver
        a_list = soup.select("a[href*='read.naver']")
        print(len(a_list))
        for a in a_list:
            title = a.text.strip()
            news_link = urljoin(url, a['href'])
            print(title, news_link)