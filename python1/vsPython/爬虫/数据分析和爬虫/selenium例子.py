from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://image.so.com/z?ch=beauty')
# print(driver.page_source)
#page_source是拿到动态内容的源代码
soup = BeautifulSoup(driver.page_source,'html.parser')
imgs = soup.select('img') #返回一个列表
for img in imgs:
    print(img.attrs['src'])