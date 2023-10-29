from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool
import requests
import os 
def download_picture(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        filename = url[url.rfind('/') + 1:]
        with open(f'images/{filename}','wb') as f:
            f.write(resp.content)

with ThreadPoolExecutor(max_workers=16) as pool:
    list = ['food','design','art','car']
    for ch in list:
        for num in range(1,4):
            resp = requests.get(url=f'https://image.so.com/zjl?sn=0&ch={ch}&sn={num*30}')
            data_Dic = resp.json()
            # print(data_Dic)
            for each in data_Dic['list']:        
                    url = each['qhimg_url']
                    pool.submit(download_picture,url)   # 方法，参数

filenames = os.listdir('images')
for filename in filenames:
    print(f'已下载：{filename}')



#IDLE可运行
