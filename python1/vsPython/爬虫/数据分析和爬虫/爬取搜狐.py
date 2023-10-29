import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

# 将不是https开头的链接加上https

def fix(url):
    url = pattern.sub('',url)
    if not url.startswith('https'):
        url = 'https://' + url
    return url

pattern = re.compile(r'(?<!https)\/\/')
url = 'https://sohu.com/index.html'
resp = requests.get(url)
print(resp.raise_for_status  )
if resp.status_code ==200:
    soup = BeautifulSoup(resp.text,'html.parser')
    anchor = soup.select('div.list16>ul>li>a')
    for each in anchor:
        print(type(each))
        print(each.attrs['title'])
        print(fix(each.attrs['href']))