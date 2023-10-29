import requests
import time
from threading import Thread

def download_picture(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        filename = url[url.rfind('/') + 1:]
        with open(f'images/{filename}','wb') as f:
            f.write(resp.content)
    
def main():
    threads = []
    start = time.time()
    key = 'e8c5524dd2a365f20908ced735f8e480'
    for page in range(1,6):
        resp = requests.get(
            f'http://api.tianapi.com/meinv/index?key={key}&page={page}&num={10}')
        beaty_list = resp.json()['newlist']
        for each in beaty_list:
            picture_url = each['picUrl']
            t = Thread(target=download_picture,args=(picture_url))
            threads.append(t)
            t.start()
    #等待所有线程结束
    for t in threads:
        t.join()
    end = time.time()
    print('执行时间：{:.3f}秒'.format(end-start))

if __name__ == '__main__':
    main()

