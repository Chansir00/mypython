from selenium import webdriver
import time,os
import json

outdir = r'C:\Users\64271\Desktop\vsPython\爬虫'
browser = webdriver.Chrome()
browser.get('https://jd.com/')
time.sleep(30)
cooks = browser.get_cookies()
with open(os.path.join(outdir,'cookies.txt'),mode='w') as f:
    f.write(json.dumps(cooks))