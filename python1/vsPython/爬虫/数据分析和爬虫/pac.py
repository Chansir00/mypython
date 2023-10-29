import requests

head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54'}


r = requests.get(url='https://www.baidu.com',headers = head,timeout=30)
print(r.raise_for_status)
text = r.text
print(text)