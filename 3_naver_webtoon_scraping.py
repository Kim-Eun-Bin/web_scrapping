# naver webtoon image download
# import requests
# import os # for find file path
#
# req_header = {
#     'referer': 'https://comic.naver.com/webtoon/detail?titleId=552960&no=410&weekday=fri'
# }
#
# img_url_list = [
#     'https://image-comic.pstatic.net/webtoon/552960/410/20220113151757_90bb11af8a341a8bf8a8558fb3d3c121_IMAG01_1.jpg',
#     'https://image-comic.pstatic.net/webtoon/552960/410/20220113151757_90bb11af8a341a8bf8a8558fb3d3c121_IMAG01_2.jpg',
#     'https://image-comic.pstatic.net/webtoon/552960/410/20220113151757_90bb11af8a341a8bf8a8558fb3d3c121_IMAG01_3.jpg'
# ]
#
# for img_url in img_url_list:
#     res = requests.get(img_url, headers=req_header)
#     if res.ok:
#         img_data = res.content
#         file_name = os.path.basename(img_url)
#
#         with open(file_name, 'wb') as file:
#             print(f'Write to file {file_name} ({len(img_data)}) bytes')
#             file.write(img_data)

import requests
from bs4 import BeautifulSoup

main_url = 'https://comic.naver.com/webtoon/detail?titleId=764040&no=54&amp;weekday=fri'
res = requests.get(main_url)

if res.ok:
    soup = BeautifulSoup(res.text, 'html.parser')
    img_tags = soup.select("img[src$='jpg']")

    img_url_list = []
    for img in img_tags:
        img = img['src']
        img_url_list.append(img)

# create image directory
import os

dir_path = '../image'
if not os.path.isdir(dir_path):
    os.mkdir(dir_path)

# image download
for idx, img_url in enumerate(img_url_list, 1):
    # print(f'download number {idx} URL = {img_url}')
    req_header = {'referer': main_url}
    res = requests.get(img_url, headers=req_header)
    if res.ok:
        img_data = res.content
        file_name = os.path.basename(img_url)

        with open('../image/' + file_name, 'wb') as file:
            file.write(img_data)

# delete directory
import shutil

dir_path = '../image'
if os.path.exists(dir_path):
    shutil.rmtree(dir_path)

# webtoon의 제목 & 특정회차 url argument -> download method
def download_image(title, round_url):
    import requests
    from bs4 import BeautifulSoup
    import os
    import shutil

    dir_path = 'image'
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
    else:
        title_path = os.path.join(dir_path, title)
        print(title_path)
        os.mkdir('../' + title_path)

    res = requests.get(round_url)
    if res.ok:
        soup = BeautifulSoup(res.text, 'html.parser')
        img_tags = soup.select("img[src$='.jpg']")

        req_header = {'referer': round_url}

        for idx, img in enumerate(img_tags, 1):
            img = img_tags['src']

            res_img = requests.get(img_url, headers=req_header)
            if res_img.ok:
                img_data = res_img.content

download_image()