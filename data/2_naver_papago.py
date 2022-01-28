# Urllib -> Papago Translation API example
import os
import sys
# import urllib.request
#
# client_id = "wQ9rTHcG6V0QrWMJn6Ir"  # Client ID
# client_secret = "6Uwj2ZLN72"  # Client Secret
# encText = urllib.parse.quote("Yesterday all my troubles seemed so far away")
# data = "source=en&target=ko&text=" + encText
# url = "https://openapi.naver.com/v1/papago/n2mt"
# request = urllib.request.Request(url)
# request.add_header("X-Naver-Client-Id", client_id)
# request.add_header("X-Naver-Client-Secret", client_secret)
# response = urllib.request.urlopen(request, data=data.encode("utf-8"))
# rescode = response.getcode()
#
# if (rescode == 200):
#     response_body = response.read()
#     print(response_body.decode('utf-8'))
# else:
#     print("Error Code:" + rescode)

# Requests -> Papago Translation API example
# import requests
#
# client_id = "wQ9rTHcG6V0QrWMJn6Ir"  # Client ID
# client_secret = "6Uwj2ZLN72"  # Client Secret
# url = "https://openapi.naver.com/v1/papago/n2mt"
#
# # req header
# req_header = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}
#
# with open('yesterday.txt') as f:
#     for txt in f:
#         if txt != '\n':
#             # req parameter
#             req_param = {"source": "en", "target": "ko", "text": txt}
#             res = requests.post(url, headers=req_header, data=req_param)
#
#             if res.ok:
#                 trans_txt = res.json()['message']['result']['translatedText']
#                 print(trans_txt)
#             else:
#                 print('Error Code', res.status_code)
#                 break

# session
from requests import Request, Session
client_id = "x1w2gCjyLlgkMkkE3HLv"  # Client ID
client_secret = "31iV0oybjH"  # Client Secret
url = "https://openapi.naver.com/v1/papago/n2mt"

# req header
req_header = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}


def get_text_file():
    with open('yesterday.txt', 'r', encoding='utf-8') as file:
        contents = file.read()
        result = contents.split('\n')
        return result


def save_to_file(m_list):
    with open('yesterday_trans.txt', 'w', encoding='utf-8') as file:
        file.writelines(m_list)


def main():
    # create session object
    session = Session()
    # list comprehension -> delete empty string
    source_list = get_text_file()
    source_list = [source for source in source_list if len(source) != 0]

    req_param = {"source": "en", "target": "ko"}

    result = []
    for txt in source_list:
        req_param['text'] = txt

        req = Request('POST', url, headers=req_header, data=req_param)
        prepared_req = req.prepare()

        res = session.send(prepared_req)
        if res.ok:
            try:
                trans_txt = res.json()['message']['result']['translatedText']
                print(trans_txt)
                result.append(txt + '\n')
                result.append(trans_txt + '\n')
            except Exception as e:
                print('error', res.status_code, e)
                break

    save_to_file(result)
    print('---------- end ----------')

main()
