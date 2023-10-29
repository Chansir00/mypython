import requests
from bs4 import BeautifulSoup
import time
import random


head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54'}
# 获取多个页面
resp = requests.get(url='https://image.so.com/c?ch=car',headers=head)
if resp.status_code == 200:
    soup = BeautifulSoup(resp.text,'html.parser')
    img_lsit = soup.find_all('#app > div > div.content > div.waterfall__wrap > div > div.waterfall__inner > ul:nth-child > li:nth-child > a > div > img')

for img in img_lsit:
    with open(f"{img}file",'wb') as f:
        f.write(img.content)



