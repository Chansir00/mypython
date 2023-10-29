from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import json

#selenium反爬措施
option = webdriver.ChromeOptions()
option.add_experimental_option('excludeSwitches',['enable-automation'])
option.add_experimental_option('useAutomationExtension',False)
browser = webdriver.Chrome(options=option)
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',{
    'source':'Object.defineProperty(navigator,"webdriver",{get:() => undefined})'})
#CDP - Chrome Developer Protocl 谷歌开发者协议

#向网页添加cookies
browser.get('https://jd.com/')
time.sleep(3)
browser.delete_all_cookies()
with open (r'C:\Users\64271\Desktop\vsPython\爬虫\cookies.txt','r',) as f:
    cookies_list = f.read()
    cookies_list1 = json.loads(cookies_list)

for cook in cookies_list1:
    browser.add_cookie(cook)
browser.refresh()



kw_input = browser.find_element(by=By.ID,value='key')
kw_input.send_keys('手机')
kw_input.send_keys(Keys.RETURN)
#隐式等待,如果元素不存在，则等待五秒钟
#如果元素任不存在，测产生TimeOutException
#如果不等待直接拿取元素，可能产生NoSuchElementException
browser.implicitly_wait(5)
cart_botton =  browser.find_element(by=By.XPATH,value='//*[@id="settleup-2014"]/div[1]/a')
cart_botton.click()

#切换窗口
windows = browser.window_handles
browser.switch_to.window(windows[-1])
#显式等待
wait = WebDriverWait(browser,20)

# add_button = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-tabs-1']/ul/div/div/div/div//div/div/div/div[2]/a")))
# wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='react-tabs-1']/ul/div/div/div/div//div/div/div/div[2]/a[@class='btn reco-add-cart xh-highlight']")))
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.parent-element a.btn.reco-add-cart.xh-highlight")))

add_button = browser.find_elements(By.XPATH, "//*[@id='react-tabs-1']/ul/div/div/div/div//div/div/div/div[2]/a")
print(add_button)

for each in add_button[:3]:
    # ActionChains(browser).move_to_element(each).click().perform()
    browser.execute_script("arguments[0].click();", each)
    # each.click()
    time.sleep(2)

buy_button = browser.find_element(by=By.XPATH,value='//*[@id="cart-body"]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/a')
buy_button.click()
time.sleep(2)
check_button = browser.find_element(by=By.XPATH,value="//*[@id='order-submit']")
check_button.click()



    
#招聘，租房，卖车
