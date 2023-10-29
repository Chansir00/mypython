import requests
from bs4 import BeautifulSoup

url = 'https://cupfox.app/list/%E7%83%AD%E9%97%A8%E7%94%B5%E5%BD%B1/movie_%E6%AC%A7%E7%BE%8E'
head = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54'}
re = requests.get(url,headers= head)
if re.status_code == 200:
    text = re.text

soup = BeautifulSoup(text,'html.parser')
ls = []
info = soup.select("div.jsx-2691002058.movie-list-item")
for i in info:
    name = soup.select_one('div.jsx-2691002058.movie-title').text
    
    ls.append(name)
print(ls)
