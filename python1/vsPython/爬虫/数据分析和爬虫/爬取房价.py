from bs4 import BeautifulSoup
import requests
import re
import csv

def getHTML(url):
    headers =  {"User-Agent":'MMozilla/5.0 (Windows Nt 6.1; WOW64; rv:31.0)Gecko/20100101 Firefox/31.0'}
    #头文件伪装
    r = requests.get(url,headers = headers)
    r.encoding = r.apparent_encoding
    return r.text

def urllist(x):
    url = "https://www.anjuke.com/fangjia/{}{}"
    urllist = [url.format(m,n) for m in x for n in range(2015,2022)]
    return urllist

#解析网页
def bsoup(url):  #煲汤
    soup = BeautifulSoup(getHTML(url),'lxml')
    a = soup.find_all(name='a',attrs= {'class':'nostyle'})
    b = soup.select('div[calss="fjlist-box boxstyle2"]>h3')      
    cs = re.findall("年([\u4e00-\u9fa5]+)房价均价",b[0].text)
    #通过for循环将内容保存至列表
    for i in range(len(a)):  #a中是一年12月的数据，使用循环获得一个月数据
        b = a[i].text.strip().split('\n')
        b.append(cs[0])
        didian = b[-1]
        shijian = b[0][0:-2]
        junjia = b[1][0:-3]
        bianhualv=b[2][0:-2]
        b[0] = shijian
        b[1] = didian
        b[2] = junjia
        b[3] = bianhualv
        l.append(b)

#处理报错
def li(x):
    for url in urllist(x):
        try:
            bsoup(url)
        except:
            continue

def main(x,name):
    li(x)
    f = open(name,'w',newline='')
    headers = ['时间','地点','均价','变化率']
    csv_write = csv.writer(f)
    csv_write.writer(headers)
    for i in l:
        csv_write.writerow(i)
    f.close()

yixian = ["beijing",'guangzhou']
xinyixian = ['hangzhou','suzhou','nanjing','chongqing','wuhan','tianjing','cs']
erxian = ['wuxi','xm','jinan','dalian','km','jx']

l = []
main(yixian,name = "yixian.csv")

l = []
main(xinyixian,name = "xinyixian.csv")

l = []
main(erxian,name= 'erxian.csv')



