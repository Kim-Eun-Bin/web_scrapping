import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.melon.com/chart/index.htm'
req_header_dict = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

res = requests.get(url, headers=req_header_dict)
print(res.status_code)

if res.ok:
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    print(len(soup.select("div#tb_list tr a[href*='playSong']")))
    a_tags = soup.select("div#tb_list tr a[href*='playSong']")
    for idx, a_tag in enumerate(a_tags, 1):
        song_title = a_tag.text
        href_value = a_tag['href']
        print(href_value)
        # print(idx, song_title)
