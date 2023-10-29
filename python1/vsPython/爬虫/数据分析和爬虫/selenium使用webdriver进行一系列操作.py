from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

opentions = webdriver.ChromeOptions()
# 添加参数设置无头浏览器
opentions.add_argument('--headless')
browser = webdriver.Chrome(options=opentions)
browser.get('https://image.so.com/')
print(browser.get_cookies())
kw_input = browser.find_element(by=By.NAME,value='q')
kw_input.send_keys('美食')
# kw_input.send_keys(Keys.RETURN)
search_botton = browser.find_element(by=By.XPATH,value='//*[@id="so-search"]/form/button')
search_botton.click()
imgs = browser.find_elements(by=By.CSS_SELECTOR,value='img[src]')
for each in imgs:
    print(each.get_attribute('src'))

