import os
import re
import requests

def gethtml(url):
    req = requests.request(url)
    req.add_header("User-Agent",'Mozilla/5.0 (Macintosh;Intel Mac OS X 10_10_1) AppleWebkit/537.36 (KHTML, like Gecko) CHrome/39.0.2171.95 Safari/537.36')
    page = req.get(url)
    html= page.text()
    return html

def get_img(html):
    p = 'r<img class="BDE_Image".*?src="([^"]*\.jpg)".*?>)'
    imglist = re.findall(p,html)

    try:
        os.mkdir("newpics")
    except:
        pass
    
    os.chdir("newpics")

    for each in imglist:
        filename = each.split("/")[-1]
        requests.request(each,filename,None)
    
if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/8326829315'
    get_img(gethtml(url))
