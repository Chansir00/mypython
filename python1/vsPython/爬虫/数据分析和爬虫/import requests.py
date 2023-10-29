import requests
from bs4 import BeautifulSoup
import os

def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
    else:
        print("访问被拒")

def crawl_bilibili_images():
    url = 'https://www.bilibili.com/'
    response = requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.54'}
)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        image_tags = soup.find_all('img')
        for img in image_tags:
            img_url = img['src']
            if img_url.startswith('http'):
                filename = img_url.split('/')[-1]
                save_path = os.path.join('images', filename)
                download_image(img_url, save_path)
                print(f"Downloaded: {img_url}")
    else:
        print("访问被拒")

if __name__ == '__main__':
    if not os.path.exists('images'):
        os.makedirs('images')
    crawl_bilibili_images()
