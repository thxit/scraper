
#coding:utf-8
#抓取死理性派首页文章标题
#运行环境python3

import urllib.request
from bs4 import BeautifulSoup
url =("http://www.guokr.com/scientific/subject/math/")
user_agent ="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36"
headers={'User-Agent':user_agent}
request = urllib.request.Request(url,None,headers)
html = urllib.request.urlopen(request)
obj = BeautifulSoup(html,"lxml")

namelist = obj.findAll(class_="article-title")
for name in namelist:
    print(name.get_text())

