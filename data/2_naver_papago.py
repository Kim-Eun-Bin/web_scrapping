# Urllib -> Papago Translation API example
import os
import sys
import urllib.request

client_id = "wQ9rTHcG6V0QrWMJn6Ir"  # Client ID
client_secret = "6Uwj2ZLN72"  # Client Secret
encText = urllib.parse.quote("Yesterday all my troubles seemed so far away")
data = "source=en&target=ko&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()

if (rescode == 200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

# Requests -> Papago Translation API example
import requests

client_id = "wQ9rTHcG6V0QrWMJn6Ir"  # Client ID
client_secret = "6Uwj2ZLN72"  # Client Secret
url = "https://openapi.naver.com/v1/papago/n2mt"

# req header
req_header = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}

with open('yesterday.txt') as f:
    for txt in f:
        if txt != '\n':
            # req parameter
            req_param = {"source": "en", "target": "ko", "text": txt}
            res = requests.post(url, headers=req_header, data=req_param)

            if res.ok:
                trans_txt = res.json()['message']['result']['translatedText']
                print(trans_txt)
            else:
                print('Error Code', res.status_code)