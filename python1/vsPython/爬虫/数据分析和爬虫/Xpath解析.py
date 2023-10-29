from lxml import etree
from lxml import html
import requests

resp = requests.get(url='https://movie.douban.com/top250?start=0&filter=',
                    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54'}
)
# 将页面生成element对象
#爬取豆瓣图片成功
root = etree.HTML(resp.text)
movie_list = root.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[1]/a/img/@src')
for each in movie_list:
    print(each)
    res = requests.get(each)
    pic = res.content
    fime_name = each.split('/')[-1]
    file_path = 'images/'+ fime_name
    with open(file_path,'wb') as f:
        f.write(pic)



